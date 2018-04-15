# coding=utf-8

import sys
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import mlab

def get_detection_evals_from(caffe_log):
    evals = [0.0]
    with open(caffe_log, 'r') as file:
        for line in file:
            if 'Test net output #0: detection_eval =' in line:
                detection_eval = line.split('=')[-1].strip()
                evals.append(detection_eval)
    return evals; 

def make_plot(X, Y, plot_name):
    plt.plot(X, Y, 'ro-')
    plt.show()
    plt.savefig(plot_name)

caffe_log_path = sys.argv[1]
evals = get_detection_eval_from(caffe_log_path)

lower_bound = 0
upper_bound = 120000
step = 10000

iterations = [i for i in range(lower_bound, upper_bound + step, step)]

make_plot(iterations, evals, 'eval-graph.png')
