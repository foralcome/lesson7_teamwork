def check_inp_data(val: str):
    if val.isdigit() or val[0] == '-' and val[1:].isdigit() \
            or val[0].isdigit() and val[1] == '.' and val[2:].isdigit() \
            or val[0] == '-' and val[1].isdigit() and val[2] == '.' and val[3:].isdigit():
        return val
    else:
        print(f"Error, {val} is not an appropriate argument! Pleas try again.")

