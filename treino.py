
print("")
print("Instruções:") 
print("Para jogar escolha um número de início da contagem e um número para finalizar a contagem")
print("")
print("Para que o programa funcione corretamente, o número inicial deve ser sempre menor que o número final")

#imputar a quantidade de números conforme o que o usuário digitar, e então printar a quantidade de números e dentre esses, quantos são pares.



primeiro_numero=int(input("Digite o primeiro número:"))
segundo_numero=int(input("Digite o último número:"))


for x in range(primeiro_numero, segundo_numero):
    if x % 2 == 0:
        print("Os números pares são {}.".format(x))
