menu="""
Welcome to currency converter 💰

1 - Colombian Pesos
2 - Argentine Pesos
3 - Mexican Pesos

Select an option: """

option=input(menu)

mxn_pesos=float(input('How many Mexican pesos do you have? '))
dolar_value=20.34

dolars=mxn_pesos/dolar_value
dolars=round(dolars,2)
print('you have $'+str(dolars)+' dolars')
