import random as r
import math
#import MockSensor as sensor
import temp_sensor as sensor

class TempController(object):
    
    def __init__(self, min, max):
        self.current_temp = 0
        self.min = min
        self.max = max
        self.last_temp = None
        self.minimum_change = 5
        self.gas_flow_change_amount = 5
        print(min, max)

    def read(self):
        temp = sensor.get_current_temp()   
        return temp

    def decrease_gas_flow(self, amount):
        print("decreasing gas flow {}".format(amount))

    def increase_gas_flow(self, amount):
        print("increasing gas flow {}".format(amount))

    def control(self):
        current_temp = self.read()
        
        if self.last_temp == None:
            self.last_temp = current_temp
        
        if abs(current_temp - self.last_temp) >= self.minimum_change:
            if current_temp > self.last_temp:
                self.decrease_gas_flow(self.gas_flow_change_amount)
            else:
                self.increase_gas_flow(self.gas_flow_change_amount)
        else:
            print("done nothing")
    
    def run(self):
        try:
            while True:
                self.control()
        except KeyboardInterrupt:
            print("keyboard")
            pass