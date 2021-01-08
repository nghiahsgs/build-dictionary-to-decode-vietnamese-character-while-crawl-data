from flask import Flask, request, render_template
from database_api_setup_0 import *


app = Flask(__name__)

@app.route('/api', methods=['POST'])
def index2():
    if request.method=="POST":
        func=request.get_json()['func']
        Post.create_table()
        dB_Interact1=DB_Interact()

        #select_rows_db
        if func=='select_rows_db':
            id=request.get_json()['id']
            post1=dB_Interact1.select_row_from_id(id)
            print('post1',post1)

        if func=='insert_new_row_db':
            # post_url = request.get_json()['post_url']
            # i_page = request.get_json()['i_page']
            # dict_fields={
            #     'post_url':post_url,
            #     'i_page':i_page,
            # }
            dict_fields=request.get_json()
            dB_Interact1.insert_new_row_db(dict_fields)
        
        # insert_new_row_db(post_url,i_page)
        return {'res':'ok'}
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=9000)