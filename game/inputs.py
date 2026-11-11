from game.validations import is_not_empty,is_in_range_1_10
def get_name(msg):
    while True:
        name = input(f"{msg}:").strip()
        if is_not_empty(name) == False:
            continue
        return name

def get_num(msg):
    while True:
        try:
            num = int(input(f"{msg}:").strip())
            if is_in_range_1_10(num) == False:
                print("just between 1-10")
                continue
            return num
        except ValueError as error:
            print(f"{error},try again!!")
