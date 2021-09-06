import json


class FirstClass:

    def __init__(self, value: dict):
        self.value = value

    # def print(self):
    #     print(str(self))

    # def __str__(self):
    #     return 'temp.json'

    def serialize(self, value):
        print('My file name:', value)
        if type(value) == str:
            return eval(value)
        elif type(value) == dict:
            return str(value)
        return

    def open_file(self):
        obj_json = json.loads(self.serialize(open(str(self), 'r').read()))
        print(obj_json)
        return obj_json

    def write_file(self):
        value = self.serialize(value=self.value)
        file = open(str(self), 'w')
        file.write(value)
        file.close()
        return value


class SecondClass(FirstClass):

    def __str__(self):
        value = super().__str__()
        return value + '2'


file_name = 'temp.json'

# obj_class = FirstClass(value={'64': 'mix'})
# obj_class = SecondClass(value="{'64': 'mix'}")
# obj_class.write_file()
value = FirstClass.open_file()
# value = ff.serialize(value="my string")
# value = ff.serialize(value="my string")
print(value)
# obj_json = json.loads(open(file_name, 'r').read())
# print(obj_json)
