from multiprocessing import Process
import configparser
from control_temp import TempController
from control_water import WaterController
import logging

jobs = list()

log_level_dict = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warn': logging.WARN,
    'error': logging.ERROR
}

def start_temp_controller(input):
    tc = TempController(**input)
    p = Process(target=tc.start)
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



    #water = { 'min': int(config['water']['min']), 'max': int(config['water']['max']) }
    temp = {
        'target': float(config['temp']['target']),
        'change_amount': float(config['temp']['change_amount']),
        'wait_time': float(config['temp']['wait_time']),
        'avg_measures': int(config['temp']['loop_count'])
    }
    
    log_str = config['logging']['level']
    log_format = r'%(asctime)s %(levelname)s %(process)d %(processName)s %(message)s'

    if log_str.lower() in log_level_dict.keys():
        logging.basicConfig(level=log_level_dict[log_str.lower()], format=log_format)
    else:
        logging.basicConfig(level=logging.INFO, format=log_format)
        logging.warn("Log level {} not found. Continuing with info".format(log_str))

    start_temp_controller(temp)
    #start_water_controller(water)

    logging.info("Starting...")
    try:
        for j in jobs:
            j.join()
    except KeyboardInterrupt:
        print("finishing")


if __name__ == '__main__':
    main()
