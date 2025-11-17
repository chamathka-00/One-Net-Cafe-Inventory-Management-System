# Import necessary modules
import datetime
import random

file_items = 'items.txt'    # File to store and retrieve item details
file_dealers = 'dealers.txt'    # File containing dealers' details

items = []  # Initialize an empty list to store item dictionaries

# Function to read and load item details from the items file
def read_item_file():
    try:
        with open(file_items, 'r') as file: # Opens the file in read mode
            for line in file:    # Reads each line in the file
                item_details = line.strip().split(',')  # Removes whitespace and splits the line by comma
                if len(item_details) == 7: # Checks if the line has exactly 7 values
                    items.append({  # Appends a new item dictionary to the 'items' list
                        'item_code': item_details[0],
                        'item_name': item_details[1],
                        'item_brand': item_details[2],
                        'item_price': item_details[3],
                        'quantity': int(item_details[4]),
                        'category': item_details[5],
                        'purchased_date': item_details[6]
                    })
                else:   # If the line doesn't have 7 values, it will be skipped
                    print(f'Skipped invalid line: {line.strip()}')

    except FileNotFoundError:   # Handles the case where file does not exist
        print(f"\nThe file '{file_items}' does not exist in the current directory.")
        print(f"Please check if the file is located in a different directory, or create a file named '{file_items}' in the current directory")
        exit()  # Exiting the program since the items file is essential

# Function to add a new item
def add_item():
    while True: # Loops until a valid code is entered
        item_code = input('Enter item code: ').strip()
        if item_code == '':
            print('Item code is required. Please try again.')   # Rejecting empty values
        elif any(item['item_code'] == item_code for item in items):
            print('Error: Item code already exists. Please enter a different code.')    # Rejecting if code already exists
        elif len(item_code) != 3:
            print('Invalid format. Please enter an item code in three digit format.')   # Rejecting if the code does not contain 3 characters
        else:
            break   # Accepts the code if it is valid

    while True: # Loops until a valid name is entered
        item_name = input('Enter item name: ').strip()
        if item_name == '':
            print('Item name is required. Please try again.')   # Rejecting empty values
        else:
            break   # Accepts the name if it is valid

    while True: # Loops until a valid brand is entered
        item_brand = input('Enter item brand: ').strip()
        if item_brand == '':
            print('Item brand is required. Please try again.')  # Rejecting empty values
        else:
            break   # Accepts the brand if it is valid

    while True: # Loops until a valid price is entered
        price = input('Enter item price: ').strip()
        if price == '':
            print('Item price is required. Please try again.')  # Rejecting empty values
        else:
            try:
                price = float(price)    # Converting user input to a float
                if price <= 0:
                    print('Price must be a positive number.')   # Rejecting if the input is not a positive number
                else:
                    item_price = f'Rs. {price:.2f}' # Formating price with 2 decimal places and 'Rs.' prefix
                    break   # Accepts the price if it is valid
            except ValueError:  # Handles the case where input is not a valid number
                print('Invalid input. Please enter a number for price.')

    while True: # Loops until a valid quantity is entered
        quantity = input('Enter item quantity: ').strip()
        if quantity == '':
            print('Item quantity is required. Please try again.')   # Rejecting empty values
        else:
            try:
                quantity = int(quantity)    # Converting user input to an integer
                if quantity <= 0:
                    print('Quantity must be a positive number.')    # Rejecting if the input is not a positive number
                else:
                    break   # Accepts the quantity if it is valid
            except ValueError:  # Handles the case where input is not a valid number
                print('Invalid input. Please enter a whole number for quantity.')

    while True: # Loops until a valid category is entered
        category = input('Enter item category: ').strip()
        if category == '':
            print('Item category is required. Please try again.')   # Rejecting empty values
        else:
            break   # Accepts the category if it is valid

    while True: # Loops until a valid date is entered
        purchased_date = input('Enter the purchased date (YYYY-MM-DD): ').strip()
        if purchased_date == '':
            print('Item purchased date is required. Please try again.') # Rejecting empty values
        else:
            try:
                datetime.datetime.strptime(purchased_date, "%Y-%m-%d")  # Checking whether the date format is valid
                break   # Accepts the date if it is valid
            except ValueError:  # Handles the case where input format is wrong
                print('Invalid date. Please enter a valid date in the format YYYY-MM-DD.')
    # Add the validated item to the 'items' list as a dictionary
    items.append({
        'item_code': item_code,
        'item_name': item_name,
        'item_brand': item_brand,
        'item_price': item_price,
        'quantity': quantity,
        'category': category,
        'purchased_date': purchased_date
    })
    print(f'New item with the code {item_code} added to the items file successfully!')

