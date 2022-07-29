import entity
import object


def game_explore(player):
    print("Vous explorez le donjon")

def game_loop(player):
    while player.hp != 0:
        print("Player : " + str(player.hp) + " hp, " + str(player.level) + " level, " + str(player.gold) + " gold, " + str(len(player.inventory)) + " items")
        print("Voir l'inventaire ? (1)")
        print("Explorer le donjon ? (2)")
        response = input("Que voulez vous faire ? : ")
        if response == "1":
            print(player.inventory)
            print("Utiliser un objet ? (1)")
            print("Continuer ? (2)")
            responseInventory = input("Votre choix : ")
            if responseInventory == "1":
                responseItem = input("Quel objet voulez vous utiliser ? ")
                print("----------------------------------------------------")
            if responseInventory == "2":
                print("----------------------------------------------------")
        if response == "2":
            game_explore(player)
            print("----------------------------------------------------")



def setup():
    annonce()
    player_name = input("Quel est votre nom ? ")
    player = entity.entity(player_name,"player", 40, 5, 1, 0, [])
    player.inventory.append(object.item("health potion", "Une potion pour vous soigner", 10, "health"))
    game_loop(player)


def annonce():
    print("Bienvenue dans LiteRPG!")
    print("Apparament dans ce type de jeu y'a un scenario, euh donc on va dire :")
    print("Scenario :")
    print("Vous etes un heros qui a pour but de buter tout les monstres d'un donjon.")
    print("Fin du scenario")
    print("Vous connaiser les rpgs, donc pas besoin de vous expliquer les mechaniques(Hp, attaque, etc)")
    print("Bref, Préparez-vous à affronter des monstres!")
    print("Beaucoup de monstres..........")
    print("et aussi a ouvrir quelques coffres..........")
    print("Bonne chance")

def game_over():
    print("Malheuresement, votre etes est mort")
    print("Non pas vous derière votre ecran, mais votre heros")
    print("Donc je crois que vous avez perdu, Yep je sais, je suis perspicace")
    print("GAME OVER")

def main():
    setup()


if __name__ == "__main__":
    main()
