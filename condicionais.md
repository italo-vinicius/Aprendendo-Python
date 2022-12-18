### If, elif e else (operadores condicionais)
****
A estrutura condicional é uma seção que ajuda a definir condições para a execução de determinados blocos de comandos. Em vez de executar tudo de vez, sem nenhuma interrupção, o programa deve parar para executar um teste e decidir qual caminho seguir.

##### Else em Python
O ELSE surge depois do IF, em complemento lógico a ele. Então, não existe hipótese de escrever um ELSE sem um IF antes. 
Geralmente, o ELSE não requer um teste, uma comparação, pois ele executa algo caso a comparação do IF não passe. 
Portanto, você só precisa declarar o ELSE e adicionar o bloco de comandos. 

##### IF em Python
Já o IF deve propor alguma coisa. É preciso escrever o IF e logo depois colocar a condição analisada. Então, em seguida, o bloco de comandos. 

##### Elif em Python
O elif é uma estrutura intermediária dentro da seção if-else no python e deve vir como um complemento a ambos. Quando você já tem um IF e um ELSE, mas precisa de uma condição para especificar outra regra, pode usar o elif.


```
if 5 % 2 == 0: # verifica se é par ou impar
    print('par')
else:
    print('impar')

output: impar

```