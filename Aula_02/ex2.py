# Exemplo 02 - Tipos de prints 

# variavel para armazenar o nome do aluno
nome_aluno = 'Rock' # Declara a variavel com a idade do aluno
idade_aluno = 15
media_aluno = 8.45 # declaração de variável

print('nome do aluno %s, ele tem %d anos e sua média é %f.' %(nome_aluno,idade_aluno,media_aluno))
print('Nome do aluno %s, ele tem %d anos e sua média é %.2f.' %(nome_aluno,idade_aluno,media_aluno))
print('Nome do aluno é {}, ele tem {} anos e sua média é {}.'.format(nome_aluno,idade_aluno,media_aluno))
print(f'Nome do aluno {nome_aluno}, ele tem {idade_aluno} e sua média é {media_aluno:.2f}.')