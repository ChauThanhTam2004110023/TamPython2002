import time
from Account import *
from CreateAccountController import *
from NewAccountUI import *
from LoggedinAccountController import *
from LoggedinAccountUI import *
from Movie import *
from Reservation import *


# =============================== Object Initilaization ===============================
acc = Account()
mov = Movie()
ca_cont = CreateAccountController(acc)
na_ui = NewAccountUI(ca_cont)
lg_cont = LoggedinAccountController(acc, mov)
lg_ui = LoggedinAccountUI(lg_cont)
# =============================== Main Loop ===============================

def display_options(cont):
    print("********************* MENU *********************")
    if not cont.accObj.check_loggedin():
        print("""Enter one of the commands in the brackets
                    [CA] Create Account
                    [LI] Login
                    """)
    else:
        print("""Enter one of the command in the brackets:
                [LO] Logout
                [VM] View Movies
                [VR] View Reservations
                [RM] Reserve A Movie
                """)

def get_prompt(cont):
    if not cont.accObj.check_loggedin():
        return " "
    else:
        return f"[LOGGED IN AS {cont.accObj.username}]"

print("Welcome to the cinema reservation system! \n (To exist type 'exist)")

rep = None

while rep != "exist":
    time.sleep(0.5)
    display_options(ca_cont)
    rep = input(f"{get_prompt(ca_cont)}>")
    if rep.upper() == "CA":
        cmd_res = na_ui.handle_command(rep)
        print(cmd_res)
        if cmd_res and cmd_res != "Unkown Command.":
            na_ui.handle_inputs()

    elif rep.upper() == "LI" or rep.upper() == "LO":
        cmd_res = lg_ui.handle_command(rep)
        if cmd_res and cmd_res != "Unkown Command.":
            lg_ui.handle_inputs()

    elif rep.upper() == "VM":
        cmd_res = lg_ui.handle_command(rep)
        if cmd_res and cmd_res != "Unkown Command.":
            lg_ui.handle_inputs()

    elif rep.upper() == "RM":
        cmd_res = lg_ui.handle_command(rep)
        if cmd_res and cmd_res != "Unkown Command.":
            lg_ui.handle_inputs()

    



            
