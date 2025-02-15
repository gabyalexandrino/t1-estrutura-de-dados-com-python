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
    # Abrindo o arquivo no modo de leitura
    with open(nome_arquivo, 'r') as arquivo:
        # Ler todas as linhas do arquivo em uma lista
        linhas = arquivo.readlines()
        
        # Armazena os dados da primeira linha
        primeira_linha = linhas[0].strip().split()
        print(primeira_linha)

        # Remover a primeira linha (não será usada para a matriz)
        linhas_restantes = linhas[1:]
        
        # Inicializa uma matriz vazia
        matriz_fornecedores = []

        for linha in linhas_restantes:
            # Separar os valores da linha, convertendo para inteiros e float
            dados = linha.strip().split()
            linha_convertida = [int(dados[0]), int(dados[1]), int(dados[2]), float(dados[3])]
            
            fornecedor = linha_convertida[0]
            
            # Se o fornecedor for maior que o tamanho da matriz, aumentamos a matriz
            while len(matriz_fornecedores) <= fornecedor:
                matriz_fornecedores.append([])
            
            # Adiciona a linha convertida na lista do fornecedor correspondente
            matriz_fornecedores[fornecedor].append(linha_convertida)
        
        matriz = []
        while len(matriz_fornecedores) < len(matriz):
            matriz.append([])
        
        # for fornecedor in matriz_fornecedores:
        #     for contrato in fornecedor:

        #return m, n, t, matriz     

def imprimir_matriz(matriz, k=None):
    
    return None

def exportar_csv(nome_arquivo, matriz):

    return None