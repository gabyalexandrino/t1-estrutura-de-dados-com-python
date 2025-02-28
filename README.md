<img src="imgs/UNIFOR_logo1b.png" width="400">
<br>
<b>
<font size="6" face="arial" color="blue">
    MBA em Gestão Analitica com BI e Big Data
</font>
</b>
<br>
<b>
<font size="4" face="arial">
    Disciplina: Análise de Dados com Python
</font>
</b>

Orientador: Prof. Me. Ricardo Carubbi <br>

**TRABALHO 1**: CARREGAMENTO, LEITURA E ESTRUTURA DE DADOS <br>

**Grupo**:
1. Nome: Grazia Gabriella Alexandrino Lima | Mat: 2428958/3 <br>
2. Nome: Gabriel Scotto Sbrana | Mat: 2429124/3 <br>
3. Nome:Maria Esther de Almeida Soares | Mat: 2429248/7 <br>
4. Nome: Alexsandro Vieira Santos | Mat: 2428825/X <br>
5. Nome: Rodrigo Amadeu Reis Cavalcante | Mat: 2428957/5 <br>

## **Etapa 1**: Configuração do ambiente de desenvolvimento

Um ambiente virtual no Python permite isolar as dependências do seu projeto, o que é uma boa prática para evitar conflitos entre diferentes projetos.

### **Passo 1**: Criar o Ambiente Virtual

No terminal, digitamos o seguinte comando para criar o ambiente virtual:

```bash
python -m venv t1
```

Aqui, `.t1` é o nome da pasta onde o ambiente virtual será armazenado.

### **Passo 2**: Ativar o Ambiente Virtual

* Windows:

```bash
t1\Scripts\activate
```

* Mac/Linux:

```bash
source t1/bin/activate
```

Para desativar um ambiente virtual e retornar ao ambiente global do Python, basta digitar: `deactivate`

### **Passo 4**: Instalar Dependências no Ambiente Virtual

Agora que o ambiente virtual está ativo, instalamos as dependências necessárias para o projeto.

O arquivo nomeado como `requirements.txt` lista todas as dependências necessárias para nosso projeto. O arquivo pode ser criado no Bloco de Notas com os nomes de todos os pacotes desejados, inclusive versões, como no exemplo abaixo:

```txt
numpy
matplotlib
pandas
gdown
ipykernel
jupyterlab
```

Instalamos os pacotes listados no arquivo com:

```bash
pip install -r requirements.txt
```

## **Etapa 2**: Configurar o Ambiente Python no VS Code

Após ativar o ambiente virtual, configuramos o VS Code para usar este ambiente Python específico.

1. Pressionamos Ctrl + Shift + P para abrir a barra de comandos.
2. Pesquisamos por Python: Select Interpreter e selecionamos o ambiente virtual que acabamos de criar.

Isso garantirá que o VS Code use o Python e os pacotes instalados no ambiente virtual.

## **Etapa 3**: Download do dataset
Estamos utilizando a função download da biblioteca `gdown`, que facilita o download de arquivos diretamente do Google Drive.

**Documentação**:
 * Instrução `with`: https://docs.python.org/pt-br/3/reference/compound_stmts.html#grammar-token-python-grammar-with_stmt
 * Função `open`: https://docs.python.org/pt-br/3/library/functions.html#open

 ### 1.1 Importar a função `download` da biblioteca `gdown`
 ```python
 from gdown import download
 ```
### 1.2 Definir a função `download_from_drive`

Criamos uma função chamada `download_from_drive` que recebe dois parâmetros:

* `link`: o link compartilhado do Google Drive.
* `filename`: o nome que o arquivo baixado terá.

1. **Extrair o ID do Arquivo**: Dentro do link compartilhado do Google Drive, o ID do arquivo é uma parte importante, pois é usado para gerar o URL de download direto. Usamos a função `split()` para quebrar o link em partes, e o ID do arquivo é a quinta parte (índice 5).

2. **Criar a URL de Download**: Com o ID do arquivo, construímos uma URL no formato aceito pelo Google Drive para permitir o download direto.

