import tkinter as tk
from tkinter import ttk
from Classes.vote import Vote, Vote_all
from .voting_add import VotingAdd
import matplotlib.pyplot as plt

class VotingManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Votes Management")
        # userlist to class
        self.vote_all = Vote_all()
        # put items into the class
        self.tree = ttk.Treeview(self.root, columns=("Number", "Name", "StartTime", "EndTime"))
        self.tree.column("#0", width=0)  # ID width
        self.tree.heading("#0", text="")
        self.tree.heading("Number", text="Number")
        self.tree.column("#1", width=50) 
        self.tree.heading("Name", text="Name")
        self.tree.column("#2", width=300) 
        self.tree.heading("StartTime", text="StartTime")
        self.tree.heading("EndTime", text="EndTime")
        self.update_table()
        self.add_button = tk.Button(self.root, text="Add New", command=lambda: self.add_new())
        self.export_button = tk.Button(self.root, text="Export Pie", command=lambda: self.get_pie())

        self.tree.pack()

        placeholder_frame = tk.Frame(self.root)
        placeholder_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        self.add_button.pack(side=tk.LEFT, padx=10)
        self.export_button.pack(side=tk.LEFT, padx=10)
        # pack the layout

    def add_new(self):
        VotingAdd(self, self.vote_all.vote_list)
        # self.update_table()

    def update_table(self):
        # This function is for every time user_list is modified will be used for updating
        for row in self.tree.get_children():
            self.tree.delete(row)
        self.vote_all.vote_list = Vote_all().vote_list
        # update data
        for i, vote in enumerate(self.vote_all.vote_list):
            self.tree.insert("", "end", values=(vote.number, vote.name, vote.start_time, vote.end_time))

    def get_pie(self):
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
            tk.messagebox.showwarning("Warning", "Selecting Wrong")
            return
        
        data = selected.choices
        labels = list(data.keys())
        sizes = list(data.values())

        if (sum(sizes) == 0):
            tk.messagebox.showwarning("Warning", "No voting is maked!")
            return
        
        # create a pie
        fig, ax = plt.subplots()
        ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

        # set title
        ax.set_title('Pie Chart')

        # figure save
        plt.savefig("./Visualization/"+ str(selected.number) + ".jpg")

        tk.messagebox.showwarning("Success", "Success!")
        return
