#variavel
contador = 0
numero = 0

#algoritimo
numero = int(input("Informe o número para tabuada: "))

for contador in range(1,11,1):
    print(f"{numero} X {contador} = {numero*contador}")