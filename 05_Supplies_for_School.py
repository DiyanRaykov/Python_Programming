pack_of_pens_BGN = 5.80
pack_of_markers_BGN = 7.20
detergent_BGN = 1.20

number_of_pen_packs = int(input())
number_of_markers_packs = int(input())
liters_of_detergent = int(input())
percent = int(input())
percent = percent / 100

pens_price = pack_of_pens_BGN * number_of_pen_packs
markers_price = pack_of_markers_BGN * number_of_markers_packs
detergent_price = detergent_BGN * liters_of_detergent


price_total = pens_price + markers_price + detergent_price
discounte_price = price_total - (price_total * percent)

print(discounte_price)