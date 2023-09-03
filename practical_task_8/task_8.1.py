# 8.1[49]: Создать телефонный справочник с возможностью импорта и экспорта данных в формате csv. 
# Доделать задание вебинара и реализовать Update, Delete
# Информация о человеке: Фамилия, Имя, Телефон, Описание
# Корректность и уникальность данных не обязательны.
# Функционал программы
# 1) телефонный справочник хранится в памяти в процессе выполнения кода.
# Выберите наиболее удобную структуру данных для хранения справочника.
# 2) CRUD: Create, Read, Update, Delete
# Create: Создание новой записи в справочнике: ввод всех полей новой записи, занесение ее в справочник.
# Read: он же Select. Выбор записей, удовлетворяющих заданном фильтру: по первой части фамилии человека. 
# Берем первое совпадение по фамилии.
# (*) Усложнение. Update: Изменение полей выбранной записи. Выбор записи как и в Read, заполнение новыми значениями.
# Delete: Удаление записи из справочника. Выбор - как в Read.
# 3) экспорт данных в текстовый файл формата csv
# 4) импорт данных из текстового файла формата csv
# Используйте функции для реализации значимых действий в программе


class Data:
    lst = {'sur_name': 'Фамилия', 'name': 'Имя', 'phone_number': 'Номер телефона', 'description': 'Описание'}
    def __init__(self, sur_name='', name='', phone_number='', description='', sep=','):
        self.sur_name = sur_name
        self.name = name
        self.phone_number = phone_number
        self.description = description
        self.sep = sep

    def __str__(self):
        return self.sep.join([self.__dict__[i] for i in self.__dict__.keys() if i != 'sep'])


class Table:
    def __init__(self, sep=',', row=Data):
        self.table = []
        self.sep = sep
        self.row = Data
        self.translater = self.row.lst

    def show_table(self):
        print('\nВыводим таблицу на экран...')
        print('*' * 50)
        print(*[f'Строка №{ind}: {str(i)}.' for ind, i in enumerate(self.table, 1)], sep='\n')
        print('*' * 50)

    def add_row(self, lst: list):
        self.table.append(self.row(*lst, sep=self.sep))

    def update_row(self, ind, lst):
        if ind is None:
            return
        self.table[ind] = self.row(*lst, sep=self.sep)

    def delete_row(self, ind):
        self.table.pop(ind)


class Menu:
    def __init__(self):
        sep = self.__choise_sep()
        print(f'В качестве разделителя будет использоваться символ - {sep}.\n')
        self.table = Table(sep)
        self.menu = ['Для создания записи в таблицу нажмите - 1.',
                     'Для вывода таблицы на экран нажмите - 2.',
                     'Для обновления данных нажмите - 3.',
                     'Для удаление данных нажмите - 4',
                     'Для импорта данных из файла нажмите - 5',
                     'Для экспорта данных в файл csv нажмите - 6',
                     'Для выхода из программы нажмите - Q.']
        self.action = {'1': (self.table.add_row, (self.__get_data_from_user,)),
                       '2': (self.table.show_table, None),
                       '3': (self.table.update_row, (self.__find_sur_name, self.__get_data_from_user)),
                       '4': (self.table.delete_row, (self.__find_sur_name,)),
                       '5': (self.__import_data_to_table, None),
                       '6': (self.__export_data_to_file, None)
                       }
    
    def main(self):
        while True:
            print(*self.menu, sep='\n')
            user_choice = self.__user_choice()
            if not user_choice:
                break
            if user_choice is True:
                continue
            if self.action[user_choice][1]:
                flag = True
                res = []
                for i in self.action[user_choice][1]:
                    res.append(i())
                    if res[-1] is None:
                        flag = False
                        break
                if flag:
                    self.action[user_choice][0](*res)
            else:
                self.action[user_choice][0]()
            print('\nПродолжаем работать...\n')

    def __choise_sep(self):
        while True:
            sep = input('Введите символ, который будет разделителем в таблице: ')
            if len(sep) != 1:
                print('Необходимо ввести только один символ!')
                continue
            break
        return sep

    def __user_choice(self):
        while True:
            answer = input('Сделайте выбор: ').lower()
            if answer.lower() == 'q':
                res = self.__are_you_sure()
                return res
            if answer not in map(str, range(1, len(self.menu))):
                print('Введено не корректное значение. Попробуйте еще раз. -')
                continue
            return answer

    def __are_you_sure(self):
        print('При выходе из программы, несохраненные данные будут удалены!')
        while True:
            answer = input('Если уверены в своем решении - нажмите "y", иначе - "n": ').lower()
            if answer not in ('y', 'n'):
                print('Введено не корректное значение. Попробуйте еще раз.')
                continue
            return not answer == 'y'

    def __get_data_from_user(self) -> list:
        res = [input(f'Введите значение для колонки <{self.table.translater[i] if i in self.table.translater else i}>: ') for i in self.table.row.lst]
        return res

    def __find_sur_name(self):
        search = input('Введите фамилию (или ее часть) для поиска данных: ')
        for ind, obj in enumerate(self.table.table):
            if search in obj.sur_name:
                print(f'В строке №{ind + 1} было надено следующее значение - {str(obj)}')
                while True:
                    answer = input('Продолжить работу с данной строкой? (y/n): ').lower()
                    if answer not in ('y', 'n'):
                        print('Введено не корректное значение. Попробуйте еще раз.')
                        continue
                    if answer == 'y':
                        return ind
                    break
        print('Значение не было найдено.')
        return None
    
    def __import_data_to_table(self):
        file = input('Введите полное название файл (включая расширение): ')
        sep_file = input('Укажите какой разделитель используется в файле: ')
        data = None
        try:
            with open(file, 'r', encoding='utf-8') as f:
                data = [i[:-1] if i[-1] == '\n' else i for i in f.readlines()]
        except FileNotFoundError:
            print(f'\nФайл с названием "{file}" не найден.')
            return
        for i in data:
            self.table.add_row(i.split(sep_file))
    
    def __export_data_to_file(self):
        file = input('Введите название файл (без расширения): ') + '.csv'
        sep_file = input('Укажите какой разделитель вы хотите использовать: ')
        data = None
        with open(file, 'w', encoding='utf-8') as f:
            for i in self.table.table:
                f.write(sep_file.join(str(i).split(self.table.sep)) + '\n')

app = Menu()
app.main()

