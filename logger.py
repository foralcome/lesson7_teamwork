from datetime import datetime as dt


def operation_logger(data_typ: str, op_type: str, inp_data: list, res: int):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};data type;{};operation type;{};input data;{};result;{}'
                   .format(time, data_typ, op_type, inp_data, res))
