import json
from datetime import datetime

class Vote_all:

    def __init__(self) -> None:
        try:
            # open json file and read the data pre-stored.
            with open("./Data/votes.json", "r") as file:
                vote_data = json.load(file)
            # initialization the list
            self.vote_list = [Vote(vote["index"], vote["name"], 
                               vote["choices"], vote["start_time"], vote["start_time"]) 
                               for vote in vote_data]
        except FileNotFoundError:
            # empty file, wrong
            return None
        
        self.vote_count = len(self.vote_list) + 1

    def update_file(self, votes):
        with open("./Data/votes.json", "w") as file:
            user_data = [{"index": vote.number, 
                      "name": vote.name, 
                      "choices": vote.choices,
                      "start_time": vote.start_time, 
                      "end_time": vote.end_time}
                    for vote in votes]
            json.dump(user_data, file, indent=2)

class Vote:

    def __init__(self, number, name, choices, start_time, end_time) -> None:
        self.number = number
        self.name = name
        self.choices = choices
        self.start_time = start_time
        self.end_time = end_time
        
    def voting():
        pass




def initialize_voting():

    votes = [
        # only 2 classification user are considered, 0 means admin, 1 means user.
        Vote("1", "Student union presedent selection", 
             {"John Doe":0, "Tom Sivan":1, "Troye Sam": 2}, datetime(2023, 11, 10, 12, 30, 0).strftime("%Y-%m-%d %H:%M:%S"), 
             datetime(2023, 12, 10, 12, 30, 0).strftime("%Y-%m-%d %H:%M:%S")),
        Vote("2", "Are you done the homework?", 
             {"Yes":0, "No":1}, datetime(2023, 10, 10, 12, 30, 0).strftime("%Y-%m-%d %H:%M:%S"), 
             datetime(2023, 12, 10, 12, 59, 0).strftime("%Y-%m-%d %H:%M:%S"))
        # ...
    ]

    # store the data into json file.
    with open("./Data/votes.json", "w") as file:
        user_data = [{"index": vote.number, 
                      "name": vote.name, 
                      "choices": vote.choices,
                      "start_time": vote.start_time, 
                      "end_time": vote.end_time}
                    for vote in votes]
        json.dump(user_data, file, indent=2)

        
if __name__ == "__main__":
    
    initialize_voting()
    print(Vote_all().vote_list)
    # users = Users()
    # print(users.user_list)