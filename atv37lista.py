#Ler um vetor com 20 idades e exibir a maior e menor
idade = []

for i in range(20):
    a = int(input(f"Coloque a idade da pessoa {i+1}:"))
    idade.append(a)
b = max(idade)
c = min(idade)
print(f"A maior idade é: {b}, ja a menor idade é: {c}")