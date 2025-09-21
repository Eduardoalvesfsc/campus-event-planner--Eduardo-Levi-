from models.Menu import Menu
# Função para validar a data
def validarData(dataStr):
    """
    Verifica se a data está no formato AAAA-MM-DD.
    Retorna True se for válido, False caso contrário.
    """
    try:
        datetime.strptime(dataStr, "%Y-%m-%d")
        return True
    except ValueError:
        return False
    
    
# Função para adicionar evento
def adicionarEvento(listaEventos, nome, data, local, categoria):
     """
    Cria um novo evento (dicionário) e adiciona na lista de eventos.
    Valída a data e se os campos não estão vazios.
    """
     # Verifica se todos os campos foram preenchidos
     if not nome or not data or not local or not categoria:
         print("❌ Erro: Todos os campos são obrigatórios")
         return
     
     # Valída a data
     if not validarData(data):
         print("❌ Erro: Data invalida! Use o formato AAAA-MM-DD")
         return
    
     # Gera um ID único
     novoId = len(listaEventos) + 1

     # Cria o dicionario do evento
     evento = {
         "id": novoId,
         "nome": nome,
         "data": data,
         "local": local,
         "categoria": categoria, 
         "participado": False
     }

     # Adiciona na lista
     listaEventos.append(evento)
     print(f"✅ Evento '{nome}' adicionado com sucesso!")


# Função para listar todos os eventos
def listarEventos(listaEventos):
    """
    Mostra todos os eventos cadastrados na lista.
    """
    if not listaEventos:
        print("📭 Nenhum evento cadastrado.")
        return
    
    print("\n--- LISTA DE EVENTOS ---")
    for evento in listaEventos:
        print(f"ID: {evento['id']} | Nome: {evento ['nome']} | Data: {evento['data']} | Local: {evento['local']} | Categoria: {evento['categoria']} | Participado: {evento['participado']}")


# Função para procurar evento por nome
def procurarEventoPorNome(listaEventos, nome):
    """
    Busca eventos que contenham o nome informado.
    Retorna uma lista de eventos encontrados
    """
    " 'ev' é o equivalente à evento, porém foi abreviado para não ser confundido com 'evento' de outra função nessa implementação."
    encontrados = [ev for ev in listaEventos if nome.lower() in ev["nome"].lower()]
    
    if not encontrados:
        print("🔎 Nenhum evento encontrado com esse nome.")
    else:
        print("\n--- RESULTADOS DA BUSCA ---")
        for ev in encontrados:
            print(f"ID: {ev['id']} | Nome: {ev['nome']} | Data: {ev['data']} | Local{ev['local']} | Categoria: {ev['categoria']} | Participado: {ev['participado']}")

    return encontrados

# Função para deletar evento por ID
def deletarEvento(listaEventos, id):
    """
    Remove um evento da lista pelo seu ID
    """
    for ev in listaEventos:
        if ev["id"] == id:
            listaEventos.remove(ev)
            print(f"🗑 Evento '{ev['nome']}' removido com sucesso!")
        return
    print("❌ Evento não encontrado.")

if __name__ == '__main__':
    menu = Menu()
    menu.iniciar()