soma = 0
numero = 0 #variavel que vai receber o numero digitado
contagem = 1 #variavel que vai contar quantas vezes o programa sera executado
while contagem <= 5:
    numero = int(input('Digite um valor: '))
    soma = soma + numero
    contagem = contagem + 1
resultado = soma / 5
print(resultado)


