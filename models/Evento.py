class Evento:
    def __init__(self, id, nome, data, local, categoria):
        self.id = id
        self.nome = nome
        self.data = data
        self.local = local
        self.categoria = categoria
        self.participado = False

    def __str__(self):
        return f"ID: {self.id} | Nome: {self.nome} | Data: {self.data} | Local: {self.local} | Categoria: {self.categoria} | Participado: {self.participado}"