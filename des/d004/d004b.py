entrada = (input('insira algo'))
print(type(entrada),'é o tipo primitivo')
print('só tem espaços',entrada.isspace())
print(entrada.isnumeric(),'para numérico')
print(entrada.isalnum(), 'para alphanumerico')
print(entrada.isalpha(), 'para alpha')