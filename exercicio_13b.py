'''
Resolução do professor: Paulo Andre Vechiatto de Miranda

Dada uma sequência de n > 0 números reais, imprimi-los eliminando as repetições.
'''

def pertence(lista, valor):
  print(id(lista))
  pert = False
  for j in range(len(lista)):
    if lista[j] == valor:
      pert = True
  return pert

def main():
  n = int(input('Digite n: '))
  seq = []

  for i in range(n):
    num = float(input('Digite o %dº número: '%(i+1)))
    print(id(seq))
    if not pertence(seq, num):
      seq.append(num)
  print(seq)

main()
