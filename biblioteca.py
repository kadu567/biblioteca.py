# Classe Livro
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            print(f"O livro '{self.titulo}' foi emprestado com sucesso.")
        else:
            print(f"O livro '{self.titulo}' não está disponível no momento.")

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            print(f"O livro '{self.titulo}' foi devolvido com sucesso.")
        else:
            print(f"O livro '{self.titulo}' já está disponível na biblioteca.")

# Classe Usuario
class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestados = []

    def emprestar_livro(self, livro):
        if livro.disponivel:
            livro.emprestar()
            self.livros_emprestados.append(livro)
        else:
            print(f"O livro '{livro.titulo}' já está emprestado.")

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            livro.devolver()
            self.livros_emprestados.remove(livro)
        else:
            print(f"Você não possui o livro '{livro.titulo}' emprestado.")

# Classe Biblioteca
class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f"O livro '{livro.titulo}' foi adicionado à biblioteca.")

    def buscar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo.lower() == titulo.lower():
                return livro
        print(f"O livro '{titulo}' não foi encontrado na biblioteca.")
        return None

# Função principal com menu
def menu():
    biblioteca = Biblioteca()
    usuario = Usuario("João")

    while True:
        print("\n--- Menu da Biblioteca ---")
        print("1. Adicionar Livro")
        print("2. Buscar Livro")
        print("3. Emprestar Livro")
        print("4. Devolver Livro")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            livro = Livro(titulo, autor)
            biblioteca.adicionar_livro(livro)

        elif opcao == "2":
            titulo = input("Digite o título do livro para buscar: ")
            livro = biblioteca.buscar_livro(titulo)
            if livro:
                status = "disponível" if livro.disponivel else "emprestado"
                print(f"Livro encontrado: {livro.titulo} de {livro.autor}. Status: {status}")

        elif opcao == "3":
            titulo = input("Digite o título do livro para emprestar: ")
            livro = biblioteca.buscar_livro(titulo)
            if livro:
                usuario.emprestar_livro(livro)

        elif opcao == "4":
            titulo = input("Digite o título do livro para devolver: ")
            livro = biblioteca.buscar_livro(titulo)
            if livro:
                usuario.devolver_livro(livro)

        elif opcao == "5":
            print("Saindo do sistema da biblioteca.")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Executa o menu
if __name__ == "__main__":
    menu()
