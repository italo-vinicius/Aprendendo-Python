a = 'AAAAA'
b = 'BBBBBB'
c = 1.1
d = 'Messi'
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)
print('hello fuck world, This is {d}'.format(d=d))

print(47%5)