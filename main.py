def aprAtlaidi(summa):
  rez=""
  if summa<100:
    rez="Atlaide nav piešķirta, jānomaksa vēl "+ str(summa)
  elif summa>=100 and summa <200:
    rez="Atlaide 5%, jānomaksā vēl " + str(summa*0.95)
  else:
    rez="Atlaide 10%, jānomaksā vēl " + str(summa*0.90)
  return rez

summa=float(input("Ievadiet summu: "))
print(aprAtlaidi(summa))