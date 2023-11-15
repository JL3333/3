import tkinter as tk
from tkinter import ttk
from Classes.vote import Vote, Vote_all

class VotingUser:
    def __init__(self, root):
        self.root = root
        self.root.title("Votes Users")
        # userlist to class
        self.vote_all = Vote_all()
        print(self.vote_all.vote_list)
        # put items into the class
        self.tree = ttk.Treeview(root, columns=("Number", "Name", "StartTime", "EndTime"))
        self.tree.column("#0", width=0)  # ID width
        self.tree.heading("#0", text="")
        self.tree.heading("Number", text="Number")
        self.tree.column("#1", width=50) 
        self.tree.heading("Name", text="Name")
        self.tree.column("#2", width=300) 
        self.tree.heading("StartTime", text="StartTime")
        self.tree.heading("EndTime", text="EndTime")
        self.update_table()
        self.add_button = tk.Button(root, text="Select", command=self.show_new_root)

        # pack the layout
        self.tree.pack()
        self.add_button.pack()

    def show_new_root(self):
        selected_item = self.tree.selection()
        number = self.tree.item(selected_item, "values")[0]
        
        if (not selected_item):
            tk.messagebox.showwarning("Warning", "Please do selection!")
            return
       
        
        selected = None
        for vote in self.vote_all.vote_list:
            if vote.number == number:
                selected = vote

        if (not selected_item) or (selected is None):
            tk.messagebox.showwarning("Warning", "Please select a vote.")
            return

        new_root = tk.Toplevel()
        new_root.title("Select your choice")
        new_root.geometry("300x200")

        # add frame items.
        tk.Label(new_root, text="Question:\n" + selected.name + '\n').pack(side=tk.TOP)

        combobox = ttk.Combobox(new_root, 
                                values=[key for key in selected.choices.keys()])
        combobox.set("Select an option")  
        combobox.pack(pady=10)

        add_button = tk.Button(new_root, text="Submit", 
                               command=lambda: self.make_selection(
                                   selected, combobox.get(), new_root))
        add_button.pack()


    def make_selection(self, selected, combobox, new_root):
        if not combobox == 'Select an option':
            # print(ombobox)
            selected.choices[combobox] += 1
            print(self.vote_all.vote_list)
            self.vote_all.update_file(self.vote_all.vote_list)
            self.update_table()
            new_root.destroy()
        else:
            tk.messagebox.showwarning("Warning", "Please make your selection.")

    def update_table(self):
        # This function is for every time user_list is modified will be used for updating
        for row in self.tree.get_children():
            self.tree.delete(row)

        # update data
        for i, vote in enumerate(self.vote_all.vote_list):
            self.tree.insert("", "end", values=(vote.number, vote.name, vote.start_time, vote.end_time))
