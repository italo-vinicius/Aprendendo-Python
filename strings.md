### Strings
****
Python é uma linguagem de tipagem dinâmica / Forte, Ou seja, o python já sabe qual o tipo da informação que está sendo passada.
Na tipagem dinâmica, o python ler um número e já conhece o valor como número, não sendo necessário especificar se é string ou number
```
print("Italo Vinicius é uma string")
output: Italo Vinicius é uma string
```

Python possui tipagem forte, então não permite um mesmo dado ser tratado como se fosse de outro tipo. 
```
nome = "italo"
idade = 20

print(nome + idade) 
output: TypeError: can only concatenate str (not "int") to str
```

****

### F-Strings
Podemos usar as F-strings no python para formatar impressões no print.
```
nome = 'Italo'
print(f'sou {nome} e estou usando uma F-String')

output: sou italo e estou usando uma F-String
```

Tambem é possível definir a quantidade de casas decimais da seguinte forma:

```
valor_a = 5/3
valor_b = 1888888888

print(f'o resultado é {valor_a:.2f}')
print(f'o resultado é {valor_b:,.2f}')

output: o resultado é 1.67
output: o resultado é 1,888,888,888.00
```