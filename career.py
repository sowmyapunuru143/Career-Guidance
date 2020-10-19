'''
This functions returns the greeting message according to  the tym
'''
from datetime import datetime
import random
def current_time():
    current_time=datetime.now()
    greeting="Good morning"
    if current_time.hour>12 and current_time.hour<17:
        greeting="Good afternoon"
    elif current_time.hour>=17 and current_time.hour<22:
        greeting="Good evening"
    elif current_time.hour>=22:
        greeting="Hi,its too late"
    return greeting
'''
   This function gives the welcome message
'''
def welcome(name):
    message=[
        "How can i help you?",
        "Is there anything i can help with?"'
    ]
    print(f"{current_time()}!{name},{random.choice(message)}")
def career_guidance():
    print("1.Science")
    print("2.Arts")
    print("3.Commerce")
    try:
        return(int(input("Enter your option:")))
    except:
        print("Invalid input")
        return 0
def type1_Science():
    print("Select any one option from 1 to 3")
    def Science_option():
        print("1.Science subjects")
        print("2.Science career options")
        print("3.Go back")
        try:
            return(int(input("Enter your choice:")))
        except:
            print("Invalid input")
            return 0
    def Science_subjects():
        print("This subjects you should choose according to your goal or interest in science")
        print("Mathematics")
        print("English")
        print("Biology")
        print("Physics")
        print("Chemistry")
        print("Computer Science")
    def Science_career__options():
        print("Engineering")
        print("Doctor")
        print("Scientist")
        print("Astronauts")
        print("Pharmacists")
        print("Software Programmers")
        print("Web Developers and lot more")
    def print_option():
        option=Science_option()
        while option !=3:
            if option == 1:
                Science_subjects()
            elif option == 2:
                Science_career__options()
            else:
                print("Sorry!Invalid input")
            option=Science_option()
    print_option()
    def type2_Arts():
        print("Select any one option from 1 to 3")
        def Arts_option():
            print("1.Arts subjects")
            print("2.Arts career options")
            print("3.Go back")
            try:
                print(int(input("Enter your choice:")))
            except:
                print("Invalid input")
                return 0
        def Arts_subjects():
            print("This subjects you should choose according to your goal or interest in arts")
            print("English")
            print("Economics")
            print("History")
            print("Geography")
            print("Political Science")
            print("Hindi")
            print("Sanskrit")
            print("Home Science")
        def Arts_career_options():
            print("Journalism")
            print("Teaching")
            print("Lawyer")
            print("Graphic Designer")
            print("Mass Communication and Journalism")
            print("Hotal Management and Many more")
        def print_option():
            option=Arts_option()
            while option!=3:
                if option==1:
                    Arts_subjects()
                elif option==2:
                    Arts_career_options()
                else:
                    print("Sorry!Invalid input")
                option=Arts_option()
        print_option()
def type3_commerce():
    print("Select any one option from 1 to 3")
    def commerce_option():
        print("1.commerce subjects")
        print("2.commerce career options")
        print("3.Go back")
        try:
            print(int(input("Enter your Choice:")))
        except:
            print("Invalid input")
                return 0
    def commerce_subjects():
        print("Among this subjects you should choose accoring to your goal or interest in commerce")
        print("Business Studies")
        print("Accountancy")
        print("Econamics")
        print("Mathematics")
        print("English")  
        print("Informatics Practices(if nor maths)")    
    def commerce_career_options():
        print("Chartered Accountants(CA)")
        print("Company Secretaries(CS)")
        print("Chief Finacial Accountant(CFA)")
        print("Finacial planner")
        print("Lawyer")
        print("Bank PO and many more")
    def print_option():
        option=commerce_option()
        while option!=3:
            if option==1:
                commerce_subjects()
            elif option==2:
                commerce_career_options()
            else:
                print("Sorry!Invalid input")
            option=commerce_option()
    print_option()
def chatbot():
     print("This chatbot helps you to choose best career ")
     name=input("Enter your name:")
     welcome(name)
     print("Select any one of the below stream to know the subjects and career options")
     choice=career_guidance()
     while choice!=4:
        if choice==1:
            type1_Science()
        elif choice==2:
            type2_Arts()
        elif choice==3:
            type3_commerce()
         else:
            print("Please enter the number between 1 to 5")
         choice=career_guidance()
chatbot()



     