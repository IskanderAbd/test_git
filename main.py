import schedule
import time
import csv

def write_csv():
    name = input('enter ur name: ')
    age = input('enter age: ')
    with open('users.csv', 'a') as csv_file:
        writer = csv.writer(csv_file, delimiter='/')
        writer.writerow(
            (name, age)
        )
    answ = input('continue? y or n: ')
    if answ == 'y':
        write_csv()
    else:
        print('stop')

def mailing():
    with open('users.csv', 'r') as csv_file:
        data = csv_file.readlines()
        names = [i.replace('\n','')for i in data]
        for i in names:
            name = i.split('/')
            if int(name[-1]) >=18:
                print(f'skidki segodnya {name[0]}')

schedule.every(3).second.do(mailing)

while True:
    schedule.run_pending()
    time.sleep(1)

# write_csv()
# mailing()


# class Info:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age

#     def check(self):
#         if self.age > 18:
#             print('pokypai vodky so skidkoi')
#         else:
#             print('uchi uroki debil')


#     def write_csv(self):
#         with open('info.csv', 'a') as csv_file:
#             writer = csv.writer(csv_file, delimiter='/')

#             writer.writerow(
#                 (
#                     self.name
#                     self.age
                    
#                 )
#             )



# #основные команды

# git init # инициализация пустого локального репозитори
# git remote add origin SSH/HTTPS #Привязка локального репозитория к удаленному репозиторию в гитхабе
# git remote remove origin #удаляет привязку 
# git remote -v #просмотр привязки, к какому репозиторию привязано
#git pull origin branch_name стянуть изменения/данные с гитхаба(с определенной ветки
# git status #команда для проверки статуса коммита(подготовлены ли файлы к отправке, какие игнорируются и т д)

#привязка

# git remote add origin SSH/HTTPS #Привязка локального репозитория к удаленному репозиторию в гитхабе
# git remote remove origin #удаляет привязку 
# git remote -v #просмотр привязки, к какому репозиторию привязано

#отправка 

# git add  . # какие изменения, новые файлы нужно добавить в последующую отправку(упаковка)
# git commit -m 'Напиши название проекта' #команда для подготовки(коммита) к отправке, добавляем описание(опционально), кратко что было сделано, либо добавлено ит д
# git push origin branch_name #отправка куда и на какую ветку


#ветки

# git branch -v #просмотр всех веток и где находимся(на какой ветке)
# git branch branch_name #создание ветки
# git checkout branch_branch_name #переключение с ветки на ветку
# git remote -d branch_name #удаление ветки локально