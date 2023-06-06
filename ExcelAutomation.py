import pandas as pd



def excluir_linhas(arquivo): #função para retirar o nome das colunas
    linhas = []
    with open(arquivo, 'r') as file:
        linhas = file.readlines()
    
    linhas = linhas[6:]  
    
    with open(arquivo, 'w') as file:
        file.writelines(linhas)


def excel():
    dataframe = pd.read_excel('database.xlsx')


    entrada = input("Digite uma palavra ou número: ")

    colunas = "NUM_DE,TIPO DOCUMENTO,CORRETOR,NOME INTERVENIENTE,SEGURADO,PREMIO LIQUIDO" #colunas que eu escolhi para filtrar
    colunas = [col.strip() for col in colunas.split(',')]

    dataframe = dataframe.applymap(str)


    dataframe = dataframe[colunas]

    resultado = dataframe[dataframe.apply(lambda row: entrada.lower() in ' '.join(row).lower(), axis=1)]

    if resultado.empty:
        print("A entrada não foi encontrada no arquivo.")
    else:
        print(resultado)
        nome_arquivo = 'resultado.txt'
        resultado.to_csv(nome_arquivo, index=False, sep='\n')
        excluir_linhas('resultado.txt')       
        print(f"O resultado foi salvo no arquivo '{nome_arquivo}'.")
        
        
        

