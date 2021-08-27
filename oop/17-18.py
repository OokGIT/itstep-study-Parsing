import xlsxwriter
import openpyxl

xls_file = 'example.xlsx'
xls_sheet = 'from_my_dict'

class ListIteration:

    def __init__(self, a):
        print(a)
        # print('init')
        self.a = a
        self.my_dict = {}
        self.workbook = xlsxwriter.Workbook(xls_file)
        self.worksheet = self.workbook.add_worksheet(xls_sheet)
        # self.row = 0
        # self.col = 0

    def unpack_list(self):
        for i in self.a:
            print(i, end=' ')
        print()

    def dictate(self):
        # self.my_dict = {}
        for i in self.a:
            self.my_dict[i] = i
        print(self.my_dict)

    def write_to_xls(self):
        if self.my_dict:
            row = 0
            col = 0
            print('дикт для распаковки в xls:', self.my_dict)
            # order = sorted(self.my_dict.keys())
            # for key in order:
            for key in self.my_dict.keys():
                print(key)
                self.worksheet.write(row, col, key)
                self.worksheet.write(row, col, self.my_dict[key])

                row += 1

                # for item in self.my_dict[key]:
                #     print(item, row, col + 1)
                #     self.worksheet.write(row, col + 1, item)
                #     col += 1
                # col = 0
            self.workbook.close()

    def from_xls(self):
        file = open(xls_file)
        xls_to_dict = file.read()
        file.close()
        print('Дикт из нашего xls:', xls_to_dict)


obj_a = ListIteration(a=[1, 2, 3, 12, 8, 4])
obj_a.unpack_list()
obj_a.dictate()
obj_a.write_to_xls()
# obj_a.from_xls()
# obj_a.func()
# obj_a._func()
