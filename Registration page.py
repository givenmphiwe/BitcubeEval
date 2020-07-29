#importing all the modules i will need
from tkinter import *
from tkinter import messagebox
import re
import os

#CallbackFunction for validating user phone number

def validate_phoneno(user_phoneno):
    if user_phoneno.isdigit():
        return True
    elif user_phoneno is "":
        return True
    else:
        messagebox.showinfo('information','This is not a valid email address')
        return False

#Function for validating email address
def isValidEmail(user_email):
    if len(user_email)> 6:
        if re.match("^,+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(J?)$", user_email) !=None:
            return True
        return False
    else:
        messagebox.showinfo('Information', 'invalid Password')
        return False

#Function for validating passsword
def isValidPassword(user_pwd):
    if len(user_pwd)> 6:
        if re.match("^,+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(J?)$", user_pwd) !=None:
            return True
        return False
    else:
        messagebox.showinfo('Error', 'Invalid password')
        return False
    
#Function for validating all other User Input Fields

def validateAllFields():
    if v_fName.get() =="":
        messagebox.showinfo('Information', 'Please enter fullName')

    elif v_pwd.get() == "":
        messagebox.showinfo('Information', 'Please enter password')
        
    elif v_confirmPwd.get() == "":
        messagebox.showinfo('Information', 'Please confirm password')
            
    elif v_phoneNo.get() == "":
        messagebox.showinfo('Information', 'please enter your phone number')

    elif v_phoneNo.get() == "":
             messagebox.showinfo('Information', 'make sure your phone is 10 digit')

    elif v_emailId.get() == "":
        messagebox.showinfo('Information', 'Enter your email address')

    elif v_gender.get() == 0:
        messagebox.showinfo('Information', 'select gender to proceed')

    elif v_country.get() == "" or v_country.get() == "select Your country":
        messagebox.showinfo('Information', 'select country')

    elif varl_skill.get() == 0:
        messagebox.showinfo('Information', 'select skill to proceed')

    elif v_pwd.get() != v_confirmPwd.get():
        messagebox.showinfo('Information', 'confirmation password don"t match ')

    elif v_emailId.get() != "":
        status = isValidEmail(v_emailId.get())
        if(status):
            messagebox.showinfo('Information', 'user Registered succefully')
    else:
        messagebox.showinfo('Information', 'Registered Successfully')
        

#Function to clear all user input fields
def clearAllFields():
    v_fName.set("")
    v_pwd.set("")
    v_confirmPwd.set("")
    v_phoneNo.set("")
    v_emailId.set("")

def callNewScreen():
    window.destroy()
    #user os.system('sendEmail.py if the file id in same locarion else use os.system('python sendEmail.py)
    os.system('python LoginScreen.py')

#To create the main window for application, we use Tk class
window = Tk()

window.title("Registration page")

#window.geometry(), set the size of the window and winfow.configure(), et its background color

window.geometry('500x500')
window.configure(background = "light green")

v_fName = StringVar()
v_pwd = StringVar()
v_confirmPwd = StringVar()
v_phoneNo = StringVar()
v_emailId = StringVar()
v_gender = IntVar()
v_country = StringVar()
v_skills = StringVar()

#Label wodget implements a display box where you can place text or images
lb_heading=Label(window,text="Login Screen", width=20, font=("bold",20), bg="light blue")
lb_heading.place(x=90,y=53)

lb_fullname=Label(window,text="FullName", width=20, font=("bold", 10), bg="light green")
lb_fullname.place(x=80,y=130)

#Entry will allow user to enter any kind of values
entry_fullname=Entry(window, textvariable = v_fName)
entry_fullname.place(x=240,y=130)

lb_pwd=Label(window,text="Password", width=20, font=("bold", 10), bg="light green")
lb_pwd.place(x=80,y=170)
entry_pwd=Entry(window, show="*", textvariable = v_pwd)
entry_pwd.place(x=240,y=170)

lb_confirm_pwd=Label(window,text="Confirm Password", width=20, font=("bold", 10), bg= "light green")
lb_confirm_pwd.place(x=80,y=210)
entry_confirm_pwd=Entry(window, show="*", textvariable = v_confirmPwd)
entry_confirm_pwd.place(x=240,y=210)

lb_phoneno=Label(window,text="Phone No.", width=20, font=("bold", 10), bg="light green")
lb_phoneno.place(x=80,y=250)
entry_phoneno=Entry(window, textvariable = v_phoneNo)
entry_phoneno.place(x=240,y=250)

#Register Callback function to validate phone number
valid_phoneno = window.register(validate_phoneno)
#Pass optionvalueto callback function -validate(when to validate), validatecommand (which function to call)
# %p is an specifier
entry_phoneno.config(validate="key", validatecommand=(valid_phoneno, '%p'))

lb_email=Label(window,text="Email", width=20, font=("bold", 10), bg="light green")
lb_email.place(x=80,y=290)
entry_email=Entry(window, textvariable = v_emailId)
entry_email.place(x=240,y=290)                                                      

lb_gender=Label(window,text="Gender", width=20, font=("bold", 10), bg="light green")
lb_gender.place(x=80,y=330)
Radiobutton(window, text="Male", bg="light green", padx=5, variable=v_gender, value=1).place(x=230,y=330)
Radiobutton(window, text="Female", bg="light green", padx=20, variable=v_gender, value=2).place(x=290,y=330)
                                                      
lb_country=Label(window,text="Country", width=20, font=("bold",10), bg="light green")
lb_country.place(x=80,y=370)
list_country = ['South africa', 'Mozambique', 'Zimbabwe', 'swaziland'];

# *list_country shows all items in the list vertically
droplist=OptionMenu(window,v_country, *list_country)                                                      
droplist.config(width=16, bg="light green")
v_country.set('Select Your Country')
droplist.place(x=240,y=370)

               
lb_skills=Label(window,text="Term and Condition",width=20, font=("bold",10), bg="light green")
lb_skills.place(x=80,y=410)
varl_skill=IntVar()
Checkbutton(window, text="T&C's", bg="light blue", variable=varl_skill).place(x=230,y=410)
                                                      
                                                      
btn_login = Button(window, text="LOGIN", command = validateAllFields, bg="dark blue", fg = "white", font=("bold", 10)).place(x=150, y=450)
btn_clear = Button(window, text="CLEAR", command = clearAllFields, bg="dark blue", fg = "white", font=("bold", 10)).place(x=250, y=450)
btn_existinguser = Button(window, text="Existing User?", command = callNewScreen, bg="dark green", fg = "white", font=("bold")).place(x=330, y=450)

window.mainloop()  
