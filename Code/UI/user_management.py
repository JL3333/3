import tkinter as tk
from tkinter import ttk
from Classes.user import User
from .voting_management import VotingManagement

class UserManagementSystem:
    def __init__(self, root, users):
        self.root = root
        self.root.title("User Management")

        # userlist to class
        self.user_list = users

        # put items into the class
        self.tree = ttk.Treeview(root, columns=("username", "password", "name", "identify"))
        self.tree.column("#0", width=0)  # ID 列宽
        self.tree.heading("#0", text="")
        self.tree.heading("username", text="Username")
        self.tree.heading("password", text="Password")
        self.tree.heading("name", text="Name")
        self.tree.heading("identify", text="Identify")
        self.update_table()
        self.add_button = tk.Button(root, text="Add User", command=self.show_new_root)
        self.vote_enter_button = tk.Button(root, text="Enter Vote Section", 
                               command=lambda: self.enter_vote(root))
        
        # pack the layout
        self.tree.pack()

        placeholder_frame = tk.Frame(root)
        placeholder_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)


        self.add_button.pack(side=tk.LEFT, padx=10)
        self.vote_enter_button.pack(side=tk.LEFT, padx=10)

    def show_new_root(self):
        new_root = tk.Toplevel(self.root)
        new_root.geometry("300x200")
        new_root.title("Add User")

        # add frame items.
        tk.Label(new_root, text="Username:").pack()
        username_entry = tk.Entry(new_root)
        username_entry.pack()

        tk.Label(new_root, text="Password:").pack()
        password_entry = tk.Entry(new_root)
        password_entry.pack()

        tk.Label(new_root, text="Name:").pack()
        name_entry = tk.Entry(new_root)
        name_entry.pack()

        tk.Label(new_root, text="Identify(0-Admin, 1-User):").pack()
        iden_entry = tk.Entry(new_root)
        iden_entry.pack()

        add_button = tk.Button(new_root, text="Add", 
                               command=lambda: self.add_user(username_entry.get(), 
                                                             password_entry.get(), 
                                                             name_entry.get(),
                                                             iden_entry.get(),
                                                             new_root))
        add_button.pack()

    def enter_vote(self, new_root):
        root = tk.Toplevel()
        VotingManagement(root)
        # new_root.destroy()

    def add_user(self, username, password, name, iden, new_root):
        if username:
            user = User(username, password, name, iden)
            self.user_list.append(user)
            self.update_table()
            new_root.destroy()
        else:
            tk.messagebox.showwarning("Warning", "Please enter a username.")

    def update_table(self):
        # This function is for every time user_list is modified will be used for updating
        for row in self.tree.get_children():
            self.tree.delete(row)

        # update data
        for i, user in enumerate(self.user_list):
            self.tree.insert("", "end", values=(user.username, user.password, user.name, user.identify))
