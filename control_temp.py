import random as r
import logging
import MockConSen as sensor
import MockConSen as controler
import time
from statistics import mean
#import RaspberrySensor as sensor
#import RaspberryControler as controler


class TempController(object):
    
    def __init__(self, target, change_amount, wait_time, avg_measures):
        self.current_temp = 0
        self.target_temp = target
        self.last_temp = None
        self.gas_flow_change_amount = change_amount

        self.wait_time = wait_time
        self.avg_measures = avg_measures

        logging.debug("Current configuration of TempController: target temp: {}, \
            gas flow change amount: {}, wait time between measures: {}, times to read: {}"
            .format(target, change_amount, wait_time, avg_measures))

    def read(self):
        temp_list = list()
        for i in range(0, self.avg_measures):
            temp_list.append(sensor.get_current_temp())
            time.sleep(self.wait_time)
        return mean(temp_list)

    def decrease_gas_flow(self, amount):
        logging.debug("decreasing gas flow by {}".format(amount))
        controler.decrease_temp(amount)

    def increase_gas_flow(self, amount):
        logging.debug("increasing gas flow by {}".format(amount))
        controler.increase_temp(amount)

    def control(self):
        current_temp = self.read()
        
        if self.last_temp is None:
            self.last_temp = current_temp
        
        if current_temp > self.target_temp:
            self.decrease_gas_flow(self.gas_flow_change_amount)
        else:
            self.increase_gas_flow(self.gas_flow_change_amount)

    def start(self):
        try:
            logging.info("start controlling the gas flow by temp...")
            while True:
                self.control()
        except KeyboardInterrupt:
            pass
