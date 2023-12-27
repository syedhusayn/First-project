companies = [
    ["01", "67815",  "Pran Co.", 100000],
    ["02", "12313",  "Al-AJTF Org.", 100000],
    ["03", "26803",  "Walton Co.", 100000],
    ["04", "01738",  "Shelby Co. LTD", 100000],
    ["05", "11078",  "Brac Bank", 0],
    ["06", "56418",  "RFL Co.", 0],
    ["07", "78657",  "Jamuna Co.", 0],
    ["08", "66880",  "Shin Org.", 0],
    ["09", "23106",  "Roton Co.", 0],
    ["10", "10690",  "Annex Co.", 0],
]
#1st fuction
def check_total_donation(companies):
  print("{0:5}{1:12}{2:27}{3:1}".format("No.", "ID", "Name", "Amount"))
  print()
  for i in companies:
    if i[3] != 0:
      print("{0:5}{1:12}{2:24}{3:9}/-".format(i[0], i[1], i[2], i[3]))
      print()

  #print(f"Total donation: {sum(x[i][3] for i in range(len(x)))}/-") #if extra function is not usable

#extra fuction
def add(companies):
  total_donation = 0
  for item in companies:
    total_donation += item[3]
  print(f"Total number of donations:{total_donation}/-")

#2nd function
def display_non_donating_companies(companies):
  print()
  print("{0:5}{1:12}{2:27}{3:1}".format("No.", "ID", "Name", "Amount"))
  print()
  for i in companies:
      if i[3] == 0:
        print("{0:5}{1:12}{2:24}{3:9}/-".format(i[0], i[1], i[2], i[3]))
        print()

#3rd function
def collect_donations(companies):
  print("{0:5}{1:12}{2:27}".format("No.", "ID", "Name"))
  print()
  for company in companies:
      print("{0:5}{1:12}{2:24}".format(company[0], company[1], company[2]))
      print()
  valid_c=False
  while not valid_c:
      company_id = input("Enter company ID: ")   #if id is int make a change here
      for company in companies:
          if company[1] == company_id:
              valid_c = True
              selected_company = company
              break
      else:
          print("Company is not in the list. \nPlease register your company.")

  if selected_company[3] == 0:
     donation_amount=int(input("Enter donation amount: "))
     if donation_amount>=100000:
        selected_company[3]+=donation_amount
        print(f"Donation of {donation_amount}/- recived from {selected_company[2]}.")
     else:
        print("Donation amount must be 100000/- or more.")
  else:
    print("Company has already donated.")

#4th function
def add_new_company(companies):
  new_company_serial=str(len(companies)+1)
  new_company_name=input("Enter the name of your company: ")
  new_company_id=input('Enter company ID: ')       #if id is int make changes here
  new_company_donation=int(input(f"Enter the donation for {new_company_name}: "))
  if new_company_donation < 100000:
    print("Donetion must be 100000/- or more.")
  else:
    companies.append([new_company_serial, new_company_id, new_company_name, new_company_donation])
    print(f"Your company {new_company_name} is now registered.\nThank you for donating {new_company_donation}.")


while True:
  print()
  print ("Welcome to Pracheshta NGO Donation Manager App")
  print ("Please select an option from the menu below")
  print()
  print ("1. Total Number of Donations")
  print ("2. List of companions who haven't donated yet")
  print ("3. Collect donations(100k or More)")
  print ("4. Add New Company")
  print ("0. Exit")
  print ()
  choice = input("Enter option --> ")


  if choice == '1':
    print("List of Companies: ")
    check_total_donation(companies)
    add(companies)
  elif choice == '2':
    print("List of Companies that haven't donated yet: ")
    display_non_donating_companies(companies)
  elif choice == '3':
    print("Select your company")
    collect_donations(companies)
  elif choice == '4':
    add_new_company(companies)
  elif choice == "0":
    print("Thanks for using Pracheshta NGO Donation Manager App!")
    print("Developed by Monty Python's Flying Circus Org.")
    break
  else:
    print("Invalid choice. Please enter a number between 0 and 4")

  print()