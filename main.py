import math
a = float(input('Por favor digite  a '))
print('{}'.format(a))
b = float(input('Por favor digite b '))
print('{}'.format(b))

c = float(input('Por favor digite c '))
print('{}'.format(c))
delta = (b**2) - 4 * a * c

print('valor de delta é ', delta)
if a == 0:
    print("O valor de a, deve ser diferente de 0")

elif delta < 0:
    print("Sem raizes reais")

else:
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)

    print("x1: {}, x2: {}".format(x1, x2))
