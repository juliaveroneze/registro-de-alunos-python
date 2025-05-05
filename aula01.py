nome = 'Julia'
peso = float(80)
altura = 1.70
imc = peso / (altura**2)
#f-strings
print(f'{nome} seu peso ideal é: {imc:.2f}')
#format
a = 'a'
b = 'b'
c = 'c'
string = 'a={0} b={1} c={2}'
formato = string.format(a,b,c)
print(c)