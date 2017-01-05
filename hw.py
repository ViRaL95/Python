#Assignment Number 1. The follwing program was written in Python 2 therefore raw_input was used to record inputs rather than the input function 
#All Values 

firstname=raw_input("Please enter your first name: ")
firstletter=firstname[0]
lastname=raw_input("Please enter your last name: ")

if(len(lastname)>=7):
	loginlastname=lastname[:7]
else:
	loginlastname=lastname
flag=0
while (not(flag)):
	IDnumber=raw_input("Please enter an ID Number: ")
	if(len(IDnumber)==9 and IDnumber.isdigit()):
		flag=1;
	else:
		output="Please enter a valid ID number...."
		print(output)			

lastdigit=IDnumber[len(IDnumber)-1]

loginname=firstletter+loginlastname+lastdigit

loginoutput="login name is "+loginname
print(loginoutput);

flag=0
while(not(flag)):
	password=raw_input("Please enter your password: ")
	CapitalLetters=sum(1 for c in password if c.isupper())
	LowerCase=sum(1 for c in password if c.islower())
	DigitCase=sum(1 for c in password if c.isdigit())
	if(len(password)>=7 and CapitalLetters>=1 and LowerCase>=1 and DigitCase>=1):
		flag=1;
	else:
		output="Please enter a valid password..."
		print(output)
output="Password was valid.  Password you entered was: "+password+". Please record this somewhere safe"				
print(output);

