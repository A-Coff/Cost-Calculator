# Alex Coffman 4/Aug/23
# CMIS 102/6980 Week 8 Final project
# This program is designed to take in user inputs for the type of service required: house cleaning or yard service
# If the user selects house cleaning, they will be prompted to enter the number of rooms needing to be cleaned and the type of cleaning
# If the user selects yard service, they will be prompted to enter the SqFt of the yard, the linear feet of the yard, and the number of shrubs
# The last prompt will be to enter if they are eligible for a senior discount
# It will then send inputs to the appropriate function to calculate total cost based off the fixed costs for services selected

def totalcost_calculate(numberofRooms, typeofCleaning):
    light_cleaning = 15.00    # Fixed pricing variables for the types of cleaning available
    deep_cleaning = 40.00   # Deep cleaning has a $30 upcharge
    total_cost = 0 
    # intialize a menu off of the two string options 
    menu1 = 'light cleaning' 
    menu2 = 'deep cleaning' 
    # if/elif statements for the function to calculate the correct costs for the cleaning based on number of rooms and type of cleaning
    if typeofCleaning == menu1:
        total_cost = light_cleaning * numberofRooms
    elif typeofCleaning == menu2:
        total_cost = deep_cleaning * numberofRooms
    else:
        print("We don't provide that service option")
        return 
    # This is where the function calculates the applicable surcharges for homes in the medium and large categories
    if 3 < numberofRooms <= 7: 
        total_cost *= 1.5 # Medium sized houses have a 1.5x surcharge 
    elif numberofRooms > 7:
        total_cost *= 2 # Large sized houses have a 2x surcharge
    # Rounds total_cost to the hundredths place   
    return round(total_cost, 2)

# This is the function that calculates the cost if the user chooses yard service
def totalcost_calculate_Yardservice(mowing, edging, pruning):
    mowing_per_sq_ft = 0.015    # Service charge for each sq ft of lawn to be mowed
    edging_per_ft = 0.30    # Service charge for each liner foot of lawn to be edged
    pruning_per_shrub = 10.00   # Service charge for each shrub to be pruned
    # Formulas that calculate the cost for each of the yard service services
    mowing_cost = mowing_per_sq_ft * mowing    
    edging_cost = edging_per_ft * edging
    pruning_cost = pruning_per_shrub * pruning
    # Sums all three categories of yard service
    total_cost = mowing_cost + edging_cost + pruning_cost
    # Returns the total_cost rounded to the hundredths place
    return round(total_cost, 2)

# This is the function that applies the 20% senior discount if the customer says 'yes' to the senior discount prompt
def senior_discount_rate(senior_discount, total_cost):
    # If the anser is yes then the discount is applied
    if senior_discount == 'yes':
        total_cost *= 0.85 # Applies a 20% senior discount rate
    # Returns the total_cost rounded to the hundredths place
    return round(total_cost, 2)


def main(): # welcome message for the user and some instruction on what to do when prompted
    print("\nWelcome to Alex's house cleaning service; we provide cleaning services for small, medium, and large homes.")
    print("We are now providing a yard service that includes: mowing, edging, and shrub pruning.")
    
    while True:
        # Loops statements to ensure that the user is continuosly prompted till an appropriate response is received
        type_of_service = input("\nPlease enter the type of service you need? ""house cleaning"" or ""yard service""\n")
        # If house cleaning is entered in the prompt then this loop is selected
        if type_of_service == "house cleaning":
            
            print("\nWhen prompted, please enter the amount of rooms that require cleaning and the types of cleaning needed.")
            print("\nOur list of services:\nlight cleaning: $15\ndeep cleaning: $40")
            # Loop that makes sure an integer is entered in the prompt, it also prints a statement if numbeofRooms is over 3
            while True:
                try:
                    numberofRooms = int(input("\nHow many rooms need to be cleaned: "))
                    if numberofRooms > 3:
                        print("There is a cleaning fee surcharge for medium and large homes.") # up front notice there is an upcharge for medium and large homes
                    break
                except ValueError:
                    print("Please enter a valid number.")
            # Next prompt after numberofRooms, the customers menu choices
            print("\nCleaning Menu:\nLight cleaning\nDeep cleaning")
            while True:
                typeofCleaning = input("\nEnter the type of cleaning from the menu:\n") # menu restated so the user knows how to input the preferred cleaning needed
                # Loop to check if the user inputed an expected string ('light cleaning', 'deep cleaning')
                if typeofCleaning in ('light cleaning', 'deep cleaning'):
                    break
                else:
                    print("Invalid house cleaning service. Please choose from the provided menu")   # If user enters a string or value not defined in typeofCleaning then they will be prompted to re-enter
            while True:
                senior_discount = input("Are you eligible for a senior discount? (yes/no): ")   # Last prompt to the user        
                if senior_discount in ('yes', 'no'): # If a yes or no is entered then the loop is finally broken and will call the appropriate functions and print the total_cost
                    break
                else:
                    print("Please enter a valid input ('yes' or 'no').")# If a 'yes' or 'no' is not received then the user is re-prompted 
            # Once all inputs are received and are expected, then Main calls the two functions for house cleaning
            total_cost = totalcost_calculate(numberofRooms, typeofCleaning) # Calls the function so it can be displayed 
            total_cost = senior_discount_rate(senior_discount, total_cost)  # Only called if the user enters 'yes' when prompted if they qualify for senior discount
            print("\nThe cost of house cleaning is: $",round(total_cost, 2)) # Displays the total cost the user will be charged for number of rooms, type of cleaning, and home upcharge if applicable
            break
        # If yard service is entered in the prompt then this loop is selected
        elif type_of_service == 'yard service':
            # Loop that makes sure an an integer is entered in the prompt, if not, an error response will print and they will be re-prompted
            while True:
                try:
                    mowing = float(input(f"\nPlease enter the square footage of your lawn that needs to be mowed:\n"))  # User is asked for integers concerning the categories of the yard service which will be fed to the appropriate function for calcualtion
                    edging = float(input(f"Please enter the linear footage of your lawn that needs edging:\n"))
                    pruning = int(input(f"Please enter the number of shrubs that need pruning:\n"))
                    break
                except ValueError:
                    print("Please enter a valid number")    # This print statement is prompted if the user enters an unexpected value like alpha characters
            # The last prompt to the user once all other inputs are received concerning yard service
            while True:
                senior_discount = input("Are you eligible for a senior discount? (yes/no): ")        
                if senior_discount in ('yes', 'no'): # Looks for the user to enter a yes or no specifically, anything else prints the error message and re-prompts the user
                    break
                else:
                    print("Please enter a valid input ('yes' or 'no').")
            # After all input are received, the Main can call the two functions for yard service
            total_cost = totalcost_calculate_Yardservice(mowing, edging, pruning)
            total_cost = senior_discount_rate(senior_discount, total_cost)  # Only called if user enters yes
            print("\nThe cost of your yard servicing is: $", total_cost)    # Displays the total cost the user will be chared for yard service
            break
        # This is the error message that is printed if the user enters an unexpected value for type_of_service
        else:
            print("Invalid service option entered. Please choose 'house cleaning' or 'yard service'.")

       
main()