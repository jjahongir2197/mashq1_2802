class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.available = True

    def info(self):
        status = "Bo‘sh" if self.available else "Band"
        return f"{self.brand} {self.model} - {self.price} so'm - {status}"


class Client:
    def __init__(self, name):
        self.name = name
        self.rented = []


class RentalService:
    def __init__(self):
        self.cars = []
        self.clients = []

    def add_car(self, brand, model, price):
        self.cars.append(Car(brand, model, price))

    def add_client(self, name):
        self.clients.append(Client(name))

    def show_cars(self):
        for i, car in enumerate(self.cars):
            print(i+1, car.info())

    def rent_car(self, client_name, index):
        car = self.cars[index]
        client = next((c for c in self.clients if c.name == client_name), None)

        if car.available and client:
            car.available = False
            client.rented.append(car)
            print("Mashina ijaraga berildi")
        else:
            print("Xatolik")

def run():
    rs = RentalService()
    rs.add_car("BMW", "X5", 500000)
    rs.add_car("Malibu", "Turbo", 300000)
    rs.add_client("Jahongir")

    while True:
        print("\n1. Mashinalar\n2. Ijara\n3. Chiqish")
        c = input("Tanlang: ")

        if c == "1":
            rs.show_cars()
        elif c == "2":
            rs.show_cars()
            rs.rent_car(input("Ism: "), int(input("Mashina: ")) - 1)
        else:
            break

run()
