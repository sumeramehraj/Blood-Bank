from models import *
from datetime import datetime
from tabulate import tabulate

def register():
	username=input("enter user name-->")
	user=User.select().where(User.username == username)
	if user.exists():
		print("username exists :/")
		username=input("enter user name-->")


	password=input("create password-->")
	fullname=input("enter full name-->")
	user_type=input("enter user type (donor or hospital) -->")

	if user_type == "donor":
		user_type = 0;
	else:
		user_type = 1;

	entry=User.create(full_name=fullname,username=username,password=password,user_type=user_type)
	print(entry.full_name)

	if user_type == 0:
		age=int(input("enter age-->"))
		contact=int(input("enter contact-->"))
		blood_type=input("enter blood_type (eg: B+ for B positive) -->")

		entry=Donor.create(name=entry.full_name,age=age,contact=contact,blood_type=blood_type)


	return user.get()

def login():
	username=input("enter user name-->")
	password=input("enter password-->")
	user=User.select().where(User.username == username)

	if not user.exists():
		print("incorrect credentials :/")
		return None

	if user.get().password == password:
		print("\nsuccesfully logged in\n")
		return user

	else:
		print("fail\n")
		return None

def new_camp():
	name=input("enter Blood Camp Name-->")
	place=input("enter Blood Camp Place-->")
	date=input("enter Blood Camp Date (dd/mm/yyyy) -->")

	entry=Camp.create(name=name,place=place,date=date)

	print("Camp details are -->")
	print(entry.name , entry.place, entry.date)

def all_camps():
	camps = Camp.select()
	headers = ["Name","Place","Date"]
	det = []
	for camp in camps:
		det.append(tuple((camp.name,camp.place,camp.date)))
	print(tabulate(det, headers=headers,tablefmt="grid"))
	

def donate_blood(user):
	name = user.get().full_name
	blood_type = Donor.select().where(Donor.name==name).get()
	print("Name --> ",name)
	print("Blood Group --> ",blood_type.blood_type)
	quantity = int(input("enter Blood Quantity (in millilitres) -->"))

	donation = Donate.create(name = name, blood_type= blood_type, quantity=quantity, date=datetime.now())
	print("Thank You for donating blood :) ")


def update(user):
	user = user.get()
	donor = Donor.select().where(Donor.name==user.full_name).get()
	donor.age = int(input("Update age-->"))
	donor.contact = int(input("Update Contactt-->"))
	donor.save()
	print("Details saved")


def search():
	blood_type = input("search for blood_type (eg: B+ for B positive) -->")
	donors = Donor.select().where(Donor.blood_type==blood_type)
	headers = ["Name","Age","Contact","Blood Type"]
	det = []
	for donor in donors:
		det.append(tuple((donor.name,donor.age,donor.contact,donor.blood_type)))

	print(tabulate(det, headers=headers, tablefmt="grid"))