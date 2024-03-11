# LEIA-ME: Médias Móveis

## Grupo
- Nichael Filho
- Rosilene da Silva Santos
- Deivison Delmiro

### Descrição
Este programa em Python foi desenvolvido para calcular médias móveis de um conjunto de dados de tráfego. Ele permite ao usuário inserir os dados manualmente pelo teclado ou carregar os dados de um arquivo. As médias móveis são calculadas com base em um valor de "k" especificado pelo usuário.

### Funcionalidades
- Entrada de dados de tráfego pelo teclado.
- Carregamento de dados de tráfego a partir de um arquivo.
- Cálculo de médias móveis com base em um valor de "k" especificado.
- Exibição das médias móveis calculadas.
- Opção de salvar as médias móveis em um arquivo de saída.

### Utilização
1. Execute o programa.
2. Escolha a origem dos dados (teclado ou arquivo).
3. Insira os dados de tráfego.
4. Especifique um valor para "k".
5. O programa calculará as médias móveis e as exibirá.
6. Se desejar, poderá salvar as médias móveis em um arquivo.

### Observações
- Certifique-se de que os dados de tráfego estejam formatados corretamente para evitar erros durante a leitura.
- Caso opte por carregar os dados de um arquivo, certifique-se de que o arquivo esteja no mesmo diretório do programa ou forneça o caminho completo até o arquivo.

### Comentário da Equipe sobre o Desempenho do Cálculo da Média Móvel considerando a Notação Big O

O código lê os números que mostram quanto tráfego passa em cada interseção e, em seguida, calcula a média móvel para cada ponto de dados. A parte principal do código, onde ele faz os cálculos, é rápida. Para este código, o Big O é O(n), o que significa que, à medida que adicionamos mais dados, o tempo de execução do código aumenta depedendo de n.

### Referências
- [Deques - PandaIME](https://panda.ime.usp.br/pythonds/static/pythonds_pt/03-EDBasicos/15-Deques.html)
- [Implementação de Deque - PandaIME](https://panda.ime.usp.br/pythonds/static/pythonds_pt/03-EDBasicos/17-DequeImplementacao.html)
- [Deque in Python - GeeksforGeeks](https://www.geeksforgeeks.org/deque-in-python/)
- [Filas em Python com deque (queue) - OtavioMiranda](https://www.otaviomiranda.com.br/2020/filas-em-python-com-deque-queue/)
- [RicardoRubens - Filas](https://replit.com/@RicardoRubens/filas-21)
- [YouTube - Filas em Python - OtavioMiranda](https://www.youtube.com/watch?v=zY2VZoFGxJk)
- [YouTube - Deque in Python - GeeksforGeeks](https://www.youtube.com/watch?v=Wr4wcfYSSoI)

### Comentários
Diante do trabalho realizado, tentamos otimizar ao máximo o código e implementar algumas funções que, na nossa perspectiva, melhorariam o mesmo, como a possibilidade de escolha de um valor para “K”, mesmo tendo a preferência do 7. Assim como o fato de se adaptar a mais de uma forma de interpretação do arquivo com as médias móveis, para alavancar a funcionalidade geral do código!
