import pickle
from high_order_framework_requests_python import utils_class
import requests

string_Interact1 = utils_class.String_Interact()


def save_dict_to_picker_file(dict_obj,file_name):
    file = open(file_name, 'wb')
    pickle.dump(dict_obj, file)
    file.close()

def load_dict_from_picker_file(file_name):
    file = open(file_name, 'rb')
    dict_obj = pickle.load(file)
    file.close()
    return dict_obj

def encode_vi_char(input_char):
    # input_char = 'á'
    url = 'https://graphemica.com/%s'%input_char
    data = requests.get(url).text

    utils_class.File_Interact('code.html').write_file(data)
    encoded_char = string_Interact1.regex_one_value("<td class='name'>\nPython\n<\/td>\n<td class='value'>\n(.*)",data)
    return encoded_char

if __name__ =="__main__":
    list_input_char = []
    # list_input_char += ["ă", "ắ", "ằ", "ẳ", "ẵ", "ặ", "á", "à", "ả", "ã", "ạ", "â", "ấ", "ầ", "ẩ", "ẫ", "ậ"]
    # list_input_char += ["Á", "À", "Ả", "Ã", "Ạ", "Ă", "Ắ", "Ằ", "Ẳ", "Ẵ", "Ặ", "Â", "Ấ", "Ầ", "Ẩ", "Ẫ", "Ậ"]
    # list_input_char += ["é","è","ẻ","ẽ","ẹ","ê","ế","ề","ể","ễ","ệ"]
    # list_input_char += ["É","È","Ẻ","Ẽ","Ẹ","Ê","Ế","Ề","Ể","Ễ","Ệ"]
    list_input_char += ["đ"]
    list_input_char += ["Đ"]
    # list_input_char += ["ó","ò","ỏ","õ","ọ","ô","ố","ồ","ổ","ỗ","ộ","ơ","ớ","ờ","ở","ỡ","ợ"]
    # list_input_char += ["Ó","Ò","Ỏ","Õ","Ọ","Ô","Ố","Ồ","Ổ","Ỗ","Ộ","Ơ","Ớ","Ờ","Ở","Ỡ","Ợ"]
    # list_input_char += ["ú","ù","ủ","ũ","ụ","ư","ứ","ừ","ữ","ử","ự"]
    # list_input_char += ["Ú","Ù","Ủ","Ũ","Ụ","Ư","Ứ","Ừ","Ử","Ữ","Ự"]
    # list_input_char += ["í","ì","ỉ","ị","ĩ"]
    # list_input_char += ["Í","Ì","Ỉ","Ị","Ĩ"]
    # list_input_char += ["ý","ỳ","ỷ","ỵ","ỹ"]
    # list_input_char += ["Ý","Ỳ","Ỷ","Ỵ","Ỹ"]

    list_output_char = []
    
    for input_char in list_input_char:
        # input_char = 'á'
        encoded_char  = encode_vi_char(input_char)
        list_output_char.append(encoded_char)

    d_encode = {}
    d_decode = {}
    for i,_ in enumerate(list_input_char):
        input_char = list_input_char[i]
        output_char = list_output_char[i]
        d_encode[input_char] = output_char
        d_decode[output_char] = input_char

    save_dict_to_picker_file(d_encode,'d_encode')
    save_dict_to_picker_file(d_decode,'d_decode')

    # load_dict_from_picker_file('d_encode')
    # load_dict_from_picker_file('d_decode')

    # d_encode['â']
    # key  = '\\u00e2'
    # key = key[0:2] + key[2:].upper()
    # d_decode[key]