'''
Resolução do professor: Paulo Andre Vechiatto de Miranda

Dada uma sequência de n > 0 números reais, imprimi-los eliminando as repetições.
'''

n = int(input('Digite n: '))
seq = []

for i in range(n):
  num = float(input('Digite o %dº número: '%(i+1)))
  repetido = False

  if num not in seq:
    seq.append(num)
print(seq)
