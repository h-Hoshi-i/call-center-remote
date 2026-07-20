import tkinter as tk
import pyperclip as clip
import AppSubmittedOnline as appsub
import compileEmail as morne
import dashboard
import admin_counselor as admic
import general_contact as genec
import contact_info

# Create the main window
root = tk.Tk()
root.attributes('-topmost', True)
root.attributes("-toolwindow", 1)
root.title("")
root.geometry("100x100")
root.configure(background="#9370DB")

saved_username = "Nathaniel"

def clear_screen():
    """Destroys all widgets currently in the root window"""
    for widget in root.winfo_children():
        widget.destroy()

def users():
    """Select the user either by typing your name or skipping and default is 'Nathaniel'."""
    clear_screen()
    root.geometry("100x150")

    user_var = tk.StringVar()

    all_users = tk.Label(root, text="SELECT USER", bg="#9370DB")
    all_users.pack()

    user_input = tk.Entry(root, textvariable=user_var, bg="#E2D6FF")
    user_input.pack()

    def save_user():
        global saved_username
        saved_username = user_var.get()  # Gets value when button is clicked
        print(f"Selected user: {saved_username}")
        selection_screen()
        return saved_username

    tk.Button(root, text="Confirm", command=save_user, bg="#E2D6FF").pack()
    tk.Button(root, text="SKIP", command=selection_screen, bg="#E2D6FF").pack()

def selection_screen():
    """Select the campaign you are working form"""
    clear_screen()
    root.geometry("100x165")

    tk.Label(root, text="Tasks", bg= "#9370DB").pack()
    tk.Button(root, text="Admissions", command=hoshi_admissions, bg="#E2D6FF").pack()
    tk.Button(root, text="EMAILS", command=morning_email, bg="#E2D6FF").pack()
    tk.Button(root, text = "SLATE DASH", command=slate_dash, bg="#E2D6FF").pack()
    tk.Button(root, text="CONTACTS", command=gen_contact_select, bg="#E2D6FF").pack()
    tk.Button(root, text="BACK", command=users, bg="#C9A3D1").pack()

def slate_dash():
    clear_screen()
    root.geometry("100x150")
    tk.Label(root, text="GET CALLING >:(", bg="#9370DB").pack()
    tk.Button(root, text="vm form", command=dashboard.open_record_and_form, bg="#E2D6FF").pack()
    tk.Button(root, text="email", command=lambda: dashboard.dashboard_email(saved_username), bg="#E2D6FF").pack()
    tk.Button(root, text="BACK", command=selection_screen, bg="#C9A3D1").pack()

def gen_contact_select():
    clear_screen()
    root.geometry("100x195")
    tk.Label(root, text="CONTACT INFO", bg="#9370DB").pack()
    tk.Button(root, text="IT", command=lambda:gen_contact_screen("IT"), bg="#E2D6FF").pack()
    tk.Button(root, text="Myaccess", command=lambda:gen_contact_screen("myaccess"), bg="#E2D6FF").pack()
    tk.Button(root, text="Talge Hall", command=lambda:gen_contact_screen("talge"), bg="#E2D6FF").pack()
    tk.Button(root, text="Thatcher Hall", command=lambda:gen_contact_screen("thatcher"), bg="#E2D6FF").pack()
    tk.Button(root, text="ADMIN COUNS", command=admin_c_select_page_1, bg="#E2D6FF").pack()
    tk.Button(root, text="BACK", command=selection_screen, bg="#C9A3D1").pack()

def gen_contact_screen(name:str):
    clear_screen()
    tk.Label(root, text=f"{name.upper()}'s page", bg="#9370DB").pack()
    tk.Button(root, text="Copy NAME", command=lambda:genec.gen_contact(name,"name"), bg="#E2D6FF").pack()
    tk.Button(root, text=f"{contact_info.cont_info[name]["phone"]}", command=lambda:genec.gen_contact(name,"phone"), bg="#E2D6FF").pack()
    tk.Button(root, text=f"{contact_info.cont_info[name]["email"]}", command=lambda:genec.gen_contact(name,"email"), bg="#E2D6FF").pack()
    tk.Button(root, text="BACK", command=gen_contact_select, bg="#C9A3D1").pack()

