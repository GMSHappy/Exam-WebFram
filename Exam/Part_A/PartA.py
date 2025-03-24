class House:
    def __init__(self, house_number, street, area, number_of_beds, price):
        self.house_number = house_number
        self.street = street
        self.area = area
        self.number_of_beds = number_of_beds
        self.price = price

# Print all the details of the house
    def print_details(self):
        print(f"House Number: {self.house_number}")
        print(f"Street: {self.street}")
        print(f"Area: {self.area}")
        print(f"Number of Beds: {self.number_of_beds}")
        print(f"Price: {self.price}")

    # Update the house number if the input is valid Same thing for everyhting below from Street to Price and area
    def update_house_number(self, new_number):
        if isinstance(new_number, int):
            self.house_number = new_number
        else:
            print("Error: house number must be an integer")

    def update_street(self, new_street):
        if isinstance(new_street, str):
            self.street = new_street
        else:
            print("Error: street must be a string")

    def update_area(self, new_area):
        if isinstance(new_area, str):
            self.area = new_area
        else:
            print("Error: area must be a string")

    def update_number_of_beds(self, new_beds):
        if isinstance(new_beds, int):
            self.number_of_beds = new_beds
        else:
            print("Error: number of beds must be an integer")

    def update_price(self, new_price):
        if isinstance(new_price, (int, float)):
            self.price = new_price
        else:
            print("Error: price must be a number")

# This class represents a furnished house, which is a type of house with extra details :)
class FurnishedHouse(House):
    def __init__(self, house_number, street, area, number_of_beds, price, furnished, furniture_type):
        super().__init__(house_number, street, area, number_of_beds, price)
        self.furnished = furnished
        self.furniture_type = furniture_type

    def print_full_details(self):
        super().print_details()
        print(f"Furnished: {self.furnished}")
        print(f"Furniture Type: {self.furniture_type}")

    def update_furnished(self, new_furnished):
        if isinstance(new_furnished, bool):
            self.furnished = new_furnished
        else:
            print("Error: furnished must be True or False")

    def update_furniture_type(self, new_type):
        if isinstance(new_type, str):
            self.furniture_type = new_type
        else:
            print("Error: furniture type must be a string")



# Creating instances of House and FurnishedHouse
print("Creating instances...\n")
basic_house = House(12, "Barrack Street", "Drogheda", 3, 250000)
furnished_house = FurnishedHouse(45, "Shop Street", "Drogheda", 4, 320000, True, "Modern")

# Printing details of the basic house
print("\nBasic House Details:")
basic_house.print_details()

# Printing details of the furnished house
print("\nFurnished House Details:")
furnished_house.print_full_details()

# Updating and printing details of the basic house
print("\nUpdating Basic House...")
basic_house.update_house_number(20)
basic_house.update_price(275000)
basic_house.print_details()

# Updating and printing details of the furnished house
print("\nUpdating Furnished House...")
furnished_house.update_furnished(False)
furnished_house.update_furniture_type("Classic")
furnished_house.print_full_details()
