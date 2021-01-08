#cach 1: dung 1 list de quan ly cac luong khi nao chay xong or khong
# uu diem de code, de set up, quan ly list status o ram
# nhuoc diem khi scale up len => k on dinh

import time
import threading

global list_input, list_is_count, isStop
isStop=False

class My_thread(threading.Thread):
    def __init__(self,name,action_func):
        threading.Thread.__init__(self)
        self.name=name
        self.action_func=action_func

        
    def run(self):
        global list_input, list_is_count, isStop
        
        while not isStop:
            try:
                index=list_is_count.index(False)
                list_is_count[index]=True

                input_arg=list_input[index]
                self.action_func(input_arg)
                
            except:
                print('pass')
        
        
class My_thread_stop(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.name=name
        
    def run(self):
        global isStop
        while(True):
            try:
                index=list_is_count.index(False)
            except:
                isStop=True
                return





def run_multi_threads(nb_theads,action_func,list_input_arg):
    global list_input,list_is_count
    list_input=list_input_arg
    
    list_is_count= [False]*len(list_input)

    list_threads=[]
    
    #init
    my_thread_stop=My_thread_stop('my_thread_stop')
    for i in range(nb_theads):
        new_thread=My_thread('thread%s'%i,action_func)
        list_threads.append(new_thread)

    #start
    my_thread_stop.start()
    for i in range(nb_theads):
        list_threads[i].start()

    #join
    my_thread_stop.join()
    for i in range(nb_theads):
        list_threads[i].join()

if __name__=='__main__':
    global sum
    sum=0
    
    def action_func(input_arg):
        #print('input_arg',input_arg)
        global sum
        sum+=input_arg

    list_input_arg=list(range(0,100)) #100 phan tu
    run_multi_threads(24,action_func,list_input_arg)
    print(sum)