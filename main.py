from datetime import datetime
# Planejador de Eventos do IFConecta
# modelo de dados do evento (dicionário)

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