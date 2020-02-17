# -*- coding: utf-8 -*-
import os
from tkinter import *
from tkinter import messagebox
import hashlib
import shutil
import sys
from sys import platform
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA

proc = "Информация о процессоре"+os.environ["PROCESSOR_IDENTIFIER"] +"\n" ;
numbproc = "Число процессоров" + os.environ["NUMBER_OF_PROCESSORS"]+ "\n";
OS = "Операционная система" + os.environ["OS"]+"\n" ;
Comp ="Имя компьютера" + os.environ["COMPUTERNAME"] + "\n" ;
User= "Имя пользователя" + os.environ["USERNAME"] ;

sysinf=proc+numbproc+OS+Comp+User;
#print(os.environ);
#print(os.environ["TMP"])
#print(os.environ["USERNAME"])#собираем инфу о системе info
info= sysinf.encode("utf-8")
h1=hashlib.md5(info);
h1.update;
hashin=h1.hexdigest()
#print(h1.hexdigest())  #хешируем инфу о системе в переменную hashin

def ChekingName():
    FolderName = message.get() #введенное пользователем
    NowPath = os.getcwd() #путь до нынешней директории, можно заменить на dir_path
    print(NowPath)
    print(FolderName)
    file_path = NowPath + "/"  + FolderName + 'syst_doc.dat' #ERROR
    print (file_path)
    #file_path = 'E:/PyCharm 2017.1/PyProjects/second/testt/syst_doc.txt' # при таком формате dirname работает нормально
    
    directory = os.path.dirname(file_path)
    print(directory)
    print(os.path.exists(directory))
    if  os.path.exists(directory):
        Text = 'Папка уже существует, файл будет создан в ней.'
       
    else:
        os.mkdir(directory)
        Text = 'Папка успешно создана.'
        
    file = open(file_path,'w'); #запись в файл
    file.write(hashin + "\n");
    file.close();
    
    filer = open(file_path,'r'); #проверка данных в файле(захешированы)
    for line in filer:
        print(line)
    file.close();
    #os.mkdir("test1")
    #path = r'E:\PyCharm 2017.1\PyProjects\second\test1'
    #os.mkdir(path)

    
    messagebox.showinfo("Создание папки", Text)

dir_path = os.path.dirname(os.path.realpath(__file__)) #узнаю путь до каталога со скриптом
os.chdir(dir_path) #меняю текущий рабочий каталог на тот, что содержит скрипт
root = Tk()  # окно
root.title("Создание папки с системной информацией")
root.geometry("400x300")
label = Label(text="Введите название папки в виде: \*название папки*\ ", justify=CENTER)
label.pack()
message = StringVar()
message_entry = Entry(textvariable=message,
                      bd="2",
                      width="40"
                      )
message_entry.place(relx=.5, rely=.1, anchor="c")  # вывод поля ввода в окно
btn = Button(text="Ввод",
             background="#555",
             activebackground="#FF4040",
             foreground="#ccc",
             padx="20",
             pady="8",
             font="16",
             command=ChekingName
             )




btn.place(relx=.5, rely=.3, anchor="c")  # вывод кнопки
root.mainloop()


message = "Tolstova".encode('utf-8')
privatekey = RSA.generate(1024)
f = open('privatekey.txt','wb')
f.write(bytes(privatekey.exportKey('PEM'))); f.close()
g = open('privatekey.txt').read()
print(g)
 
key = RSA.importKey(g)
h = SHA.new(message)
 
print(h.hexdigest())
 
signer = PKCS1_v1_5.new(key)
sig = signer.sign(h)
 
f = open('HKEY_CURRENT_USER \ Software \ signature.txt','wb')
f.write(bytes(sig)); f.close()
s = open('HKEY_CURRENT_USER \ Software \ signature.txt', 'rb')
signature = s.read(); s.close()
print(signature)
 
publickey = privatekey.publickey()
f = open('publickey.txt','wb')
f.write(bytes(publickey.exportKey('PEM'))); f.close()
g = open('publickey.txt').read()
print(g)

