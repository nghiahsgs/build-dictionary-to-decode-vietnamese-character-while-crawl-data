from urllib.parse import parse_qs
from slugify import slugify
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import numpy as np
#import cv2
import hashlib
import bs4
import requests
import shutil
import urllib
import re
import sys
import time
import io
import os
import random
import requests
import json

class DataBase_VPS():
    def __init__(self, url_api):
        self.url= url_api
    
    def insert_new_row_api(self, dataPost):
        dataPost=json.dumps(dataPost)
        headers={
            'Content-Type':'application/json'
        }

        x = requests.post(self.url, data = dataPost,headers=headers)
        return x.text

class File_Interact():
    def __init__(self,file_name):
        self.file_name=file_name

    def write_file(self,ndung):
        f = io.open(self.file_name, 'w', encoding='utf-8')
        f.write(ndung)
        f.close()
    

    
    def write_file_from_list(self, list_lines):
        f = io.open(self.file_name, 'w', encoding='utf-8')
        f.write('\n'.join(list_lines))
        f.close()
    
    def replace_line_in_file(self, i_line, new_line):
        L=self.read_file_list()
        L2=L.copy()
        L2[i_line] = new_line
        self.write_file_from_list(L2)

    def write_file_line(self,ndung_line):
        f = io.open(self.file_name, 'a', encoding='utf-8')
        f.write('%s\n'%ndung_line)
        f.close()


    def read_file(self):
        f = io.open(self.file_name, 'r', encoding='utf-8')
        ndung=f.read()
        f.close()
        return ndung

    def read_file_list(self):
        f = io.open(self.file_name, 'r', encoding='utf-8')
        ndung = f.read()
        f.close()
        return ndung.split('\n')
    
    def remove_all_file_in_directory(self,folder_path):
        list_file = ['%s/%s' % (folder_path,file_name) for file_name in os.listdir(folder_path)]
        for file in list_file:
            os.remove(file)
    
    def conver_vi_file_2_en_file_name(self,folder_path):
        # folder_path = r'Anh_thay_giao_ba/lop_1'
        list_vi_file = os.listdir(folder_path)
        string_Interact1 = String_Interact()
        
        for vi_file in list_vi_file:
            en_file = string_Interact1.convert(vi_file)
            en_file = en_file.replace(' ', '-').lower()
            # print(vi_file)
            # print(en_file)
            os.rename('%s/%s' % (folder_path, vi_file), '%s/%s' % (folder_path, en_file))


    def short_link(self,longUrl):
        url='https://app.bitly.com/proxy/v3/user/link_save'

        dataPost={'longUrl':longUrl}

        #cookie nick bitly.com cua futuregohan1997@gmail.com
        cookie='_ga=GA1.2.24684873.1573118678; _mkto_trk=id:754-KBJ-733&token:_mch-bitly.com-1573118678539-90732; _xsrf=ca8c4295a4aa447e8b18c861260ec11e; optimizelyEndUserId=oeu1593502806637r0.4732796373653363; _gid=GA1.2.1569544785.1593502807; 2fa=|1593502804|93f5740a21922924569780c4e4fadadbebd8c5b7; cookie_banner=1; anon_u=cHN1X185OTU2YmU0YS04NjkwLTQ2ZjgtYTViOS0zNDdmZDAwMmU3ZTA=|1593502823|4acee57f8ff2fc083df22cee9b7a62f97dcfbb2a; user=b18zZGtsanR2bjZn|1593502823|e3dfbf33352540921debf6eb80edfb0fe199afbc; __stripe_mid=ba1ff2d8-ea6a-4ab2-90ca-a2f67ca72d90; __stripe_sid=445fda8d-53d9-4f66-9e33-292f79e90770'

        headers={
            'cookie':cookie,
            'referer': 'https://app.bitly.com/Bk6u7MHRRKI/bitlinks/38bvMmi?actions=create',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
            'x-bitly-brand-guid': 'Bk6u7MHRRKI',
            'x-bitly-client': 'bbt2',
            'x-xsrftoken': 'ca8c4295a4aa447e8b18c861260ec11e'
        }
        data=requests.post(url, data=dataPost,headers=headers).json()

        user_hash=data['data']['link_save']['user_hash']
        link='http://bit.ly/'+user_hash

        return link

