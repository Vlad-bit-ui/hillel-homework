class DiscountCalculator:
    def get_discount(self, price):
        if price >= 1000:
            return price * 0.20
        elif price >= 500:
            return price * 0.10
        else:
            return 0


calculator = DiscountCalculator()

assert calculator.get_discount(300) == 0

assert calculator.get_discount(500) == 50

assert calculator.get_discount(1000) == 200

print("Усі тести пройдено успішно!")