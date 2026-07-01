class Redbus:
    def __init__(self,username,phoneno):
        self.username=username
        self.phoneno=phoneno
        print(f"Welcome to the redbus{self.username}")
        Redbus.banner()
    seats={}
    for i in range(1,11):
        if i%3==0:
            seats[i]='Booked'
        else:
            seats[i]='Available'
    @classmethod
    def displayseats(cls):
        for i in cls.seats:
            print(f'|{i}|{cls.seats[i]}|')
    def booking(self,seatno):
        if Redbus.seats[seatno]=='Booked':
            print('Already Booked')
        else:
            Redbus.seats[seatno]==f'Booked by{self.username}'
            print(f"Hello {self.username},You have Successfully Booked the Seat")
    @staticmethod
    def banner():
        print("20% discount is going on for AP/TS Routes")
kavya=Redbus('kavya',9876543210)
kavya.displayseats()
kavya.booking(1)
kavya.displayseats()

venky=Redbus('venky',9876543211)
venky.displayseats()
venky.booking(4)
venky.displayseats()


'''kavya=Redbus()


kavya.displayseats()
kavya.booking(1)
kavya.booking(7)
kavya.booking(9)
kavya.displayseats()'''
