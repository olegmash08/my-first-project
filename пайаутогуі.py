# import pyautogui
# width, height = pyautogui.size()
# print(f"Розмір екрана :{width}x{height}")

# current_x, current_y = pyautogui.position()
# print(f"Позиція миші: {current_x}, {current_y}")
# # pyautogui.moveTo(x, y, duration=num_seconds): #Переміщує курсор в абсолютні координати (x, y). duration — час у секундах, за який відбудеться рух.
# # pyautogui.moveRel(xOffset, yOffset, duration=num_seconds): #Переміщує курсор відносно його поточної позиції.
# #Плавно перемістити в центр екрана за 2 секунди
# pyautogui.moveTo(width /2, height/2, duration = 2)
# #Перемістити на 100 пікселів вправо
# pyautogui.moveRel(100, 0, duration = 1)


#Кліки мишею
# pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left'): Симулює клік. Можна вказати координати, кількість кліків, інтервал та кнопку ('left', 'middle', 'right').
# pyautogui.doubleClick(): Подвійний клік.
# pyautogui.rightClick(): Клік правою кнопкою.
# pyautogui.mouseDown() / pyautogui.mouseUp(): Натиснути та відпустити кнопку миші.

# Перетягування (Drag & Drop)
# pyautogui.dragTo(x, y, duration=num_seconds): Перетягнути до координат (x, y).
# pyautogui.dragRel(xOffset, yOffset, duration=num_seconds): Перетягнути відносно поточної позиції.

# Прокрутка (Scroll)
# pyautogui.scroll(amount_to_scroll): Прокручує коліщатко миші. Додатне значення — вгору, від'ємне — вниз.


#Клавіатура
# pyautogui.write('Hello, world', interval = 0.5)
# pyautogui.press('enter')
# pyautogui.hotkey('ctrl', 's')


# 3. Вікна повідомлень
# Корисно для взаємодії з користувачем або для налагодження скрипту.
# pyautogui.alert('Це повідомлення.')#Показує просте вікно з кнопкою "OK".
# pyautogui.confirm('Продовжити?', buttons=['Так', 'Ні']): Вікно з кількома кнопками. Повертає текст натиснутої кнопки.
# pyautogui.prompt('Введіть ваше ім\'я:'): Вікно для введення тексту.


# 4. Розпізнавання екрана (найпотужніше)
# PyAutoGUI може знаходити зображення на екрані. Це дозволяє створювати надійні скрипти, які не залежать від координат.
# pyautogui.screenshot('my_screenshot.png'): Робить скріншот екрана.
# pyautogui.locateOnScreen('image.png', confidence=0.8): Шукає зображення image.png на екрані. confidence (від 0 до 1) — рівень впевненості, корисний, якщо зображення трохи відрізняється. Повертає координати (left, top, width, height) або None.
# pyautogui.locateCenterOnScreen('image.png', confidence=0.8): Те ж саме, але повертає координати центру знайденого зображення, що зручно для кліку.

# import pyautogui as p
# import random, time
# a = input()
# for _ in range(1):
#     w, h = p.size()
#     p.hotkey('win', 'r')
#     time.sleep(0.5)
#     p.write('msedge', interval = 0.3)
#     p.press('enter')
#     time.sleep(2)/.py
#     p.write(f'weather{a}', interval = 0.3)
#     p.press('enter')
import pyautogui
import time
# ПЛАН ЗАВДАННЯ
# прінти для користувача
print("Ласкаво просимо в нашу розумну програму Tun tun Programun")
print("=======================ОБЕРІТЬ ДІЮ=============================\n  ")
print("1. Відкрити ютуб")
print("2. Знайти погоду в місті ")
print("3. Знайти відео на ютуб ")
print("4. Відкрити блокнот ")
print("5. Відкрити Paint")
print("6. Відкрити Telegram ")
print("7. Відкрити Visual Studio ")
print("8. Намалювати квадрат у Paint ")
print("9. Відкрити випадкову статтю у вікіпедії ")
choice = input("Обирайте : ")
pyautogui.alert("Увага зараз програма почне працювати йдіть попийте чай ")
if choice == "1":
    pyautogui.hotkey("win","r")
    time.sleep(2)
    pyautogui.write("msedge")
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.write('youtube.com',interval=2)
    pyautogui.press("enter")
    pyautogui.alert("Ютуб відкрито")
elif choice == "2":
    a = input() 
    w, h = pyautogui.size()
    pyautogui.hotkey('win', 'r')
    time.sleep(0.5)
    pyautogui.write('msedge', interval = 0.3)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.write(f'weather{a}', interval = 0.3)
    pyautogui.press('enter')
elif choice == "3":
    pyautogui.hotkey("win", "r")
    time.sleep(0.5)
    pyautogui.write("msedge", interval = 0.3)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.write("youtube.com", interval = 1)
    pyautogui.press("enter")
    b = pyautogui.prompt("Введіть назву відео?")
    pyautogui.write(f"{b}", interval = 1)
    pyautogui.press("enter")
elif choice == "4":
    pyautogui.hotkey("win", "r")
    time.sleep(0.5)
    pyautogui.write("notepad", interval = 0.3)
    pyautogui.press('enter')
elif choice == "5":
    pyautogui.hotkey("win", "r")
    time.sleep(0.5)
    pyautogui.write("mspaint", interval = 0.3)
    pyautogui.press("enter")
elif choice == "6":
    pyautogui.hotkey("win", "r")
    time.sleep(0.5)
    pyautogui.write(r"C:\Users\Admin1\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Telegram Desktop\Telegram.lnk", interval = 0.1)
    pyautogui.press("enter")
elif choice == "7":
    pyautogui.hotkey("win", "r")
    time.sleep(0.5)
    pyautogui.write(r"C:\Users\Admin1\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk", interval = 0.1)
    pyautogui.press("enter")
elif choice == "8":
    pyautogui.hotkey("win", "r")
    time.sleep(0.5)
    pyautogui.write("mspaint", interval = 0.1)
    pyautogui.press("enter")
elif choice == "9":
    pyautogui.hotkey("win", "r")
    time.sleep(0.5)
    pyautogui.write("msedge", interval = 0.1)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.write("https://uk.wikipedia.org/", interval = 0.1)
    pyautogui.press("enter")