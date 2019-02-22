# EXERCICIO 5
x = int(input('Digite um numero:'))
y = int(x + 1)
z = int(x - 1)
print('O número digitado foi {}, seu antecessor é {} e seu sucessor é {}' .format(x,z,y))

#EXERCICIO 6
a = int(input('Digite um numero:'))
b = int(a + a)
c = int(a + a + a)
d = float(a**(1/2))
print('O numero digitado é {}, o dobro do numero é {}, o triplo é {} e a raiz é {}'.format(a,b,c,d))

#EXERCICIO 7
e = float(input('Digite a primeira nota:'))
f = float(input('Digite a segunda nota:'))
print('A media no aluno é {}'.format((e + f)/2))

#EXERCICIO 8
metro = float(input('Digite a quantidade de metros:'))
centimetro = float(metro * 100)
milimetro = float(metro * 1000)
print('{} metros tem {} centimetros e {} milimetros'.format(metro,centimetro,milimetro))

#EXERCICIO 9
numero = float(input('Digite um numero:'))
i = int(0)
for i in range(11):
  print('{} x {} = {}'.format(numero,i,(numero*i)))

#EXERCICIO 10
dinheiro = float(input('Quantos R$ voce possui?'))
dolar = float(dinheiro / 3.27)
print('Voce possui R$ {} e $ {} '.format(dinheiro, round(dolar,3)))

#EXERCICIO 11
largura = float(input('Digite a largura da parede:'))
altura = float(input('Digite a altura da parede:'))
area = float(largura * altura)
print('A parede possui {} m² e para pintala será necessario {} litros de tinta'.format(area,round((area/2),2)))

#EXERCICIO 12
preco = float(input('Digite o preço do produto:'))
promo = float((preco * 5) / 100)
print('O preço do produto com disconto é {}'.format(round((preco - promo), 2)))

#EXERCICIO 13
salario = float(input('Digite seu salário atual:'))
aumento = float((salario * 15)/100)
print('Seu salário com 15% de aumento ficou em R${}'.format(round((aumento + salario),2)))
