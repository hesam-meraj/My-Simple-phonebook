import json
import re
import os

# all_data is a list which conatians all the information about user's contacts
# in this list we dictionaries that show us 
all_data = []

if os.path.isfile("./save.json"):
    with open("./save.json", "r") as file:
        all_data = json.load(file)


# Creating a menu function in order to use it after every operation
def menu():
    print()
    print()

    print("Pls choose your option 1, 2, 3, 4, 5")
    print("################################################")
    print()
    lls = ["Add contact", "Update contact", "Delete contact", "See all the contacts", "Sort the contacts"]
    for i in range(5):
        print(f'Option [{i+1}] : This option will give permission to {lls[i]}')
    print("Option [6] : Exit")    
    print()
    print()
    print("################################################")

# verify function used in add_contact function in order to verify the information

# The function below verify the names that has no special characters like !@#$%
def verify_name(name):
    if re.match(r'\w*', name):
        return True
    else:
        return False

# The length of the number should be 11
# It must start with 09 or +989 or 00989 with 9 number after that
def verify_phone_number(number):
    if re.match(r'^09\d{9}$', number):
        return True
    elif re.match(r'^\+989\d{9}$', number):
        return True
    elif re.match(r'^00989\d{9}$', number):
        return True
    else:
        return False


def verify_email(email):
    if re.match(r'^[a-zA-Z0-9\.\_]+@[a-zA-Z0-9]+\.[a-zA-Z]{3}$', email):
        return True
    else:
        
        return False


# User can not add 2 contacts with same names
def add_contact(ls):
    mydict = {}
    mylist = []
    print("######")
    print('''
            Your name should not have any special characters


          ''')
    name  = input("Pls enter your name :  ")

    # checking if the name exists
    for dict in all_data:
        for ex_name in dict:
            if name == ex_name:
                print('''

            You cant have 2 contacts with  a same name 
                      ''')
                return


    if verify_name(name):
        print("your name is fine")
        print("########")
        phnum = input("Pls enter your phone number : ")
        if verify_phone_number(phnum):
            print("your phone number is fine")
            print("########")
            mylist.append(phnum)
            email = input("Pls enter your email : ")
            if verify_email(email):
                print("your email address is fine")
                print("#####")
                mylist.append(email)
                print("Adding you as contact to the list")
                mydict[name] = mylist
                all_data.append(mydict)
                menu()
            
            
            else:
                print("we can not verify your email addres ,,, bringing you back to menu")
                menu()



            
        else:
            print("we can not verify your phone number ,,, bringing you back to menu")
            menu()

    else:
        print("we can not verify your name ,,, bringing you back to menu")
        menu()
        





# updating the contact's information with name and phone number

def update_contact(ls):
    name = input("enter the name you want to changee the information about : ")
    ph_num = input("enter the phone nubmber : ")
    
    print('''
        Wrong information bringing you back to the menu
          ''')
    # matching the name and the phone number 
    for dict in ls:
        for nm in dict:
            if nm == name and ph_num == dict[nm][0]:
                print("your information is correct !")
                
                    
                print('''
            what do you want to update about this contact:
                      Option [1]:name
                      Option [2]:phone number
                      option [3]:email address
                      option [4]:back to menu
                      ''')

                x = input("Enter your option :  ")
         
# operations which will be active after right information
                if x == "1":
                    new_name = input("pls enter the new name of the contact : ")
                    if verify_name(new_name):
                        dict[new_name] = dict.pop(name)
                        

                            
                        print(f"name has been changed to {new_name}")

                        break
                elif x == "2":
                    new_ph = input("pls enter the phone number of the contact : ")
                    if verify_name(new_ph):
                        dict[nm][0] = new_ph
                        print(f"phone number has been changed to {new_ph}")
                    
                elif x == "3":
                    new_email = input("pls enter the new email of the contact : ")
                    if verify_name(new_email):
                        dict[nm][1] = new_email
                        print(f"name has been changed to {new_email}")
                elif x == "4":
                    break
                
                else:
                    "Invalid command"
            else:
                   

                print('''
        Wrong information bringing you back to the menu
          ''')
    menu()




def delete_contact(ls):
    name = input("enter the name you want to delete : ")
    ph_num = input("enter the phone number : ")
    # matching the users input with all_data list
    for dict in ls:
        for nm in dict:
            if nm == name and ph_num == dict[nm][0]:
                print("your information is correct !")
                question = input('''
                                 
                Are you sure ?
                enter 1 if yes
                enter 2 if no
                            
                                 ''')
                if question == "1":
                    ls.remove(dict)

                    break
                else:
                    print('''


                brining you back to the menu
                            ''')
                    return
        break
    print('''

    your contact has been deleted from the phone book

          ''')
    print("Enter command from the menu : ",end=" ")

    

def show_all_contacts(ls):
    for i in ls:
        for j,k in i.items():
            print('''
    [{}] with phone number [{}] and email address [{}]
                  
                  '''.format(j,k[0],k[1]))
    print("#######")
    print("Here all the information we have ")
    print("#######")        
    print("Enter command from the menu : ",end=" ")
        

def sort_contacts(ls):
    new_all_data = []
    names = []
    for i in ls:
        for j in i:
            names.append(j)
    sort_names = sorted(names)
    for i in sort_names:
        for dic in ls:
            for nm in dic:
                if nm == i:
                    new_all_data.append(dic)
    show_all_contacts(new_all_data)





menu()


while True:
    x = input()
    if x == "1":
        add_contact(all_data)
    elif x == "2":
        update_contact(all_data)
    elif x == "3":
        delete_contact(all_data)
    elif x == "4":
        show_all_contacts(all_data)
    elif x == "5":
        sort_contacts(all_data)
    elif x == "6":
        break
    else:
        print("Invalid command ")
        menu()
        print('''
              pls choose a number between 1, 2, 3, 4, 5, 6
              
              
              ''')
print("The program is being closed!")

with open("save.json", "w") as file:
    json.dump(all_data, file)




