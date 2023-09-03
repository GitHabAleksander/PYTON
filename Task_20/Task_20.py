# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет 
# определенную ценность. В случае с английским алфавитом очки 
# распределяются так:
# ●      A, E, I, O, U, L, N, S, T, R – 1 очко; 
# ●      D, G – 2 очка;
# ●      B, C, M, P – 3 очка;
# ●      F, H, V, W, Y – 4 очка;
# ●      K – 5 очков;
# ●      J, X – 8 очков;
# ●      Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ●      А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ●      Д, К, Л, М, П, У – 2 очка; 
# ●      Б, Г, Ё, Ь, Я – 3 очка;
# ●      Й, Ы – 4 очка;
# ●      Ж, З, Х, Ц, Ч – 5 очков; 
# ●      Ш, Э, Ю – 8 очков;
# ●      Ф, Щ, Ъ – 10 очков.
# Напишите  программу,  которая  вычисляет  стоимость  введенного
# пользователем  слова. Будем  считать,  что  на  вход  подается  
# только  одно  слово,  которое  содержит  либо  только английские,
# либо только русские буквы.
# Ввод: ноутбук Вывод: 12

# ochko1 = { '1' : {'а', 'в', 'е', 'и', 'н', 'о', 'р', 'с', 'т', 'a', 'e', 'i', 'o', 'u', 'l', 'n', 's', 't', 'r'}}
# ochko2 = { '2' : {'д', 'к', 'л', 'м', 'п', 'у', 'd', 'g'}}
# ochko3 = { '3' : {'б', 'г', 'ё', 'ь', 'я', 'b', 'c', 'm', 'p'}}
# ochko4 = { '4' : {'й', 'ы', 'f', 'h', 'v', 'w', 'y'}}
# ochko5 = { '5' : {'ж', 'з', 'х', 'ц', 'ч', 'k'}}
# ochko8 = { '8' : {'ш', 'э', 'ю', 'j', 'x'}}
# ochko10 = { '10' : {'ф', 'щ', 'ъ', 'q', 'z'}}

k = 'ноутбук' #input('')
# summa = 0
# for i in k:
#     for key, values in ochko4.items():
#         if i in values:
#             summa += int(key)
#         else:
#             for key, values in ochko10.items():
#                 if i in values:
#                     summa += int(key)
#             else:
#                 for key, values in ochko8.items():
#                     if i in values:
#                         summa += int(key)
#                 else:
#                     for key, values in ochko5.items():
#                         if i in values:
#                             summa += int(key)
#                     else:
#                         for key, values in ochko3.items():
#                             if i in values:
#                                 summa += int(key)
#                         else:
#                             for key, values in ochko2.items():
#                                 if i in values:
#                                     summa += int(key)
#                             else:
#                                 for key, values in ochko1.items():
#                                     if i in values:
#                                         summa += int(key)           
#             print(summa)
# dict = {'1' : {'а', 'в', 'е', 'и', 'н', 'о', 'р', 'с', 'т'}, 
#         '2' : {'д', 'к', 'л', 'м', 'п', 'у'},
#         '3' : {'б', 'г', 'ё', 'ь', 'я'},
#         '4' : {'й', 'ы'},
#         '5' : {'ж', 'з', 'х', 'ц', 'ч'},
#         '8' : {'ш', 'э', 'ю'},
#         '10' : {'ф', 'щ', 'ъ'}}
# k = input('')
# summa = 0
# for i in k:
#     for key, values in dict.items():
#         if i in values:
#             summa += int(key)
#             print(summa)

symbol_cost = {
    'А':1, 'В':1, 'Е':1, 'И':1, 'Н':1, 'О':1, 'Р':1, 'С':1, 'Т':1,
    'Д':2, 'К':2, 'Л':2, 'М':2, 'П':2, 'У':2,
    'Б':3, 'Г':3, 'Ё':3, 'Ь':3, 'Я':3,
    'Й':4, 'Ы':4,
    'Ж':5, 'З':5, 'Х':5, 'Ц':5, 'Ч':5,
    'Ш':8, 'Э':8, 'Ю':8,
    'Ф':10, 'Щ':10, 'Ъ':10,
    'A':1, 'E':1, 'I':1, 'O':1, 'U':1, 'L':1, 'N':1, 'S':1, 'T':1, 'R':1, 
    'D':2, 'G':2, 
    'B':3, 'C':3, 'M':3, 'P':3, 
    'F':4, 'H':4, 'V':4, 'W':4, 'Y':4, 
    'K':5,
    'J':8, 'X':8,
    'Q':10, 'Z':10
    }

def count_mass(my_str) -> int:
    if len(my_str) <= 0: return 0
    
    my_str = my_str.upper()
    count = 0
    for sym in my_str:
        count += symbol_cost[sym]
    return count

print(count_mass(k))