# Entrada de números decimais com vírgula
# Armazena o preço na variável 'preco' e substitui vírgula por pontos para conversão correta para float 
preco = float(input('Digite o preço: ').replace(',', '.'))    
print (f'Preco: R$ {preco:.2f}')

       

