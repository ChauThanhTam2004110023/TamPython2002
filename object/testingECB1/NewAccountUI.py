class NewAccountUI:
    def __init__(self, createAccountControlerObj):
        self.createAccountControllerObj = createAccountControlerObj
        self.command = None
    
    def handle_command(self, rep):
        rep = rep.upper()
        self.command = rep
        if self.command == "CA":
            return "Enter a username, a password, an email.."
        else:
            return "Uknown Command."

    def handle_inputs(self):
        if self.command == "CA":
            Un, Ps, Email = self.create_account_inputs()
            self.createAccountControllerObj.create_account(Un, Ps, Email)

    def create_account_inputs(self):
        Un = input("USERNAME: ")
        Ps = int(input("PASSWORD: "))
        Email = input("EMAIL: ")
        return Un, Ps, Email