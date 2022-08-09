class CreateAccountController:
    def __init__(self, accObj):
        self.accObj = accObj

    def account_valid(self, Un, Email):
        idx = self.accObj.accounts.search("Un", Un)
        if idx != -1:
            return False, "[USERNAME_EXISTS] A User with that username already exists"
        
        idx = self.accObj.accounts.search("Email", Email)
        if idx != -1:
            return False, "[EMAIL_EXISTS] A User with that username already exists"
        
        return True, "[ACCOUNT_CREATED] An Account has been created."

    def create_account(self, Un, Ps, Email):
        valid, msg = self.account_valid(Un, Email)

        if not valid:
            print(msg)
        else:
            self.accObj.accounts.update(Un=Un, Ps=Ps, Email=Email)
            self.accObj.accounts.write()
            print(msg)