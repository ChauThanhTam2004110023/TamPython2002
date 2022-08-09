from StoredFiles import *
from Reservation import *

class Account:
    accounts = StoredFiles("data.json")

    def __init__(self):
        self.username = None
        self.password = None
        self.email = None
        self.loggedin = False
        self.has_res = False
        self.resObj = Reservation()

    def check_loggedin(self):
        return self.loggedin

    def set_account(self, Un, Ps, Email):
        self.username = Un
        self.password = Ps
        self.email = Email
        self.loggedin = True

    def logout(self):
        self.username = None
        self.password = None
        self.email = None
        self.loggedin = False
        print("[LOGGED_OUT]: You have been logged out")

    def get_username(self):
        return self.username

    def check_has_res(self):
        return self.has_res

    def set_has_res(self):
        self.has_res = True

   

