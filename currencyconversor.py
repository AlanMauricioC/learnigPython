def convert_currency(dolar_value,currency):
  mxn_pesos=float(input('How many '+currency+ ' pesos do you have? '))
  dolars=mxn_pesos/dolar_value
  dolars=round(dolars,2)
  print('you have $'+str(dolars)+' dolars')
  return dolars

menu="""
Welcome to currency converter 💰

1 - Colombian Pesos
2 - Argentine Pesos
3 - Mexican Pesos

Select an option: """

option=input(menu)

if option == '1':
  convert_currency(3875,'colombian')
elif option == '2':
  convert_currency(65,'argeninian')
elif option == '3':
  convert_currency(20,'mexican')
else:
  print('please select a valid option')

