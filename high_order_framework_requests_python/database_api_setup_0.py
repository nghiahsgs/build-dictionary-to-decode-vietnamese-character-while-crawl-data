from peewee import *
import requests
import json

db_name='test'
db_user='root'
db_pass=''
db = MySQLDatabase(db_name, user=db_user, passwd=db_pass)

class Post(Model):
    post_url=CharField()
    i_page=IntegerField()

    class Meta:
        database=db
    
    def __str__(self):
        return 'post_url: %s and i_page: %s'%(self.post_url,self.i_page)


class DB_Interact():
    def __init__(self):
        pass

    def insert_new_row_db(self,dict_fields):
        post1=Post(**dict_fields)
        post1.save()

    def select_rows_db(self,condition_where):
        list_rows=Post.select().where(condition_where)
        return list_rows
    def select_row_from_id(self,id):
        post1=Post.select().where(Post.id==id).get()
        return post1

if __name__=="__main__":
    Post.create_table()
    dB_Interact1=DB_Interact()

    #insert_new_row_db
    # dict_fields={
    #     'post_url':'nghia',
    #     'i_page':1,
    # }
    # dB_Interact1.insert_new_row_db(dict_fields)

    #select_rows_db
    # condition_where=Post.post_url=='nghia'
    # condition_where&=(Post.i_page==1)
    
    #select_row_from_id
    # id=15
    # post1=dB_Interact1.select_row_from_id(id)