
#Languages = ["python", "Ruby", "Go", "JavaScript"]
#start of for loop
#for lang in Languages:
    #print(lang)
    #print(".....")
#end of for loop
#print("These are programming languages.")

#a program to find the sum of numbers from 1 to 10
#number = int(input("Enter an integer: "))
#for count in range (1,11):
    #i want the sum of all numbers to 
    #sum = number + count
    #print(f"{number} + {count} = {sum}")
#end of for loop

#even number using for loop
#count = 0
#for even in range (1,20):
    #if even % 2 == 0:
     #count += 1
     #print(even)
#print(f"We have {count} even numbers in the range of 1 to 20")

#for i in range(1, 11):
  # Outer loop iterates through rows (multiplication factors)
  #for j in range(1, 11):
    # Inner loop iterates through columns (other factors)
    #product = i * j
    #print(f"{i} x {j} = {product}", end="\t")  # Print with tabs for better formatting
  #print()  # Move to a new line after each row

#Crafting Creative Patterns:
rows = 5

#for i in range(1, rows + 1):
  # Outer loop controls the number of rows
  #for j in range(1, i + 1):
    # Inner loop prints asterisks for each row
    #print("*", end="")
  #print()  # Move to a new line after each row of asterisks

#Drawing Patterns with Nested Loops
#pattern = int
#print("Enter the size of the pattern: ")

pattern = int(input("Enter the size of the pattern: " ))
for x in range(pattern):
    for y in range (pattern):
        print("*", end="")
    print()
    

