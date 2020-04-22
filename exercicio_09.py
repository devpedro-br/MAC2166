'''
def binomial(n, k):
  numerador = fatorial(n)
  denominador = fatorial(k)*fatorial(n-k)
  return numerador//denominador
'''

'''  
def binomial(n, k):
  if k > (n-k):
    den = fatorial(n-k)
    num = fatorial_gen(k+1, n)
  else:
    den = fatorial(k)
    num = fatorial_gen(n-k+1, n)
  return num//den
'''


'''
def maior(a, b):
  if a > b:
    m = a
  else:
    m = b
  return m

def menor(a, b):
  if a < b:
    m = a
  else:
    m = b
  return m
'''

def main():
  n = int(input('Digite n: '))
  i = 0

  while i < n:
    j = 0
    while j <= i:
      b = binomial(i, j)
      print('%4d'%b, end=' ')
      j += 1
    print()
    i += 1

def fatorial(n):
  fat = 1
  i = 1

  while i <= n:
    fat *= i
    i += 1
  return fat

def fatorial_gen(inicio, n):
  fat = 1
  i = inicio

  while i <= n:
    fat *= i
    i += 1
  return fat

def binomial(n, k):
  den = fatorial(min(k, n-k))
  num = fatorial_gen(max(k, n-k)+1, n)
  return num//den

main()
