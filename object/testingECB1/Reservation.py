from StoredFiles import *


class Reservation:
    reservations = StoredFiles("Reservations.json")
    halls = StoredFiles("halls.json")
    if len(reservations.get_all()) < 1:
        res_count = 0
    else:
        res_count = reservations.get_all()[-1]["resid"]
    
    def __init__(self):
        self.res_id = None
        self.seats = None
        self.time = None
        self.hallno = None

    def resetResInfo(self):
        Reservation.res_count += 1
        self.resid = Reservation.res_count

    def set_res_id(self):
        Reservation.res_count += 1
        self.resid = Reservation.res_count


    def setResInfo(self, seats, time, hallno):
        self.set_res_id()
        self.seats = seats
        self.time = time
        self.hallno = hallno

    def reserve_seats(self, hallnoIDX, seats_list):
        for seatno in seats_list:
            Reservation.halls.memory[hallnoIDX]['seats'][str(seatno)] = 1
            Reservation.halls.write()
        print(f"[SEATS_RESERVED] Seats {seats_list} has been succfully reserved.")


    def check_seat_available(self, hallnoIDX, seats_list):
        halls = Reservation.halls.get_all()
        for seanto in seats_list:
            if halls[hallnoIDX]['seats'][str(seanto)] != 0:
                print(
                    f"[SEAT_UNAVAILABLE] Seat no. {seanto} is already reserved. \nPlease choose a different seat.")
                return False
        print(f"[SEATS_AVAIBLABLE] Seats {seats_list} are aviable.")
        return True

    # xem dat cho
    def view_seats(self, hallnoIDX):
        halls = Reservation.halls.get_all()
        print(f"{'-'*10} HALL NO.{hallnoIDX+1} {'-'*10}")
        i = 1
        j = 1
        seats_per_line = 0
        print("SEATS: \t", end=" ")
        while i <= len(halls[hallnoIDX]['seats']):
            print(f"{i:5d}", end=" ")
            seats_per_line += 1
            if seats_per_line == 4 or i == 16:
                print()
                print("TAKEN: \t", end=" ")
                for x in range(j, j+4):
                    print(f"{halls[hallnoIDX]['seats'][str(x)]:5d}", end=" ")
                j += 4
                print("\n")
                seats_per_line = 0
                if i == 16:
                    break
                print("SEATS: \t", end=" ")
            i += 1
    
    def get_resid(self):
        return self.resid
   

    
#r = Reservation()
#r.view_seats(0)
