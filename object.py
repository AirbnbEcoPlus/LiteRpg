class item:

    def __init__(self, name, description, value, target):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_value(self):
        return self.value



