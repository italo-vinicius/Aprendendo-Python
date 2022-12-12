### Conversão de tipos
****
Em python, por ser de tipagem fraca, não podemos concatenar tipos diferentes como int e str, mas podemos converter tipos de dados. Por exemplo, posso transformar um valor int em uma str

```
print(100 + 'teste')
output: TypeError: unsupported operand type(s) for +: 'int' and 'str'

print(str(100) + 'teste')
output: 100teste
```
