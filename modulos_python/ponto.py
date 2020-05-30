'''
Módulo auxiliar do arquivo desenho.py
'''

import math
 
def distancia(Pa, Pb):
  """Calcula a distância entre dois pontos Pa = [xa, ya] e Pb = [xb, yb]."""
  xa,ya = Pa #xa, ya = Pa[0], Pa[1]
  xb,yb = Pb #xa, ya = Pb[0], Pb[1]
  dx = xb - xa
  dy = yb - ya
  d = math.sqrt(dx*dx + dy*dy)
  
  return d

def pontomedio(Pa, Pb):
  """Calcula o ponto médio entre dois pontos Pa = [xa, ya] e Pb = [xb, yb]."""
  xa,ya = Pa #xa, ya = Pa[0], Pa[1]
  xb,yb = Pb #xa, ya = Pb[0], Pb[1]
  Mx = (xb + xa)/2
  My = (yb + ya)/2
  PM = [Mx, My]
  
  return PM

if __name__ == '__main__':
  if pontomedio([-1, 0], [1, 0]) == [0, 0]:
    print('Ok')
  else:
    print('Erro')
