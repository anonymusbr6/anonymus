print("Concurso da Polícia Militar")
Idade=float(input("Digite a sua idade:"))
Sexo=(input("Digite o seu sexo, M pra masculino e F pra feminino:"))
Altura=float(input("Digite a sua altura:"))
if (Idade >=18 and Sexo=='M' and Altura >=1.60):
    print("Aprovado")
else:
    print("Reprovado")