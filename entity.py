class entity:

    def __init__(self, name, type, hp, atk, level, gold, inventory):
        self.name = name
        self.type = type
        self.hp = hp
        self.atk = atk
        self.level = level
        self.gold = gold
        self.inventory = inventory

    def __str__(self):
        return "Name: " + self.name + "\nType: " + self.type + "\nHP: " + str(self.hp) + "\nAttack: " + str(self.atk) + "\nLevel: " + str(self.level) + "\nGold: " + str(self.gold) + "\nInventory: " + str(self.inventory)

    def get_name(self):
        return self.name

    def get_type(self):
        return self.type

    def get_hp(self):
        return self.hp

    def get_level(self):
        return self.level

    def get_gold(self):
        return self.gold

    def get_inventory(self):
        return self.inventory

    def get_attack(self):
        return self.atk

    def set_hp(self, hp):
        self.hp = hp

    def set_level(self, level):
        self.level = level

    def set_gold(self, gold):
        self.gold = gold

    def set_attack(self, atk):
        self.atk = atk
