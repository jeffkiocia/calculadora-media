# Calculadora de Média de Notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
if media >= 7:
    status = "Aprovado"
elif media >= 5:
    status = "Recuperação"
else:
    status = "Reprovado"
print(f"Sua média é {media:.2f} - Status: {status}")
	
