from UI.login_management import LoginManagement
from UI.voting_management import VotingManagement
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginManagement(root)
    root.mainloop()