# contact book dictionary
name = str(input("Enter contact name: "))
number = input("Enter contact number: ")
#print contact and number
contacts = {name: number}
print(f"{name}: {number}")
# search for a contact
search_name = str(input("Enter the name to search: "))
if search_name in contacts:
    print(f"Found contact - {search_name}: {contacts[search_name]}")
    
    
