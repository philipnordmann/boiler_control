from multiprocessing import Process
import configparser
from control_temp import TempController
from control_water import WaterController

jobs = list()

def start_temp_controller(input):
    tc = TempController(**input)
    p = Process(target=tc.run)
    p.start()
    jobs.append(p)

def start_water_controller(input):
    wc = WaterController(**input)
    p = Process(target=wc.run)
    p.start()
    jobs.append(p)


def main():

    config = configparser.ConfigParser()
    config.read('settings.ini')

    water = { 'min': int(config['water']['min']), 'max': int(config['water']['max']) }
    temp = { 'min': int(config['temp']['min']), 'max': int(config['temp']['max']) }

    start_temp_controller(temp)
    #start_water_controller(water)

    print("Started...")

    for j in jobs:
        j.join()

    print("finishing")


if __name__ == '__main__':
    main()
    