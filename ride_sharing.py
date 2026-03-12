# Ride Sharing System Simulation
# This program simulates a ride-sharing platform where drivers
# can register available rides and passengers can request rides.
# The system matches passengers with available drivers.
drivers = []
ride_requests = []

def add_driver():
    name = input("Enter driver name: ")
    location = input("Enter driver location: ")

    driver = {
        "name": name,
        "location": location,
        "available": True
    }

    drivers.append(driver)

    print("Driver added successfully.\n")


def request_ride():
    passenger = input("Enter passenger name: ")
    location = input("Enter pickup location: ")

    for driver in drivers:
        if driver["available"] and driver["location"] == location:

            driver["available"] = False

            print("\nRide Matched Successfully!")
            print("Passenger:", passenger)
            print("Driver:", driver["name"])
            print("Location:", location)
            print()

            return

    print("No drivers available at this location.\n")


def view_drivers():

    print("\n========== DRIVER LIST ==========")

    if not drivers:
        print("No drivers registered.")

    for driver in drivers:
        status = "Available" if driver["available"] else "Busy"
        print(f"Driver: {driver['name']} | Location: {driver['location']} | Status: {status}")

    print("=================================\n")

def main():
 
    while True:

        print("========= RIDE SHARING SYSTEM =========")
        print("1. Add Driver")
        print("2. Request Ride")
        print("3. View Drivers")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_driver()

        elif choice == "2":
            request_ride()

        elif choice == "3":
            view_drivers()

        elif choice == "4":
            print("Exiting system...")
            break

        else:
            print("Invalid option.\n")


main()