import math

print("Loja de Tintas!")
tamanho_area_M2 = int(input("Digite o tamanho da área a ser pintada em M2: "))
litros_usados = (tamanho_area_M2 / 6) * 1.10

# Situação 1: apenas latas
lata_de_tinta = math.ceil(litros_usados / 18)
preco_lata = lata_de_tinta * 80

# Situação 2: apenas galões
galao_de_tinta = math.ceil(litros_usados / 3.6)
preco_galao = galao_de_tinta * 25

# Situação 3: mistura
latas_misturadas = litros_usados // 18
litros_restantes = litros_usados % 18
galoes_misto = math.ceil(litros_restantes / 3.6)
preco_misto = (latas_misturadas * 80) + (galoes_misto * 25)

print(f"\nQuantidade de litros de tinta: {litros_usados:.1f}")
print(f"Apenas latas:  {lata_de_tinta} latas → R$ {preco_lata:.2f}")
print(f"Apenas galões: {galao_de_tinta} galões → R$ {preco_galao:.2f}")
print(
    f"Mistura: {int(latas_misturadas)} latas + {galoes_misto} galões → R$ {preco_misto:.2f}"
)

#preciso de mais pratica neste!