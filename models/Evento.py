class Evento:
    def __init__(self, id, nome, data, local, categoria):
        self.id = id
        self.nome = nome
        self.data = data
        self.local = local
        self.categoria = categoria
        self.participado = False

    def __str__(self):
        info = (
            f" ▸ ID: {self.id}\n"
            f" ▸ Nome: {self.nome}\n"
            f" ▸ Data: {self.data}\n"
            f" ▸ Local: {self.local}\n"
            f" ▸ Categoria: {self.categoria}\n"
            f" ▸ Participado: {'Sim' if self.participado else 'Não'}"
        )
        return f"{info}\n"