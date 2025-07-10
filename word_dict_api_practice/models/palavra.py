class Palavra:
    def __init__(self, palavra:str, significado:str):
        self.palavra = palavra
        self.significado = significado

    def to_dict(self):
        return {"palavra": self.palavra, "significado": self.significado}