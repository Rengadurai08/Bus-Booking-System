import random

class Customer:
    def __init__(self, name, gender, age, contact_number):
        self.name = name
        self.gender = gender
        self.age = age
        self.contact_number = contact_number
    
    def display_customer_details(self):
        print(f"Name: {self.name}")
        print(f"Gender: {self.gender}")
        print(f"Age: {self.age}")
        print(f"Contact Number: {self.contact_number}")


class Booking:
    def __init__(self):
        self.route = None
        self.travel_date = None
        self.seat_type = None
        self.comfort = None
        self.travels = None
        self.otp = None

    def select_route(self):
        route = int(input("Travelling Routes:\n"
                          "1 - Chennai to Trichy\n"
                          "2 - Chennai to Bangalore\n"
                          "3 - Madurai to Salem\n"
                          "4 - Chennai to Coimbatore\n"
                          "Enter the choice (1-4): "))
        if route == 1:
            self.route = "Chennai to Trichy"
        elif route == 2:
            self.route = "Chennai to Bangalore"
        elif route == 3:
            self.route = "Madurai to Salem"
        elif route == 4:
            self.route = "Chennai to Coimbatore"
        else:
            print("Invalid Choice")

    def input_travel_date(self):
        self.travel_date = input("Enter the date of travel (DD/MM/YYYY): ")
        print("Travel Date:", self.travel_date)

    def select_seat(self):
        seat = int(input("Select the seat:\n"
                         "1 - Window seat\n"
                         "2 - Middle seat\n"
                         "3 - Corner seat\n"
                         "Enter the choice (1-3): "))
        if seat == 1:
            self.seat_type = "Window seat"
        elif seat == 2:
            self.seat_type = "Middle seat"
        elif seat == 3:
            self.seat_type = "Corner seat"
        else:
            print("Invalid Choice")

    def select_comfort(self):
        comfort = int(input("Select the bus comfort:\n"
                            "1 - AC\n"
                            "2 - Non-AC\n"
                            "Enter the bus comfort (1-2): "))
        if comfort == 1:
            self.comfort = "AC"
        elif comfort == 2:
            self.comfort = "Non-AC"
        else:
            print("Invalid Choice")

    def select_travels(self):
        travels = int(input("Select the travels:\n"
                            "1 - Parveen Travels\n"
                            "2 - Intercity Travels\n"
                            "3 - Ranganathan Travels\n"
                            "4 - KPN Travels\n"
                            "Enter the choice (1-4): "))
        if travels == 1:
            self.travels = "Parveen Travels"
        elif travels == 2:
            self.travels = "Intercity Travels"
        elif travels == 3:
            self.travels = "Ranganathan Travels"
        elif travels == 4:
            self.travels = "KPN Travels"
        else:
            print("Invalid Choice")

    def generate_otp(self):
        self.otp = random.randint(100000, 999999)
        print(f"Your OTP is: {self.otp}")
        entered_otp = int(input("Please enter the OTP: "))
        if entered_otp == self.otp:
            print("OTP verified!")
        else:
            print("Invalid OTP, please try again.")
            self.generate_otp()

    def display_booking_details(self, customer):
        print("\n--- Booking Details ---")
        customer.display_customer_details()
        print(f"Route: {self.route}")
        print(f"Travel Date: {self.travel_date}")
        print(f"Seat Type: {self.seat_type}")
        print(f"Bus Comfort: {self.comfort}")
        print(f"Bus Travels: {self.travels}")
        print(f"OTP: {self.otp}")


# Main function to drive the bus booking process
def Bus_booking():
    print("Welcome to the Bus Booking System")
    
    # Input Customer Details
    name = input("Enter your name: ")
    gender = input("Enter your gender: ")
    age = input("Enter your age: ")
    contact_number = input("Enter your contact number: ")
    
    # Create Customer object
    customer = Customer(name, gender, age, contact_number)
    
    # Create Booking object
    booking = Booking()

    # Select routes, seat, bus comfort, travels
    booking.select_route()
    booking.input_travel_date()
    booking.select_seat()
    booking.select_comfort()
    booking.select_travels()

    # Generate and verify OTP
    booking.generate_otp()

    # Display the final booking details
    booking.display_booking_details(customer)


# Run the bus booking process
Bus_booking()
