class Budget():

    category_list = [] #List of categories
    category_bank = {} #categories with balance pair

    #default function call as the app opeens to create categories
    def __init__(self):
        print("**********\tBudget App\t**********")
        number_of_categories = int(input("How many category do you wish to create: "))
        for i in range(1,number_of_categories+1):
            input_category = input("\nPlease input categories name for number %s: "%i)
            self.category_list.append(input_category)
        for category in self.category_list:
            self.category_bank[category] = 0
        print("\n******** Categories created Successfullly ********\n")

        self.action()
    #action function
    def action(self):
        print("\nThese are the availble actions that can be performed: ")
        print("1 to Deposit to category")
        print("2 to Withdrawl from category")
        print("3 to Get category balance")
        print("4 to Transfer between category")
        print('5 to Add New Category')
        selected_input = int(input("Enter valid option: "))
        if selected_input == 1:
            self.deposit_fund()
        elif selected_input == 2:
            self.withdrawl_fund()
        elif selected_input == 3:
            self.balance_fund()
        elif selected_input == 4:
            self.transfer_fund()
        elif selected_input == 5:
            self.add_category()
        else:
            self.action()

    #Adding new category if needed apart from the ones created initiallly
    def add_category(self):
        category_name = input("Enter category name: ")
        self.category_bank[category_name] = 0
        print("Category added successfully")
        self.action()

    #action call categories    
    def call_category(self,action):
        global selected_category
        if action == 'deposit':
            print('\nWhich category do you wish to deposit to: ')
            for category in self.category_list:
                print(self.category_list.index(category) + 1, " " , category)
            print("0 Main menu")
            try:
                selected_category = int(input("Input valid option: "))
                if selected_category > len(self.category_list) or selected_category < 0:
                    print("Invalid input")
                    self.call_category(action)
                elif selected_category == 0:
                    self.action()
                else:
                    return selected_category
            except ValueError:
                print("Digit input is required")
                self.call_category(action)
        elif action == 'balance':
            print("\n1. All Categories")
            print('2. A Category')
            print("0 Main menu")
            try:
                selected_input = int(input("Input Valid option: "))
                if selected_input == 1:
                    print('\nCategories\t\tBalance')
                    for category,balance in self.category_bank.items():
                        print(category, '\t\t\t#' , balance)
                    self.action()
                elif selected_input == 2:
                    for category in self.category_list:
                        print(self.category_list.index(category) + 1, " " , category)
                    try:
                        selected_category = int(input("Input valid option: "))
                        gotten_balance = self.category_bank[self.category_list[selected_category - 1]]
                        print(self.category_list[selected_category - 1], ':  #' ,gotten_balance, '\n')
                        self.action()
                    except (ValueError,IndexError):
                        print("Invalid Input detected")
                        self.call_category(action)
                elif selected_input == 0:
                    self.action()

            except ValueError:
                print("Invalid input, Digit input is expected")
                self.call_category(action)
        elif action == 'withdrawl':
            print("\nWhich category do you want to withdrawl from: ")
            for category in self.category_list:
                print(self.category_list.index(category) + 1, " for " , category)
            print("0 Main menu")
            try:
                selected_category = int(input("Input valid option: "))
                if selected_category > len(self.category_list) or selected_category < 0:
                    print("Category does not exist\n")
                    self.call_category(action)
                elif selected_category == 0:
                    self.action()
                else:
                    return selected_category
            except ValueError:
                print("Digit input is required\n")
                self.call_category(action)


            

    def deposit_fund(self):
        self.call_category('deposit')
        deposit_selected_category = self.category_list[selected_category - 1]
        print("Category Fethced Successfully!!!!\n")
        amount_deposit = int(input("input amount to deposit: "))
        self.category_bank[deposit_selected_category] = self.category_bank[deposit_selected_category] + amount_deposit
        print("Fund deposited successfully\n")
        print("************* Available Categories *************")
        for category,balance in self.category_bank.items():
            print(category, ' #' , balance, '\n')
        
        self.action()
    def withdrawl_fund(self):
        self.call_category('withdrawl')
        withdrawl_selected_category = self.category_list[selected_category - 1]
        print("\nYou are about to withdrawl from %s\n"%withdrawl_selected_category)
        balance = self.category_bank[withdrawl_selected_category]
        amount_withrwal = int(input("input amount to withdrawl: "))
        if amount_withrwal <= balance:
            balance = balance - amount_withrwal
            self.category_bank[withdrawl_selected_category] = balance
            print("Fund withdrawl successfully\n")
            self.action()
        else:
            print("\nInsufficient Fund\n")
            self.action()

    def balance_fund(self):
        self.call_category('balance')

    def transfer_fund(self):
        print('\n')
        for category in self.category_list:
            print(self.category_list.index(category) + 1, " " , category)
        try:
            transfer_from = int(input("Funds transfer from category:  "))
            transfer_to = int(input("Funds transfer to category:  "))
            amount_to_transfer = int(input("Enter amount to transfer: "))
            previous_transfer_balance = self.category_bank[self.category_list[transfer_from - 1]]
            if previous_transfer_balance >= amount_to_transfer:
                 self.category_bank[self.category_list[transfer_to - 1]] = self.category_bank[self.category_list[transfer_to - 1]] + amount_to_transfer
                 self.category_bank[self.category_list[transfer_from - 1]] = self.category_bank[self.category_list[transfer_from - 1]] - amount_to_transfer
                 self.action()
            else:
                print("Insufficient Funds")
                self.action()
        except ValueError:
            print("Digit input is expected")
            self.transfer_fund()



Budget()