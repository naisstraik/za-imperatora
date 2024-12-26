import random
import time


# a  = [2,4,6,7,8]

# print( random.choices(a, weights=[0.2, 0.2, 0.2,0.2, 0.2], k = 10))

# import random

# a = random.choice([random.randint(1,200),"21312","dqwasdsa",random.randint(1,200)])
# print(a)

bosse = ["Босс Смертных","Челик","Häpuchi","你的死！","Гарри Поттер"]
boss = random.choices(bosse,weights=[0.2 , 0.2 , 0.2 , 0.2, 0.2], k = 10)

hpboss = random.randint(75,200)

hpplayr = 100

damageplayre = [0,10,20,30,40,50]
damageplayr = random.choices(damageplayre,weights=[0.05, 0.05, 0.05, 0.05, 0.05, 0.05], k = 1)

damagebosse = [0,10,20,30,40,50]
damageboss = random.choices(damagebosse,weights=[0.05, 0.05, 0.05, 0.05, 0.05, 0.05], k = 1)

items = {"Яблоко": " - Востанавливает вам 20 HP", "Кастеты": " - Нанести Урон","Enchanted golden apple": " - +100 hp"}

energyplayr = 100

energybos = 100

enersys = random.randint(10,50)
enersyse = random.randint(10,50)
energysp = random.randint(10,50)
energyb = random.randint(10,50)




print("💀💀   НЕ UNDERTALE   💀💀")
a = input("Нажмите Enter для старта")
while True:
    if a == "":
        break
    else:
        print(a)
    a = input("Нажмите Enter для старта")
while True:
    print("_______________________________________________________________")
    print(f"Ваш враг:{boss}")
    print(f"Его здоровье:{hpboss}")
    print()
    print()
    print(f"Ваша энергия:{energyplayr}")
    print(f"Ваше здоровье:{hpplayr} ")
    print("[ИНВЕНТАРЬ]   [ВОСТАНОВИТЬ ЭНЕРГИЮ]   [АТАКА]")
    print()
    print("1 - Инвентарь;2 - Востановить энергию;3 - Удар")
    xod = int(input("Выберите категорию: "))
    print("_______________________________________________________________")
    if energybos <= energyb:
        print("Враг усталь...🌚")
        energybos += enersyse
    if xod == 1:
        print("Ваш инвентарь: ",items)
        deystvie = int(input("Ваш действия(Для выхода напишите назад): "))
        print("Напишите номер предмета")
        if deystvie == 1 and "Яблоко" in items:
            print("Вы съeли яблоко")
            hpplayr += 20
            del items["Яблоко"]
        if deystvie == 2 and "Кастеты" in items:
            print(f"Вами был избит {t}")
            hpboss -= damageplayr
            del items["Кастеты"]
        if deystvie == 3 and "Enchanted golden apple" in items:
            print("Вы съeли Enchanted golden apple")
            hpplayr += 100
            del items["Enchanted golden apple"]
    if xod == 2:
        print(f"Вы востановили энергию:{energysp} энергии")
        energyplayr += enersys
        time.sleep(1)
        if energybos <= energyb:
            print("Враг усталь...🌚")
            energybos += enersyse
            time.sleep(1)
        else:
            print(f"Враг наносит вам {damageboss} урона")
            hpplayr -= damageboss
            time.sleep(1)
    if xod == 3 and energyplayr >= energysp:
        print(f"Вы наносите {damageplayr} урона")
        energyplayr -= energysp
        hpboss -= damageplayr
        time.sleep(1)
        if energybos <= energyb:
            print("Враг усталь...🌚")
            energybos += enersyse
            time.sleep(1)
        if hpboss <= 0:
            print("")
        else:
            print(f"Враг наносит {damageboss} урона")
            hpplayr -= damageboss
            time.sleep(1)
    else:
        print("Недостаточно энергии")
    if hpboss <= 0:
        print("Бос повержен!")
        del boss[bosse]
        print(f"Ваш новый противник: {boss}")
    if hpplayr <= 0:
        print("Вы проиграли...")
        break