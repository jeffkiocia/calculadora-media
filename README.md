# calculadora-media
Calculadora que calcula a média de notas e exibe se o aluno foi aprovado, em recuperação ou reprovado
python
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
	1. No terminal, dentro da pasta do projeto, digite:

bash
git add .
git commit -m "Adicionando o projeto Calculadora de Média"
git push origin main
![image](https://github.com/user-attachments/assets/b1efbc78-df66-4b68-9db5-794ac37fe96d)
