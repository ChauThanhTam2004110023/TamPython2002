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

    

    