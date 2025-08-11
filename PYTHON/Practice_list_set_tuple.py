#Task:Write a program that:
#creates an empty list
#asks the user to enter a friend's name 5 times and adds these names to the list
#then prints all the names the user entered
#after that, asks for a name and checks if it is in the list (prints "yes" or "no")
name_list =[]
for i in range(5):
 add_list = input("Add name to the list: ")
 name_list.append(add_list)
print(name_list)

ask_name = input("Enter name to check if already exists in the list: ")
if ask_name in name_list:
    print("Yes, name is part of the list")
else:
    print("No, name is not in the list")


#Task: Write a program that:
#creates an empty set
#adds names entered by the user into the set (the user can enter the same name multiple times)
#after adding 5 names, prints the unique names
#asks for a name and tells if it is in the set
name = set()
for j in range(5):
    add_set = input("Add name to the set: ")
    name.add(add_set)
print("Unique names: ", name)
ask_set_name = input("Enter name to check if already exists in the set: ")
if ask_set_name in name:
    print("Yes, name is part of the set")
else:
    print("No, name is not in the set")


#Task:Write a program that:
# creates a tuple of three different fruits (e.g., ("apple", "banana", "cherry"))
# prints all the fruits from the tuple one by one
# know the fruit at a certain position (0, 1, or 2) and prints the fruit at that index
# if the user enters an invalid index, prints an error message
fruits_tuple = ("cherry", "blueberry", "raspberry","apple", "banana")
print("Fruits in basket",fruits_tuple)
choose_index = int(input("Choose index (0, 1, or 2) to know which fruit is there: "))
if 0 <= choose_index < len(fruits_tuple):
    print(f"Index {choose_index} - fruit {fruits_tuple[choose_index]}")
else:
    print("Invalid index number")
