nome = str(input('Digite seu nome: '))
salario = float(input('Digite seu salário, com os centavos separados por ponto: '))
resultado = (salario * 15) / 100 + salario
print('{0}o seu salário aumentou para {1}' .format(nome, resultado))