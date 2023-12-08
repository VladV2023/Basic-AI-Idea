#import a function called random that will generate random number
import random

#Class named AI_Cannibal
class AI_Cannibal:
    #function to create Cannibal instance of a Class AI_Cannibal, as well as 2 private variables anger and interest
    def __init__(self):
        #Variable used to make Ai behave a certain way in a more agressive way when compared to interest
        self.__anger = 0 #This is a private anger  attribute of AI

        #Variable used to make Ai move closer to Player and possible initiate action on threshold.
        self.__interest = 0 #This is a private interest attribute of AI

    #public funtion that will update Cannibal's mood attributes based on provided numbers
    def mood_update(self, i, a):
        self.__interest += i #increase Cannibal's interest
        self.__anger += a #increase Cannibal's anger
         
    #public function that return private attributes of the class
    def mood_return(self):

        print("The Cannibal's attrubtes are:\n"
              "Anger: ", self.__anger,"\n"
              "Interest: ", self.__interest)
    
#Instance of the Class AI_Cannibal is created
Cannibal = AI_Cannibal()

#make function for "Action on threshold"
# (if anger >= 25):
    #Take action

#simple function that displays the selection menu
def menu():
    print("====================================")
    print("~~~Choose an action to do~~~")
    print("(1)~~Move forward")
    print("(2)~~Move backward")
    print("(3)~~Chop a tree")
    print("(4)~~Vacant")
    print("(5)~~Show Cannibal's Attributes")
    print("====================================")

#random number generator, when calling, use "randomizer(1, 20)" as default
def randomizer(min, max):

    #actual generation of a number by sending min and max into a function
    random_num = random.randint(min, max)

    #return the randomly generated number back
    return random_num
    
#This function will be used to observe the player when interest threashold reached.
def observe():
    print("I am observing the Player")
    print("I think I will try to get closer to them...")

    ran_num = randomizer(1, 20)

    return ran_num

#This function will be used to take action on "interest" variable reached threshold
def chop_tree():
    amount = 0

    #endless loop for repeated use
    while True:
        
        num=input("How many trees should I chop?: ")
        print() #print new line

        #check if the input is an integer or a letter
        #if num.isdigit():
        if num.isdigit():
            num = int(num) 
            #check if the number is not negative
            if num >= 0:
                        
                #loop throughthe range of "num"
                for i in range(num):

                    #call Cannibal's class function to update its private attributes
                    Cannibal.mood_update(5, 1)

                    amount += 1 #increase amount of tree chopped

                print("I have chopped: ", amount, " trees")
                break
            else:
                print("Invalid input. Please enter a positive number. I can't chop negative amount of trees!\n")

        else:
            print("Invalid input. Please enter a positive number.\n")


#This function will be used to take action on "interest" variable reached threshold
def action1():
    print("I am engaging the Player")


while True:
    print() #print new line

    #("Press 'M' to open the menu.")
    key = input("Press 'M' to open Menu, 'X' to terminate Key: ").lower() #ask for input

    print() #print new line

    if key == 'm':
        
        menu() #call menu function
        print() #print new line
        choice = int(input("I choose: ")) #ask for input
    
        if choice == 1:
            print("\nExecuting selected choice.\n")
            
            action1()

            ran_num = observe()


        elif choice == 2:
            print("execuse selected choice.\n")


        elif choice == 3:
            print("\n====================================")#print new line
            print("Executing selected action.")
            print() #print new line

            chop_tree()

            print("\n====================================")#print new line

        elif choice == 4:
            print("execuse selected choice.\n")
            

        elif choice == 5:
            print("\n====================================")#print new line
            print("Showing Cannibal's Attributes\n")

            Cannibal.mood_return()

            print("\n====================================")#print new line

        else:
            print("Invalid choice, please selecti something else.")

    elif key == 'x':
        print("--------------------------") #print new line
        print("Terminating the simulation")
        print("--------------------------") #print new line
        break

    else:
        print("Invalid input, try again.")






#Experimental code, may implement later
#============================================================================
#def greet(name="Guest", age=None, location="Unknown"):
#    message = f"Hello, {name}!"
#    if age is not None:
#        message += f" You are {age} years old."
#    if location != "Unknown":
#        message += f" You are from {location}."
#    return message

# Call the function with different combinations of parameters
#print(greet("Alice"))  # Provide only 'name'
#print(greet("Bob", 30))  # Provide 'name' and 'age'
#rint(greet("Charlie", location="New York"))  # Provide 'name' and 'location'
