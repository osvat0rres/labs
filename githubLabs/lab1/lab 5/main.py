from flights import Flights

flights = Flights('flights.json')

while True:
    print("\nMenu:")
    print("1. Add flight")
    print("2. Print flight schedule")
    print("3. Set flight schedule filename")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        origin = input("Enter the origin: ")
        destination = input("Enter the destination: ")
        flight_number = input("Enter the flight number: ")
        departure = input("Enter the departure time (HHMM): ")
        next_day = input("Arrival the next day (Y/N): ")
        arrival = input("Enter the arrival time (HHMM): ")

        if flights.add_flight(origin, destination, flight_number, departure, next_day, arrival):
            print("Flight added successfully.")
        else:
            print("Invalid departure or arrival time. Flight not added.")
    
    elif choice == '2':
        flight_schedule = flights.get_flights()
        print("\nFlight Schedule:")
        for flight in flight_schedule:
            
            print(f"Origin: {flight['origin']}")
            print(f"Destination: {flight['destination']}")
            print(f"Flight Number: {flight['flight_number']}")
            print(f"Departure: {flight['departure']}")
            print(f"Arrival: {flight['arrival']}")
            print(f"Duration: {flight['duration']}")
            print()
    
    elif choice == '3':
        filename = input("Enter the new flight schedule filename: ")
        flights = Flights(filename)
        print(f"Flight schedule filename set to {filename}.")
    
    elif choice == '4':
        print("Exiting program...")
        break
    
    else:
        print("Invalid choice. Please try again.")