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


def vopros(raynd):
  voprosi = {1:"Что растёт в огороде?", 2:"Как называют манекенщицу супер-класса?", 3:"Как называют микроавтобусы, совершающие поездки по определённым маршрутам?", 4:"Кто вырос в джунглях среди диких зверей?",
             5:"Как называлась детская развлекательная программа, популярная в прошлые годы?", 6:"Как звали невесту Эдмона Дантеса, будущего графа Монте-Кристо?", 7:"В какое море впадает река Урал?", }


  otveti = {1:"Лук", 2:"Топ-модель", 3:"Маршрутка", 4:"Маугли", 5:"АБВГДейка", 6:"Мерседес", 7:"Каспийское", 8:"Гром-камень",
            9:"Фиолетовый", 10:"Баранина", 11:"Венгры", 12:"Углерод", 13:"Сен-Жермен", 14:"Азербайджан", 15:"Кобальт"}

  rand_otveti = {1:"Пистолет", 2:"Пулемёт", 3:"Путёвка",
                 4:"Тяп-модель", 5:"Поп-модель", 6:"Колобок",
                 7:"Рейсовка", 8:"Путёвка", 9:"Курсовка",
                 10:"Бэтмен", 11:"Чарльз Дарвин", 12:"Ракета СС-20",
                 13:"ЁКЛМНейка", 14:"ЁПРСТейка", 15:"ЁЖЗИКейка",
                 16:"Тойота", 17:"Хонда", 18:"Лада", }


  banki = {1:500, 2:1000, 3:2000, 4:3000, 5:5000, 6:10000, 7:15000, 8:25000, 9:50000, 10:100000, 11:200000, 12:40000, 13:800000, 14:1500000, 15:3000000}

  voprosik = voprosi.get(raynd)
  otvetic = otveti.get(raynd)
  bank = banki.get(raynd)
  bred1=rand_otveti.get(raynd*3)
  bred2=rand_otveti.get(raynd*3-1)
  bred3=rand_otveti.get(raynd*3-2)
  return voprosik, otvetic, bank, bred1, bred2, bred3


def main():
  print("Доброго времени суток! Это игра кто хочет стать миллионером!")
  a=0
  voprosik=1
  while a!=1:
    testy=input("Начать тест?\n1 - Начать тест\n2 - Играть!\n")
    if testy=="1":
      a=1
      test()
    elif testy=="2":
      a=1
      name = input("Как тебя зовут? Ответ - ")
      print("Начали " + name + "!\n")
      while voprosik <= 15:
        print("Вопрос " ,voprosik, "!\n")
        voprosik, otvetic, bank, bred1, bred2, bred3 = vopros(voprosik)
        voprosik+=1
    else:
      print("Что-то не странное\n")


main()