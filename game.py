class event:
    def __init__(self, name, history, hp_change, atk_change, gold_change, inventory_change):
        self.name = name
        self.history = history
        self.hp_change = hp_change
        self.atk_change = atk_change
        self.gold_change = gold_change
        self.inventory_change = inventory_change

    def get_name(self):
        return self.name

    def get_history(self):
        return self.history

    def get_hp_change(self):
        return self.hp_change

    def get_atk_change(self):
        return self.atk_change

    def get_gold_change(self):
        return self.gold_change

    def get_inventory_change(self):
        return self.inventory_change

class open_chest:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_value(self):
        return self.value

