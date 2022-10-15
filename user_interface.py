def load_menu_main():
    menu = {0: 'exit'}
    menu[1] = 'Рациональные числами'
    menu[2] = 'Комплексные числами'
    return menu


def load_menu_operation():
    menu = {}
    menu[1] = 'Сложение (sum)'
    menu[2] = 'Вычитание (sub)'
    menu[3] = 'Умножение (mul)'
    menu[4] = 'Деление (div)'
    menu[5] = 'Возведение в степень (pow)'
    menu[6] = 'Вычисление корня сисла (sqrt)'
    menu[7] = 'назад в основное меню'
    return menu


def print_menu(menu_title, menu_data):
    print(f'----- {menu_title} -----')

    for key_menu, title_menu in menu_data.items():
        print(key_menu, '-', title_menu)


def get_select_menu(menu):
    select = int(input('выберите пункт меню: '))
    while select not in menu.keys():
        print('error - указан неверный пункт меню!')
        select = int(input('выберите пункт меню: '))
    return select


def input_rational_number(postfix=''):
    number_str = input(f'Введите значение рационального числа {postfix}:')
    while not number_str.isdigit():
        print('введённая строка должна быть числом!')
        number_str = input(f'Введите значение рационального числа {postfix}:')
    return int(number_str)

def print_rational_number(value, prefix=''):
    print(f'{prefix}: {value}')

def input_complex_number(postfix=''):
    print('Комплексное число имеет вид A+Bi, где A и B – действительные числа, i – так называемая мнимая единица')

    numberA_str = input(f'Введите значение A (действительная часть) комплексного числа {postfix}:')
    while not numberA_str.replace('-', '').replace('.', '').isdecimal():
        print('введённая строка должна быть числом!')
        numberA_str = input(f'Введите значение A (действительная часть) комплексного числа {postfix}:')

    numberB_str = input(f'Введите значение B (мнимая часть) комплексного числа {postfix}:')
    while not numberA_str.replace('-', '').replace('.', '').isdigit():
        print('введённая строка должна быть числом!')
        numberB_str = input(f'Введите значение B (мнимая часть) комплексного числа {postfix}:')

    return complex(float(numberA_str), float(numberB_str))

def print_complex_number(value, prefix=''):
    print(f'{prefix}: {value}')