'''
Resolução do professor: Paulo Andre Vechiatto de Miranda

Dada uma sequência de n > 0 números reais, imprimi-los eliminando as repetições.
'''

n = int(input('Digite n: '))
seq = []

i = 0
while i < n:
  num = float(input('Digite o %dº número: '%(i+1)))
  repetido = False

  j = 0
  while j < len(seq) and repetido == False:
    if seq[j] == num:
      repetido = True
    j += 1

  if not repetido:
    seq.append(num)
  i += 1
