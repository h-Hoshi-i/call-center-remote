from pyperclip import copy
from contact_info import cont_info as conti

def gen_contact(name:str, contact:str):
    copy(conti[name][contact])