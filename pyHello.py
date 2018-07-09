def currency_converter(rate,rupee):
    dollars = rupee*rate
    return dollars

r = input("Enter rate: ")
e = input("Enter euros: ")


print(currency_converter(float(r),float(e)))