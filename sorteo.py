from os import system
system("cls")
import random

resultado=[]
nom=input("Ingresa el nombre del archivo .txt donde se guardarán los resultados: ")
abre=open(nom+".txt","a")
system("cls")

cant_personas=int(input("Ingresa la cantidad de personas que desea sortear: "))
system("cls")
for ingreso_personas in range(cant_personas):
	personas=input("Ingresa el nombre de uno de los participantes. Luego presiona ENTER para escribir el siguiente: ")
	resultado.append(personas)

system("cls")
random.shuffle(resultado)
for mostrar in range(len(resultado)):
	print("Sorteado",mostrar+1,":",resultado[mostrar])
	abre.write("Sorteado"+" ")
	abre.write(str(mostrar+1))
	abre.write(":"+" ")
	abre.write(resultado[mostrar]+" "+"\n")
