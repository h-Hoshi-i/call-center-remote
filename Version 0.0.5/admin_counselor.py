from pyperclip import copy
from contact_info import cont_info as conti

def admin_intro(name:str):
    """Copies all of the contact points """
    copy(f"To reach {conti[name]["name"].split()[0]} you can call {conti[name]["phone"]} or email {conti[name]["email"]}. Alternitivly I would reccomend scheduling and appointment by following this link: {conti[name]["meeting"]}")

def admin_contact(name:str, contact:str):
    copy(conti[name][contact])

if __name__=="__main__":
    print("hello world")