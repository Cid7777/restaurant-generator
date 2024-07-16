import random

def gen_restaurant_list():
    rest_dir = "./restaurants/"
    f = str(input("List the city:\n").lower() + "_rest.txt")

    with open(rest_dir + f, "r") as file:
        line_list = file.readlines()
        rest_list = [item.rstrip() for item in line_list]
        file.close()
    return rest_list

def get_restaurant(list):

    rand_num = random.randint(0, len(list)-1)
    return f"The restaurant we'll be going to is: {list[rand_num]}"


