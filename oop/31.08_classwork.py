class DictToJson:

    def __init__(self, a):
        print("Наш список для итераций: \n", a)
        # print('init')
        self.a = a
        self.my_dict = {}

    def dictate(self):
        # self.my_dict = {}
        print("Собрали из списка такой dict:")
        for i in self.a:
            self.my_dict[i] = i
        print(self.my_dict)

    def write_to_file(self):
        if self.my_dict:
            import json
            print(str(self.my_dict))
            with open(str(self.my_dict), 'w') as file:
                json_str = json.dumps(self.my_dict, sort_keys=True, indent=2)
                file.write(json_str)


obj_a = DictToJson(a=[1, 2, 3, 12, 8, 4])
obj_a.dictate()
obj_a.write_to_file()
