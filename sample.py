from random import randint
#BANK
name = []
bal = []
unique = []

def user_id(id):
	n = name.index(id)
	b = bal.index(id)
	u = unique.index(id)
	if n == b == u:
		return id
	else:
		...

def register():
	give_name = input("Enter a name: ")
	give_balance = int(input("Enter a balance: "))
	give_user_id = randint(10000,99999)
	name.append(give_name) 
	bal.append(give_balance) 
	unique.append(give_user_id)
	print(f"\nRegister Succesfully \nYour Name: {give_name} \nYour Current Balance: {give_balance}\nYour PIN ID: {give_user_id }\n")
	main()
	
	return 

def check_balance():
	a = user_id(id)
	print(a)


def deposit():
	while True:
		user_id = int(input("Enter your PIN ID: "))
		if user_id in unique["user"]:
			depo = int(input("Enter a number to deposit: "))
			val = account["balance"][0]
			bal = val + depo
			account["balance"].pop()
			account["balance"].append(bal)
			main()
		else:
			print("Incorrect PIN")

		

def withdraw():
	while True:
		user_id = int(input("Enter your PIN ID: "))
		if user_id in unique["user"]:
			cashout = int(input("Enter a number to withdraw: "))
			val = account["balance"][0]
			bal = val - cashout
			account["balance"].pop()
			account["balance"].append(bal)
			main()
		else:
			print("Incorrect PIN")


def delete():
	while True:
		user_id = int(input("Enter your PIN ID: "))
		if user_id in unique["user"]:
			account["name"].pop()
			account["balance"].pop()
			unique["user"].pop()
			main()
		else:
			print("Incorrect PIN")

def main():
	while True:
		print("\nWELCOME TO PYTHON BANK!\n[DEPOSIT | WITHDRAW | CREATE ACCOUNT | CHECK BALANCE]\n")
		print("Type 'Create' to register\nType 'Deposit' to deposit\nType 'Withdraw' to withdraw\nType 'Check' to check balance\nType 'Delete' to delete account\n")
		command = input("Enter your command: ").capitalize()
		if command == "Create":
			register()
			command = input("Enter your command: ").capitalize()
		elif command == "Deposit":
			deposit()
			command = input("Enter your command: ").capitalize()
		elif command == "Withdraw":
			withdraw()
			command = input("Enter your command: ").capitalize()
		elif command == "Delete":
			delete()
		elif command == "Check":
			check_balance()
			command = input("Enter your command: ").capitalize()
		else:
			print("Error Command")
			command = input("Enter your command: ").capitalize()

main()
	