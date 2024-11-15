# Define the list of authorized vehicles
AllowedVehiclesList = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']

# Function to print the list of authorized vehicles
def print_vehicles():
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
    for vehicle in AllowedVehiclesList:
        print(vehicle)

# Function to search for a vehicle in the allowed list
def search_vehicle():
    # Ask user for vehicle name
    vehicle_to_search = input("Please Enter the full Vehicle name: ").strip()

    # Search for the vehicle in the list
    if vehicle_to_search in AllowedVehiclesList:
        print(f"{vehicle_to_search} is an authorized vehicle")
    else:
        print(f"{vehicle_to_search} is not an authorized vehicle, if you received this in error please check the spelling and try again")

# Function to add a new vehicle to the allowed list
def add_vehicle():
    # Ask user for the new vehicle name
    vehicle_to_add = input("Please Enter the full Vehicle name you would like to add: ").strip()

    # Add the new vehicle to the list and confirm
    AllowedVehiclesList.append(vehicle_to_add)
    print(f'You have added "{vehicle_to_add}" as an authorized vehicle')

# Function to display the main menu and handle user input
def menu():
    while True:
        print("********************************")
        print("AutoCountry Vehicle Finder v0.3")
        print("********************************")
        print("Please Enter the following number below from the following menu:\n")
        print("1. PRINT all Authorized Vehicles")
        print("2. SEARCH for Authorized Vehicle")
        print("3. ADD Authorized Vehicle")
        print("4. Exit")
        
        # Get user input
        choice = input("Enter your choice (1, 2, 3, or 4): ").strip()
        
        if choice == "1":
            print_vehicles()
        elif choice == "2":
            search_vehicle()
        elif choice == "3":
            add_vehicle()
        elif choice == "4":
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("Invalid choice, please enter 1, 2, 3, or 4.")

# Start the program
menu()
