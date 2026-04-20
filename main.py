class ValyutaKonvertor:
    def __init__(self):
        self.valyutalar = {
            "USD": 1,
            "EUR": 0.88,
            "GBP": 0.76,
            "RUB": 74.35,
            "JPY": 109.35,
            "CNY": 6.45
        }

    def konvertor(self, valyuta1, summa, valyuta2):
        if valyuta1 not in self.valyutalar or valyuta2 not in self.valyutalar:
            return "Kerakli valyutalar mavjud emas"
        if valyuta1 == valyuta2:
            return summa
        return summa * self.valyutalar[valyuta2] / self.valyutalar[valyuta1]


def main():
    konvertor = ValyutaKonvertor()
    valyuta1 = input("Birinchi valyutani kiriting (USD, EUR, GBP, RUB, JPY, CNY): ")
    summa = float(input("Summani kiriting: "))
    valyuta2 = input("Ikkinchi valyutani kiriting (USD, EUR, GBP, RUB, JPY, CNY): ")
    natija = konvertor.konvertor(valyuta1, summa, valyuta2)
    if isinstance(natija, str):
        print(natija)
    else:
        print(f"{summa} {valyuta1} = {natija} {valyuta2}")


if __name__ == "__main__":
    main()
```

Kodda quyidagi funksiyalar mavjud:

- `ValyutaKonvertor` klassi valyuta konvertorini amalga oshiradi.
- `konvertor` metodi valyuta konvertorini amalga oshiradi.
- `main` funksiyasi dastur ishga tushirish uchun javob beradi.