list_first_name_vi = ["An","Uc","Uat","Dam","Dao","Dinh","Doan","An","Banh","Bach","Cao","Chau","Chu","Chu","Chung","Duu","Diep","Doan","Giang","Ha","Han","Kieu","Kim","Lam","Luong","Luu","Lac","Luc","La","Lieu","Ma","Mac","Mach","Mai","Ngu","Nghiem","Phi","Pho","Phung","Quach","Quang","Quyen","To","Ton","Ta","Tong","Thai","Sai","Than","Thach","Thao","Thuy","Thi","Tieu","Truong","Tram","Trinh","Trang","Trieu","Van","Vinh","Vuong","Vuu","Nguyen","Tran","Le","Pham","Huynh","Hoang","Phan","Vu","Vo","Dang","Bui","Do","Ho","Ngo","Duong","Ly","Nguyen","Tran","Le","Pham","Huynh","Hoang","Phan","Vu","Vo","Dang","Bui","Do","Ho","Ngo","Duong","Ly","Nguyen","Nguyen","Nguyen","Nguyen","Nguyen","Nguyen","Nguyen","Nguyen","Nguyen","Nguyen","Nguyen","Nguyen","Nguyen","Nguyen","Nguyen","Nguyen","Nguyen","Tran","Le","Pham","Huynh","Hoang","Phan","Vu","Vo","Dang","Bui","Do","Ho","Ngo","Duong","Ly","Nguyen","Tran","Le","Pham","Huynh","Hoang","Phan","Vu","Vo","Dang","Bui","Do","Ho","Ngo","Duong","Ly"]
list_last_name_vi = ["Bao An","Binh An","Dang An","Duy An","Khanh An","Nam An","Phuoc An","Thanh An","The An","Thien An","Truong An","Viet An","Xuan An","Cong An","Duc An","Gia An","Hoang An","Minh An","Phu An","Thanh An","Thien An","Thien An","Vinh An","Ngoc An","Chi Anh","Duc Anh","Duong Anh","Gia Anh","Hung Anh","Huy Anh","Minh Anh","Quang Anh","Quoc Anh","The Anh","Thieu Anh","Thuan Anh","Trung Anh","Tuan Anh","Tung Anh","Tuong Anh","Viet Anh","Vu Anh","Ho Bac","Hoai Bac","Gia Bach","Cong Bang","Duc Bang","Hai Bang","Yen Bang","Chi Bao","Duc Bao","Duy Bao","Gia Bao","Huu Bao","Nguyen Bao","Quoc Bao","Thieu Bao","Tieu Bao","Duc Binh","Gia Binh","Hai Binh","Hoa Binh","Huu Binh","Khanh Binh","Kien Binh","Kien Binh","Phu Binh","Quoc Binh","Tan Binh","Tat Binh","Thai Binh","The Binh","Xuan Binh","Yen Binh","Quang Buu","Thien Buu","Khai Ca","Gia Can","Duy Can","Gia Can","Huu Canh","Gia Canh","Huu Canh","Minh Canh","Ngoc Canh","Duc Cao","Xuan Cao","Bao Chan","Bao Chau","Huu Chau","Phong Chau","Thanh Chau","Tuan Chau","Tung Chau","Dinh Chien","Manh Chien","Minh Chien","Huu Chien","Huy Chieu","Truong Chinh","Duc Chinh","Trong Chinh","Trung Chinh","Viet Chinh","Dinh Chuong","Tuan Chuong","Minh Chuyen","An Co","Chi Cong","Thanh Cong","Xuan Cung","Huu Cuong","Manh Cuong","Duy Cuong","Viet Cuong","Ba Cuong","Duc Cuong","Dinh Cuong","Duy Cuong","Hung Cuong","Huu Cuong","Kien Cuong","Manh Cuong","Ngoc Cuong","Phi Cuong","Phuc Cuong","Thinh Cuong","Viet Cuong","Ngoc Dai","Quoc Dai","Minh Dan","The Dan","Minh Dan","Nguyen Dan","Sy Dan","Hai Dang","Hong Dang","Minh Danh","Ngoc Danh","Quang Danh","Thanh Danh","Hung Dao","Thanh Dao","Binh Dat","Dang Dat","Huu Dat","Minh Dat","Quang Dat","Quang Dat","Thanh Dat","Dac Di","Phuc Dien","Quoc Dien","Phi Diep","Dinh Dieu","Vinh Dieu","Manh Dinh","Bao Dinh","Huu Dinh","Ngoc Doan","Thanh Doan","Thanh Doanh","The Doanh","Dinh Don","Quang Dong","Tu Dong","Vien Dong","Lam Dong","Bach Du","Thuy Du","Hong Duc","Anh Duc","Gia Duc","Kien Duc","Minh Duc","Quang Duc","Tai Duc","Thai Duc","Thien Duc","Thien Duc","Tien Duc","Trung Duc","Tuan Duc","Hoang Due","Anh Dung","Chi Dung","Hoang Dung","Hung Dung","Lam Dung","Manh Dung","Minh Dung","Nghia Dung","Ngoc Dung","Nhat Dung","Quang Dung","Tan Dung","The Dung","Thien Dung","Tien Dung","Tri Dung","Trong Dung","Trung Dung","Tuan Dung","Viet Dung","Hieu Dung","Dai Duong","Dinh Duong","Dong Duong","Hai Duong","Nam Duong","Quang Duong","Thai Duong","Viet Duong","Anh Duy","Bao Duy","Duc Duy","Khac Duy","Khanh Duy","Nhat Duy","Phuc Duy","Thai Duy","Trong Duy","Viet Duy","The Duyet","Vuong Gia","Bao Giang","Chi Giang","Cong Giang","Duc Giang","Hai Giang","Hoa Giang","Hoang Giang","Hong Giang","Khanh Giang","Long Giang","Minh Giang","Thien Giang","Truong Giang","Nguyen Giap","Huy Kha","Anh Khai","Duc Khai","Hoang Khai"]

