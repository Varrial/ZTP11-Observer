
class Bank:
    def __init__(self):
        self.__subscribers = []
        self.currency = {'USD': 3.8,
                         'EUR': 4.3,
                         'GBP': 5.0}

    def subscribe(self, subscriber):
        self.__subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        self.__subscribers.remove(subscriber)

    def __notify_subscribers(self, currency):
        for subscriber in self.__subscribers:
            if currency in subscriber.currencies:
                subscriber.update(currency)

    def update_currency(self, currency, rate):
        self.currency[currency] = rate
        self.__notify_subscribers(currency)


class Subscriber:  # to jest interfejs
    def __int__(self):
        """Wymagana jest zmienna currencies, która jest listą subskrybowanych walut"""
        self.currencies = []

    def update(self, currencies):
        """Metoda do updatowania kursu waluty"""
        pass


class Product:
    def __init__(self, name, original_price, currency):
        self.name = name
        self.original_price = original_price
        self.local_price = bank.currency[currency] * original_price
        self.currency = currency

    def __str__(self):
        return f"\n Produkt: {self.name}, cena w {self.currency}: {self.original_price}, cena w PLN: {self.local_price}"


class Shop(Subscriber):
    def __init__(self):
        self.products = []
        self.currencies = []
        bank.subscribe(self)

    def add_product(self, product):
        self.products.append(product)
        self.currencies.append(product.currency)

    def update(self, currency):
        for product in self.products:
            if currency == product.currency:
                product.local_price = bank.currency[currency] * product.original_price

    def __str__(self):
        return f"Sklep:{'  '.join(str(produkt) for produkt in self.products)}\n"


if __name__ == "__main__":
    bank = Bank()

    shop = Shop()
    shop.add_product(Product("Kurtka", 100, "USD"))
    shop.add_product(Product("Spodnie", 50, "EUR"))
    shop.add_product(Product("Koszula", 200, "GBP"))

    print(shop)

    bank.update_currency("USD", 4.0)
    print(shop)

    bank.update_currency("EUR", 4.5)
    print(shop)

    bank.update_currency("GBP", 5.5)
    print(shop)

    bank.unsubscribe(shop)
    bank.update_currency("GBP", 5.0)
    print(shop)