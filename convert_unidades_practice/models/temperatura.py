class Temperatura():

    def __init__(self, tipo:str, quantidade:float):
        self.tipo = tipo.strip().lower()
        self.quantidade = quantidade
        self.cel = 0
        self.fahr = 0
        self.temperatura_celsius = ["c", "celsius", "°c", "cel"]
        self.temperatura_fahrenheit = ["f", "fahrenheit", "°f", "fah"]

    def converter(self):
        if self.tipo in self.temperatura_celsius:
            self.cel = self.quantidade
            self.fahr = (self.cel * 9/5) + 32

        elif self.tipo in self.temperatura_fahrenheit:
            self.fahr = self.quantidade
            self.cel = (self.fahr - 32) * 5/9

        else:
            pass