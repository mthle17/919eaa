def calculate_discount(price, percentage):
    assert price > 0, "Price is 0 or negative"

    assert 0 <= percentage <= 100, "Percentage is not within allowed interval"

    return price * (1 - percentage / 100)

price, discount_percentage = 20, 10
print(f"{price} - {discount_percentage}% = {calculate_discount(price, discount_percentage)}")
# 20 - 10% = 18.0

price, discount_percentage = -20, 10
print(f"{price} - {discount_percentage}% = {calculate_discount(price, discount_percentage)}")
# AssertionError: Price is 0 or negative

price, discount_percentage = 20, -10
print(f"{price} - {discount_percentage}% = {calculate_discount(price, discount_percentage)}")
# AssertionError: Percentage is not within allowed interval
