import random 
from datetime import datetime
import time

user_details = []
def process_boot():
    print("** Welcome to UBA bank **\n")

    #Ask user to login or rgister

    print("Press 1 for existing user login\nPress 2 for new user enrollment")

    try:
        selected_option = int(input())
        if selected_option == 1:
            login()
        elif selected_option == 2:
            sign_up()
        else:
            print('Invalid input, please try again\n')
            process_boot()
    except ValueError:
        print('\nDigit input is expected, please try again\n')
        process_boot()

count = 0   
def login():
    global count
    print('************** Login ****************\n')
    print("Please supply your credentials")
    user_account_number = input('Enter your account: ')
    user_password = input("Enter your password: ")

    for entry in user_details:
        entry_index = user_details.index(entry)
        for account_number,details in entry.items():
            if account_number == user_account_number:
                if details['password'] == user_password:
                    return transaction(account_number,entry_index)
                elif count == 2:
                    print("That was your last trial. Thank you for banking with us")
                    process_boot()
                else:
                    print("Invalid password supplied")
                    count +=1
                    login()
    else:
        print('Account number not registered')
        process_boot()

def sign_up():
    global password,first_name,last_name,phone_number
    print("\nPlease supply correct valid information below\n")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    phone_number = input('Phone Number: ')
    if len(phone_number) < 11:
        print("Inavlid phone number, Phone number is not up to 11")
        return phone_number_failed() 
    print("\nPassword must not be less than eight character long and it must contains both letters and numbers")
    password = input("Password: ")
    if len(password) < 8:
        print("Password too short\n")
        password_failed()
    elif password.isdigit():
        print('Password must contains both letters and number\n')
        password_failed()
    elif password.isalpha():
        print("Password must contains both letters and numbers\n")
        password_failed()
    else:
        generated_account_number = account_number_generator()




def account_number_generator():
    account_number = random.randrange(2000000000, 2999999999)  
    print("Below is your account number and password please save it and don't share with anybody")
    user_details.append({str(account_number):{'first_name':first_name, 'last_name':last_name, 'phone_number':phone_number, 'password':password, 'balance':0}})
    print('Account Number: ', account_number)
    print('Password: ', password ,'\n')
    print(user_details)
    process_boot()
        

def password_failed():
    global password
    password = input("Password: ")
    if len(password) < 8:
        print("Password too short\n")
        password_failed()
    elif password.isdigit():
        print('Password must contains both letters and number\n')
        password_failed()
    elif password.isalpha():
        print("Password must contains both letters and numbers\n")
        password_failed()
    else:
        account_number_generator()
    return password


def phone_number_failed():
    global phone_number
    phone_number = input('Phone Number: ')
    if len(phone_number) < 11:
        print("Inavlid phone number, Phone number is not up to 11")
        phone_number_failed()
    else:
        password_failed()



def transaction(account_number,entry_index):
    try:
        previous_balance = user_details[entry_index][str(account_number)]['balance']
        print('\nToday\'s date and time: %s (%s)\n' %(datetime.now().date(),datetime.now().time()))
        print("Available Balance:# %d\n" % previous_balance)
        print('Below are the available transaction options: \n')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Airtime Purchase')
        print('4. Complaint')
        print('5. Logout')

        selectedOption = int(input('Input an option: '))

        if selectedOption == 1:
            amount_to_withdrawl = int(input('How much do you want to withdrawl? '))
            if amount_to_withdrawl <= previous_balance:
                print('\nHere is your cash.\n')
                time.sleep(5)
                new_balance = previous_balance - amount_to_withdrawl
                print('Current balance is:# ' + str(new_balance))
                user_details[entry_index][str(account_number)]['balance'] = new_balance
                transaction(account_number,entry_index)
            else:
                print('\ninsufficient funds'.upper())
                transaction(account_number,entry_index)
        elif selectedOption == 2:
            deposit = int(input('How much would you like to deposit? '))
            new_balance = previous_balance + deposit
            user_details[entry_index][str(account_number)]['balance'] = new_balance
            print('Current Balance is :# ' + str(new_balance)) 
            transaction(account_number,entry_index)
        elif selectedOption == 3:
            airtime_purchase(account_number, entry_index)
        elif selectedOption == 4:
            complain = input('What issue will you like to report? ')
            print("Thank you for contacting us")
            transaction(account_number,entry_index)
        elif selectedOption == 5:
            logout()
    except ValueError:
        print('Digit input is expected here\n')
        transaction(account_number,entry_index)

def logout():
    print("Thank you for banking with us\n")
    process_boot()

def airtime_purchase(account_number, entry_index):
    previous_balance = user_details[entry_index][str(account_number)]['balance']
    network = ['MTN','Glo', 'Airtel', '9Mobile']
    amount_to_recharge = int(input("How much to reacharge: "))
    if amount_to_recharge <= previous_balance:
        print('Available Networs are: ')
        print('1. MTN')
        print('2. Glo')
        print('3. Airtel')
        print('4. 9Mobile')
        selectedOption = int(input(">>> "))
        if selectedOption == 1:
            print("Here is your MTN card")
            new_balance = previous_balance - amount_to_recharge
            user_details[entry_index][str(account_number)]['balance'] = new_balance
            transaction(account_number,entry_index)
        elif selectedOption == 2:
            print("Here is your Glo card")
            new_balance = previous_balance - amount_to_recharge
            user_details[entry_index][str(account_number)]['balance'] = new_balance
            transaction(account_number,entry_index)
        elif selectedOption == 3:
            print("Here is your Airtel card")
            new_balance = previous_balance - amount_to_recharge
            user_details[entry_index][str(account_number)]['balance'] = new_balance
            transaction(account_number,entry_index)
        elif selectedOption == 4:
            print("Here is your 9Mobile card")
            new_balance = previous_balance - amount_to_recharge
            user_details[entry_index][str(account_number)]['balance'] = new_balance
            transaction(account_number,entry_index)


process_boot()