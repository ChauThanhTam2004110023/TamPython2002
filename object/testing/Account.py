from StoredFiles import *


class Account:
    accounts = StoredFiles("data.json")

    def __init__(self):
        self.username = None
        self.password = None
        self.email = None
        self.loggedin = False

    def check_loggedin(self):
        return self.loggedin

    def login(self, Un, Ps):
        temp_mem = Account.accounts.get_all()
        idx = Account.accounts.search("Un", Un)
        if self.username == Un:
            print("[ALREADY_LOGGEDIN] You are already logged in.")
        
        elif self.username and self.username != Un:
            print("[INVALID_MUL_LOGINS] You need to logout first to attemt another loggin.")
        
        elif idx != -1:
            if temp_mem[idx]["Ps"] == Ps:
                Email = temp_mem[idx]["Email"]
                self.set_account(Un, Ps, Email)
                print("[LOGGED_IN] You are logged in.")
            else:
                print("[WRONG_PASS] The password you entered is incorredt.")
        else:
            print("[NOT_REGISTERED] You have to register first.")

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
        print("[LOGGED_OUT]: You have been logged in")

    @classmethod
    def account_valid(self, Un, Email):
        idx = Account.accounts.search("Un", Un)
        if idx != -1:
            return False, "[USERNAME_EXISTS] A user with that username already exists."
        
        idx = Account.accounts.search("Email", Email)
        if idx != -1:
            return False, "[EMAIL_EXISTS] a user with that email already exists."
        
        return True, "[ACCOUNT_EXISTS] An account has been create."

    @classmethod
    def create_account(cls, Un, Ps, Email):
        valid, msg = cls.account_valid(Un, Email)

        if not valid:
            print(msg)
        else:
            Account.accounts.update(Un=Un, Ps=Ps, Email=Email)
            Account.accounts.write()
            print(msg)