# Function to delete an existing item
def delete_item():
    while True: # Loops until a value is entered
        delete_code = input('Enter the code of the item to delete: ').strip()
        if delete_code == '':
            print('Item code is required. Please try again.')   # Rejecting empty values
        else:
            break   # Accepts any value entered

    for item in items:  # Loops through each item in the 'items' list
        if item['item_code'] == delete_code:    # Checking whether the item's code matches with the input code
            print(f'Item with the code {delete_code} found.')   # Informing user that the code was found
            print(f"Item Name: {item['item_name']}")
            print(f"Brand: {item['item_brand']}")
            print(f"Price: {item['item_price']}")
            print(f"Quantity: {item['quantity']}")
            print(f"Category: {item['category']}")
            print(f"Purchased Date: {item['purchased_date']}")

            while True: # Asking for a valid confirmation command to delete
                confirm_delete = input('Are you sure you want to delete this item? (yes/no): ').strip().lower()
                if confirm_delete == 'yes':
                    items.remove(item)  # Removing the item from the list upon confirmation
                    print(f'Item with the code {delete_code} deleted from the items file successfully!')
                    return  # Exit the function after deleting
                elif confirm_delete == 'no':
                    print("Item deletion canceled.")
                    return  # Exit the function without deleting
                else:
                    print("Invalid input. Please type 'yes' or 'no'.")

    print(f'Item with the code {delete_code} not found.')   # Informing if no matching item code is found after looping through all items

# Function to update an item's details
def update_item():
    while True: # Loops until a value is entered
        update_item_code = input('Enter the code of the item to update: ').strip()
        if update_item_code == '':
            print('Item code is required. Please try again.')   # Rejecting empty values
        else:
            break   # Accepts any value entered

    for item in items:  # Loops through each item in the 'items' list
        if item['item_code'] == update_item_code:   # Checking whether the item's code matches with the input code
            new_item_name_input = input(f"Enter new name or press enter to keep current data (current name: {item['item_name']}): ").strip()
            if new_item_name_input == '':   # If user press enter
                new_item_name = item['item_name']   # Keep the current value
            else:
                new_item_name = new_item_name_input # Use the new value

            new_item_brand_input = input(f"Enter new brand or press enter to keep current data (current brand: {item['item_brand']}): ").strip()
            if new_item_brand_input == '':
                new_item_brand = item['item_brand']
            else:
                new_item_brand = new_item_brand_input

            new_price_input = input(f"Enter new price or press enter to keep current data (current price: {item['item_price']}): ").strip()
            if new_price_input == '':
                new_item_price = item['item_price']
            else:
                while True: # Validates new price input
                    try:
                        new_price = float(new_price_input)
                        if new_price <= 0:
                            print('Price must be a positive number.')
                        else:
                            new_item_price = f'Rs. {new_price:.2f}'
                            break
                    except ValueError:
                        print('Invalid input. Please enter a number for price.')

            new_quantity_input = input(f"Enter new quantity or press enter to keep current data (current quantity: {item['quantity']}): ").strip()
            if new_quantity_input == '':
                new_quantity = item['quantity']
            else:
                while True: # Validates new quantity input
                    try:
                        new_item_quantity = int(new_quantity_input)
                        if new_item_quantity <= 0:
                            print('Quantity must be a positive number.')
                        else:
                            new_quantity = new_item_quantity
                            break
                    except ValueError:
                        print('Invalid input. Please enter a whole number for quantity.')

            new_category_input = input(f"Enter new category or press enter to keep current data (current category: {item['category']}): ").strip()
            if new_category_input == '':
                new_category = item['category']
            else:
                new_category = new_category_input

            new_purchased_date_input = input(f"Enter new purchased date or press enter to keep current data (current date: {item['purchased_date']}): ").strip()
            if new_purchased_date_input == '':
                new_purchased_date = item['purchased_date']
            else:
                while True: # Validates new date input
                    try:
                        datetime.datetime.strptime(new_purchased_date_input, "%Y-%m-%d")
                        new_purchased_date = new_purchased_date_input
                        break
                    except ValueError:
                        print('Invalid date format. Please enter the date in YYYY-MM-DD format.')
            # Update the item dictionary with new values
            item['item_name'] = new_item_name
            item['item_brand'] = new_item_brand
            item['item_price'] = new_item_price
            item['quantity'] = new_quantity
            item['category'] = new_category
            item['purchased_date'] = new_purchased_date
            print('Item updated successfully!')
            return  # Exit the function after updating
    print(f'Item with the code {update_item_code} not found.')  # Informing if no matching item code is found after looping through all items

