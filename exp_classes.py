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
        return f"""
                Brand: 🚗 {self.brand}
                Price 💰 {self.price}
                Type: {self.type}
                Old prices 📈 {self.old_prices}
                """    


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


if __name__ == "__main__":
    car_1 = Car("BMW", 1000)
    motor_1 = Motor("Kawasaki", 1500)
    bicycle_1 = Bicycle("Batavus", 500)
    pass