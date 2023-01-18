class ROI():
    '''This is class used to calculate a return on investment for any rental
    property. The attributes are monthly income, monthly expenses
    monthly cash flow and total investment. All expected to be an empty string. '''

    def __init__(self, monthly_income, monthly_expenses, cash_flow, total_investment):
        self.monthly_income = monthly_income 
        self.monthly_expenses = monthly_expenses
        self.cash_flow = cash_flow
        self.total_investment = total_investment

    def monthlyIncome(self):
        rental_income = int(input("Estimated rental income: "))
        laundry = int(input("Estimated laundry income: "))
        storage = int(input("Estimated storage income: "))
        misc = int(input('Estimated miscellaneous income: '))
        self.monthly_income = rental_income + laundry + storage + misc
        print(f'Total Monthly Income: ${self.monthly_income}')
    
    def monthlyExpense(self):
        t = int(input("Estimated taxes: "))
        i = int(input("Estimated insurance: "))
        u = int(input("Estimated utility cost: "))
        hoa= int(input("Estimated HOA cost: "))
        l = int(input("Estimated Lawn/Snow care cost: "))
        r = int(input("Estimated repairs cost: "))
        capex = int(input("Estimated Capital Repairs: "))
        property_manager = int(input("Estimated Property Manager cost: "))
        m = int(input("Estimated Mortgage cost: "))
        self.monthly_expenses = t + i + u + hoa + l + r + capex + property_manager + m
        print(f'Total Monthly Expenses: ${self.monthly_expenses}')

    def cashFlow(self):
        self.cash_flow = self.monthly_income - self.monthly_expenses
        print(f'Total Monthly Cashflow: ${self.cash_flow}')

    def totalInvestment(self):
        down_payment = int(input("Estimated Down Payment: "))
        closing_cost = int(input("Estimated Closing Costs: "))
        rehab = int(input("Estimated Rehab budget: "))
        misc_1 = int(input("Estimated other investments: "))
        self.total_investment = down_payment + closing_cost + rehab + misc_1
        print(f'Total Invenstment into property: ${self.total_investment}')
    
    def roiCalc(self):
        annual_cashflow = self.cash_flow * 12 
        find_percent = annual_cashflow / self.total_investment
        cash_cash_ROI = find_percent *100
        print(f'Cash on Cash ROI = {cash_cash_ROI}%')
    
    def simpleCalc(self):
        self.monthly_income = int(input('Estimated total monthly income from property: '))
        self.monthly_expenses = int(input('Estimated total monthly expenses from property: '))
        self.cash_flow = self.monthly_income - self.monthly_expenses
        print(f'Total monthly cash flow: ${self.cash_flow}')
        self.total_investment = int(input('Estimated total invenstment into property: '))
        annual_cashflow = self.cash_flow * 12 
        find_percent = annual_cashflow / self.total_investment
        cash_cash_ROI = find_percent *100
        print(f'Cash on Cash ROI = {cash_cash_ROI}%')

    
my_ROI = ROI('','','','')

def run():
    while True:
        user_input = input('Return on Investment Calculator:Choose Full/Simple/Quit ')
        if user_input.lower() == 'full':
            my_ROI.monthlyIncome()
            my_ROI.monthlyExpense()
            my_ROI.cashFlow()
            my_ROI.totalInvestment()
            my_ROI.roiCalc()
        elif user_input.lower() == 'simple':
            my_ROI.simpleCalc()
        elif user_input.lower() == 'quit':
            break
        print('Thanks for using ROI calculator')

run()