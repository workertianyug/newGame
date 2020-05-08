import numpy as np
import tensorflow as tf
import gym
import time
# from spinup.algos.tf1.sac import core

import algo_mameta.core as core
from spinup.algos.tf1.sac.core import get_vars
from spinup.utils.logx import EpochLogger

import envs

# note: currently can only use v1
# from abstractGameLP.createGraph import *

# must be in the same directory




class DefHard():

    def __init__(self, env_fn):

        env = env_fn()

       self.direcMatrix = np.zeros((10,10,2))


       self.direcMatrix[5][5] = [0, -20]
       self.direcMatrix[4][5] = [-20, 0]
       self.direcMatrix[4][4] = [0, -20]
       self.direcMatrix[4][3] = [0, -20]
       self.direcMatrix[4][2] = [20, 0]
       self.direcMatrix[3][2] = [0, 20]
       self.direcMatrix[3][3] = [0, -20]
       self.direcMatrix[2][3] = [20, 0]
       self.direcMatrix[2][4] = [0, 20]
       self.direcMatrix[1][4] = [0, 20]
       self.direcMatrix[1][5] = [0, 20]
       # self.direcMatrix[1][6] = 

       

    def reset(self):
    	pass

    def set_session(self, sess):
        pass


    def act(self, o, t, deterministic=False):

        curX = o[0]
        curY = o[1]

        r = curY // 50
        c = curX // 50

    	return self.direcMatrix[r][c]
        
        
    def train(self, o, a, r, o2, d, t, oa):
        pass










