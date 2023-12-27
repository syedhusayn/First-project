# -*- coding: utf-8 -*-
"""accessories_of_project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XYOYUTKBfvsvwd6dWawvWN7qAYlxDZaN

listttt with int
"""

companies = [
    ["01", 67815, "     Pran Co.", 100000],
    ["02", 21729, "     Akij Co.", 100000],
    ["03", 26803, "     Walton Co.", 100000],
    ["04", 17389, "     Shelby LTD.", 100000],
    ["05", 11078, "     Brac Bank", 0],
    ["06", 31318, "     RFL Co.", 0],
    ["07", 78657, "     Jamuna Co.", 0],
    ["08", 66880, "     Shin Org.", 0],
    ["09", 23106, "     Roton Co.", 0],
    ["10", 10690, "     Annex Co.", 0],
]

"""1st function

"""

def check_total_donation(companies):
    print("{0:5}{1:12}{2:27}{3:1}".format("No.", "ID", "Name", "Amount"))
    print()
    company = 0
    while company < len(companies):
        if companies[company][3] != 0:
            print("{0:5}{1:12}{2:24}{3:9}/-".format(companies[company][0], companies[company][1],companies[company][2],companies[company][3]))
            print()
            company += 1

def check_total_donation(companies):
  print()
  print("{0:5}{1:10}{2:22}{3:1}".format("No.", "ID", "Name", "Amount"))
  print()
  for i in companies:
    if i[3] != 0:
      print("{0:5}{1:1}{2:24}{3:9}/-".format(i[0], i[1], i[2], i[3]))
      print()

"""2nd func"""

def display_non_donating_companies(companies):
  print()
  print("{0:5}{1:10}{2:22}{3:1}".format("No.", "ID", "Name", "Amount"))
  print()
  for i in companies:
      if i[3] == 0:
        print("{0:5}{1:1}{2:24}{3:9}/-".format(i[0], i[1], i[2], i[3]))
        print()

def check_total_donation(companies):
    print("{0:5}{1:12}{2:27}{3:1}".format("No.", "ID", "Name", "Amount"))
    print()
    company = 0
    while company < len(companies):
        if companies[company][3] == 0:
            print("{0:5}{1:12}{2:24}{3:9}/-".format(companies[company][0], companies[company][1],companies[company][2],companies[company][3]))
            print()
            company += 1

"""extra function in a nutshell"""

sum += company[3]
    print(f"Total number of donations: {sum}/-")

"""change in collect don"""

company_id = int(input("Enter company ID: "))

"""change in add co.

"""

new_company_id = int(input('Enter company ID: '))

"""update if id already exists"""

def add_new_company(companies):
  new_company_serial=str(len(companies)+1)
  new_company_name=input("Enter the name of your company: ")
  new_company_id=input('Enter company ID: ')       #if id is int make changes here
  for i in companies:
    if i[1] == new_company_id:
      print("id already exists")
      break
  else:
    new_company_donation=int(input(f"Enter the donation for {new_company_name}: "))
    if new_company_donation < 100000:
        print("Donetion must be 100000/- or more.")
    else:
        companies.append([new_company_serial, new_company_id, new_company_name, new_company_donation])
        print(f"Your company {new_company_name} is now registered.\nThank you for donating {new_company_donation}.")