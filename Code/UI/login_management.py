import tkinter as tk
from tkinter import messagebox
from Classes.user import Users
from .user_management import UserManagementSystem
from .voting_management import VotingManagement
from .voting_user import VotingUser
 
 # As login frame only need in VERTICAL, so grid is used as layout.
class LoginManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.user = None
        self.user_list = Users().user_list

        # create the input box and label on username and password.
        self.username_label = tk.Label(root, text="Username:")
        self.username_label.grid(row=0, column=0, padx=10, pady=10)

        self.username_entry = tk.Entry(root)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        self.password_label = tk.Label(root, text="Password:")
        self.password_label.grid(row=1, column=0, padx=10, pady=10)

        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        # create the login botton
        self.login_button = tk.Button(root, text="Login", command=lambda: self.on_login_button_click())
        self.login_button.grid(row=2, column=0, columnspan=2, pady=10)

    def validate_login(self, username, password):
        # check whether the input is right or not.
        
        for user in self.user_list:
            if username == user.username and password == user.password:
                self.user = user
                return True
        return False

    def on_login_button_click(self):
        # get input from user.
        username = self.username_entry.get()
        password = self.password_entry.get()

        # validate the massage and inform user of massage.
        if self.validate_login(username, password):
            messagebox.showinfo("Success", "Welcome back, {}".format(self.user.name))

            self.root.destroy()
            
            if self.user.identify == '0':
                root = tk.Tk()
                UserManagementSystem(root, self.user_list)
            else:
                root = tk.Tk()
                VotingUser(root)
        else:
            messagebox.showerror("Error", "Username or password wrong!")

