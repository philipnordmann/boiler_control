import random, time

current_temp = 20
new_temp = current_temp

def get_current_temp():
    global current_temp
    time.sleep(random.randint(0,1))
    #print("temps: {}/{}".format(current_temp, new_temp))
    if (current_temp < new_temp):
        current_temp = random.randint(current_temp, new_temp)
    else:
        current_temp = random.randint(new_temp, current_temp)
    return current_temp

def increase_temp(amount):
    global new_temp
    new_temp += amount
    return new_temp

def decrease_temp(amount):
    global new_temp
    new_temp -= amount
    return new_temp