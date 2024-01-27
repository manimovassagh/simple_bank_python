class Account:

    def __init__(self, email, amount):
        self.email = email
        self.amount = amount
        self.currency = "Euro"
    
    #define new
    #define new
    def __str__(self):
        return f"The Bank Account holder name is {self.email} and amount is {self.amount} {self.currency}"

    def say_hi_to_account_holder(self):
        return print(f"Hello, Nice to meet you {self.email}")

    def say_goodbye_to_user(self):
        return print(f"Dear {self.email}, Thanks for using our servie ! see you soon")

    def withdraw(self, withdraw_request):
        if withdraw_request > self.amount:
            print("You can not withdraw more than your amount")
        else:
            self.say_hi_to_account_holder()
            print(f"You had {self.amount} {self.currency} in your account")
            print(f"You have initialised withdraw of {
                  withdraw_request} {self.currency}")
            latest_amount = self.amount - withdraw_request
            self.amount = latest_amount
            print(f"Your new remain is {self.amount}")
            self.say_goodbye_to_user()

    def get_current_amount(self):
        return f" Your current amount is {self.amount}"

    def deposit_amount(self, deposit_value):
        self.say_hi_to_account_holder()
        print(f"You had {self.amount} {self.currency} in your account")
        print(f"You have initialised deposit of {
              deposit_value} {self.currency}")
        self.amount = self.amount + deposit_value
        print(f"Your new remain is {self.amount}")
        self.say_goodbye_to_user()
