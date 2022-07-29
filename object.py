class item:

    def __init__(self, name, display_name, description, price, value, target):
        self.name = name
        self.display_name = display_name
        self.description = description
        self.price = price
        self.value = value
        self.target = target

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

    def get_name(self):
        return self.name

    def get_display_name(self):
        return self.display_name


    def get_description(self):
        return self.description

    def get_price(self):
        return self.price

    def get_value(self):
        return self.value

    def get_target(self):
        return self.target



