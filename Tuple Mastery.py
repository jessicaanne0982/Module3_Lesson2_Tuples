# Task 1

def format_itinerary():
    for index, itinerary in enumerate(itineraries):
        customer_name, trip_origin, trip_destination = itinerary
        print(f"Itinerary {index + 1}: {customer_name} - From {trip_origin} to {trip_destination}")

itineraries = [
            ("Alice", "New York", "London"), 
            ("Bob", "Tokyo", "San Francisco"),
            ("Jack", "Miami", "Chicago")
]

format_itinerary()
