numero = int(input('QUAL O VALOR?'))

cem = int(numero / 100)
numero = numero - (cem*100)

cinquenta = int(numero/50)
numero = numero - (cinquenta*50)

vinte = int(numero/20)
numero = numero - (vinte*20)

dez = int(numero/10)
numero = numero - (dez*10)

cinco = int(numero/5)
numero = numero - (cinco*5)

dois = int(numero/2)
numero = numero - (dois*2)

um = int(numero/1)
numero = numero - (um*1)

um = numero

print('NOTAS DE 100 = ',cem)
print('NOTAS DE 50 = ',cinquenta)
print('NOTAS DE 20 = ',vinte)
print('NOTAS DE 10 = ',dez)
print('NOTAS DE 5 = ',cinco)
print('NOTAS DE 2 = ',dois)
print('NOTAS DE 1 = ',um)