list_first_name_en = ['Boris', 'Fred', 'Albert', 'Tom', 'James', 'Matthew', 'Mark', 'Luke', 'John', 'David', 'Harold', 'Bob', 'Jack', 'Mike', 'Raymond', 'Cuthbert', 'Casper', 'Harry', 'Cameron', 'Warwick', 'Steve', 'Steven', 'Simon', 'Jeff', 'Zach', 'Chris', 'Christian', 'Matt', 'Mathias', 'Alex', 'Will', 'William', 'Forest', 'Clarke', 'Gregory', 'Joshua', 'Josh', 'Andy', 'Andrew', 'Dick', 'Rick', 'Richard', 'Rob', 'Robert', 'Mohammad', 'Hector', 'Reginald', 'Phillip', 'Phil', 'Pete', 'Roger', 'Brad', 'Chad', 'Shane', 'Daniel', 'Dan', 'Tristan', 'Roy', 'Gary', 'Tony', 'Toby', 'Barry', 'Graham', 'Kevin','Tommy','Sandie','Darth','Garth','Annie', 'Mary', 'Sarah', 'Laura', 'Lauren', 'Katy', 'Kate', 'Catherine', 'Naomi', 'Helen', 'Nadine', 'Alice', 'Alison', 'Susan', 'Suzanne', 'Sharon', 'Georgina', 'Sonya', 'Marion', 'Beth', 'Una', 'Sophia', 'Rachel', 'Christiana', 'Maud', 'Mildred', 'Zoe', 'Chantal', 'Charlotte', 'Chloe', 'Flora', 'Annabelle', 'Elizabeth', 'Morwenna', 'Jenna', 'Jenny', 'Gemma', 'Wenna', 'Fairydust', 'Charity', 'Ocean', 'Virginia', 'Hannah', 'Mavis', 'Harriet', 'Kathy', 'Heather', 'Kimberly', 'May', 'Carla', 'Suki', 'Michelle', 'Rhiannon', 'Ruth', 'Polly', 'Sally', 'Molly', 'Dolly', 'Maureen', 'Maud', 'Doris', 'Felicity','Jessica','Stanley']
list_last_name_en = ['Gump', 'Doop', 'Gloop', 'Snozcumber', 'Giantbulb', 'Slaughterhouse', 'Godfrey', 'Smith', 'Jones', 'Bogtrotter', 'Ramsbottom', 'Cockle', 'Hemingway', 'Pigeon', 'Parker', 'Nolan', 'Parkes', 'Butterscotch', 'Barker', 'Trescothik', 'Superhalk', 'Barlow', 'MacDonald', 'Ferguson', 'Donaldson', 'Platt', 'Bishop', 'Blunder', 'Thunder', 'Sparkle', 'Walker', 'Raymond', 'Thornhill', 'Sweet', 'Parker', 'Johnson', 'Randall', 'Zeus', 'England', 'Smart', 'Gobble', 'Clifford', 'Thornton', 'Cox', 'Blast', 'Plumb', 'Wishmonger', 'Fish', 'Blacksmith', 'Thomas', 'Grey', 'Russell', 'Lakeman', 'Ball', 'Chan', 'Chen', 'Wu', 'Khan', 'Meadows', 'Connor', 'Williams', 'Wilson', 'Blackman', 'Jones','Humble','Noris','Bond','Rabbit','McCallister','DeVito','Malkovich','Olsson','Sparrow','Kowalski','Vader','Torrance', 'Greenway','Rockatansky','Pitt','Willis','Jolie']

