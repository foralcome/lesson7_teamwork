from datetime import datetime as dt


def operation_logger(val_1, op_type, val_2, res):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};{};{};{}; = ;{}'.format(time, val_1, op_type, val_2, res))
