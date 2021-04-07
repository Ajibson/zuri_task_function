from datetime import datetime
allowedUsers = ['user1', 'user2', 'user3']

password_allowed = ['passuser1','passuser2','passuser3']


balance = 0

count = 0

while True: 
    count +=1
    print("\nWelcome to the ATM stand \n")
    user = input('Enter your username: ')
    if user in allowedUsers:
        password = input('Enter your password: ')
        password_index = allowedUsers.index(user)
        if password == password_allowed[password_index]:
            try:
                count = 0
                print('\nToday\'s date and time: %s (%s)\n' %(datetime.now().date(),datetime.now().time()))
                print('Hello %s\n' % user)
                print("Available Balance:# %d\n" % balance)
                print('Below are the available options: ')
                print('1. Withdrawal')
                print('2. Cash Deposit')
                print('3. Complaint')

                selectedOption = int(input('Input an option: '))

                if selectedOption == 1:
                    amount_to_withdrawl = int(input('How much do you want to withdrawl? '))
                    if amount_to_withdrawl <= balance:
                        print('here is your cash.')
                        balance = balance - amount_to_withdrawl
                        print('Current balance is:# ' + str(balance))
                    else:
                        print('insufficient funds')
                elif selectedOption == 2:
                    deposit = int(input('How much would you like to deposit? '))
                    balance = balance + deposit
                    print('Current Balance is :# ' + str(balance))
                else:
                    complain = input('What issue will you like to report? ')
                    print("Thank you for contacting us")
            except ValueError:
                print('Number is expected here')
        else:
            print('Incorrect password supplied')
            print('That is your %s trial' %(count))
            if count == 4:
                break

    else:
        print('username not recognized')
        print('That is your %s trial' %(count))
        if count == 3:
            print('This is your last trial!!!')
        if count == 4:
            break