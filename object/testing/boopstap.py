import time
from Account import *
from UITerminal import *

acc = Account()
ui = UITerminal(acc)
print("Welcome to the cinema reservation system! \n (To exist type 'exist)")

rep = None

while rep != "exist":
    time.sleep(0.5)
    ui.display_options()
    rep = input(f"{ui.get_prompt()}>")
    print(rep)
    cmd = ui.handle_commmand(rep)
    if cmd and cmd != "Unkown Command.":
        ui.handle_inputs()