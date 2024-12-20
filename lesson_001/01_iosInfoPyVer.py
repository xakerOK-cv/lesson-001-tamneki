# Потрібно зібрати інформацію від операційної системи версії Патчина, не бійтеся. І запустити цей скрипт
# Good

# -*- coding: utf-8 -*-


import platform
import sys


info = (
    f"OS info is {platform.uname()}\n\n"
    f"Python version is {sys.version}\n"
    f"Architecture: {platform.architecture()}\n"
)


print(info)


with open('os_info.txt', 'w') as ff:
    ff.write(info)
