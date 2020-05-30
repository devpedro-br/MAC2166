'''
Resolução do professor: Paulo Andre Vechiatto de Miranda

Dados dois números naturais n e m e duas sequências ordenadas com n > 0 e m > 0 números inteiros, criar uma lista contendo a sequência ordenada com todos os elementos das duas sequências originais sem repetição.

Sugestão: Imagine uma situação real, por exemplo, dois fichários de uma biblioteca.
'''

m = int(input('Digite m: '))

seq1 = []
for i in range(m):
  num = int(input('Digite o %dº número: '%(i+1)))
  if num not in seq1:
    seq1.append(num)

n = int(input('Digite n: '))

seq2 = []
for i in range(n):
  num = int(input('Digite o %dº número: '%(i+1)))
  if num not in seq2:
    seq2.append(num)

seq3 = []
i, j = 0, 0

while i < len(seq1) or j < len(seq2):
  if i == len(seq1):
    seq3.append(seq2[j])
    j += 1
  elif j == len(seq2):
    seq3.append(seq1[i])
    i += 1
  elif seq1[i] < seq2[j]:
    seq3.append(seq1[i])
    i += 1
  elif seq1[i] > seq2[j]:
    seq3.append(seq2[j])
    j += 1
  else:
    seq3.append(seq1[i])
    i += 1
    j += 1

print(seq1)
print(seq2)
print(seq3)
