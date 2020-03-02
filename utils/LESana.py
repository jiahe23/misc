import numpy as np
from data_postprocess import *
from expplots import *
import matplotlib.pyplot as plt

import argparse

def main():
    # get folders names
    parser = argparse.ArgumentParser(prog='PyCLES')
    parser.add_argument("expfolder")
    parser.add_argument("expname")
    parser.add_argument("t1")
    parser.add_argument("t2")
    args = parser.parse_args()

    t1 = np.float(args.t1)
    t2 = np.float(args.t2)

    # lespath = '/export/data1/jiahe/LESdata/'+args.expfolder
    lespath = '/Users/jiahe/Documents/pycles_data/'+args.expfolder
    lesobj = lesdata(lespath,args.expname)

    plotobj = lesplots(lesobj)

    plotobj.plot_profile('thetali_mean',t1,t2)
    plotobj.plot_profile('updraft_fraction',t1,t2)
    plotobj.plot_profile('updraft_w',t1,t2)
    plotobj.plot_profile('updraft_b',t1,t2)
    plotobj.plot_profile('updraft_thetali',t1,t2)
    plotobj.plot_profile('updraft_ddz_p_alpha',t1,t2)

    plotobj.plot_tz('updraft_fraction')
    plotobj.plot_tz('updraft_w')
    plotobj.plot_tz('updraft_b')

    plt.show()

    return

if __name__ == '__main__':
    main()
