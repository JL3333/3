import tkinter as tk
from Classes.vote import Vote_all, Vote

class VotingAdd:
    def __init__(self, votingManagement, voting_list):
        self.root = tk.Tk()
        self.votingManagement = votingManagement
        self.root.geometry('250x300')
        self.root.title("Add new voting")
        self.voting_list = voting_list

        self.choice_boxes = []  # for store the choices

        tk.Label(self.root, text="Question: ").pack()
        self.question = tk.Entry(self.root)
        self.question.pack()

        tk.Label(self.root, text="Start From: ").pack()
        self.start = tk.Entry(self.root)
        self.start.pack()

        tk.Label(self.root, text="End util: ").pack()
        self.end = tk.Entry(self.root)
        self.end.pack()

        self.add_button = tk.Button(self.root, 
                                    text="Add choices", 
                                    command=self.add_choice_boxes)
        self.add_button.pack(pady=10)


        self.show_content_button = tk.Button(self.root, 
                                             text="Add", 
                                             command=self.update_file)
        self.show_content_button.pack(pady=10)

        self.root.mainloop()


    def add_choice_boxes(self):
        new_choice_boxes = tk.Entry(self.root)
        new_choice_boxes.pack(pady=5)
        self.choice_boxes.append(new_choice_boxes)


    def update_file(self):
        content_list = {value: 0 
                        for value in 
                        [choice_boxes.get() for choice_boxes in self.choice_boxes]}
        
        question = self.question.get()
        start = self.start.get()
        end = self.end.get()


        temp = Vote_all()
        self.voting_list.append(Vote(str(temp.vote_count), question, content_list, start, end))
        print(content_list)
        Vote_all.update_file(temp, self.voting_list)
        self.votingManagement.update_table()
        self.root.destroy()

