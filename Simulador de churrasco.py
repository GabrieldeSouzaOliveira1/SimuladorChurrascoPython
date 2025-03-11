# crie um apliactivo para simular os custos de um churrasco.
# front: quantidade de adultos(homens e mulheres) e crianças.
# retorne a quantidade de carne, frango, carvão, refrigerante e cerveja com os custos, individuais e totais.
# back: faça uma simulação atribuindo gramas para caada tipo de pessoa (valores diferente para homens, mulheres e crianças)
# faça os calculos atribuindo valores para cada item
# mulitiplique tudo e some para calcular o valor total do churrasco.


print("=-="*30)
print("Calculadora de churrasco em familia ")
print("=-="*30)

# identificar a quantidade de pessoas na festa

homens = 0 
mulheres = 0 
criancas = 0
homens =+ int(input("Digite a quantidades de homens que haverá na festa: "))

mulheres =+ int(input("Digite a quantidades de mulheres que haverá na festa: "))

criancas =+ int(input("Digite a quantidades de crianças que haverá na festa: "))



# calculos

print()

#calculos para os homens
quanti_homens = homens * 500
carne_homens = quanti_homens * 0.065
frango_homens = quanti_homens * 0.025
cerveja_homens = homens * 3.75

#calculos para as mulheres
quanti_mulheres = mulheres * 400
carne_mulheres = quanti_mulheres * 0.065
frango_mulheres = quanti_mulheres * 0.025
refri_mulheres = mulheres * 5

#calculos para as crianças
quanti_crianca = criancas * 300
carne_crianca = quanti_crianca * 0.065
frango_crianca = quanti_crianca * 0.025
refri_crianca = criancas * 5

#calculo do carvão
carvao = (quanti_homens + quanti_mulheres + quanti_crianca) / 1000
carvao_preco = carvao * 15

#quantidade
quan_carne = quanti_crianca + quanti_mulheres + quanti_homens  /1000
quan_refri = mulheres + criancas
quan_cerveja = homens

# Preços
valor_total_carne = carne_homens + carne_mulheres + carne_crianca
valor_total_frango = frango_homens + frango_mulheres + frango_crianca
refri_total = refri_mulheres + refri_crianca + cerveja_homens


#valor Total
valor_total = carne_homens + carne_mulheres + carne_crianca + frango_homens + frango_mulheres + frango_crianca + cerveja_homens + refri_mulheres + refri_crianca + carvao_preco

#Impressão dos valores restantes
print(f"Para um churrasco que tem {homens} homens, {mulheres} mulheres e {criancas} crianças é preciso: ")

print(f"Carne: {quan_carne} gramas ")
print(f"Frango: {valor_total_frango} preço")
print(f"Bebidas: {homens} cervejas, {quan_refri} refrigerantes sendo um total de {refri_total}")
print(f"Carvão: {carvao} kg e o preço é {carvao_preco}")
print()
print(f"Dando no final um total de {valor_total}")
