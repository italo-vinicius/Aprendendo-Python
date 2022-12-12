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