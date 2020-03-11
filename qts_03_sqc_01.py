Python 3.7.4 (default, Aug 13 2019, 20:35:49) 
[GCC 7.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> ano = 365
>>> ano = anos_fumando
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    ano = anos_fumando
NameError: name 'anos_fumando' is not defined
>>> ano = 365
>>> ano = "anos_fumando"
>>> anos_fumando = 12
>>> cigarros_dia = 20
>>> valor_carteira = 7.00
>>> print(anos_fumando * cigarros_dia * valor_carteira)
1680.0
>>> ano = 365
>>> ano = "anos_fumando"
>>> anos_fumando = 12
>>> cigarros_dia = 20
>>> valor_carteira = R$ 7.00
SyntaxError: multiple statements found while compiling a single statement
>>> ano = 365
>>> ano = "anos_fumando"
>>> anos_fumando = 12
>>> cigarros_dia = 20
>>> valor_carteira = 7.00
SyntaxError: multiple statements found while compiling a single statement
>>> ano = 365
>>> ano = "anos_fumando"
>>> anos_fumando = 12
>>> cigarros_dia = 20
>>> valor_carteira = R$ 7.00
>>> print(anos_fumando * cigarros_dia * valor_carteira)
SyntaxError: multiple statements found while compiling a single statement
>>> ano = 365
>>> ano = "anos_fumando"
>>> anos_fumando = 12
>>> cigarros_dia = 20
>>> valor_carteira = 7.00
>>> print(anos_fumando * cigarros_dia * valor_carteira)
SyntaxError: multiple statements found while compiling a single statement
>>> ano = 365
>>> ano = "anos_fumando"
>>> anos_fumando = 12
>>> cigarros_dia = 20
>>> valor_carteira = 8.50
>>> print(anos_fumando * cigarros_dia * valor_carteira ("R$"))
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(anos_fumando * cigarros_dia * valor_carteira ("R$"))
TypeError: 'float' object is not callable
>>> print(float(anos_fumando * cigarros_dia * valor_carteira (R$))
      
SyntaxError: invalid syntax
>>> print(anos_fumando * cigarros_dia * valor_carteira, 'R$')
2040.0 R$
>>> f'R$ {valor_carteira}'
'R$ 8.5'
>>> f'R$ {valor_carteira:.2f}'
'R$ 8.50'
>>> 
>>> 
