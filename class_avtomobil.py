class Avtomobil:
    def __init__(self, marka, god, tsvet):
        self.marka = marka 
        self.god = god
        self.tsvet = tsvet

    def info(self):
        print(f"Марка: {self.marka}")
        print(f"Год: {self.god}")
        print(f"Цвет: {self.tsvet}")

    def vozrast(self):
        print(f"Машине {2026 - self.god} лет.")

avto = Avtomobil("Toyota", 1999, "Белая")
avto.info()

#Перекрасили машину
avto.tsvet = "Красный"
print("-----------------\nПосле перекраски\n---------------")

avto.info()
avto.vozrast()



