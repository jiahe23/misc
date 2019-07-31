import numpy as np
import netCDF4 as nc

import matplotlib.pyplot as plt
import seaborn as sns
import argparse

def main():
    # get exp name from input
    parser = argparse.ArgumentParser(prog='pycles')
    parser.add_argument('expname')
    args = parser.parse_args()

    path = '/export/data1/jiahe/LESdata/'+args.expname
    stat = nc.Dataset(path+'/stats/Stats.'+args.expname.split('.')[1]+'.nc')

    z_half = stat.groups['reference'].variables['z'][:].data
    z_full = stat.groups['reference'].variables['z_full'][:].data
    t = stat.groups['timeseries'].variables['t'][:].data/3600.0
    s_prof = stat.groups['profiles']

    # last time step
    plt.close('all')
    fig, ax = plt.subplots(2,4, figsize=(32,16))

    ax[0,0].plot(s_prof.variables['ql_mean'][-1,:], z_half, 'k', lw=2)
    ax[0,0].set_title('<ql>')

    ax[0,1].plot(s_prof.variables['qt_mean'][-1,:], z_half, 'k', lw=2)
    ax[0,1].set_title('<qt>')

    ax[0,2].plot(s_prof.variables['thetali_mean'][-1,:], z_half, 'k', lw=2)
    ax[0,2].set_title('<thetali>')

    ax[0,3].plot(s_prof.variables['tke_mean'][-1,:], z_half, 'k', lw=2)
    ax[0,3].set_title('<tke>')

    ax[1,0].plot(s_prof.variables['updraft_fraction'][-1,:], z_half, 'k', lw=2)
    ax[1,0].set_title('a_upd')

    ax[1,1].plot(s_prof.variables['updraft_w'][-1,:], z_half, 'k', lw=2)
    ax[1,1].set_title('w_upd')

    ax[1,2].plot(s_prof.variables['updraft_b'][-1,:]-s_prof.variables['buoyancy_mean'][-1,:]*(s_prof.variables['updraft_fraction'][-1,:]!=0), z_half, 'k', lw=2)
    ax[1,2].set_title('b_upd')

    ax[1,3].plot(s_prof.variables['updraft_ql'][-1,:], z_half, 'k', lw=2)
    ax[1,3].set_title('ql_upd')

    plt.savefig(path+'/Visualization/sanitycheck_laststep.pdf')
    plt.close('all')

    # time series
    fig, ax = plt.subplots(2,3, figsize=(24,16))

    tdata = s_prof.variables['updraft_fraction'][:].data.transpose()
    C = ax[0,0].contourf(t,z_half, tdata, vmin=-abs(tdata).max(), vmax=abs(tdata).max(), cmap='RdBu_r')
    plt.colorbar(C,ax=ax[0,0])
    ax[0,0].set_title('a_upd')

    tdata = s_prof.variables['updraft_w'][:].data.transpose()
    C = ax[0,1].contourf(t,z_half, tdata, vmin=-abs(tdata).max(), vmax=abs(tdata).max(), cmap='RdBu_r')
    plt.colorbar(C,ax=ax[0,1])
    ax[0,1].set_title('w_upd')

    tdata = s_prof.variables['updraft_ql'][:].data.transpose()
    C = ax[0,2].contourf(t,z_half, tdata, vmin=-abs(tdata).max(), vmax=abs(tdata).max(), cmap='RdBu_r')
    plt.colorbar(C,ax=ax[0,2])
    ax[0,2].set_title('ql_upd')

    tdata = (s_prof.variables['updraft_b'][:].data-s_prof.variables['buoyancy_mean'][:].data*(s_prof.variables['updraft_fraction'][:].data!=0)).transpose()
    C = ax[1,0].contourf(t,z_half, tdata, vmin=-abs(tdata).max(), vmax=abs(tdata).max(), cmap='RdBu_r')
    plt.colorbar(C,ax=ax[1,0])
    ax[1,0].set_title('b_upd')

    tdata = s_prof.variables['updraft_dyn_pressure'][:].data.transpose()
    C = ax[1,1].contourf(t,z_half, tdata, vmin=-abs(tdata).max(), vmax=abs(tdata).max(), cmap='RdBu_r')
    plt.colorbar(C,ax=ax[1,1])
    ax[1,1].set_title('p_upd')

    plt.savefig(path+'/Visualization/sanitycheck_timeseries.pdf')
    plt.close('all')

if __name__ == '__main__':
    main()
