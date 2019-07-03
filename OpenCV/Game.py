import numpy as np
import time


class Game:

    def __init__(self, vision, controller):
        self.vision = vision
        self.controller = controller
        self.state = 'not started'

    def can_see_object(self, template, threshold=0.9):
        matches = self.vision.find_template(template, threshold=threshold)
        return np.shape(matches)[1] >= 1

    def click_object(self, template, offset=(0, 0)):
        matches = self.vision.find_template(template)

        x = matches[1][0] + offset[0]
        y = matches[0][0] + offset[1]

        self.controller.move_mouse(x, y)
        self.controller.left_mouse_click()

        time.sleep(0.5)

    def can_start_round(self):
        return self.can_see_object('arrow')

    def launch_player(self):
        # Try multiple sizes of goalpost due to perspective changes for
        # different opponents
        scales = [1.2, 1.1, 1.05, 1.04, 1.03, 1.02, 1.01, 1.0, 0.99, 0.98, 0.97, 0.96, 0.95]
        matches = self.vision.scaled_find_template('arrow')
        x = matches[1][0]
        y = matches[0][0]

        self.controller.left_mouse_click(
            x,y
        )

        time.sleep(0.5)
