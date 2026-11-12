from game.validations import is_not_empty,is_in_range
def get_name(msg):
    while True:
        name = input(f"{msg}:").strip()
        if is_not_empty(name) == False:
            continue
        return name

def get_num(msg,max_num):
    while True:
        try:
            num = int(input(f"{msg}:").strip())
            if is_in_range(num,max_num) == False:
                print("just between the range")
                continue
            return num
        except ValueError as error:
            print(f"{error},try again!!")
