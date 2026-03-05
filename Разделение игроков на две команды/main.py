list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# индекс середины
middle = len(list_players) // 2             #Находим середину

first_team = list_players[:middle]          #Делим с 0 индекса до середины
second_team = list_players[middle:]         #Делим с середины до конца
print(first_team)                           #Вывод 1 порловины
print(second_team)                          #Вывод 2 порловины
