#def user_info(name, age=None):
 #   """Prints user information."""
#    print(f"Name: {name}")
#    if age:
#       print(f"Age: {age}")
#user_info(name="Bob", age=30)

#def square(number):
# """Returns the square of a number."""
# return number * number
#squared_value = square(4) 
#print(squared_value) # squared_value will be 16

#x = 10  # Global variable

#def my_function():
 #   x = 5  # Local variable
  #  print("Inside function:", x)
#my_function()
#print("Outside function:", x)

#a function to greet the user by name.
#def greet_user(name):
#    print(f"Hi, {name}!")
#greet_user("Alice")
#greet_user("Bob")
#greet_user("Charlie")

#A function to calculate the area of a rectangle.
#def calculate_area(length, width):
#    area = length * width
#    return area
#result = calculate_area(5, 3)
#print(f"The area of the rectangle is: {result}")


 #a function to check if a number is even or odd.
#def check_even_odd(number):
#    if number % 2 == 0:
#        return "Even"
#    else:
#        return "Odd"
#status = check_even_odd(8)
#print(f"The number is: {status}")

#def greet(name):
#    print(f"Hi, {name}")
#greet("Darrell")
#greet("Dylan")

#a list to store names of your favorite fruits. Write code to access the second element and print it.

                  #data structure

#fruits = ["orange", "banana", "apple", "berries"]
#fruits[1]
#print(fruits)
#print(f"second fruit is: {fruits[1]}")

#a dictionary to store information about your favorite book, including title, author, and genre. Use the method to retrieve the genre.

#favourite_book = {
#    "Author" : "Morgan Housel",
#    "Title" : "The Psychology of Money",
#    "Genre" : "Finance"
#}
#print(favourite_book)
#x = favourite_book.get("Genre")
#print(f"The genre of the book is: {x}")

#program to generate a random set of numbers between 1 and ten. Use set operations to remove duplicates and display the unique numbers.
#number = {1, 2, 3, 1, 4, 7, 4, 1}
#print(number)
#number.remove(1)
#number.remove(4)
#number.add(5)
#number.add(6)
#print(f"The unique numbers are: {number}")

#import requests

#response = requests.get("https://api.github.com")
#if response.status_code == 200:
#    print("Success!")   
#else:   
#    print("An error occurred.")

#print(response.text)
#data = response.json()
#print(data)

#import requests

# Get info about a specific GitHub user
#user = "octocat"
#url = f"https://api.github.com/users/{user}"

#response = requests.get(url)
#if response.status_code == 200:
#    data = response.json()
#    print("User:", data["login"])
#    print("Name:", data["name"])
#    print("Public Repos:", data["public_repos"])
#    print("Followers:", data["followers"])
#else:
#    print("Error:", response.status_code)