class String_Interact():
    def __init__(self):
        pass

    def regex_one_value(self,pattern, input_str):
        regex1=re.compile(pattern)
        kq=regex1.search(input_str)
        if kq:
            kq=kq.group(1)
        else:
            kq=''
        return kq

    def regex_many_value(self,pattern, input_str):
        regex1=re.compile(pattern)
        kq=regex1.findall(input_str)
        return kq

    def convert(self,text):
        patterns = {
            '[àáảãạăắằẵặẳâầấậẫẩ]': 'a',
            '[đ]': 'd',
            '[èéẻẽẹêềếểễệ]': 'e',
            '[ìíỉĩị]': 'i',
            '[òóỏõọôồốổỗộơờớởỡợ]': 'o',
            '[ùúủũụưừứửữự]': 'u',
            '[ỳýỷỹỵ]': 'y'
        }
        """
        Convert from 'Tieng Viet co dau' thanh 'Tieng Viet khong dau'
        text: input string to be converted
        Return: string converted
        """
        output = text
        for regex, replace in patterns.items():
            output = re.sub(regex, replace, output)
            # deal with upper case
            output = re.sub(regex.upper(), replace.upper(), output)
        return output

    
    def encode_tieng_viet_html(self,string_input):
        dict_char={
            'à':'&#224;',
            'á':'&#225;',
            'â':'&#226;',
            'ã':'&#227;',

            'À':'&#192;',
            'Á':'&#193;',
            'Â':'&#194;',
            'Ã':'&#195;',

            'è':'&#232;',
            'é':'&#233;',
            'ê':'&#234;',

            'È':'&#200;',
            'É':'&#201;',
            'Ê':'&#202;',


            'ì':'&#236;',
            'í':'&#237;',

            'Ì':'&#204;',
            'Í':'&#205;',


            'ò':'&#242;',
            'ó':'&#243;',
            'ô':'&#244;',

            'Ò':'&#210;',
            'Ó':'&#211;',
            'Ô':'&#212;',

            'ù':'&#249;',
            'ú':'&#250;',

            'Ù':'&#217;',
            'Ú':'&#218;'
        }


        string_output=[]
        for char in string_input:
            # print(char)

            if char in dict_char:
                string_output+=dict_char[char]
            else:
                string_output+=char
        return ''.join(string_output)

    
    def md5_encode(self,text):
        hash_object = hashlib.md5(text.encode())
        md5_hash = hash_object.hexdigest()
        return md5_hash
    
    def keep_normal_char(self, full_string):
        list_valid_char = 'qwertyuiopasdfghjklzxcvbnm'
        list_valid_char += 'qwertyuiopasdfghjklzxcvbnm'.upper()
        list_valid_char += '0123456789'
        list_valid_char += ' '

        kq = ''
        for char in full_string:
            if char in list_valid_char:
                kq += char
        return kq
    
    def get_element_by_css_selector(self, data, css_selector):
        soup = bs4.BeautifulSoup(data, 'html.parser')
        eles=soup.select(css_selector)
        return eles #get_text() and get('href')

    
    def gen_slug(self,title):
        
        slug=self.convert(title).replace(' ','-').replace(':','').replace('.','').replace(',','').lower()
        slug=slug.replace('--','-')


        slug = slugify(slug)

        return slug

    def url_decode(self,href):
        o = parse_qs(href)
        return o

    def remove_all_a_tag_in_html(self,ndung):
        list_a_tag=self.get_element_by_css_selector(ndung,'a')
        for a_tag in list_a_tag:
            ndung=ndung.replace('%s'%a_tag,a_tag.get_text())
        return ndung
    def download_all_image_in_html_file(self, ndung, folder_save):
        image_Interact1=Image_Interact()
        #get all src image (direct src)
        list_image_tag=self.regex_many_value(r'<img(.*?)>',ndung)

        list_image_src=[]
        for image_tag in list_image_tag:
            src=self.regex_one_value(r'src="(.*?)"',image_tag)
            data_original=self.regex_one_value(r'data-original="(.*?)"',image_tag)
            if data_original:
                real_source=data_original
                #replace src anh gif => url that cua anh
                image_tag_new=image_tag.replace(src, real_source)
                ndung=ndung.replace(image_tag,image_tag_new)
            else:
                real_source=src
            list_image_src.append(real_source)
            

        #download image
        list_local_image=[]
        for image_src in list_image_src:
            nameFile='%s-%s'%(int(time.time()),random.randint(0,1000))
            image_Interact1.downloadImg(image_src,nameFile,folder_save)
            
            list_local_image.append(nameFile+'.jpg')
        
        #replace link image to local image
        for i in range(len(list_image_src)):
            ndung=ndung.replace(list_image_src[i],'%s/%s'%(folder_save,list_local_image[i]))
        return list_local_image,ndung

    def randomFirstName(self,type='en'):
        if type=='vi':
            return random.choice(list_first_name_vi)
        return random.choice(list_first_name_en)

    def randomLastName(self,type='en'):
        if type=='vi':
            return random.choice(list_last_name_vi)
        return random.choice(list_last_name_en)
        
    def randomUserName(self,type='en'):
        firstname = self.randomFirstName(type)
        lastname = self.randomLastName(type)
        number = random.randint(1000,9999)
        return '%s_%s_%s'%(firstname,lastname,number)

    def randomPass(self,type='en'):
        username=self.randomUserName(type)
        number = random.randint(1000,9999)
        return '%s@%s'%(username,number)