def morning_email():
    clear_screen()
    root.geometry("100x150")
    tk.Label(root, text="STAY HAPPY", bg= "#9370DB").pack()
    
    def roughdraft_email():
        result = morne.select_email("base", user_name=saved_username)
        #print(result)
        clip.copy(result)
    def swag():
        result = morne.select_email("swag", user_name=saved_username)
        clip.copy(result)
    tk.Button(root, text="base email", command=roughdraft_email, bg="#E2D6FF").pack()
    tk.Button(root, text="teacher swag", command=swag, bg="#E2D6FF").pack()
    tk.Button(root, text="ADMIN COUNS", command=admin_c_select_page_1, bg="#E2D6FF").pack()
    tk.Button(root, text="BACK", command=selection_screen, bg="#C9A3D1").pack()

def admin_c_select_page_1():
    clear_screen()
    root.geometry("100x230")
    tk.Label(root, text="CONTACT INFO", bg="#9370DB").pack()
    tk.Button(root, text="Brenda", command=lambda:admin_contact_screen("brenda"), bg="#E2D6FF").pack()
    tk.Button(root, text="Brittany", command=lambda:admin_contact_screen("brittany"), bg="#E2D6FF").pack()
    tk.Button(root, text="Daniela", command=lambda:admin_contact_screen("daniela"), bg="#E2D6FF").pack()
    tk.Button(root, text="Emily", command=lambda:admin_contact_screen("emily"), bg="#E2D6FF").pack()
    tk.Button(root, text="Grace", command=lambda:admin_contact_screen("grace"), bg="#E2D6FF").pack()
    tk.Button(root, text="PAGE 2", command=admin_c_select_page_2, bg="#E2D6FF").pack()
    tk.Button(root, text="BACK", command=gen_contact_select, bg="#C9A3D1").pack()

def admin_c_select_page_2():
    clear_screen()
    root.geometry("100x200")
    tk.Label(root, text="CONTACT INFO", bg="#9370DB").pack()
    tk.Button(root, text="Jessica", command=lambda:admin_contact_screen("jessica"), bg="#E2D6FF").pack()
    tk.Button(root, text="Leticia", command=lambda:admin_contact_screen("leticia"), bg="#E2D6FF").pack()
    tk.Button(root, text="Rosa", command=lambda:admin_contact_screen("rosa"), bg="#E2D6FF").pack()
    tk.Button(root, text="Stahl", command=lambda:admin_contact_screen("stahl"), bg="#E2D6FF").pack()
    tk.Button(root, text="PAGE 1", command=admin_c_select_page_1, bg="#E2D6FF").pack()
    tk.Button(root, text="BACK", command=gen_contact_select, bg="#C9A3D1").pack()

def admin_contact_screen(name):
    clear_screen()
    root.geometry("150x185")
    tk.Label(root, text=f"{name.upper()}'s page", bg="#9370DB").pack()
    tk.Button(root, text="Copy Intro", command=lambda:admic.admin_intro(name), bg="#E2D6FF").pack()
    tk.Button(root, text="Copy NAME", command=lambda:admic.admin_contact(name,"name"), bg="#E2D6FF").pack()
    tk.Button(root, text=f"{contact_info.cont_info[name]["phone"]}", command=lambda:admic.admin_contact(name,"phone"), bg="#E2D6FF").pack()
    tk.Button(root, text=f"{contact_info.cont_info[name]["email"]}", command=lambda:admic.admin_contact(name,"email"), bg="#E2D6FF").pack()
    tk.Button(root, text="Copy MEET LINK", command=lambda:admic.admin_contact(name,"meeting"), bg="#E2D6FF").pack()
    tk.Button(root, text="BACK", command=admin_c_select_page_1, bg="#C9A3D1").pack()

def hoshi_admissions():
    clear_screen()
    root.geometry("100x150")

    tk.Label(root, text=f"Hello {saved_username}", bg= "#9370DB").pack()
    tk.Button(root, text="Run All", command=appsub.process, bg="#E2D6FF").pack()
    tk.Label(root, text="Split", bg= "#9370DB").pack()
    tk.Button(root, text="EMAIL", command= appsub.write_email, bg="#E2D6FF").pack()
    tk.Button(root, text="FORM", command= appsub.fillout_submitForm, bg="#E2D6FF").pack()
    tk.Button(root, text="BACK", command=selection_screen, bg="#C9A3D1").pack()

users()

root.mainloop()