# Function to view items in the form of a table
def view_items_by_category():
    categories = [] # Initialize an empty list to store unique categories
    for item in items:  # Loops through all items to collect unique categories
        if item['category'] not in categories:  # Checking whether the category is not already in the 'categories' list
            categories.append(item['category']) # Adding new category to the 'categories' list

    for i in range(len(categories)):    # Sort categories in alphabetical order
        for j in range(i+1, len(categories)):
            if categories[i] > categories[j]:
                categories[i], categories[j] = categories[j], categories[i] # Swapping if out of the order

    total_quantity = 0  # Initialize total quantity for all categories
    total_amount = 0    # Initialize total amount for all categories

    print(f"{' ':<64} {'**** Item Details ****'}")  # Displaying a centered header
    for category in categories: # Loops through each category in 'categories' list
        print(f"\nCategory: {category}")    # Displaying current category name
        print('_' * 140)
        # Displaying column headers for item details
        print(f"{'item Code':<15} {'Name':<30} {'Brand':<20} {'Purchased Date':<20} {'Quantity':<15} {'Price':<20} {'Amount'}")
        print('_' * 140)

        category_items = [] # Initialize a list to hold items of the current category
        for item in items:  # Collects all the items that belong to the current category
            if item['category'] == category:
                category_items.append(item)

        for i in range(len(category_items)):    # Sort items in descending order based on item code
            for j in range(i+1, len(category_items)):
                if category_items[i]['item_code'] < category_items[j]['item_code']:
                    category_items[i], category_items[j] = category_items[j], category_items[i] # Swapping if out of the order

        quantity_per_category = 0   # Initialize total quantity in the current category
        amount_per_category = 0 # Initialize total amount in the current category

        for item in category_items: # Loops through each item in the sorted 'category_items' list
            amount = float(item['item_price'][3:]) * item['quantity']   # Calculating amount
            quantity_per_category += item['quantity']   # Adding current item's quantity to the total quantity of the current category
            amount_per_category += amount   # Adding calculated amount to the total amount in the current category
            # Displaying item details in a formatted row
            print(f"{item['item_code']:<15} {item['item_name']:<30} {item['item_brand']:<20} {item['purchased_date']:<20} {item['quantity']:<15} {item['item_price']:<20} Rs. {amount:.2f}")
        print('_' * 140)
        # Displaying total quantity and total amount for the current category
        print(f"{' ':<86} = {quantity_per_category} {' ':<31} = Rs. {amount_per_category:.2f}")
        # Adding category totals to overall totals
        total_quantity += quantity_per_category
        total_amount += amount_per_category

    print('_' * 140)
    # Displaying overall totals for all categories
    print(f"{' ':<71} Total Quantity = {total_quantity} {' ':<18} Total Amount = Rs. {total_amount:.2f}")

