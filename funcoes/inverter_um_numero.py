num = '12345'

def inverter(num: str):
    num = num[::-1]
    return num


if __name__ == '__main__':

    print(inverter(num))