3. **Baixar o Arquivo**: Usamos a função download() da biblioteca gdown para baixar o arquivo da URL gerada, salvando-o com o nome especificado em filename. A opção quiet=False garante que o progresso do download seja exibido.
 ```python
 def download_dataset(link: str, filename: str) -> None:
    """
    Baixa um arquivo csv do Google Drive a partir de um link, e o salva na pasta 'dataset'.
    
    Parameters
    ----------
    link : str
        Link do Google Drive do arquivo a ser baixado
    filename : str
        Nome do arquivo a ser salvo na pasta 'dataset'.
    """
    # A pasta 'dataset' onde os arquivos serao salvos
    foldername = 'dataset'

    # Cria a pasta 'dataset' se nao existir
    if not os.path.exists(foldername):
        os.makedirs(foldername)
    
    # Pega o id do arquivo que fica no index 5 apos o split do link
    file_id = link.split('/')[5]
    # Define a URL do arquivo no Google Drive
    url = f'https://drive.google.com/uc?id={file_id}'
    # Baixa o arquivo
    download(url, filename, quiet = False)
    return None
 ```

 ## **Etapa 4**: Implementar função preencher_matriz_contratos()
 ### 4.1. Abrir o arquivo
A primeira coisa que precisamos fazer é abrir o arquivo. Em Python, usamos a função `open()` para abrir arquivos. Quando abrimos um arquivo, temos duas opções principais:

* **Modo de leitura** ('r'): Para apenas ler o arquivo.
* **Modo de escrita** ('w' ou 'a'): Para escrever no arquivo (não usado aqui).

O arquivo será aberto para leitura ('r'), e é importante fechá-lo depois de usá-lo para liberar os recursos do sistema. Para garantir que o arquivo seja sempre fechado, mesmo se ocorrer algum erro, usamos o bloco `with`. Isso garante que o arquivo seja fechado automaticamente.

O objeto `_io.TextIOWrapper` é o tipo de objeto retornado pelo método `open()` em Python quando abrimos um arquivo em modo texto (por exemplo, 'r' para leitura ou 'w' para escrita). Este objeto atua como um manipulador de arquivos e permite realizar operações de leitura, escrita e fechamento de arquivos.

**Métodos Comuns de _io.TextIOWrapper**:

1. **read()**: Lê o arquivo inteiro como uma string.
2. **readline()**: Lê uma única linha do arquivo por vez.
3. **readlines()**: Lê todas as linhas do arquivo e as armazena em uma lista.
4. **write()**: Escreve uma string no arquivo.
5. **writelines()**: Escreve várias linhas no arquivo a partir de uma lista de strings.
6. **close()**: Fecha o arquivo para liberar os recursos.

**Documentação**:
 * Instrução `with`: https://docs.python.org/pt-br/3/reference/compound_stmts.html#grammar-token-python-grammar-with_stmt
 * Função `open`: https://docs.python.org/pt-br/3/library/functions.html#open

 ### 4.2. Ler a Primeira Linha

A primeira linha do arquivo contém três valores: m (número de fornecedores), n (número de contratos) e t (taxa de mudança de fornecedor). Precisamos ler essa linha e separá-la em três partes para obter esses valores.

Primeiro, usamos o método `readline()` para ler a primeira linha do arquivo. O método `strip()` remove espaços em branco extras no início e no final da linha, incluindo quebras de linha (\n), e o método `split()` divide a linha em partes com base nos espaços entre os valores.

### 4.3. Inicializar a Matriz de Contratos

Depois de obter os valores de `m` e `n`, precisamos criar uma matriz tridimensional para armazenar os valores dos contratos. A matriz será composta de:

1. **Primeira dimensão**: Fornecedores.
2. **Segunda dimensão**: Mès de nício do contrato.
3. **Terceira dimensão**: Mês de término do contrato.

Inicializamos a matriz com valores de infinito (`float('inf')`), que será substituído pelos valores dos contratos conforme os dados do arquivo forem lidos.

A matriz terá `n` camadas (uma para cada fornecedor), e cada camada será uma matriz de tamanho `(m+1) x (m+1)`. Usamos `m+1` para lidar com a indexação, já que os índices começam em 1 no arquivo, mas em Python eles começam em 0.

### 4.4. Ler o Restante do Arquivo e Preencher a Matriz

Agora que a matriz está inicializada, precisamos preencher os valores a partir das linhas restantes do arquivo. Cada linha representa um contrato e contém quatro valores:

1. **Fornecedor**: Fornecedor do contrato.
2. **Início**: Mês de início do contrato.
3. **Fim**: Mês de término do contrato.
4. **Valor**: Valor do contrato.

