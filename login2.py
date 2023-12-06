from tkinter import *   # Import tkinter
from PIL import ImageTk # Import ImageTk

class Login:    
    def __init__(self, root):   
        self.root = root   # Create a root window
        self.root.title("Login System") # Set title
        self.root.geometry("1110x560+100+50") # Set window size
        self.root.resizable(False, False)   # Disable maximize window

        #background image
        self.bg = ImageTk.PhotoImage(file="image/1.jpg")    # Load image
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1) # Place image

        # Login frame
        Frame_login = Frame(self.root, bg="white")  # Create frame
        Frame_login.place(x=330, y=150, width=450, height=360) # Place frame

        # Title & subtitle
        tittle = Label(Frame_login, text="Login here", font= ("Impact", 35, "bold"), fg="#FF90BC", bg="white").place(x=90, y=20) # Place title
        subtitle = Label(Frame_login, text="Member Login Area", font=("times new roman", 15, "bold"), fg="#8ACDD7", bg="white").place(x=90, y=85)   # Place subtitle

        # Username
        lbl_user = Label(Frame_login, text="Username", font=("times new roman", 12, "bold"), fg="gray", bg="white").place(x=90, y=125)  # Place label
        self.username = Entry(Frame_login, font=("times new roman", 15), bg="lightgray")    # Create entry
        self.username.place(x=90, y=150, width=280, height=30)  # Place entry

        # Password
        lbl_password = Label(Frame_login, text="Password", font=("times new roman", 12, "bold"), fg="gray", bg="white").place(x=90, y=190)  # Place label
        self.password = Entry(Frame_login, font=("times new roman", 15), bg="lightgray")    # Create entry
        self.password.place(x=90, y=220, width=280, height=30)  # Place entry

        # Button
        forget = Button(Frame_login, text="Forget Password?", cursor="hand2", bg="white", fg="#8ACDD7", bd=0, font=("times new roman", 12)).place(x=90, y=260)  # Place button
        submit = Button(Frame_login, text="Login?", cursor="hand2", fg="white", bg="#8ACDD7", bd=0, font=("times new roman", 15)).place(x=90, y=290, width=180, height=35)  # Place button
        


root = Tk() # Create window
obj = Login(root) # Create object
root.mainloop() # Keep the window open


