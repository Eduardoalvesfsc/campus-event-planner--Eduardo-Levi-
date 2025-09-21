from models.PlanejadorEventos import PlanejadorEventos

class Menu:
    def __init__(self):
        pass

    def _display_title(self, title):
        return f"{title}".center(70, "-")

    def _display_menu(self):
        menu_options = [
            "1. Adicionar Evento",
            "2. Listar Eventos",
            "3. Filtrar Eventos por Categoria",
            "4. Marcar Evento como Participado",
            "5. Gerar Relatório",
            "0. Sair"
        ]

        print(self._display_title(" Planejador ") + "\n")
        for option in menu_options:
            print(option)
        print("\n" + self._display_title(""))

    def _display_header(self):
        message = r"""
  /$$$$$$ /$$$$$$$$ /$$$$$$                                            /$$              
 |_  $$_/| $$_____//$$__  $$                                          | $$              
   | $$  | $$     | $$  \__/  /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$$ /$$$$$$    /$$$$$$ 
   | $$  | $$$$$  | $$       /$$__  $$| $$__  $$ /$$__  $$ /$$_____/|_  $$_/   |____  $$
   | $$  | $$__/  | $$      | $$  \ $$| $$  \ $$| $$$$$$$$| $$        | $$      /$$$$$$$
   | $$  | $$     | $$    $$| $$  | $$| $$  | $$| $$_____/| $$        | $$ /$$ /$$__  $$
  /$$$$$$| $$     |  $$$$$$/|  $$$$$$/| $$  | $$|  $$$$$$$|  $$$$$$$  |  $$$$/|  $$$$$$$
 |______/|__/      \______/  \______/ |__/  |__/ \_______/ \_______/   \___/   \_______/                                                                                         
Developed by: Eduardo and Levi
"""
        print(message)

    def __escolha_do_usuario(self) -> int:
        try:
            return int(input("Escolha uma opcao: "))
        except ValueError:
            print("Entrada inválida, digite um número.")
            return -1
        
    def __cadastrar_evento(self, planejador: PlanejadorEventos):
        print(self._display_title(" Adicionar Evento ") + "\n")
        nome = input("Nome do Evento: ")
        data = input("Data (AAAA-MM-DD): ")
        local = input("Local: ")
        categoria = input("Categoria: ")
        planejador.adicionar_evento(nome, data, local, categoria)
        
    def __listar_eventos(self, planejador: PlanejadorEventos):
        print(self._display_title(" Listar Eventos ") + "\n")
        planejador.listar_eventos()
        
    def iniciar(self):
        planejador = PlanejadorEventos()
        self._display_header()
        
        while True:
            self._display_menu()
            escolha = self.__escolha_do_usuario()
            
            if escolha == 1:
                self.__cadastrar_evento(planejador)
            elif escolha == 2:
                self.__listar_eventos(planejador)
            elif escolha == 0:
                print("Saindo do Planejador de Eventos. Até logo!")
                break
            else:
                print("Opção inválida, tente novamente.")