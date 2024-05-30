import numpy as np
import matplotlib.pyplot as plt 

def heatMap(seasons, players, vals, stat):
    plt.figure(figsize = (10, 10))

    plt.imshow(vals, cmap="Reds")
    plt.xticks(np.arange(0, len(players)), players, rotation=90)
    plt.yticks(np.arange(0, len(seasons)), seasons)

    plt.colorbar() 

    plt.title("Liverpool FC Player " + stat)
    plt.show()
    
def seasonName(year):
    return str(year) + "/" + str(year + 1)
  
data = {
    2017: {
        "Mohamed Salah": {"goals": 44, "appearances": 52},
        "Roberto Firminho": {"goals": 27, "appearances": 54},
        "Sadio Mane": {"goals": 20, "appearances": 44},
        "Alex Oxlade-Chamberlain": {"goals": 5, "appearances": 42}
    },
    2018: {
        "Mohamed Salah": {"goals": 27, "appearances": 52},
        "Roberto Firminho": {"goals": 16, "appearances": 48},
        "Sadio Mane": {"goals": 26, "appearances": 50},
        "Alex Oxlade-Chamberlain": {"goals": 0, "appearances": 2}
    },
    2019: {
        "Mohamed Salah": {"goals": 23, "appearances": 48},
        "Roberto Firminho": {"goals": 12, "appearances": 52},
        "Sadio Mane": {"goals": 22, "appearances": 47},
        "Alex Oxlade-Chamberlain": {"goals": 8, "appearances": 43}
    },
    2020: {
        "Mohamed Salah": {"goals": 31, "appearances": 51},
        "Roberto Firminho": {"goals": 9, "appearances": 48},
        "Sadio Mane": {"goals": 16, "appearances": 48},
        "Alex Oxlade-Chamberlain": {"goals": 1, "appearances": 17},
        "Diogo Jota": {"goals": 13, "appearances": 30}
    },
    2021: {
        "Mohamed Salah": {"goals": 31, "appearances": 51},
        "Roberto Firminho": {"goals": 11, "appearances": 35},
        "Sadio Mane": {"goals": 23, "appearances": 51},
        "Alex Oxlade-Chamberlain": {"goals": 3, "appearances": 29},
        "Diogo Jota": {"goals": 21, "appearances": 55},
        "Luis Diaz": {"goals": 6, "appearances": 26}
    },
    2022: {
        "Mohamed Salah": {"goals": 30, "appearances": 51},
        "Roberto Firminho": {"goals": 13, "appearances": 35},
        "Alex Oxlade-Chamberlain": {"goals": 1, "appearances": 13},
        "Diogo Jota": {"goals": 7, "appearances": 28},
        "Luis Diaz": {"goals": 5, "appearances": 21}
    }
}

players = []
seasons = []

for season in data:
    seasons.append(seasonName(season))
    players = players + list(data[season].keys())
    

players = list(dict.fromkeys(players))
players.sort()
    
ans = ""

while (ans != 0):
    print ("1: goals")
    print ("2: appearances")
    print ("0: Exit")

    while True:
        try:
            ans = int(input("Select a stat"))
            break
        except:
            print("Invalid option. Please try again.")
    
    if (ans == 1): stat = "goals"
    if (ans == 2): stat = "appearances"
    if (ans == 0): break
    if (ans > 2 or ans < 0): continue
        
    stats = []
    
    for season in list(data.keys()):
        arr = []
        for player in players:
            if (player in data[season]):
                arr.append(data[season][player][stat])
            else:
                arr.append(0)
                
        stats.append(arr)
    
    print(players)
    print(seasons)
    print(stats)
    heatMap(seasons, players, stats, stat)
