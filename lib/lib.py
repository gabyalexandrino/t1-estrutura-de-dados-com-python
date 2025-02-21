import os, csv
from gdown import download

# Definir a função download_from_drive
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
        # A matriz terá dimensões: (número de fornecedores + 1) x (tamanho + 1) x (tamanho + 1)
        matriz = [[[float('inf') for _ in range(tamanho + 1)] for _ in range(tamanho + 1)] for _ in range(len(matriz_fornecedores))]
        
        # Preenche a matriz com os valores dos contratos
        for fornecedor_idx, contratos in enumerate(matriz_fornecedores):
            for contrato in contratos:
                # Atribui o valor do contrato à posição correta na matriz
                matriz[fornecedor_idx][contrato[1]][contrato[2]] = contrato[3]  
        
        return m, n, t, matriz     

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