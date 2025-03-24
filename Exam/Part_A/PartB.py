import unittest
from PartA import House, FurnishedHouse  


class TestHouseMethods(unittest.TestCase):
    
    def setUp(self):
        # Initialize test objects for House and FurnishedHouse
        self.house = House(10, "Main Street", "Dublin", 3, 200000)
        self.furnished_house = FurnishedHouse(20, "Green Street", "Cork", 4, 300000, True, "Modern")

    # B2: Test if an object is an instance of a class
    def test_instance_of_class(self):
        self.assertIsInstance(self.house, House)
        self.assertIsInstance(self.furnished_house, FurnishedHouse)

    # B3: Test if an object is NOT an instance of a class
    def test_not_instance_of_class(self):
        self.assertNotIsInstance(self.house, FurnishedHouse)
        self.assertNotIsInstance(self.furnished_house, str)

    # B4: Test if 2 objects are identical
    def test_objects_are_identical(self):
        same_house = self.house
        self.assertIs(self.house, same_house)
        self.assertIsNot(self.house, self.furnished_house)

    # B5: Test update methods work correctly (from Part A4)
    def test_update_house_number(self):
        self.house.update_house_number(25)
        self.assertEqual(self.house.house_number, 25)

    def test_update_street(self):
        self.house.update_street("New Street")
        self.assertEqual(self.house.street, "New Street")

    def test_update_area(self):
        self.house.update_area("Galway")
        self.assertEqual(self.house.area, "Galway")

    def test_update_number_of_beds(self):
        self.house.update_number_of_beds(5)
        self.assertEqual(self.house.number_of_beds, 5)

    def test_update_price(self):
        self.house.update_price(255000.0)
        self.assertEqual(self.house.price, 255000.0)

    def test_update_furnished(self):
        self.furnished_house.update_furnished(False)
        self.assertFalse(self.furnished_house.furnished)

    def test_update_furniture_type(self):
        self.furnished_house.update_furniture_type("Classic")
        self.assertEqual(self.furnished_house.furniture_type, "Classic")


def main():
    unittest.main()


if __name__ == '__main__':
    main()
