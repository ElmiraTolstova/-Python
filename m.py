import os
import shutil
import hashlib
import time
import sys



parol = input(( ' Введите пароль --> ' ) )# ввод пароля
y=type(parol) #тип переменной (просто для интереса,можно удалить)
print (y)

    # Пароль, сохраненный в базе'5f4dcc3b5aa765d61d8327deb882cf99'
h2 = hashlib.md5(b"$parol")   # Пароль, введенный пользователем - хешируется
if (parol == h2.hexdigest()): print("Пароль правильный")
# то,что захешировано - обратно декодируется. ВСегда должно совпадать,т е пароль д б правильным,т к его же и ввели. Но нет.
#ВВела это для проверки части. как кодирует-шифрует Просто строку он шифрует(ниже представлен код)
  # sys.exit - фигня,выключающая программу. Проблема - не работает.По сей причине заккоментили. Другой вариант os.abort() вроде

h = hashlib.md5(b"password")
print (h)
p = h.hexdigest()
print (p)
h2 = hashlib.md5(b"password")   # Пример работающего хеширования
print(h2)
if p == h2.hexdigest(): print("Пароль правильный")


else:
     cur_dir = os.getcwd()
     filepath = os.path.join(cur_dir)
     print(filepath) #выдает эти 3 строки текущую директорию


     file = open("C:/Users/мартын/Desktop/template.tbl", 'w')
     file.write("") #Запись в файл. Writelines - построчно вроде. Кидаем сюда 1 строка - пароль,со 2-й папки,Файлы,которые нельзя редактить

     file = open("C:/Users/мартын/Desktop/template.tbl", 'r')
     file.readlines() #чтение файла,вроде этот метод по строкам(Но нам нужно игнорить 1-ю.Там д б пароль





    parol = input ( ' Change password --> ' )
    file = open("C:/Users/мартын/Desktop/template.tbl", 'w')
    file.write("")
 # хотела ввести штуку,вдруг пользователь захочет поменять пароль

