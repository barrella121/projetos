### criar uma "concessionária virtual" onde o usuario pode entrar na loja e receber uma série de carros e motos, pode escolher se quer um carro ou uma moto, e também qual 
#   carro/moto quer escolher. Com base em classes
while True:
    print("o que você quer comprar?")
    print("Carro", "[C]")
    print("Motocicleta", "[M]")

    choice = input().strip().upper()


    class Car:
        def __init__(self, brand, model, engine):
            self.brand = brand
            self.model = model
            self.engine = engine
            ## Ideia: Fazer uma função para checar quanto vale, se for barata exibe $, se for razoavel exibe $$ e se for cara exibe $$$
        def display_info(self):
            print(f"--> {self.brand} {self.model}, motor {self.engine}")

            #Vou fazer dps
        # class Toyota:
        #     def __init__(self, model, engine, year):
        #         pass

    class Moto:
        def __init__(self, brand, model, engine):
            self.brand = brand
            self.model = model
            self.engine = engine
        def display_info(self):
            print(f"--> {self.brand} {self.model}, {self.engine} cilindradas")

    cars = [
        car1:= Car("Toyota", "Corolla", "1.6"),
        car2:= Car("Volkswagen", "Gol", "1.0"),
        car3:= Car("Chevrolet", "Onix", "1.0"),
        car4:= Car("Nissan", "Sentra", "2.0"),
        car5:= Car("Renault", "Kwid", "1.0"),
        car6:= Car("Jeep", "Compass", "1.3")
    ]

    motorcycles = [
        moto:= Moto("Honda", "CG 160", "162,7"),
        moto:= Moto("Yamaha", "factor 150", "146"),
        moto:= Moto("Honda", "Biz 125", "124,9"),
        moto:= Moto("Yamaha", "Fazer 150", "149"),
        moto:= Moto("Shineray", "Worker 125", "123"),
        moto:= Moto("Kawasaki", "Z400", "399")
    ]

    if choice.startswith("C"):
        for car in cars:
            car.display_info()
    elif choice.startswith("M"):
        for moto in motorcycles:
            moto.display_info()
