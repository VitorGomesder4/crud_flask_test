class Comprimento():

    def __init__(self, tipo:str, quantidade:float):
        self.tipo = tipo.strip().lower()
        self.quantidade = quantidade
        self.metros = 0
        self.pes = 0
        self.comprimento_metros = ["m", "metro", "metros"]
        self.comprimento_pes = ["ft", "pé", "pés", "foot", "feet"]


    def converter(self):
        if self.tipo in self.comprimento_metros:
            self.metros = self.quantidade
            self.pes = self.metros * 3.28084

        elif self.tipo in self.comprimento_pes:
            self.pes = self.quantidade
            self.metros = self.pes / 3.28084

        else:
            pass