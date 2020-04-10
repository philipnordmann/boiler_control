import random as r

class WaterController(object):

    def __init__(self, min, max):
        self.current_temp = 0
        self.count = 0
        self.min = min
        self.max = max

    def read(self, input):
        self.current_temp = input
        print("read stuff {}".format(input))

    def control(self):
        if self.current_temp >= 10:
            self.count += 1
            print("down with the water")
        else:
            print("do nothing")
    
    def run(self):
        try:
            while self.count <= 20:
                self.read(r.randint(self.min, self.max))
                self.control()
        except KeyboardInterrupt:
            print("keyboard")
            pass