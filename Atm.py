class Atm():
    def __init__(self,cardNumber,pinNumber):
        self.cardNumber=cardNumber
        self.pinNumber=pinNumber
    def balance(self):
        print("Your balance is 50,000")
    def withdrawl(self,amount):
        new_amount=50000-amount
        print("Your balance is ", str(new_amount))
def main (): 
    card_number=input("Insert your card number:")
    pin_number=input("Insert your pin number:")
    user=Atm("270340","210")
    user.withdrawl(10000)
main()