#Escreva um Programa que declara uma matriz 5x7 de numeros inteiros e 
# preenche todos os valores com numeros aleatorios num intervalo de 0 a 1000
#Busca Matriz Ordenação 
#olhar exercicio 6 da lista matriz
import random
matriz = []             #cria uma matriz 5x7 com valores zero 
for _ in range(5):
    matriz.append( [0] * 7)

for i in range(5):
    for j in range(7):
        #Gera numeros aleatorios, incluindo ambas as extremidades 
        matriz[i][j] = random.randint(0, 1000)

for lin in matriz:
    print(lin)  # imprime a matriz linha por linha

