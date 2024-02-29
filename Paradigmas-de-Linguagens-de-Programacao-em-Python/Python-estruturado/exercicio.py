# Implementar uma solução em Python que some todos os números pares de uma lista
# Por exemplo, se a lista for [10, 2, 5, 7, 6, 3], o resultado deve ser igual a 18.

list = [10, 2, 5, 7, 6, 3]
n = len(list)
soma = 0

# Forma 01:
for i in range(n):
    if(list[i]%2 == 0):
        soma = soma + list[i]
print(f"O somatório dos elementos pares da lista é: {soma}")

# Forma 02:
for num in list:
    if(num%2==0):
        soma = soma + num
print(f"O somatório dos elementos pares da lista é: {soma}")
