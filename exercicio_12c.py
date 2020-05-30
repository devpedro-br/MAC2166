'''
Resolução do professor: Paulo Andre Vechiatto de Miranda

Dados n > 0 lançamentos de uma roleta (números entre 0 e 36), calcular a frequência de cada número.

Dica: Criar uma lista com 37 zeros.
Dica: usar comando for para imprimir.
'''
n = int(input('Digite n: '))
frequencia = [0] * 37

for i in range(n)
  num = int(input('Digite o %dº lançamento: '%(i+1)))
  frequencia[num] += 1

for i in range(len(frequencia)):
  if frequencia[i] > 0:
    print('Frequência relativa %d = %f'%(i, frequencia[i]/n))
