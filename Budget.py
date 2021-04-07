class Budget():
    category_list = []
    category_bank = {}
    def __init__(self):
        self.name = input("Please enter your name: ")
        number_of_categories = int(input("How many category do you wish to create: "))
        for i in range(1,number_of_categories+1):
            input_category = input("Please input categories number %s: "%i)
            self.category_list.append(input_category)
        for category in self.category_list:
            self.category_bank[category] = 0
        self.action()

    def action(self):
        print("******** Categories created Successfullly ********")
        print("These are the availble actions that can be performed: ")
        print("1. Deposit to category")
        print("2. Withdrawl from category")
        print("3. Get category balance")
        print("4. Transfer between category")
        selected_input = int(input("Enter valid option: "))
        if selected_input == 1:
            self.deposit_fund()
        elif selected_input == 2:
            self.withdrawl_fund()
        elif selected_input == 3:
            self.balance_fund()
        elif selected_input == 4:
            self.transfer_fund()

    def call_category(self,action):
        global selected_category
        if action == 'deposit':
            print('Which category do you wish to deposit to: ')
            for category in self.category_list:
                print(self.category_list.index(category) + 1, " " , category)
            try:
                selected_category = int(input("Input valid option: "))
                return selected_category
            except ValueError:
                print("Digit input is required")
                self.call_category(action)
            

    def deposit_fund(self):
        self.call_category('deposit')
        deposit_selected_category = self.category_list[selected_category - 1]
        print("Category Fethced Successfully!!!!")
        amount_deposit = int(input("input amount to deposit: "))
        self.category_bank[deposit_selected_category] = self.category_bank[deposit_selected_category] + amount_deposit
        print("Fund deposited successfully")
        for category,balance in self.category_bank.items():
            print(category, ' ' , balance)
    def withdrawl_fund(self):
        pass

    def balance_fund(self):
        pass

    def transfer_fund(self):
        pass





Budget()