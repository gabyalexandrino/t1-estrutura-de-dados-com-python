from lib import download_dataset
from lib import preencher_matriz_contratos
from lib import imprimir_matriz
from lib import exportar_csv

def main():
    
    # Download do dataset
    #link_txt = "https://drive.google.com/file/d/1YjPaHv8aAVsXNzhHxum5gyUDFfY5iw1_/view?usp=drive_link"
    link_txt = "https://drive.google.com/file/d/17KOe8bJvHDceTpGZ9ru1YvjlROIMWhZ3/view?usp=drive_link"
    file_txt = 'dataset/entrada.txt'
    download_dataset(link_txt,file_txt)

    # Preencher a matriz de contratos
    m, n, t, matriz = preencher_matriz_contratos(file_txt)
    
    # Imprimir os resultados
    print(m, n, t, "\n")
    imprimir_matriz(matriz)

    # Exportar a matriz de contratos
    file_csv = "resultados/contratos.csv"
    exportar_csv(file_csv, matriz)
    
if __name__ == "__main__":
    main()