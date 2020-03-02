import numpy as np
from data_postprocess import *
from expplots import *
import argparse

def main():
    # get folders names
    parser = argparse.ArgumentParser(prog='PyCLES')
    parser.add_argument("expfolder")
    parser.add_argument("expname")
    args = parser.parse_args()

    lespath = '/export/data1/jiahe/LESdata/'+args.expfolder
    lesobj = lesdata(lespath,args.expname)

    plotobj = lesplots(lesobj)

    plotobj.plot_profile('thetali_mean',args.t1,args.t2)

    plotobj.plot_profile('updraft_fraction',args.t1,args.t2)
    plotobj.plot_profile('updraft_w',args.t1,args.t2)
    plotobj.plot_profile('updraft_b',args.t1,args.t2)
    plotobj.plot_profile('updraft_thetali',args.t1,args.t2)
    plotobj.plot_profile('updraft_ddz_p_alpha',args.t1,args.t2)

    plotobj.plot_tz('updraft_fraction')
    plotobj.plot_tz('updraft_w')
    plotobj.plot_tz('updraft_b')

    return

if __name__ == '__main__':
    main()
