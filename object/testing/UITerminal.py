class UITerminal:
    def __init__(self, accObj):
        self.accObj = accObj
        self.prompt = " "
        self.command = None
        self.args = None
        self.actions = {
            "CA": self.accObj.create_account,
            "LI": self.accObj.login,
            "LO": self.accObj.logout
        }
    
    def run(self):
        action =  self.actions.get(self.command)
        if self.args:
            action(*self.args)
        else:
            action()


    def get_prompt(self):
        return self.prompt

    def handle_commmand(self, rep):
        rep = rep.upper()
        self.command = rep
        if rep == "CA":
            return "Enter a username, a password, an email... "
        elif rep == "LI":
            return "Enter a username, a password... "
        elif rep == "LO":
            return "Logging out... "
        else:
            return "Unlown Command. "

    def handle_inputs(self):
        if self.command == "CA":
            #Un, Ps, Email = self.create_account_inputs()
            self.create_account_inputs()
            #self.accObj.create_account(Un, Ps, Email)
            self.run()
        elif self.command == "LI":
            #Un, Ps = self.login_inputs()
            self.login_inputs()
            #self.accObj.login(Un, Ps)
            self.run()
        elif self.command == "LO":
            self.accObj.logout()


    def login_inputs(self):
        Un = input("USERNAME: ")
        Ps = int(input("PASSWORD: "))
        #return Un, Ps
        self.args = [Un, Ps]


    def create_account_inputs(self):
        Un = input("USERNAME: ")
        Ps = int(input("PASSWORD: "))
        Email = input("EMAIL: ")
        #return Un, Ps, Email
        self.args = [Un, Ps, Email]

    def display_options(self):
        print("********************* MENU *********************")
        if not self.accObj.check_loggedin():
            self.prompt = " "
            print("""Enter one of the commands in the brackets
                    [CA] Create Account
                    [LI] Login
                    """)
        else:
            self.prompt = f"[LOGGET IN] AS #{self.accObj.username}]"
            print("""Enter one of the command in the brackets:
                    [LO] Logout
                    """)
