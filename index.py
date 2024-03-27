def calculate_discount(price, discount_percent):
    discounted_price = price - (discount_percent / 100 * price) 
    if discount_percent >= 20:
        return discounted_price
    else:
        return price
print(calculate_discount(400, 15))
print(calculate_discount(400, 25))

