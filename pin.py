
pin = "1001"
attempts = 3

while attempts > 0:
    supplied_pin = input("Enter your PIN: ")
    if supplied_pin == pin:
        print('Your pin has been accepted')
        break
    else:
        print("Incorrect.")
        attempts -= 1
        print("You have ", attempts, " attempts left.")
