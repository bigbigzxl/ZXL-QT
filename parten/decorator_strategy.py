promos = []

def promotion_register(promo_func):
    promos.append(promo_func)
    return promo_func

@promotion_register
def fidelity(order):
    return order.total() * .05 if order.customer.score >= 1000 else 0

@promotion_register
def bulk_item(order):
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() *.1
    return discount

@promotion_register
def large_order(order):
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0
def best_promo(order):
    return max(promo(order) for promo in promos)


# class customer:
#     def __init__(self, name, score) -> None:
#         self.name = name
#         self.score = score
from collections import namedtuple
Customer = namedtuple("Customer", "name score")


# class Item:
#     def __init__(self, product, quantity, price) -> None:
#         self.product = product
#         self.quantity = quantity
#         self.price = price
class LineItem:
    def __init__(self, product, quantity, price) -> None:
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity

         
# class Cart:
#     def __init__(self, items) -> None:
#         self.cart = list(items)

class Order:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, "__total"):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())

#307

if __name__ == "__main__":
    zxl = Customer("zxl", 100000)
    cart = [LineItem("banano", 100, 0.9), 
            LineItem("apple", 200, 0.8)]
    order = Order(zxl, cart)

    print(best_promo(order))

    print("{:.2f}".format(12345.67892))