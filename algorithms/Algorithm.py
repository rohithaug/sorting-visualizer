import random, time

class Algorithm():
    def __init__(self, name):
        self.name = name

    def update(self, swap_index_1=None, swap_index_2=None, pivot=None):
        from visualizer import update_screen
        update_screen(self, swap_index_1, swap_index_2, pivot)

    def start(self, length):
        self.array = random.sample(range(10, length-10), length//4)

        from visualizer import fixed_update_screen
        fixed_update_screen(self, "Start")
        time.sleep(1.5)
        #Implement the algorithm
        self.algorithm()
        fixed_update_screen(self, "End")
        time.sleep(1)
