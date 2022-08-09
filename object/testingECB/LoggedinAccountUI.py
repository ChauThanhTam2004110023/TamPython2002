class LoggedinAccountUI:
    def __init__(self, LoginControllerObj):
        self.LoginControllerObj = LoginControllerObj
        self.command = None

    def handle_command(self, rep):
        rep = rep.upper()
        self.command = rep

        if self.command == "LI":
            return "Enter a username, a password..."
        elif self.command == "LO":
            return "Logging out..."
        else:
            return "Unkown Command."

    def handle_inputs(self):
        if self.command == "LI":
            Un , Ps = self.login_inputs()
            self.LoginControllerObj.login(Un, Ps)
        elif self.command == "LO":
            self.LoginControllerObj.logout()


    def login_inputs(self):
        Un = input("USERNAME: ")
        Ps = int(input("PASSWORD: "))
        return Un, Ps
