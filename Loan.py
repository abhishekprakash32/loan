# Multiple Inheritance With Single Base and Multiple Derived Classes In Python
# Bit exception handling also used
try:
    import loanmodule
    # Using customize module file name=loanmodule.py 
    class loan:
        interest_rate : float
        loan_amount : float
        loan_tenure : float
        processing_fee : float
        name : str
        mobile_no : int
        residential_pincode:int
        ir:float
        gst:float
        def loandetails(self):
            pass
        def loanaccept(self):
            pass
        def customer_details(self):
            self.name = input("Enter your name=")
            self.mobile_no = input("Enter mobile no.")
            self.residential_pincode = input("Enter your current residential pincode=")
            self.loan_amount= float(input("Enter loan amount="))
            self.loan_tenure= int(input("Enter tenure="))
        def customer_show(self):
            print("****************************************")
            print(f"Customer Name={self.name}")
            print(f"Mobile No. = {self.mobile_no}")
            print(f"Pincode = {self.residential_pincode}")
            print(f"Loan amount = {self.loan_amount}")
            print(f"Tenure = {self.loan_tenure}yr")
            print(f"IR = {self.ir}")
            print(f"Processing fee = {self.processing_fee}")
            print(f"GST = {self.gst}")
            self.total = self.loan_amount + self.ir + self.processing_fee + self.gst
            print(f"Total amount {self.loan_amount} + {self.ir} + {self.processing_fee} + {self.gst} = {self.total}")
    class homeloan(loan):
        def loandetails(self):
            print("Bank Name = LIC HFL Home Loan")
            print("Interest Rate = 6.90% p.a. onwards")
            print("Processing Fee =>0.25% of Loan Amount (Plus GST)")
            print("1-5 Years Tenure Range")
        def loanaccept(self):
            loan.customer_details(self)
            self.ir = self.loan_amount * loanmodule.home/100 * self.loan_tenure
            self.processing_fee = self.loan_amount * loanmodule.processhome/100
            self.gst = self.loan_amount * loanmodule.newgst/100
    class personalloan(loan):
        def loandetails(self):
            print("Bank Name = HDFC Bank Personal Loan")
            print("Interest Rate = 15% p.a. onwards")
            print("Processing Fee =>2.50% of Loan Amount (Plus GST)")
            print("1-5 Years Tenure Range")
        def loanaccept(self):
            loan.customer_details(self)
            self.ir = self.loan_amount * loanmodule.personal/100 * self.loan_tenure
            self.processing_fee = self.loan_amount * loanmodule.processpersonal/100
            self.gst = self.loan_amount * loanmodule.newgst/100
    class carloan(loan):
        def loandetails(self):
            print("Bank Name = ICICI Bank Car Loan")
            print("Interest Rate = 7.90% p.a. onwards")
            print("Processing Fee =>0.5% of Loan Amount (Plus GST)")
            print("1-5 Years Tenure Range")
        def loanaccept(self):
            loan.customer_details(self)
            self.ir = self.loan_amount * loanmodule.car/100 * self.loan_tenure
            self.processing_fee = self.loan_amount * loanmodule.processcar/100
            self.gst = self.loan_amount * loanmodule.newgst/100
    d = 'yes'
    while(d == 'yes'):
        print("**********Welcome to bank bazaar************")
        print("We offering you multiple types of loan")
        print("1.Home Loan")
        print("2.Personal Loan")
        print("3.Car Loan")
        print("4.Exit")
        print("NOTE:-Processing Fee 0% - 3% of the loan amount + GST ")
        choice = int(input("Hello sir, which type of loan do you want? 1/2/3/4="))
        if choice not in (1,2,3,4):
            print("please enter correct input!!!")
        else:
            if choice == 1:
                h1 = homeloan()
                h1.loandetails()
                h1.loanaccept()
                h1.customer_show()
            if choice == 2:
                p1 = personalloan()
                p1.loandetails()
                p1.loanaccept()
                p1.customer_show()
            if choice == 3:
                c1 = carloan()
                c1.loandetails()
                c1.loanaccept()
                c1.customer_show()
            if choice == 4:
                exit()
            d = input("Do you want procced more another type of loan? yes/no=")
except BaseException as be:
    print(f"Error Occurred = {be}")
    print("Something went wrong...........") 
