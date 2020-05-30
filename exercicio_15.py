'''
Resolução do professor: Paulo Andre Vechiatto de Miranda

Problema:
Dada uma sequência de n > 0 números reais, imprimir a frequência de cada valor.
'''

'''
def insereSeNovo(x, lista):
  for i in range(len(lista)):
    if lista[i] == x:
      return i
  lista.append(x)
  return len(lista) - 1
'''
'''
def insereSeNovo(x, lista):
  if x not in lista:
    lista.append(x)
    return len(lista) - 1
  else: # Sei que x está na lista
    i = 0
    while x != lista[i]:
      i += 1
    return i
'''

def insereSeNovo(x, lista):
  if x in lista:
    return lista.index(x)
  else:
    lista.append(x)
    return len(lista) - 1

def main():
  n = int(input('Digite n: '))
  listaNum = []
  contaNum = []

  i = 1
  while i <= n:
    num = float(input('Digite o %dº número: '%(i)))
    indice = insereSeNovo(num, listaNum)

    if len(listaNum) > len(contaNum):
      contaNum.append(1)
    else:
      contaNum[indice] += 1
    i += 1
  
  for i in range(len(listaNum)):
    if contaNum[i] > 1:
      print('%f aparece %d vezes'%(listaNum[i], contaNum[i]))
    else:
      print('%f aparece uma vez'%(listaNum[i]))
main()
