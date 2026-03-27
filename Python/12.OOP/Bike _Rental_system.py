class Bike:
    def __init__(self,tb):
        self.totalbikes=tb;
    def display(self):
        print("Total bikes Available: ",self.totalbikes)
    def rentBike(self,n):
        if(n<=0):
            print("Enter value Greater than Zero!")
        elif(n<=self.totalbikes):
            self.totalbikes-=n
            print("Bike Booked Successfully !")
            print("Total Rent: ",n*100)
        else :
            print("Bike not Available.....")

b1=Bike(100)

while True:
    print("Enter Your choice....")
    choice=int(input("1.Show Available Bikes\n2.Rent bike\n3.Exit.."))
    if(choice==1):
        b1.display()
    elif(choice==2):
        n=int(input("Enter quantity: "))
        b1.rentBike(n)
    elif(choice==3):
        print("Exiting...")
        break;
    else:
        print("Enter a valid choice!")