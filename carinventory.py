# car_inventory.py

import json

# Sample dataset with 5 cars
car_inventory = [
    {"id": 1, "make": "Toyota", "model": "Camry", "year": 2021, "price": 25000},
    {"id": 2, "make": "Honda", "model": "Civic", "year": 2020, "price": 22000},
    {"id": 3, "make": "Ford", "model": "Mustang", "year": 2022, "price": 30000},
    {"id": 4, "make": "Chevrolet", "model": "Malibu", "year": 2019, "price": 20000},
    {"id": 5, "make": "Nissan", "model": "Altima", "year": 2023, "price": 28000}
]


# Function 1 Search cars by budget
def search_by_budget(inventory, max_price):
    """
    Filters cars based on a maximum price.

    Args:
        inventory (list): List of car dictionaries.
        max_price (int): Maximum budget.

    Returns:
        list: List of cars within the budget.
    """
    # TODO: Implement budget filtering logic
    pass  
    
# Function 2: Save inventory to a file
def save_inventory(inventory, filename="car_inventory.json"):
    """
    Saves the car inventory to a JSON file.

    Args:
        inventory (list): List of car dictionaries.
        filename (str): Filename to save the inventory.

    Returns:
        str: Filename after successful save.
    """
    # TODO: Implement file saving logic
    pass 

# Execute the functions
if __name__ == "__main__":

    search_by_budget(car_inventory, 25000)
    save_inventory(car_inventory)