class Rent_code():
    def __init__(self):
        self.string_Interact1=String_Interact()
        self.apiKey='fecZ6WQ12XVKTqRQeSc7HwA4mHMRH3wJnogm9VgTyNgv'
    
    def create_order(self):
        apiKey=self.apiKey
        #;get available service (field "id": )
        #;https://api.rentcode.net/api/v2/available-services?apiKey=dvOf8PDrXWBohvQNcUcxVvbidLoNKMahR7CGS4NujR0v
        #;create order
        #Dịch vụ sim online trong 30 phút (có thể gọi lại sim trong 30 phút): 249
        url='https://api.rentcode.net/api/v2/order/request?serviceProviderId=2&&apiKey='+apiKey
        data=requests.get(url).text

        print(data)

        order_id=self.string_Interact1.regex_one_value(r'"id":(.*?),',data)
        return order_id


    def get_sdt_in_order(self,order_id):
        apiKey=self.apiKey
        #;get sdt in order id
        url='https://api.rentcode.net/api/v2/order/'+order_id+'/check?apiKey='+apiKey
        data=requests.get(url).text

        phoneNumber=self.string_Interact1.regex_one_value(r'"phoneNumber":"(.*?)"',data)
        return phoneNumber


    def get_code_in_order(self,order_id):
        apiKey=self.apiKey
        #;get code in order id
        url='https://api.rentcode.net/api/v2/order/'+order_id+'/check?apiKey='+apiKey
        data=requests.get(url).text

        tele_code=self.string_Interact1.regex_one_value(r' ([0-9]{6})',data)
        return tele_code


