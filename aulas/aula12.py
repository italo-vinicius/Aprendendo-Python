nome = input('Qual o seu nome? ')
altura = float(input('Qual sua altura? '))
peso = float(input('Qual seu peso? '))
print('*-'*20)
print(f'Olá {nome}. Seu IMC é {peso/altura**2:.2f}')
