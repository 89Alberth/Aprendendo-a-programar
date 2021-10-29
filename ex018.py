import math
ângulo = float(input('Digite um ânglo: '))
seno = math.sin(math.radians(ângulo))
print('O ângulo de °{} tem o Seno de {:.2f}.'.format(ângulo, seno))
cos = math.cos(math.radians(ângulo))
print('O ângulo de °{} tem o Cosseno de {:.2f}.'.format(ângulo, cos))
tan = math.tan(math.radians(ângulo))
print('O ângulo de °{} tem a Tangente de {:.2f}.'.format(ângulo, tan))
