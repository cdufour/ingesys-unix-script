def getPriceWithVAT(price, vat, shouldRound=True):
    priceWithVat = price * (1 + vat/100)
    if shouldRound:
        return round(priceWithVat, 2)
    else:
        return priceWithVat

prices = [14,100,30,10,8]

userVat = float(input("TVA: "))
for p in prices:
    print(getPriceWithVAT(p, userVat, shouldRound=False))