# Function to save item details to the item file
def save_items():
    with open(file_items, 'w') as file: # Opens the file in write mode to overwrite the file
        for item in items:  # Loops through each item in the 'items' list
            # Format the item details as a comma-separated string followed by a new line
            item_details = f"{item['item_code']},{item['item_name']},{item['item_brand']},{item['item_price']},{item['quantity']},{item['category']},{item['purchased_date']}\n"
            file.write(item_details)    # Writes the formatted string to the file
    print('Modifications to the items file saved successfully!')

# Function to randomly select 4 dealers
def select_random_dealers():
    try:
        with open(file_dealers, 'r') as file:   # Opens the file in read mode
            file_content = file.read()  # Reads the entire content of the file

        dealers_details = file_content.strip().split('\n\n')    # Splits the content into separate dealer blocks

        if len(dealers_details) != 6:    # Checking whether 6 dealers are found in the file
            print(f'\nError: All 6 dealers were not found in the dealers file. Only {len(dealers_details)} dealers were found.')
            print('Please correct the dealers file according to the required format before trying again.')
            return  # Exit the function early when the requirement is not met
        else:
            selected_dealers = random.sample(dealers_details, 4)    # Randomly select 4 dealers when the requirement is met
            print('4 dealers are selected randomly.')
            return selected_dealers # Return the selected dealer details to the caller

    except FileNotFoundError:   # Handles the case where file does not exist
        print(f"\nThe file '{file_dealers}' does not exist in the current directory.")
        print('Please check if the file is located in a different directory')
        return  # Exiting the function since dealers file is essential

# Function to display randomly selected dealers' details
def display_random_dealers(random_dealers):
    print(f"\n{'*' * 34} Selected Dealers {'*' * 34}\n")    # Displaying a title header

    for i in range(len(random_dealers)):    # Sort selected dealers according to the location
        for j in range(i + 1, len(random_dealers)):
            location_i = random_dealers[i].split('\n')[2].strip()
            location_j = random_dealers[j].split('\n')[2].strip()

            if location_i > location_j:
                random_dealers[i], random_dealers[j] = random_dealers[j], random_dealers[i] # Swapping if out of order

    dealer_number = 1   # Initialize a variable to keep track of the dealer number
    for dealer in random_dealers:   # Loops through each sorted dealer
        dealer_details = dealer.strip().split('\n') # Splitting the current dealer's details into a list by line
        # Extracts current dealer's name, contact, location and list of available items from the dealer details
        name = dealer_details[0]
        contact = dealer_details[1]
        location = dealer_details[2]
        available_items = dealer_details[3:]

        print('=' * 86)
        # Displaying current dealer's basic information
        print(f'Dealer {dealer_number}: {name}')
        print(f'Contact: {contact}')
        print(f'Location: {location}')
        print('Items:')
        print('_' * 86)
        # Displaying column names for item details in a formatted table row
        print(f"{'Item Name':<25} {'Brand':<25} {'Unit Price':<25} {'Quantity'}")
        print('_' * 86)

        for item in available_items:    # Loops through each item string in the dealer's items list
            item_details = item.split(',')  # Splitting the current item string into components by commas
            if len(item_details) == 4:
                item_name, brand, price, quantity = item_details    # Unpacking values if the item has exactly 4 details
                print(f"{item_name:<25} {brand:<25} {'Rs. ' + format(float(price), '.2f'):<25} {quantity}")    # Displaying the item in a formatted table row
            else:   # If the item doesn't have 4 details, it will be skipped
                print(f'Skipped an item due to incorrect format: {item}')
        print(f"{'=' * 86}\n")  # Separating current dealer's details from the next dealer's details

        dealer_number += 1  # Increment the dealer number for the next dealer

