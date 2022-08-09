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
        elif self.command == "VM":
            return "Displaying movies list...."
        elif self.command == "VR":
            return "Dispalying your reservation list..."
        elif self.command == "RM":
            return "*** RESRATION DETAILS ***"
        else:
            return "Unkown Command."

    def handle_inputs(self):
        if self.command == "LI":
            Un , Ps = self.login_inputs()
            self.LoginControllerObj.login(Un, Ps)
        elif self.command == "LO":
            self.LoginControllerObj.logout()
        elif self.command == "VM":
            self.LoginControllerObj.movObj.view_movie_details()
        elif self.command == "RM":
            seats, hallno, time = self.reserve_movie_inputs()
            if seats and hallno and time:
                self.LoginControllerObj.add_res(seats, time, hallno)


    def login_inputs(self):
        Un = input("USERNAME: ")
        Ps = int(input("PASSWORD: "))
        return Un, Ps

    #chon phim
    def pick_movie(self):
        print("[A] Choose a movie : (Select a number from the list)")
        movies = self.LoginControllerObj.movObj.view_movie_names()

        m = {}
        for i,movie in enumerate(movies):
            m[i+1] = movie['name']
        mid = int(input(""))
        if m.get(mid):
            return mid
        return None

    #Cho tg
    def pick_time(self):
        print("[B] Choose a timing: (Select a number from the list)")
        t = {
            1: "5 PM",
            2: "8 PM",
            3: "11 PM"
        }
        for k in t:
            print(f"\t\t{k}: {t[k]}")
        time = int(input(">> "))
        if t.get(time):
            return t[time]
        return None

    #chon cho
    def pick_seats(self, hallnoIDX):
        print("[C] Choose Seats: ")
        self.LoginControllerObj.accObj.resObj.view_seats(hallnoIDX)
        seats_list = input(
            "(multiple seats are seperated by while spaces)> ").split(" ")
        seats_list = list(map(int, seats_list))
        return self.LoginControllerObj.accObj.resObj.check_seat_available(hallnoIDX, seats_list), seats_list
    

    def reserve_movie_inputs(self):
        mid = self.pick_movie()
        if not mid:
            print("[INVALID MOVIEE] Please choose a valid movie from the list.")
            return None, None, None
        time = self.pick_time()
        if not time:
            print("[INVALID MOVIE] Plearse choose a valid timing from the list")
            return None, None, None
        hallnoIDX = mid - 1
        seats_aval, seats = self.pick_seats(hallnoIDX)
        if not seats_aval:
            print("[INVALID SEATS] Please choose seats that are not occupied by someone else")
            return None, None, None
        self.LoginControllerObj.movObj.setMovieInfo(mid)
        self.LoginControllerObj.accObj.resObj.reserve_seats(hallnoIDX, seats)
        return seats, hallnoIDX+1, time
        
   




    
            
    

    


