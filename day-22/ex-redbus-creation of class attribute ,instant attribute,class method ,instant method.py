class Redbus:
    seats={}
    for i in range(1,11):
        if i%2==0:
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
            Redbus.seats[seatno]=='Booked'
            print('Successfully Booked')
kavya=Redbus()
kavya.displayseats()
kavya.booking(1)
kavya.booking(7)
kavya.booking(9)
kavya.displayseats()
