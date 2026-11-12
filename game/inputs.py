from game.validations import is_not_empty,is_in_range
def get_name(msg):
    status_run = True
    while status_run:
        name = input(f"{msg}:").strip()
        if is_not_empty(name) == False:
            continue
        status_run = False
        return name

def get_num(msg,max_num):
    status_run = True
    while status_run:
        try:
            num = int(input(f"{msg}:").strip())
            if is_in_range(num,max_num) == False:
                print("just between the range")
                continue
            status_run = False
            return num
        except ValueError as error:
            print(f"{error},try again!!")
