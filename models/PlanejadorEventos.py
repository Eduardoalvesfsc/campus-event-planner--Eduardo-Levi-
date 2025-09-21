from datetime import datetime
from models.Evento import Evento

class PlanejadorEventos:
    def __init__(self):
        self.lista_eventos = []
        self._proximo_id = 1

    def _validar_data(self, data_str) -> bool:
        try:
            datetime.strptime(data_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def adicionar_evento(self, nome, data, local, categoria):
        if not nome or not data or not local or not categoria:
            print(f"❌ Erro: Todos os campos são obrigatórios\n")
            return

        if not self._validar_data(data):
            print(f"❌ Erro: Data invalida! Use o formato AAAA-MM-DD\n")
            return

        novo_evento = Evento(self._proximo_id, nome, data, local, categoria)
        self.lista_eventos.append(novo_evento)
        self._proximo_id += 1
        print(f"✅ Evento '{nome}' adicionado com sucesso!\n")

    def listar_eventos(self):
        if not self.lista_eventos:
            print(f"📭 Nenhum evento cadastrado.\n")
            return

        print("\n--- LISTA DE EVENTOS ---")
        for evento in self.lista_eventos:
            print(evento)