import tkinter as tk
import os

# Destroying the save window
def saved_del():
    saved.destroy()

# Saved message GUI
def saved():
    global saved
    saved = tk.Toplevel(screen9)
    saved.title("Saved")
    saved.geometry("300x75")
    tk.Label(saved, text = "File saved").pack()
    tk.Button(saved, text = "OK", command = saved_del).pack()

# Saving the info
def save():
    filename = raw_filename.get()
    note = raw_note.get()

    data = open(filename, "w")
    data.write(note)
    data.close()

    saved()

# Note creation
def create_note():
    global screen9
    global raw_note
    global raw_filename
    raw_filename = tk.StringVar()
    raw_note = tk.StringVar()
    
    screen9 = tk.Toplevel(screen)
    screen9.title("Info")
    screen9.geometry("400x350")
    tk.Label(screen9, text = "Please enter a filename for the note below: ").pack()
    tk.Entry(screen9, textvariable = raw_filename).pack()
    tk.Label(screen9, text = "Please enter a note for the file below: ").pack()
    tk.Entry(screen9, textvariable = raw_note).pack()
    tk.Button(screen9, text = "Save", command = save).pack()

def delete_note1():
    filename3 = raw_filename2.get()
    os.remove(filename3)
    screen13 = tk.Toplevel(screen)
    screen13.title("Delete")
    screen13.geometry("400x400")
    tk.Label(screen13, text = filename3 + " removed").pack()

def delete_note():
    screen12 = tk.Toplevel(screen)
    screen12.title("DELETE")
    screen12.geometry("350x300")
    all_files = os.listdir()
    tk.Label(screen12, text = "Select the file to delete from below.").pack()
    tk.Label(screen12, text = all_files).pack()
    global raw_filename2
    raw_filename2 = tk.StringVar()
    tk.Entry(screen12, textvariable = raw_filename2).pack()
    tk.Button(screen12, text = "Delete", command = delete_note1).pack()

def view_note1():
    filename1 = raw_filename1.get()
    data1 = open(filename1, "r")
    data2 = data1.read()
    screen11 = tk.Toplevel(screen)
    screen11.title("Note")
    screen11.geometry("400x400")
    tk.Label(screen11, text = data2).pack()
    tk.Button(screen11, text = "DELETE", command = delete_note).pack()

def view_note():
    screen10 = tk.Toplevel(screen)
    screen10.title("Note")
    screen10.geometry("350x300")
    all_files = os.listdir()
    tk.Label(screen10, text = "Please use one of the file below.").pack()
    tk.Label(screen10, text = all_files).pack()
    global raw_filename1
    raw_filename1 = tk.StringVar()
    tk.Entry(screen10, textvariable = raw_filename1).pack()
    tk.Button(screen10, text = "Ok", command = view_note1).pack()

# Starting a session
def session():
    global screen8
    screen8 = tk.Toplevel(screen)
    screen8.title("Session")
    screen8.geometry("500x500")
    tk.Label(screen8, text = "Welcome to the dashboard.").pack()
    tk.Label(screen8, text = "").pack()
    tk.Button(screen8, text = "Create note", command = create_note).pack()
    tk.Label(screen8, text = "").pack()
    tk.Button(screen8, text = "View notes", command = view_note).pack()
    tk.Label(screen8, text = "").pack()
    tk.Button(screen8, text = "Delete a note", command = delete_note).pack()


def login_successful():
    session()


# Result window delete
def delete2():
    result1.destroy()
   
def delete3():
    result2.destroy()

def delete4():
    result3.destroy()
 
# Result widow
def result1():
    global result1
    result1 = tk.Toplevel(screen2)
    result1.geometry("300x75")
    result1.title("Title")
    tk.Label(result1, text = "Login successful!", bg = "green", font = ("calibri", 24)).pack()
    tk.Button(result1, text = "continue", command = delete2).pack()
    login_successful()


def result2():
    global result2
    result2 = tk.Toplevel(screen2)
    result2.geometry("300x75")
    result2.title("Title")
    tk.Label(result2, text = "Incorrect username or password!", font = ("calibri", 16)).pack()
    tk.Button(result2, text = "continue", command = delete3).pack()

def result3():
    global result3
    result3 = tk.Toplevel(screen1)
    result3.geometry("320x75")
    result3.title("Title")
    tk.Label(result3,text = "Registration successful!", bg = "green", font = ("calibri", 24)).pack()

# Working of the Registration button
def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
    username_entry.delete(0, 1234)
    password_entry.delete(0, 1234)
    result3()

# Working of the Login button
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0,1234)
    password_entry1.delete(0,1234)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            result1()
        else:
            result2()
    else:
        result2()

# Registration window GUI
def register():
    global screen1
    screen1 = tk.Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")
    global username_entry
    global password_entry
    global username
    global password

    username = tk.StringVar()
    password = tk.StringVar()
    tk.Label(screen1, text = "Please enter details.").pack()
    tk.Label(screen1, text = "").pack()
    tk.Label(screen1, text = "Username *").pack()  
    username_entry = tk.Entry(screen1, textvariable = username)
    username_entry.pack()
    tk.Label(screen1, text = "Password *").pack()
    password_entry = tk.Entry(screen1, textvariable = password)
    password_entry.pack()
    tk.Button(screen1, text = "Register", width = 10, height = 2, command = register_user).pack()

# Login window GUI
def login():
    global screen2
    screen2 = tk.Toplevel(screen)
    screen.title("Login")
    screen2.geometry("300x250")
    tk.Label(screen2, text = "Please enter details to login.").pack()
    tk.Label(screen2, text = "").pack()

    global username_verify
    global password_verify
    global username_entry1
    global password_entry1

    username_verify = tk.StringVar()
    password_verify = tk.StringVar()

    tk.Label(screen2, text = "Username *").pack()
    username_entry1 = tk.Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    
    tk.Label(screen2, text = "Password *").pack()
    password_entry1 = tk.Entry(screen2, textvariable = password_verify)
    password_entry1.pack()
    tk.Label(screen2, text = "").pack()
    tk.Button(screen2, text = "Login", width = 10, height = 2, command = login_verify).pack()

# First widow GUI.
def main_screen():
    global screen
    screen = tk.Tk()
    screen.geometry("300x250")
    screen.title("Login info")
    tk.Label(text= "Login Info", bg = "gray", width = "300", height = "2", font = ("Ariel", 14)).pack()
    tk.Label(text = "").pack()
    tk.Button(text = "Log in", height = 2, width = 30, command = login).pack()
    tk.Label(text = "").pack()
    tk.Button(text = "register", height = 2, width = 30, command = register).pack()
    screen.mainloop()

main_screen()
