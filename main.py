import entity
import object









def game_loop(player):
    while player.hp != 0:
        print("Player : " + str(player.hp) + " hp, " + str(player.level) + " level, " + str(player.gold) + " gold, " + str(len(player.inventory)) + " items")
        print("Que voulez vous faire ?")




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
