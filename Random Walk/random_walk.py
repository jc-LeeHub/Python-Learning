from random import choice

class RandomWalk():

    def __init__(self, num_points=5000):
        self.num_points = num_points

        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):

        while len(self.x_values) < self.num_points:
            x_direction = choice([1, -1])
            x_distance = choice([0,1,2,3,4])
            #随机运动的方向及距离
            x_step = x_distance * x_direction

            y_direction = choice([1, -1])
            y_distance = choice([0,1,2,3,4])
            #随机运动的方向及距离
            y_step = y_distance * y_direction

            #拒绝原地不动
            if x_step==0 and y_step==0:
                continue

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
            

