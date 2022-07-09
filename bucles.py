def run():
  LIMIT=1000
  count=0
  powerof_2=2**count
  while powerof_2<LIMIT:
    print('2 powered to '+str(count)+' is: '+str(powerof_2))
    count=count+1
    powerof_2=2**count

if __name__ == '__main__':
  run()
