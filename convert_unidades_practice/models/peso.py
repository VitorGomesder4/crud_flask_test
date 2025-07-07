class Peso():

    def __init__(self, tipo:str, quantidade:float):
        self.tipo = tipo.strip().lower()
        self.quantidade = quantidade
        self.kg = 0
        self.lb = 0
        self.peso_quilos = ["kg", "quilo", "quilos", "kilograma", "kilogramas"]
        self.peso_libras = ["lb", "libras", "libra", "pound", "pounds"]

    def converter(self):
        if self.tipo in self.peso_quilos:
            self.kg = self.quantidade
            self.lb = self.kg * 2.20462

        elif self.tipo in self.peso_libras:
            self.lb = self.quantidade
            self.kg = self.lb / 2.20462

        else:
            pass