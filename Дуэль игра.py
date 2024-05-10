import random
import colorama
import time

red=colorama.Fore.RED
green=colorama.Fore.GREEN
yellow=colorama.Fore.YELLOW
blue=colorama.Fore.BLUE
magenta=colorama.Fore.MAGENTA
reset=colorama.Style.RESET_ALL

a={'1':'Voin','2':'Luchnik','3':'Mag','4':'Nindzya'}
b={
    'Voin': {
          'Атака':50,
          'Защита':20,
          'Здоровье':100,

          'Навыки':{
                  'Щит':10,
                  'Зелье защиты':15
           },
          'инвентарь':[
                     'Меч','Щит','Броня'
          ]
    },
    'Luchnik':{
             'Атака':45,
             'Защита':25,
             'Здоровье':100,

             'Навыки':{
                     'Бег':10, #защита
                     'Скрытность':15
             },
             'инвентарь':[
                        'Лук','Стрелы','Колчан'
             ]
    },
    'Mag':{
         'Атака':45,
         'Защита':20,
         'Здоровье':100,

         'Навыки':{
                 'Магический щит':10,#защита
                 'Исцеленние':10
         },
         'инвентарь':[
                    'Посох','Плащ','Книга'
         ]
    },
    'Nindzya':{
             'Атака':45,
             'Защита':15,
             'Здоровье':100,

             'Навыки':{
                     'Тень':20,#защита
                     'Исчезновение':10 #HP
             },
             'инвентарь':[
                        'Кинжал','Накидка','Маска'
             ]
    }
}
def fight(enemy,hero):
    random1=random.randint(1,2)
    if random1==1:
       print(f'{green}Первым атакует герой{reset} ')
    else:
        print(f'{red}Первым атакует враг{reset} ')
    while True:
        if random1==1:
            if hero['discrip']['Здоровье']>0:
                attack_hero(hero,enemy)
            else:
                print(f'{red}Вы проиграли{reset}')
                return True

            if enemy['discrip']['Здоровье']>0:
                attack_enemy(enemy,hero)
            else:
                print(f'{green}Вы победили врага!{reset}')
                return False
        elif random1==2:
            if enemy['discrip']['Здоровье']>0:
                attack_enemy(enemy,hero)
            else:
                print(f'{green}Вы победили врага!{reset}')
                return False

            if hero['discrip']['Здоровье']>0:
                attack_hero(hero,enemy)
            else:
                print(f'{red}Вы проиграли{reset}')
                return True
        print()
        input(f'{blue}Введите Enter чтобы продолжить{reset} ')
        print()
    # 1. рандомно выбрать первого атакующего 2. проверить здоровье первого атакующего если здоровье больше 0, тогда он будет атаковать 3. проверить здоровье 2 игрока если здоровье больше 0 тогда он будет атаковать 4. продолжать пока здоровье одного из игроков не будет 0

def attack_hero(hero,enemy):
    print(f'{magenta}{hero["name"]}{reset} атакует {red}{enemy["name"]}{reset}')
    skill_enemy=skill(enemy,False)
    if skill_enemy in ['Тень','Магический щит','Бег']:
        enemy['discrip']['Защита']+=enemy['discrip']['Навыки'][skill_enemy]
    else:
        enemy['discrip']['Здоровье']+=enemy['discrip']['Навыки'][skill_enemy]
    attack=hero['discrip']['Атака']-enemy['discrip']['Защита']
    if attack<0:
        attack=5
    enemy['discrip']['Здоровье']-=attack
    print(f'Вы нанесли {red}{attack}{reset} урона, у вашего врага осталось {green}{enemy["discrip"]["Здоровье"]}{reset} здоровья ')

def attack_enemy(enemy,hero):
    print(f'{magenta}{enemy["name"]}{reset} атакует {red}{hero["name"]}{reset}')
    skill_hero=skill(hero,True)
    if skill_hero in ['Тень','Магический щит','Бег']:
        hero['discrip']['Защита']+=hero['discrip']['Навыки'][skill_hero]
    else:
        hero['discrip']['Здоровье']+=hero['discrip']['Навыки'][skill_hero]
    attack=enemy['discrip']['Атака']-hero['discrip']['Защита']
    if attack<0:
        attack=5
    hero['discrip']['Здоровье']-=attack
    print(f'Вам нанесли {red}{attack}{reset} урона, у вашего персонажа осталось {green}{hero["discrip"]["Здоровье"]}{reset} здоровья ')

def skill(dict_person,is_hero):
    if is_hero==True:
        for key in dict_person['discrip']['Навыки'].keys():
            print(key)
        skill_hero=input('Выберите навык ')
        while skill_hero.capitalize() not in dict_person['discrip']['Навыки']:
              print('Введите правильный навык ')
              skill_hero=input('Введите навык ')
        time.sleep(1)
        return skill_hero
    else:
        skill_en=random.choice(list(dict_person['discrip']['Навыки']))
        print('Ваш противник выбрал навык: ',yellow,skill_en,reset)
        time.sleep(1)
        return skill_en
def name_hero():
    name_h=input(f'{green}Введите имя {reset}')
    while name_h=='':
        name_h=input(f'{green}Введите имя {reset}')
    return name_h

def name_enemy():
    name_e1=['Сильный','Быстрый','Мега','Доктор','Летающий']
    name_e2=['Кролик','Злодей','Мозг','Алхимик','Дракон']
    name_en=random.choice(name_e1)+' '+random.choice(name_e2)
    return name_en

def create(is_hero):
    if is_hero==True:
        name=name_hero()
        while True:
            for key,val in a.items():
               print(key,'-',val)
            create_h=input(f'{blue}Выберите героя {reset}')
            while create_h not in a:
                create_h=input(f'{red}Пожалуйста, выберите правильный номер {reset}')
            print(a[create_h])
            print(b[a[create_h]])
            numb=input(f'Вы уверены в своём выборе? {green}1-Да {red}2-Нет {reset}')
            if numb=='1':
               dict_hero={'name':name,'person':a[create_h],'discrip':b[a[create_h]]}
               return dict_hero
    else:
        name_en=name_enemy()
        random_numb=random.choice(list(a))
        dict_enemy={'name':name_en,'person':a[random_numb],'discrip':b[a[random_numb]]}
        return dict_enemy
hero=create(True)
print(f'{blue}Ваш персонаж: {reset}',hero)
enemy=create(False)
print(f'{red}Вы играете против: {reset}',enemy['name'],enemy['person'])
fight(enemy,hero)

# Тернарный оператор - if внутри print