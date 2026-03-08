import os
import time

f = open("hello", "w+")
print("File descriptor:", f.fileno())  # الرقم اللي OS كيتعامل معاه
print("Mode:", f.mode)                 # 'w'
print("Encoding:", f.encoding)         # 'utf-8'
print("Is closed?", f.closed)
f.write("Asdasdasdasd")# False
print("Current position:", f.tell())   # مؤشر الكتابة داخل الملف