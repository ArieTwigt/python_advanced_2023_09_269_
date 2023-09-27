import random
import string
import pandas as pd


class Vehicle:

    def change_price(self, price_change: float) -> None:
        '''
        Change the price of the car

        - price_change: can be positive or negative 
            e.g. - 1000 for negative
        '''
        print(f"Old price {self.price}")
        self.old_prices.append(self.price)
        new_price = self.price + price_change

        if new_price < 0:
            raise ValueError("The price cannot be lower than 0")
        
        self.price += price_change
        print(f"New price {self.price}")


    def __repr__(self) -> str:
        return f"Brand: 🚗 {self.brand} Price 💰 {self.price} Type: {self.type} Old prices 📈 {self.old_prices}"


class Car(Vehicle):
    

    def __init__(self, brand: str, price: float) -> None:
        '''
        Inititate a car class:

        - brand: brand of the car
        - price: price of the car
        '''
        self.brand = brand
        self.price = price
        self.old_prices = []
        self.type = "🚗 car"



class Motor(Vehicle):

    def __init__(self, brand: str, price: float) -> None:
        self.brand = brand
        self.price = price
        self.old_prices = []
        self.type = "🏍️ motor"


class Bicycle(Vehicle):

    def __init__(self, brand: str, price: float) -> None:
        self.brand = brand
        self.price = price
        self.old_prices = []
        self.type = "🚴bicycle"


class VehicleCollection:


    def __init__(self, collection_name: str) -> None:
        self.collection_name = collection_name
        self.collection_items = []
        self.status = "Initialized"


    def add_vehicle(self, *args) -> None:
        for vehicle in args:
            self.collection_items.append(vehicle)
            print(f"Added {vehicle}")

        self.status = "Vehicles added"


    def __repr__(self) -> str:

        return f"Name: {self.collection_name} - # items: {len(self.collection_items)}"
    

    def summarize_collection(self):
        

        if len(self.collection_items) == 0:
            raise ValueError("Cannot summarize without cars")
        
        
        num_items = len(self.collection_items)
        total_price = 0


        for collection_item in self.collection_items:
            total_price += collection_item.price

        
        mean_price = total_price / num_items

        # create a dictionary witht the summary items
        summary_dict = {}
        summary_dict['num_items'] = num_items
        summary_dict['total_price'] = total_price
        summary_dict['mean_price'] = mean_price

        self.status = "Vehicles summarized"

        return summary_dict
    

    def create_df(self):

        # create the dictionary
        collection_dict = {}
        collection_dict['brand'] = []
        collection_dict['price'] = []

        # iterate over the items
        for collection_item in self.collection_items:
            if collection_item.brand is None:
                collection_dict['brand'].append(None)
            else:
                collection_dict['brand'].append(collection_item.brand)

            if collection_item.price is None:
                collection_dict['price'].append(None)
            else:
                collection_dict['price'].append(collection_item.price)


        # create the DataFrame
        df = pd.DataFrame(collection_dict)

        # add the DataFrame to the object
        self.collection_df = df

    
    def export_collection_df(self, export_name: str="export"):
        df = self.collection_df

        df.to_csv(f"{export_name}.csv", sep=";", index=False)
        print(f"✅ Successfully exported to {export_name}")


if __name__ == "__main__":
    car_1 = Car("BMW", 1000)
    motor_1 = Motor("Kawasaki", 1500)
    bicycle_1 = Bicycle("Batavus", 500)
    car_2 = Motor("Toyota", 700)
    bicycle_2 = Bicycle("Van Moof", 2500)

    # create a collection
    my_collection = VehicleCollection("My collection")
    my_collection_2 = VehicleCollection("Your collection")

    # add vehicles to the collection
    my_collection.add_vehicle(car_1, car_1, motor_1, bicycle_1, car_2, bicycle_2, car_1, car_1, motor_1, bicycle_1, car_2, bicycle_2)
    my_collection.add_vehicle(car_1, motor_1)

    # summarize the collection
    collection_summary = my_collection.summarize_collection()
    print(collection_summary)

    # create a DataFrame from the collection
    my_collection.create_df()

    # export the collection
    my_collection.export_collection_df("My export")
    pass