Para cada linha (contrato), extraímos esses valores, ajustamos o índice do fornecedor (já que no arquivo o índice começa em 1, mas em Python começa em 0) e armazenamos o valor do contrato na posição correta da matriz.

```python
def preencher_matriz_contratos(nome_arquivo: str):
    # Abre o arquivo no modo de leitura
    """
    Abre o arquivo informado e preenche uma matriz com os valores de contratação de energia.
    
    Parameters
    ----------
    nome_arquivo : str
        Nome do arquivo TXT contendo os dados de contratação de energia.
    
    Returns
    -------
    m : int
        Quantidade de meses de contratação de energia.
    n : int
        Quantidade de fornecedores de energia.
    t : float
        Valor da taxa de mudança de fornecedor.
    matriz : list
        Matriz com os valores de contratação de energia. Tem dimensões (número de fornecedores) x (tamanho + 1) x (tamanho + 1).
    """
    with open(nome_arquivo, 'r') as arquivo:
        # Ler todas as linhas do arquivo e armazena em uma lista
        linhas = arquivo.readlines()
        
        # Armazena os dados da primeira linha
        primeira_linha = linhas[0].strip().split()
        # Quantidade de meses de contratação de energia
        m = int(primeira_linha[0])
        # Quantidade de fornecedores de energia
        n = int(primeira_linha[1])
        # Valor da taxa de mudança de fornecedor
        t = float(primeira_linha[2])

        # Remover a primeira linha (não será usada para a matriz)
        linhas_restantes = linhas[1:]
        
        # Lista para armazenar os contratos de cada fornecedor
        matriz_fornecedores = []
        # Variável para armazenar o tamanho da matriz final
        tamanho = 0
        
        for linha in linhas_restantes:
            # Separar os valores da linha, convertendo para inteiros e float
            dados = linha.strip().split()
            linha_convertida = [int(dados[0]), int(dados[1]), int(dados[2]), float(dados[3])]
            
            # Atualiza o tamanho da matriz final com base no maior valor encontrado na posição [2]
            if tamanho < linha_convertida[2]:
              tamanho = linha_convertida[2]
            
            fornecedor = linha_convertida[0]
            # Se o fornecedor for maior que o tamanho da matriz, aumentamos a matriz
            while len(matriz_fornecedores) <= fornecedor:
                matriz_fornecedores.append([])
            
            # Adiciona a linha convertida na lista do fornecedor correspondente
            matriz_fornecedores[fornecedor].append(linha_convertida)
        
        # Inicializa a matriz final com infinito (float('inf')) como valor padrão
        # A matriz terá dimensões: (número de fornecedores) x (tamanho + 1) x (tamanho + 1)
        matriz = [[[float('inf') for _ in range(tamanho + 1)] for _ in range(tamanho + 1)] for _ in range(len(matriz_fornecedores))]
        
        # Preenche a matriz com os valores dos contratos
        for fornecedor_idx, contratos in enumerate(matriz_fornecedores):
            for contrato in contratos:
                # Atribui o valor do contrato à posição correta na matriz
                matriz[fornecedor_idx][contrato[1]][contrato[2]] = contrato[3]  
        
        return m, n, t, matriz
```

## **Etapa 5**: Exportar a matriz no formato csv
```python
def imprimir_matriz(matriz, k=None):
    """
    Imprime a matriz de fornecedores.

    Parameters
    ----------
    matriz : list
        A matriz de fornecedores, onde cada fornecedor contém uma lista de linhas de dados.
    k : optional
        Argumento opcional não utilizado na função.

    Returns
    -------
    None
    """
    for index, fornecedor in enumerate(matriz):
        print(f"Fornecedor: {index}")
        for linha in fornecedor:
            print(linha)
        print('-' * 80)
        print('')
    return None 

def exportar_csv(nome_arquivo, matriz):
    foldername = 'resultados'

    # Cria a pasta 'dataset' se nao existir
    if not os.path.exists(foldername):
        os.makedirs(foldername)
    with open(nome_arquivo, 'w', newline='') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        for index, fornecedor in enumerate(matriz):
            for inicio in range(len(matriz)):
                for fim in range(len(matriz)):
                    writer.writerow([index, inicio, fim, fornecedor[inicio][fim]])
    return None
```