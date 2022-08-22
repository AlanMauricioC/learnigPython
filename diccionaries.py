def run():
  country_poblation={
      'Argentina':44938512,
      'Brazil':210147125,
      'Colombia':50372424,
  }
  # print(country_poblation['Brazil'])
 # print keys 
  for country in country_poblation.keys():
    print(country)

 # print values 
  for poblation in country_poblation.values():
    print(poblation)
  
 # print item 
  for country,poblation in country_poblation.items():
    print(country+' has ' + str(poblation) + ' citizens')

if __name__ == '__main__':
    run()
