from datetime import datetime as dt


def operation_logger(data_typ, op_type, inp_data, res):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};data type;{};operation type;{};input data;{};result;{}'
                   .format(time, data_typ, op_type, inp_data, res))
