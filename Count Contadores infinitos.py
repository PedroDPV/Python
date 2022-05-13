from itertools import count

contador = count(start=1, step=2)

for i in contador:
    print(i)
    if i > 9:
        break

#para esse Iterável virar infinito basta retirar o condicional do laço For.

