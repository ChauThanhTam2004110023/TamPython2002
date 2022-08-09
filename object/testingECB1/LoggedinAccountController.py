class LoggedinAccountController:

    def __init__(self, accObj, movObj):
        self.accObj = accObj
        self.movObj = movObj

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

    def add_res(self, seats, time, hallno):
        self.accObj.resObj.setResInfo(seats, time, hallno)
        
        Un = self.accObj.get_username()
        name = self.movObj.get_name()
        resid = self.accObj.resObj.get_resid()
        self.accObj.resObj.reservations.update(resid=resid, Un=Un, name=name, seats=seats, time=time, hallno=hallno)
        self.accObj.resObj.reservations.write()
        self.accObj.set_has_res()
        idx = self.accObj.accounts.search("Un", Un)
        self.accObj.accounts.memory[idx]["has_res"] = True
        self.accObj.accounts.write()
        print("[RESERVATION_COMPLETE] A Successfull reservation has just been made.")



        
    
        