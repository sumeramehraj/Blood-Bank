from app import*
while True:
	print("-"*20)
	print("Welcome to life_saver", "-"*20, sep="\n")

	print("What would you like to do:\n\
	1. Login\n\
	2. Signup\n\
	3. Exit")

	choice = input("\n--> ")

	if choice == "1":
		user = login()

		while user is not None:
			user_type=int(user.get().user_type)
			if user_type == 0:
				print(f"Hello {user.get().full_name} \n" )
				print("What would you like to do:\n\n\
		1. Blood Camps\n\
		2. Donate\n\
		3. Update info\n\
		")

				ch = input("\n--> ")

				if ch == "1":
					all_camps()
				elif ch == "2":
					donate_blood(user)
				elif ch == "3":
					update(user)
				else:
					break

			else:
				print("What would you like to do:\n\
			1. Organize Camp\n\
			2. Search for blood\n\
			")
				ch = input("\n--> ")

				if ch == "1":
					new_camp()
				elif ch == "2":
					search()
				else:
					break


		else:
			print("Credentials do not match. or Create a New Account.\n")

	elif choice == "2":
		a=register()
		print(a)
	else:
		break
