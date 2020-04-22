def mdc(a, b):
  if a < b:
    a,b = b,a
  while b > 0:
    r = a % b
    a = b
    b = r
  return a

def main():
  n = int(input('Digite n: '))
  i = 1
  mdc_parcial = int(input('Digite um número: '))
  while i < n:
    num = int(input('Digite um número: '))
    mdc_parcial = mdc(mdc_parcial, num)
    i += 1
  print(mdc_parcial)

# print(mdc(24,15))
main()
