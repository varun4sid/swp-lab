"""
A travel booking app might offer a single method for booking a complete
travel package, handling the interactions with each service and
presenting a simplified interface to the user. 

Use facade pattern to implement this functionality.
"""

class FlightBooking:
    def book_flight(self):
        print("Booking flight...")
        
class HotelBooking:
    def book_hotel(self):
        print("Booking hotel...")
        
class CarRentalBooking:
    def book_car_rental(self):
        print("Booking car rental...")
        
class TravelBookingFacade:
    def __init__(self):
        self.flight_booking = FlightBooking()
        self.hotel_booking = HotelBooking()
        self.car_rental_booking = CarRentalBooking()

    def book_travel_package(self):
        self.flight_booking.book_flight()
        self.hotel_booking.book_hotel()
        self.car_rental_booking.book_car_rental()
        print("Travel package booked successfully!")
        
def main():
    travel_booking = TravelBookingFacade()
    travel_booking.book_travel_package()
    
    
main()