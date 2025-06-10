class ItemBiblioteca:
    def __init__(self, titulo: str, disponivel: bool, ano_publicacao: int):
        self.titulo = titulo
        self.disponivel = disponivel

        if ano_publicacao > 0:
            self.ano_publicacao = ano_publicacao
        else:
            print("> O ano da publicação deve ser maior que 0")

    def emprestar(self):
        if self.disponivel == False:
            print(f"O item '{self.titulo}' não está disponível")    # raise Exception ("")
        else:
            self.disponivel = False
            print(f"O item '{self.titulo}' foi emprestado e não está mais disponível")

    def devolver(self):
        if self.disponivel == True:
            print(f"O item '{self.titulo}' já está disponível!")
        else:
            self.disponivel = True
            print(f"O item '{self.titulo}' foi disponibilizado!")

    def obter_info(self):
        if self.disponivel == True:
            mensagem = "Sim"
        else:
            mensagem = "Não"
        print(f"Título: {self.titulo}  |  Ano: {self.ano_publicacao}  |  Disponível: {mensagem}")

# Exemplo Dorival
class ColecaoLivros(ItemBiblioteca):
    def __init__(self, titulo, ano_publicacao, disponivel):
        super().__init__(titulo, ano_publicacao, disponivel)
        self.lista_livros = []

    def adicionar_livro(self, livro:ItemBiblioteca):
        self.lista_livros.append(livro)

    def verificar_disponibilidade_colecao(self):
        for livro in self.lista_livros:
            if not livro.disponivel:
                print(f"livro {livro.titulo} nao disponivel")
                return False
        return True


colecao = ColecaoLivros("Colecao1", 2010, True)
colecao.adicionar_livro(ItemBiblioteca("a", True, 2010))
colecao.adicionar_livro(ItemBiblioteca("abc", False, 2025))
colecao.adicionar_livro(ItemBiblioteca("hsajkfsdhf", False, 2115))

colecao.verificar_disponibilidade_colecao()


