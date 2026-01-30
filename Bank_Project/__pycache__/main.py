import sqlite3
from functions import acc_creation , pin_gen , check_balance , depsoite , withdrawl , transfer
connect = sqlite3.connect("Bank.db")
cursor = connect.cursor()

#sql query for db
#cursor.execute("create table Accounts (acc_number),number(10) primary key , name varchar(32)not null,
# mobile number(10) unique,dob date ,address varchar(150) not null , mail varchar(254) Unique , 
# adhar number(12) unique,gender varchar(6)acc_type varchar(15) not null, bal number default(1000) not null, pin default(0)"))

print("-"*20,"WELCOME TO MANCHI_BANK","-"*20)
while True:
    op=int(input("""1)Account creation \n 2) pin Generation \n 3)Balance Enquiry 
    \n 4)Deposit \n 5) Withdrawl 6)Acc Transfer"""))
    if op == 1:
        name = input("Enter the Name:")
        mobile = int(input("Enter the Mobile Number:"))
        dob = input("Enter your Dob:")
        gen = int(input("Enter ypur Gender:"))


