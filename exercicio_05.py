'''
Resolução do professor: Paulo Andre Vechiatto de Miranda

Laços aninhados (repetições encaixadas)

Mostrar uma pirâmide semelhante a abaixo, sendo que o maior valor da pirâmide é definido pelo usuário.
Exemplo: n = 9

9  8  7  6  5  4  3  2  1  
8  7  6  5  4  3  2  1
7  6  5  4  3  2  1
6  5  4  3  2  1
5  4  3  2  1
4  3  2  1
3  2  1
2  1
1
'''

n = int(input('Digite n: '))

i = n

while i > 0:
  j = i

  while j > 0:
    print('%d'%j, end='  ')
    j -= 1
    
  print()
  i -= 1

