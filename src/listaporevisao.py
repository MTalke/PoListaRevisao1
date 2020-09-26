# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

if __name__ == "__main__":
    
    def questao1():
        print("Ola Mundo")
        
        Menu()
        
    def questao2():
        tamanho = 10
        x = 1
        vetor = []
        while x <= tamanho:
            opcao = int(input("digite o numero: "))
            vetor.append(opcao)
            x = x + 1
            
        print(vetor)
        
        Menu()
    
    def questao3():
        matriz = [] # lista vazia
        tamanho = 10
        valor = 0
        n_linhas = tamanho
        n_colunas = tamanho
        for i in range(n_linhas):
            # cria a linha i
            linha = [] # lista vazia
            for j in range(n_colunas):
                linha.append(valor)

            # coloque linha na matriz
            matriz.append(linha)
            
        print(matriz)
        
        Menu()
    
    def questao4():
        vetor = [] # pilha vazia
        tamanho = 10

        for i in range(tamanho):
            # cria a linha i
            numero = int(input("digite o numero: "))
            vetor.append(numero)
        
        print("Maior valor", max(vetor))
        print("Menor valor", min(vetor))
        media = sum(vetor) / len(vetor)
        print("media das notas", media)
        
        Menu()
            
    def questao5():
        arq = open('arquivo.txt', 'r')  #abre o arquivo
        texto = []  #declaro um vetor
        matriz = [] #declaro um segundo vetor
        matriz2 = [] #declaro um terceiro vetor
        texto = arq.readlines() #quebra as linhas do arquivo em vetores 

        for i in range(len(texto)):        
            if(i < 10):
                matriz.append(texto[i].split())
            else:
                if(texto[i] != '\n'):
                    matriz2.append(texto[i].split())
        
        soma = somarMatrizes(matriz, matriz2) # soma e o nosso retorno, result
        print("Resultado da soma das matrizes")
        if soma is not None:
            for i in soma:
                print(i)
        else:
            print('Matrizes devem conter o mesmo numero de linhas e colunas')
        arq.close()
        Menu()
        
    def somarMatrizes(matriz, matriz2):
        if(len(matriz) != len(matriz2) or len(matriz[0]) != len(matriz2[0])):
            return None
        result = []
        for i in range(len(matriz)):   
            result.append([])
            for j in range(len(matriz[0])):
                soma = int(matriz[i][j]) + int(matriz2[i][j])
                result[i].append(soma)
        return result
        

    
            
    def Menu():    
        print("Escolha a opcao que deseja")
        print("Escolha 1 para questao 1")
        print("Escolha 2 para questao 2")
        print("Escolha 3 para questao 3")
        print("Escolha 4 para questao 4")
        print("Escolha 5 para questao 5")
        opcao = int(input("digite a opcao: "))

        if (opcao == 1):
            questao1()
        elif(opcao == 2):
            questao2()
        elif(opcao == 3 ):
            questao3()
        elif(opcao == 4):
            questao4()
        elif(opcao == 5):
            questao5()
        else:
            print("Nao tem essa questao")
            Menu()
            
    Menu()
