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
        
    def filtrar_eventos_por_categoria(self, categoria):
        eventos_encontrados = [evento for evento in self.lista_eventos if evento.categoria.lower() == categoria.lower()]
        if not eventos_encontrados:
            print(f"🔎 Nenhum evento encontrado na categoria '{categoria}'.")
        else:
            print("\n"+ f" EVENTOS NA CATEGORIA '{categoria}' ".center(70, "-")+"\n")
            for evento in eventos_encontrados:
                print(evento)
            print("")
    
    def marcar_evento_como_participado(self, id_evento):
        for evento in self.lista_eventos:
            if evento.id == id_evento:
                evento.participado = True
                print(f"✅ Evento '{evento.nome}' marcado como participado!\n")
                return
        print(f"❌ Evento com ID {id_evento} nao encontrado.\n")
        
    def gerar_relatorio(self):
        total_eventos = len(self.lista_eventos)
        participados = sum(1 for evento in self.lista_eventos if evento.participado)
        nao_participados = total_eventos - participados
        
        print(f"Total de eventos: {total_eventos}")
        print(f"Eventos participados: {participados}")
        print(f"Eventos pendentes: {nao_participados}\n")
    