# Function to display the items of a given selected dealer
def view_dealer_items(random_dealers):
    while True: # Loops until a value is entered
        dealer_name_input = input('Enter the dealer name to view the items available: ').strip().replace(' ', '')
        if dealer_name_input == '':
            print('Dealer name is required. Please try again.')
        else:
            break   # Exit the loop when a value is entered

    dealer_found = False    # Boolean flag to check whether the dealer is found
    for dealer in random_dealers:   # Loops through each dealer in random dealers
        dealer_details = dealer.strip().split('\n') # Split current dealer block into individual lines containing dealer's details
        # Extracts current dealer's name and list of available items from the dealer details
        name = dealer_details[0]
        available_items = dealer_details[3:]

        if name.lower() == dealer_name_input.lower():   # Case-insensitive comparison of dealer name
            dealer_found = True # Set boolean flag to True when dealer is found
            print('Items:')
            print('_' * 86)
            # Displaying column names for item details in a formatted table row
            print(f"{'Item Name':<25} {'Brand':<25} {'Unit Price':<25} {'Quantity'}")
            print('_' * 86)

            for item in available_items:    # Loops through each item string in the dealer's items list
                item_details = item.split(',')  # Splitting the current item string into components by commas
                if len(item_details) == 4:
                    item_name, brand, price, quantity = item_details    # Unpacking values if the item has exactly 4 details
                    print(f'{item_name:<25} {brand:<25} {'Rs. ' + format(float(price), '.2f'):<25} {quantity}')
                else:  # If the item doesn't have 4 details, it will be skipped
                    print(f'Skipped an item due to incorrect format: {item}')
            print('_' * 86)
            break   # Exits the loop when matching dealer is found and items are displayed

    if not dealer_found:
        print('Dealer cannot be found.')    # Display error message if no dealer matched the input

# Function to display the menu options to the user
def display_menu():
    print('\n**** One Net Cafe Manager ****\n') # Display the program title
    print('Type AID for adding item details.')
    print('Type DID for deleting item details.')
    print('Type UID for updating item details.')
    print('Type VID for viewing the items table.')
    print('Type SID for saving the item details.')
    print('Type SDD for selecting four dealers randomly.')
    print('Type VRL for displaying the details of selected dealers.')
    print('Type LDI for displaying the items of a given dealer.')
    print('Type ESC to exit.')

# Main function
def main():
    read_item_file()    # Loads existing item details from the items file into the 'items' list
    randomly_selected_dealers = [] # Initialize an empty list to hold the randomly selected dealers
    random_dealers_selection = False    # Boolean flag to check whether the dealers have been selected

    while True: # Starts the main loop of the program
        display_menu()
        user_input = input('\nEnter your choice: ').strip().upper()

        if user_input == 'ESC': # Handling the exit command
            while True: # Asking for a valid confirmation command to exit
                confirm_exit = input('Are you sure you want to exit? (yes/no): ').strip().lower()
                if confirm_exit == 'yes':
                    while True: # Asking for a valid confirmation command to save before exiting
                        confirm_save = input('Do you want to save before exiting? (yes/no): ').strip().lower()
                        if confirm_save == 'yes':
                            save_items()    # Saving modifications to the items file
                            print('Exiting the program.\nThank you for using One Net Cafe Manager!')
                            exit()
                        elif confirm_save == 'no':
                            print('Exiting the program without saving.\nThank you for using One Net Cafe Manager!')
                            exit()
                        else:
                            print("Invalid input. Please enter 'yes' or 'no'.")
                elif confirm_exit == 'no':
                    print('Returning to the menu...')   # Cancelling the exit process
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")

        elif user_input == 'AID':
            add_item()

        elif user_input == 'DID':
            delete_item()

        elif user_input == 'UID':
            update_item()

        elif user_input == 'VID':
            view_items_by_category()

        elif user_input == 'SID':
            save_items()

        elif user_input == 'SDD':
            randomly_selected_dealers = select_random_dealers()
            random_dealers_selection = True

        elif user_input == 'VRL':
            if not random_dealers_selection:    # Selecting random dealers if they haven't been selected
                randomly_selected_dealers = select_random_dealers()
                random_dealers_selection = True
            display_random_dealers(randomly_selected_dealers)

        elif user_input == 'LDI':
            if not random_dealers_selection:    # Selecting random dealers if they haven't been selected
                randomly_selected_dealers = select_random_dealers()
                random_dealers_selection = True
            view_dealer_items(randomly_selected_dealers)

        else:
            print('Invalid choice. Please try again.')

main()  # Calling the main function to start the program