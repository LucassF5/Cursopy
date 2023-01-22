
# VALIDADOR DE CPF
print("_____________________________________")
cpf = []
print("Digite 9 números para fazermos um cpf ou conferir o seu: ")
print("Um de cada vez!")
for n in range(9):
    add_cpf = int(input(f"Número {n + 1}:"))
    cpf.append(add_cpf)
nums = cpf
soma = 0
j = 0

# Parte do primeiro número

for y in range(10, 1, -1):
    soma += y * nums[j]
    j += 1

result = (11 - (soma % 11))

if result > 9:
    nums.append(0)
else:
    nums.append(result)

# Parte do segundo número

soma = 0
i = 0
for z in range(11, 1, -1):
    soma += z * nums[i]
    i += 1

result2 = (11 - (soma % 11))

if result2 > 9:
    nums.append(0)
else:
    nums.append(result2)

if cpf == nums:
    print(f"Seu cpf é esse:\n")
    for i in nums:
        print(i, end="")
else:
    print("Quebrou meu código")
print("\n_____________________________________")






