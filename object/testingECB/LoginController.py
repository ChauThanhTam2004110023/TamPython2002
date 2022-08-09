class LoginController:
    def __init__(self, accObj):
        self.accObj = accObj

    def login(self, Un, Ps):
        temp_mem = self.accObj.accounts.get_all()
        idx = self.accObj.accounts.search("Un", Un)
        if self.accObj.username == Un:
            print("[AlREADT_LOGGEDIN] You are already logged in.")
        
        elif self.accObj.username and self.accObj.username != Un:
            print("[INVALID_MUL_LOGINS] You need to logout first first to attempt annther login")
        
        elif idx != -1:
            if temp_mem[idx]["Ps"] == Ps:
                Email = temp_mem[idx]["Email"]
                self.accObj.set_account(Un, Ps, Email)
                print("[LOGGED_IN] You are logged in.")
            else:
                print("[WRONG_PASS] The password you entered is incorrect.")
        else:
            print("[NOT_REGISTERED] You have to register first.")

    def logout(self):
        self.accObj.logout()
        