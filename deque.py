class Deque:
    def __init__(self, capacidade):
        self.itens = [None] * capacidade
        self.primeiro = 0
        self.ultimo = -1
        self.tamanho = 0

    def adicionar_primeiro(self, item):
        if self.tamanho == len(self.itens):
            raise Exception("Deque está cheia")
        self.primeiro = (self.primeiro - 1) % len(self.itens)
        self.itens[self.primeiro] = item
        self.tamanho += 1

    def adicionar_ultimo(self, item):
        if self.tamanho == len(self.itens):
            raise Exception("Deque está cheio")
        self.ultimo = (self.ultimo + 1) % len(self.itens)
        self.itens[self.ultimo] = item
        self.tamanho += 1

    def remover_primeiro(self):
        if self.esta_vazia():
            raise Exception("Deque está vazio")
        item = self.itens[self.primeiro]
        self.itens[self.primeiro] = None
        self.primeiro = (self.primeiro + 1) % len(self.itens)
        self.tamanho -= 1
        return item

    def remover_ultimo(self):
        if self.esta_vazia():
            raise Exception("FilaDeque está vazia")
        item = self.itens[self.ultimo]
        self.itens[self.ultimo] = None
        self.ultimo = (self.ultimo - 1) % len(self.itens)
        self.tamanho -= 1
        return item

    def esta_vazia(self):
        return self.tamanho == 0

    def esta_cheia(self):
        return self.tamanho == len(self.itens)

    def obter_tamanho(self):
        return self.tamanho

    def obter_primeiro(self):
        if self.esta_vazia():
            raise Exception("FilaDeque está vazia")
        return self.itens[self.primeiro]

    def obter_tras(self):
        if self.esta_vazia():
            raise Exception("FilaDeque está vazia")
        return self.itens[self.ultimo]

def inicializar_fila_deque(capacidade):
    return Deque(capacidade)

def ler_dados_teclado():
    dados_trafego = []
    while True:
        dado = input("Digite o volume de tráfego ou 'fim' para encerrar: ")
        if dado.lower() == 'fim':
            break
        try:
            dado = int(dado)
            dados_trafego.append(dado)
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")
    return dados_trafego

def ler_dados_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            dados_trafego = []
            for linha in arquivo:
                for num in linha.split():
                    num = num.replace(',', '')
                    try:
                        dados_trafego.append(int(num))
                    except ValueError:
                        print(f"Valor inválido: '{num}' será ignorado.")
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
        dados_trafego = []
    return dados_trafego


def calcular_media_mov(dados_trafego, k):
    medias_moveis = []
    fila_deque = inicializar_fila_deque(k)

    for i, dado in enumerate(dados_trafego):
        fila_deque.adicionar_ultimo(dado)

        if fila_deque.obter_tamanho() == k:
            media = sum(fila_deque.itens) / k
            medias_moveis.append(media)
            fila_deque.remover_primeiro()
        else:
            medias_moveis.append(None)

    return medias_moveis

def exibir_medias(medias_moveis):
    for i, media in enumerate(medias_moveis):
        if media is None:
            print(f"Período {i + 1}: {media}")
        else:
            print(f"Período {i + 1} com média: {media:.2f}")

def salvar_medias(nome_arquivo, medias_moveis):
    with open(nome_arquivo, 'w') as arquivo:
        for i, media in enumerate(medias_moveis):
            if media is None:
                arquivo.write(f"Período {i + 1}: None\n")
            else:
                arquivo.write(f"Período {i + 1}, média: {media:.2f}\n")

def main():
    opcao = input("Digite o número referente a origem dos dados - Teclado(1) / Arquivo(2): ")
    if opcao.lower() == '1':
        dados_trafego = ler_dados_teclado()
    elif opcao.lower() == '2':
        nome_arquivo = input("Digite o nome do arquivo de dados: ")
        dados_trafego = ler_dados_arquivo(nome_arquivo)
    else:
        print("Valor inválido.")
        return

    k = int(input("Digite um valor para 'K' (De preferência use 7 como padrão): "))

    medias_moveis = calcular_media_mov(dados_trafego, k)

    print("\nMédias:")
    exibir_medias(medias_moveis)

    opcao_salvar = input("\nDeseja salvar as médias móveis em um arquivo? (s/n): ")
    if opcao_salvar.lower() == 's':
        nome_arquivo_saida = input("Digite o nome do arquivo de saída: ")
        salvar_medias(nome_arquivo_saida, medias_moveis)
        print(f"Médias móveis salvas em '{nome_arquivo_saida}'.")

main()