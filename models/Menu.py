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

    def __escolha_do_usuario(self):
        try:
            return int(input("Escolha uma opcao: "))
        except ValueError:
            print("Entrada inválida, digite um número.")
            return -1
