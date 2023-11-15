import json

class Users:
    def __init__(self) -> None:
        try:
            # open json file and read the data pre-stored.
            with open("./Data/users.json", "r") as file:
                user_data = json.load(file)
            # initialization the list
            self.user_list = [User(user["username"], user["password"], 
                               user["name"], user["identify"]) 
                               for user in user_data]
        except FileNotFoundError:
            # empty file, wrong
            return None

class User:

    def __init__(self, username, password, name, identify):
        self.username = username
        self.password = password
        self.name = name
        self.identify = identify



def initialize_users():

    users = [
        # only 2 classification user are considered, 0 means admin, 1 means user.
        User("Admin", "pass1", "John Doe", "0"),
        User("Bob1", "pass2", "David Doe", "1"),
        User("Alice1", "pass3", "Alice Doe", "1"),
        User("1", "1", "Alice Doe", "1"),
        # ...
    ]

    # store the data into json file.
    with open("./Data/users.json", "w") as file:
        user_data = [{"username": user.username, "password": user.password, "name": user.name, "identify": user.identify}
                    for user in users]
        json.dump(user_data, file, indent=2)


if __name__ == "__main__":
    
    initialize_users()

    users = Users()
    print(users.user_list)