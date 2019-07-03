import cv2
import numpy as np

from Vision import Vision
from Controller import Controller
from Game import Game


vision = Vision()
controller = Controller()
game = Game(vision, controller)

s = game.can_start_round()
game.click_object("arrow")
controller.move_mouse()
controller.left_mouse_click()