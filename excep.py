def check_inp_data(val: str):
    if val.replace('-', '').isdigit():
        return int(val)
    elif val.replace('-', '').replace('.', '').isdigit():
        return float(val)
    else:
        print(f"Error, {val} is not an appropriate argument! Pleas try again.")

