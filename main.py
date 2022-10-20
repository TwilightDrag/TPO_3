import random

def millioner(testic):
  bank=0
  voprosik=1
  while voprosik <= 15:
    dict1={}
    dict2={}
    arr=[]
    vopr, otvetic, banki, bred1, bred2, bred3 = vopros(voprosik)
    for i in range(4):
      key=random.randint(1, 4)
      arr.append(key)
    for k in range(100):
      for i in range(4):
        for j in range(i+1, 4):
          if arr[i] == arr[j]:
            arr[i] = random.randint(1, 4)
    dict1[arr[0]] = otvetic
    dict1[arr[1]] = bred1
    dict1[arr[2]] = bred2
    dict1[arr[3]] = bred3
    dict2[1]=dict1[1]
    dict2[2]=dict1[2]
    dict2[3]=dict1[3]
    dict2[4]=dict1[4]
    vopri=voprosik
    if testic == {}:
      while vopri==voprosik:
        print("Вопрос", voprosik,"!\n")
        print(vopr, "\n")
        print ("A: ", dict2[1], "Б: ", dict2[2], "\nВ: ", dict2[3], "Г: ", dict2[4])
        vvod=""
        vvod = input("\nОтвет: ")
        if vvod == "A" or vvod == "а":
          voprosik+=1
          if dict2[1] == otvetic:
            bank+=banki
            print("Ура! Вы выйграли ", banki, " рублей!\nТеперь у вас ", bank, "рублей\n")
          else:
            print ("Этот вопрос вам оказался не под силу, попробуйте следующий!\n")
        elif vvod == "Б" or vvod == "б":
          voprosik+=1
          if dict2[2] == otvetic:
            bank+=banki
            print("Ура! Вы выйграли ", banki, " рублей!\nТеперь у вас ", bank, "рублей\n")
          else:
            print ("Этот вопрос вам оказался не под силу, попробуйте следующий!\n")
        elif vvod == "В" or vvod == "в":
          voprosik+=1
          if dict2[3] == otvetic:
            bank+=banki
            print("Ура! Вы выйграли ", banki, " рублей!\nТеперь у вас ", bank, "рублей\n")
          else:
            print ("Этот вопрос вам оказался не под силу, попробуйте следующий!\n")
        elif vvod == "Г" or vvod == "г":
          voprosik+=1
          if dict2[4] == otvetic:
            bank+=banki
            print("Ура! Вы выйграли ", banki, " рублей!\nТеперь у вас ", bank, "рублей\n")
          else:
            print ("Этот вопрос вам оказался не под силу, попробуйте следующий!\n")
        else:
          print ("Я вас не понимаю...\n")
    else:
      if testic[voprosik]==otvetic:
        bank+=banki
      voprosik+=1
  return bank    


def test():
  i=1
  while i<=3:
    if i == 1:
      testik = {1:"Лук", 2:"Топ-модель", 3:"Маршрутка", 4:"Маугли", 5:"АБВГДейка", 6:"Мерседес", 7:"Каспийское", 8:"Гром-камень", 
                9:"Фиолетовый", 10:"Баранина", 11:"Венгры", 12:"Углерод", 13:"Сен-Жермен", 14:"Азербайджан", 15:"Кобальт"}
      a = millioner(testik)
      if a==5751500:
        print("test 1 выполнен")
    if i == 2:
      testik = {1:"Пистолет", 2:"Топ-модель", 3:"Маршрутка", 4:"Маугли", 5:"АБВГДейка", 6:"Мерседес", 7:"Каспийское", 8:"Гром-камень", 
                9:"Фиолетовый", 10:"Баранина", 11:"Венгры", 12:"Углерод", 13:"Сен-Жермен", 14:"Азербайджан", 15:"Кобальт"}
      a = millioner(testik)
      if a==5751000:
        print("test 2 выполнен")
    if i == 3:
      testik = {1:"Пистолет", 2:"Тяп-модель", 3:"Маршрутка", 4:"Маугли", 5:"АБВГДейка", 6:"Мерседес", 7:"Каспийское", 8:"Гром-камень", 
                9:"Фиолетовый", 10:"Баранина", 11:"Венгры", 12:"Углерод", 13:"Сен-Жермен", 14:"Азербайджан", 15:"Кобальт"}
      a = millioner(testik)
      if a==5750000:
        print("test 3 выполнен")
    i+=1

