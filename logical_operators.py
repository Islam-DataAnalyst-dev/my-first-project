age=int(input("enter your age:"))
has_license=input("do you have a driving license?(yes/no):")
if age>=18 and has_license=="yes":
		print("Application Accepted:you can apply for the job!")
else:
		print("Application Rejected:you don't meet the requirments.")
