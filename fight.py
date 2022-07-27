

def fight(player, enemy):
    print("----------------------------------------------------")
    print("Que voulez vous faire contre " + enemy.name)
    print("1. Attaquer")
    print("2. Utiliser un objet")
    response = input("Votre choix : ")
    if response == "1":
        enemy.hp -= player.atk
    if response == "2":
        print(player.inventory)
        response = input("Quel objet voulez vous utiliser ? ")
        for item in player.inventory:
            if response == item:
                item_object = player.inventory.get(item)



                player.inventory.remove(item)
