list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

middle = len(list_players) // 2             #Находим середину

team_f = list_players[:middle]              #Делим с 0 индекса до середины
team_s = list_players[middle:]              #Делим с середины до конца
print(team_f)                               #Вывод 1 порловины
print(team_s)                               #Вывод 2 порловины
