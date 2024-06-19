#Lesson 2: Assignments | Tuples
#1. Tuple Mastery in Python
# Task 1:

def new_itinerary(itinerary_number, traveler_name, origin, destination):
    return(f"{itinerary_number}: {traveler_name} - from {origin} to {destination}")

print(new_itinerary("Itinerary 1", "Alice", "New York", "London"))
print(new_itinerary("Itinerary 2", "Bob", "Tokyo", "San Francisco"))

#2. Python Data Structure Challenges in Real-World Scenarios
#Task 1:
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

def book(name, author):
    new_book_entry = (name, author)
    if new_book_entry in library:
        print(f"Book '{name}' by {author} is already added.")
    else:
        library.append(new_book_entry)  


book("Dune", "Frank Herbert")
print(library)
