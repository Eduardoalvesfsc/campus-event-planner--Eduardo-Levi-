from datetime import datetime
from models.Evento import Evento

class PlanejadorEventos:
    def __init__(self):
        self.lista_eventos = []
        self._proximo_id = 1

    def _validar_data(self, data_str) -> bool:
        try:
            datetime.strptime(data_str, "%d/%m/%Y")
            return True
        except ValueError:
            return False

    def adicionar_evento(self, nome, data, local, categoria):
        if not nome or not data or not local or not categoria:
            print(f"❌ Erro: Todos os campos são obrigatórios\n")
            return

        if not self._validar_data(data):
            print(f"❌ Erro: Data invalida! Use o formato DD/MM/AAAA\n")
            return

        novo_evento = Evento(self._proximo_id, nome, data, local, categoria)
        self.lista_eventos.append(novo_evento)
        self._proximo_id += 1
        print(f"✅ Evento '{nome}' adicionado com sucesso!\n")

    def listar_eventos(self):
        if not self.lista_eventos:
            print(f"📭 Nenhum evento cadastrado.\n")
            return

        for evento in self.lista_eventos:
            print(evento)
            
    def deletar_evento(self, id_evento):
        for evento in self.lista_eventos:
            if evento.id == id_evento:
                self.lista_eventos.remove(evento)
                print(f"🗑 Evento '{evento.nome}' removido com sucesso!\n")
                return
        print("❌ Evento nao encontrado.\n")