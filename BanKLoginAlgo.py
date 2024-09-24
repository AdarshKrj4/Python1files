class bank:
    def __init__(self,name=None,ID=None,account_number=None,balance=None,age=None,FD=None,branch=None):
        self.name=name
        self.ID=ID
        self.account_number=account_number
        self.balance=balance
        self.age=age
        self.FD=FD
        self.branch=branch
        a=0
        
    
        # self.customers=[105,107,221,234,456,654,766,769,809,902,950,1001]
        
    def login(self,ID,account):
       
        self.list=[self.account_number]
        self.listID=[self.ID]
        if ID in self.listID and account in self.list:
             print("Login successful")
             if (self.balance<=5000):
                 print("Warning your balance is low",self.balance)
             else:
                print("Your bank balance is",self.balance)
             if (self.age>=60):
                print(self.name,"You are eligible for senior citizen benefits")

                 
        else:
             print("Wrong Account number,do you want to create an account?")
             d=input("YES or NO " )
             if (d=="YES"):
                 print("Welcome to SBSB Banking Services")
                 custnew.name=input("Enter your name ")
                 custnew.age=input("Enter your Age ")
                 custnew.account_number=11001
                 custnew.balance=6000
                 custnew.ID=9
                 print("Congrats",custnew.name, "account opened successfully")
                 print("Your account number is 1101")
                 print("Your customer ID is 9")
    def interestcalc(self):
        interest=self.FD*0.06
        print(self.name, "total interest generated on your FD IS",interest)
    def checklowBalance(self):
        if (self.balance<=5000):
            add=(5000-int(self.balance))
            add=int(add)
            print(self.name,"your balance is low","Please add",add)
        else:
            print("Balance is not low")
            
    def checkSenior(self):
        if (self.age>=60):
                print(self.name,"You are eligible for senior citizen benefits")
        else:
            print(self.name,"You are not eligible for Senior citizen benefits")


        
cust1=bank("Adarsh",1,10045,5500,20,10000,"Ranchi")
cust2=bank("Sameer",2,10055,4500,40,0,"Patna")
cust3=bank("Anamika",3,10345,12500,29,15000,"Kolkata")
cust4=bank("Rakesh",4,10046,20020,63,20000,"Delhi")
cust5=bank("Ayush",5,10050,6700,38,0,"Bareily")
cust6=bank("Junaid",6,10550,6100,48,25000,"Gurgaon")
cust7=bank("Jason",7,10750,2200,68,0,"Jaipur")
cust8=bank("Ankita",8,10760,8200,28,35000,"Vizag")
custnew=bank()
# b=input("Enter account number ")
c=int(input("Enter Customer ID "))

if c==1:
    print("Welcome",cust1.name,"Please follow the steps to login")
    b=int(input("Enter account number "))
    cust1.login(c,b)
if c==2:
    print("Welcome",cust2.name,"Please follow the steps to login")
    b=int(input("Enter account number "))
    cust2.login(c,b)
if c==3:
    print("Welcome",cust3.name,"Please follow the steps to login")
    b=int(input("Enter account number "))
    cust3.login(c,b)
if c==4:
    print("Welcome",cust4.name,"Please follow the steps to login")
    b=int(input("Enter account number "))
    cust4.login(c,b)
if c==5:
    print("Welcome",cust5.name,"Please follow the steps to login")
    b=int(input("Enter account number "))
    cust5.login(c,b)
if c==6:
    print("Welcome",cust6.name,"Please follow the steps to login")
    b=int(input("Enter account number "))
    cust6.login(c,b)
if c==7:
    print("Welcome",cust7.name,"Please follow the steps to login")
    b=int(input("Enter account number "))
    cust7.login(c,b)
if c==8:
    print("Welcome",cust8.name,"Please follow the steps to login")
    b=int(input("Enter account number "))
    cust8.login(c,b)
else:
    pass
# cust1.interestcalc()
# cust2.checklowBalance()
# cust3.checkSenior()




     