class Image_Interact():
    def __init__(self):
        pass

    def compress_image(self, path):
        foo = Image.open(path)
        foo.save(path, optimize=True, quality=95)
    
    def downloadImg(self, url, nameFile, result_dir):
        # for iTry in range(5):
        #     try:
        #         print(url)
        #         response = requests.get(url, stream=True, timeout=10)
        #         with open(os.path.join(result_dir, r'%s.jpg'%nameFile), 'wb') as out_file:
                
        #             shutil.copyfileobj(response.raw, out_file)
        #         del response
        #     except:
        #         print("error downloadImg")
            
        #     try:
        #         self.compress_image(os.path.join(result_dir, r'%s.jpg'%nameFile))
        #         break
        #     except:
        #         pass
        
        # print(url)
        # response = requests.get(url, stream=True, timeout=10)
        # with open(os.path.join(result_dir, r'%s.jpg'%nameFile), 'wb') as out_file:
        #     shutil.copyfileobj(response.raw, out_file)
        # del response
        try:
            response = requests.get(url,verify=False)
            file = open(os.path.join(result_dir, r'%s.jpg'%nameFile), "wb")
            file.write(response.content)
            file.close()
        except:
            pass

    def create_image_white_bg(self, in_file,out_file):
        img = cv2.imread(in_file)
        height, width, channel = img.shape

        img[int(0.3*height):int(0.7*height), :] = (255, 255, 255)
        cv2.imwrite(out_file, img)


    def add_text_to_image(self, bg_path, font_path, font_size, title, out_put_file):
        # title = 'Giải bài tập trang 45, 46 SGK Toán 1: Luyện tập Phép cộng trong phạm vi 3'
        # add_text_to_image('img.jpg', 'times.ttf', 40, title, 'img1.jpg')

        img = Image.open(bg_path)
        width, height = img.size

        font_width = int(font_size*0.4)
        max_length = width//font_width
        max_line = len(title)//max_length
        if len(title) % max_length != 0:
            max_line += 1
        # print(max_line)

        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(font_path, size=font_size)

        for i in range(max_line):
            x_start = 10
            y_start = int(0.3*height)+int(1.5*font_size)*(i+1)

            if i == max_line-1:
                draw.text((x_start, y_start), title, (0, 0, 0), font=font)
            else:
                line = ' '.join(title[:max_length].split(' ')[:-1])
                # print(line)
                draw.text((x_start, y_start), line, (0, 0, 0), font=font)

            title = title.replace(line, '')
            # print(title)
            # input('zz')

        img.save(out_put_file)

class Youtube():
    def __init__(self):
        pass
    def get_id_first_result_from_keyword(self,keyword):
        string_Interact1=String_Interact()

        url='https://www.youtube.com/results?search_query=%s'%(keyword.replace(' ','+'))
        data=requests.get(url).text
        # utils_class.File_Interact('code.html').write_file(data)

        list_id_video=string_Interact1.regex_many_value(r'"videoRenderer":{"videoId":"(.*?)"',data)
        list_title=string_Interact1.regex_many_value(r'"title":{"runs":\[{"text":"(.*?)"',data)

        list_id_video=list_id_video[:3]
        list_title=list_title[:3]
        
        if len(list_id_video)!=len(list_title):
            return [],[]
        return list_id_video,list_title
    
if __name__=='__main__':
    # insert_new_row_api('nfnfnf',20)

    # db=DataBase_VPS('http://45.32.102.157:8000/api')
    # dataPost = {
    #     "post_url":'nfnfnf',
    #     "i_page":20
    # }
    # db.insert_new_row_api(dataPost)

    image_Interact1=Image_Interact()

    url='https://lh3.googleusercontent.com/LpDMOozUZLa16PPcjwJ8oAcexyZPHDuako3NGjaQxOVEcXnRjF1Z7EDUg1wHYjrOx1oUwmUH2vGU2lwtUztFTV6i_3osAg_y7ch2NgSeRNYfWZdYmYcuj-hfx0k8m3gH5NjrPMcg'
    nameFile='file-name'
    result_dir='images'
    image_Interact1.downloadImg(url,nameFile, result_dir)
