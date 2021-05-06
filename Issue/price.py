# Объявить необходимые переменные и записать в виде инструкции присваивания формулувычисления стоимости покупки,
# состоящей из нескольких тетрадей, обложек к ним и карандашей
price_copybook = 1.25
price_cover = 1
price_pensil = 1.50
n_copybook = 3
n_pensil = 3
result = n_copybook * (price_copybook + price_cover) + n_pensil * price_pensil
print("Result: ", result)
