from pyperclip import copy
from contact_info import cont_info as conti

def admin_intro(name:str):
    """Copies all of the contact points """
    copy(f"You can reach {conti[name]["name"].split()[0]} by calling {conti[name]["phone"]} or emailing {conti[name]["email"]}. Additionally, I would recommend scheduling an appointment by following this link: {conti[name]["meeting"]}")

def admin_contact(name:str, contact:str):
    copy(conti[name][contact])

if __name__=="__main__":
    print("hello world")