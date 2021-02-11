# Get the data from the user and store it in a list then display the most recent three entries

# Set up the empty lists
all_calculations = []

# Get five items of Data
for item in range (0, 5):
    get_item = input("Enter an item: ")
    all_calculations.append(get_item)

# Show that everything made it to the list..
print()
print("*The Full List*")
print(all_calculations)

print()

print("*** The Most Recent 3 ***")
# print items starting at the END of the list
print()