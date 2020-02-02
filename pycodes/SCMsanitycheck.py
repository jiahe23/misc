import numpy as np
import netCDF4 as nc
import os
import matplotlib.pyplot as plt
import seaborn as sns
import argparse

sns.set()

def main():
    # get exp name from input
    parser = argparse.ArgumentParser(prog='pycles')
    parser.add_argument('platform')
    parser.add_argument('scm_expname')
    parser.add_argument('les_expname')
    args = parser.parse_args()

    if args.platform == 'server':
        path = '/export/data1/jiahe/SCAMPydata/'+args.scm_expname
        try:
            lespath = '/export/data1/jiahe/LESdata/'+args.les_expname
            les_flag = True
        except:
            les_flag = False
            print ('not LES results; only SCM plotted')
    elif args.platform == 'imac':
        path = '/Users/jiahe/Documents/scampy_data/'+args.scm_expname
        if os.path.exists('/Users/jiahe/Documents/pycles_data/'+args.les_expname):
            lespath = '/Users/jiahe/Documents/pycles_data/'+args.les_expname
            les_flag = True
        else:
            les_flag = False
            print ('no LES results; only SCM plotted')
        if os.path.exists('/Users/jiahe/Documents/scampy_data/Output.Bomex.masters_exp/Output.Bomex.clima-master.buoyancy_sorting/'):
            tanpath = '/Users/jiahe/Documents/scampy_data/Output.Bomex.masters_exp/Output.Bomex.clima-master.buoyancy_sorting/'
            tan_flag = True
        else:
            tan_flag = False
            print ('no old scm results')
    else:
        exit('platform must be "server" or "imac"')

    if not os.path.exists(path+'/Visualization/'):
        os.mkdir(path+'/Visualization/')

    stat = nc.Dataset(path+'/stats/Stats.'+args.scm_expname.split('.')[1]+'.nc')

    z_half = stat.groups['reference'].variables['z_half'][:].data
    z_full = stat.groups['reference'].variables['z'][:].data
    t = stat.groups['timeseries'].variables['t'][:].data/3600.0
    s_prof = stat.groups['profiles']

    if les_flag:
        les_stat = nc.Dataset(lespath+'/stats/Stats.'+args.les_expname.split('.')[1]+'.nc')
        les_z = les_stat.groups['reference'].variables['z_half'][:].data
        les_prof = les_stat.groups['profiles']
    if tan_flag:
        tan_stat = nc.Dataset(tanpath+'/stats/Stats.'+args.les_expname.split('.')[1]+'.nc')
        tan_z = tan_stat.groups['reference'].variables['z_half'][:].data
        tan_prof = tan_stat.groups['profiles']

    # plot last time step
    plt.close('all')
    fig, ax = plt.subplots(2,4, figsize=(32,16))

    ax[0,0].plot(s_prof.variables['qt_mean'][-1,:], z_half, 'b', lw=2)
    if les_flag:
        ax[0,0].plot(les_prof.variables['qt_mean'][-1,:], les_z, 'k', lw=2)
        # ax[0,0].legend(['SCM','LES'])
    if tan_flag:
        ax[0,0].plot(tan_prof.variables['qt_mean'][-1,:], tan_z, 'r', lw=2)
    ax[0,0].set_title('<qt>')

    ax[0,1].plot(s_prof.variables['ql_mean'][-1,:], z_half, 'b', lw=2)
    if les_flag:
        ax[0,1].plot(les_prof.variables['ql_mean'][-1,:], les_z, 'k', lw=2)
        # ax[0,1].legend(['SCM','LES'])
    if tan_flag:
        ax[0,1].plot(tan_prof.variables['ql_mean'][-1,:], tan_z, 'r', lw=2)
    ax[0,1].set_title('<ql>')

    ax[0,2].plot(s_prof.variables['thetal_mean'][-1,:], z_half, 'b', lw=2)
    if les_flag:
        ax[0,2].plot(les_prof.variables['thetali_mean'][-1,:], les_z, 'k', lw=2)
        # ax[0,2].legend(['SCM','LES'])
    if tan_flag:
        ax[0,2].plot(tan_prof.variables['thetal_mean'][-1,:], tan_z, 'r', lw=2)
    ax[0,2].set_title('<theta_l>')

    ax[0,3].plot(s_prof.variables['tke_mean'][-1,:], z_half, 'b', lw=2)
    if les_flag:
        ax[0,3].plot(les_prof.variables['tke_mean'][-1,:], les_z, 'k', lw=2)
        # ax[0,3].legend(['SCM','LES'])
    if tan_flag:
        ax[0,3].plot(tan_prof.variables['tke_mean'][-1,:], tan_z, 'r', lw=2)
    ax[0,3].set_title('<tke>')

    ax[1,0].plot(s_prof.variables['updraft_area'][-1,:], z_half, 'b', lw=2)
    if les_flag:
        ax[1,0].plot(les_prof.variables['updraft_fraction'][-1,:], les_z, 'k', lw=2)
        # ax[1,0].legend(['SCM','LES'])
    if tan_flag:
        ax[1,0].plot(tan_prof.variables['updraft_area'][-1,:], tan_z, 'r', lw=2)
    ax[1,0].set_title('a_upd')

    ax[1,1].plot(s_prof.variables['updraft_w'][-1,:], z_half, 'b', lw=2)
    if les_flag:
        ax[1,1].plot(les_prof.variables['updraft_w'][-1,:], les_z, 'k', lw=2)
        # ax[1,1].legend(['SCM','LES'])
    if tan_flag:
        ax[1,1].plot(tan_prof.variables['updraft_w'][-1,:], tan_z, 'r', lw=2)
    ax[1,1].set_title('w_upd')

    ax[1,2].plot(s_prof.variables['massflux'][-1,:], z_half, 'b', lw=2)
    # if les_flag:
    #     ax[1,2].plot(les_prof.variables['massflux'][-1,:], les_z, 'k', lw=2)
    #     ax[1,2].legend(['SCM','LES'])
    ax[1,2].set_title('mass flux')

    ax[1,3].plot(s_prof.variables['updraft_ql'][-1,:], z_half, 'b', lw=2)
    if les_flag:
        ax[1,3].plot(les_prof.variables['updraft_ql'][-1,:], les_z, 'k', lw=2)
        # ax[1,3].legend(['SCM','LES'])
    if tan_flag:
        ax[1,3].plot(tan_prof.variables['updraft_ql'][-1,:], tan_z, 'r', lw=2)
    ax[1,3].set_title('ql_upd')

    plt.savefig(path+'/Visualization/sanitycheck_laststep.pdf')
    plt.close('all')

    # average over last hour
    plt.close('all')
    fig, ax = plt.subplots(2,4, figsize=(32,16))

    ax[0,0].plot(s_prof.variables['qt_mean'][-1:-61:-1,:].mean(axis=0), z_half, 'b', lw=2)
    if les_flag:
        ax[0,0].plot(les_prof.variables['qt_mean'][-1:-61:-1,:].mean(axis=0), les_z, 'k', lw=2)
        # ax[0,0].legend(['SCM','LES'])
    if tan_flag:
        ax[0,0].plot(tan_prof.variables['qt_mean'][-1:-61:-1,:].mean(axis=0), tan_z, 'r', lw=2)
    ax[0,0].set_title('<qt>')

    ax[0,1].plot(s_prof.variables['ql_mean'][-1:-61:-1,:].mean(axis=0), z_half, 'b', lw=2)
    if les_flag:
        ax[0,1].plot(les_prof.variables['ql_mean'][-1:-61:-1,:].mean(axis=0), les_z, 'k', lw=2)
        # ax[0,1].legend(['SCM','LES'])
    if tan_flag:
        ax[0,1].plot(tan_prof.variables['ql_mean'][-1:-61:-1,:].mean(axis=0), tan_z, 'r', lw=2)
    ax[0,1].set_title('<ql>')

    ax[0,2].plot(s_prof.variables['thetal_mean'][-1:-61:-1,:].mean(axis=0), z_half, 'b', lw=2)
    if les_flag:
        ax[0,2].plot(les_prof.variables['thetali_mean'][-1:-61:-1,:].mean(axis=0), les_z, 'k', lw=2)
        # ax[0,2].legend(['SCM','LES'])
    if tan_flag:
        ax[0,2].plot(tan_prof.variables['thetal_mean'][-1:-61:-1,:].mean(axis=0), tan_z, 'r', lw=2)
    ax[0,2].set_title('<theta_l>')

    ax[0,3].plot(s_prof.variables['tke_mean'][-1:-61:-1,:].mean(axis=0), z_half, 'b', lw=2)
    if les_flag:
        ax[0,3].plot(les_prof.variables['tke_mean'][-1:-61:-1,:].mean(axis=0), les_z, 'k', lw=2)
        # ax[0,3].legend(['SCM','LES'])
    if tan_flag:
        ax[0,3].plot(tan_prof.variables['tke_mean'][-1:-61:-1,:].mean(axis=0), tan_z, 'r', lw=2)
    ax[0,3].set_title('<tke>')

    ax[1,0].plot(s_prof.variables['updraft_area'][-1:-61:-1,:].mean(axis=0), z_half, 'b', lw=2)
    if les_flag:
        ax[1,0].plot(les_prof.variables['updraft_fraction'][-1:-61:-1,:].mean(axis=0), les_z, 'k', lw=2)
        # ax[1,0].legend(['SCM','LES'])
    if tan_flag:
        ax[1,0].plot(tan_prof.variables['updraft_area'][-1:-61:-1,:].mean(axis=0), tan_z, 'r', lw=2)
    ax[1,0].set_title('a_upd')

    ax[1,1].plot(s_prof.variables['updraft_w'][-1:-61:-1,:].mean(axis=0), z_half, 'b', lw=2)
    if les_flag:
        ax[1,1].plot(les_prof.variables['updraft_w'][-1:-61:-1,:].mean(axis=0), les_z, 'k', lw=2)
        # ax[1,1].legend(['SCM','LES'])
    if tan_flag:
        ax[1,1].plot(tan_prof.variables['updraft_w'][-1:-61:-1,:].mean(axis=0), tan_z, 'r', lw=2)
    ax[1,1].set_title('w_upd')

    ax[1,2].plot(s_prof.variables['massflux'][-1:-61:-1,:].mean(axis=0), z_half, 'b', lw=2)
    # if les_flag:
    #     ax[1,2].plot(les_prof.variables['massflux'][-1,:], les_z, 'k', lw=2)
    #     ax[1,2].legend(['SCM','LES'])
    ax[1,2].set_title('mass flux')

    ax[1,3].plot(s_prof.variables['updraft_ql'][-1:-61:-1,:].mean(axis=0), z_half, 'b', lw=2)
    if les_flag:
        ax[1,3].plot(les_prof.variables['updraft_ql'][-1:-61:-1,:].mean(axis=0), les_z, 'k', lw=2)
        # ax[1,3].legend(['SCM','LES'])
    if tan_flag:
        ax[1,3].plot(tan_prof.variables['updraft_ql'][-1:-61:-1,:].mean(axis=0), tan_z, 'r', lw=2)
    ax[1,3].set_title('ql_upd')

    plt.savefig(path+'/Visualization/sanitycheck_lasthour.pdf')
    plt.close('all')

    # plot time series
    fig, ax = plt.subplots(2,3, figsize=(24,16))

    tdata = s_prof.variables['updraft_area'][:].data.transpose()
    tdata[tdata>0.2] = np.nan
    C = ax[0,0].contourf(t,z_half, tdata, vmin=-0.2, vmax=0.2, cmap='RdBu_r')
    ax[0,0].contour(t,z_half, tdata, levels=[1e-5], colors='m')
    ax[0,0].contour(t,z_half, tdata, levels=[1e-4], colors='k')
    plt.colorbar(C,ax=ax[0,0])
    ax[0,0].set_title('a_upd')

    tdata = s_prof.variables['updraft_w'][:].data.transpose()
    tdata[tdata>10] = np.nan
    C = ax[0,1].contourf(t,z_half, tdata, vmin=-10.0, vmax=10.0, cmap='RdBu_r')
    # C = ax[0,1].contourf(t,z_half, tdata, vmin=-abs(tdata).max(), vmax=abs(tdata).max(), cmap='RdBu_r')
    plt.colorbar(C,ax=ax[0,1])
    ax[0,1].set_title('w_upd')
    # print tdata

    tdata = s_prof.variables['updraft_ql'][:].data.transpose()
    C = ax[0,2].contourf(t,z_half, tdata, vmin=-0.002, vmax=0.002, cmap='RdBu_r')
    # C = ax[0,2].contourf(t,z_half, tdata, vmin=-abs(tdata).max(), vmax=abs(tdata).max(), cmap='RdBu_r')
    plt.colorbar(C,ax=ax[0,2])
    ax[0,2].set_title('ql_upd')

    tdata = (s_prof.variables['updraft_buoyancy'][:].data).transpose()
    C = ax[1,0].contourf(t,z_half, tdata, vmin=-0.2, vmax=0.2, cmap='RdBu_r')
    # C = ax[1,0].contourf(t,z_half, tdata, vmin=-abs(tdata).max(), vmax=abs(tdata).max(), cmap='RdBu_r')
    plt.colorbar(C,ax=ax[1,0])
    ax[1,0].set_title('b_upd')

    try:
        tdata = s_prof.variables['nh_pressure'][:].data.transpose()
    except:
        tdata = s_prof.variables['nh_pressure_tan'][:].data.transpose()
    tdata[tdata>0.1] = np.nan
    C = ax[1,1].contourf(t,z_half, tdata, vmin=-0.001, vmax=0.001, cmap='RdBu_r')
    # C = ax[1,1].contourf(t,z_half, tdata, vmin=-abs(tdata).max(), vmax=abs(tdata).max(), cmap='RdBu_r')
    plt.colorbar(C,ax=ax[1,1])
    ax[1,1].set_title('-dpdz_upd')

    plt.savefig(path+'/Visualization/sanitycheck_timeseries.pdf')
    plt.close('all')


    # tidx = np.where(t==1)[0][0]
    tdata = s_prof.variables['nh_pressure'][:].data.transpose()
    tdata = tdata[:,-1:-61:-1].mean(axis=1)
    print tdata
    fig, ax = plt.subplots(1,1, figsize=(8,8))
    ax.plot(tdata, z_half, 'k')
    tdata = s_prof.variables['nh_pressure_b'][:].data.transpose()
    tdata = tdata[:,-1:-61:-1].mean(axis=1)
    print tdata
    ax.plot(tdata, z_half, 'b')
    tdata = s_prof.variables['nh_pressure_w1'][:].data.transpose()
    tdata = tdata[:,-1:-61:-1].mean(axis=1)
    ax.plot(tdata, z_half, 'r--')
    tdata = s_prof.variables['nh_pressure_w2'][:].data.transpose()
    tdata = tdata[:,-1:-61:-1].mean(axis=1)
    ax.plot(tdata, z_half, 'r:')

    plt.savefig(path+'/Visualization/pz_last1hr.pdf')
    plt.close('all')

    tdata = s_prof.variables['nh_pressure'][:].data.transpose()
    tdata = tdata[:,-61:-121:-1].mean(axis=1)
    print tdata
    fig, ax = plt.subplots(1,1, figsize=(8,8))
    ax.plot(tdata, z_half, 'k')
    tdata = s_prof.variables['nh_pressure_b'][:].data.transpose()
    tdata = tdata[:,-61:-121:-1].mean(axis=1)
    print tdata
    ax.plot(tdata, z_half, 'b')
    tdata = s_prof.variables['nh_pressure_w1'][:].data.transpose()
    tdata = tdata[:,-61:-121:-1].mean(axis=1)
    ax.plot(tdata, z_half, 'r--')
    tdata = s_prof.variables['nh_pressure_w2'][:].data.transpose()
    tdata = tdata[:,-61:-121:-1].mean(axis=1)
    ax.plot(tdata, z_half, 'r:')

    plt.savefig(path+'/Visualization/pz_last1-2hr.pdf')
    plt.close('all')

    tdata = s_prof.variables['nh_pressure'][:].data.transpose()
    tdata = tdata[:,-121:-181:-1].mean(axis=1)
    print tdata
    fig, ax = plt.subplots(1,1, figsize=(8,8))
    ax.plot(tdata, z_half, 'k')
    tdata = s_prof.variables['nh_pressure_b'][:].data.transpose()
    tdata = tdata[:,-121:-181:-1].mean(axis=1)
    print tdata
    ax.plot(tdata, z_half, 'b')
    tdata = s_prof.variables['nh_pressure_w1'][:].data.transpose()
    tdata = tdata[:,-121:-181:-1].mean(axis=1)
    ax.plot(tdata, z_half, 'r--')
    tdata = s_prof.variables['nh_pressure_w2'][:].data.transpose()
    tdata = tdata[:,-121:-181:-1].mean(axis=1)
    ax.plot(tdata, z_half, 'r:')

    plt.savefig(path+'/Visualization/pz_last2-3hr.pdf')
    plt.close('all')

    tdata = s_prof.variables['nh_pressure'][:].data.transpose()
    tdata = tdata[:,61:121].mean(axis=1)
    print tdata
    fig, ax = plt.subplots(1,1, figsize=(8,8))
    ax.plot(tdata, z_half, 'k')
    tdata = s_prof.variables['nh_pressure_b'][:].data.transpose()
    tdata = tdata[:,61:121].mean(axis=1)
    print tdata
    ax.plot(tdata, z_half, 'b')
    tdata = s_prof.variables['nh_pressure_w1'][:].data.transpose()
    tdata = tdata[:,61:121].mean(axis=1)
    ax.plot(tdata, z_half, 'r--')
    tdata = s_prof.variables['nh_pressure_w2'][:].data.transpose()
    tdata = tdata[:,61:121].mean(axis=1)
    ax.plot(tdata, z_half, 'r:')

    plt.savefig(path+'/Visualization/pz_first1-2hr.pdf')
    plt.close('all')

    tdata = s_prof.variables['nh_pressure'][:].data.transpose()
    tdata = tdata[:,121:181].mean(axis=1)
    print tdata
    fig, ax = plt.subplots(1,1, figsize=(8,8))
    ax.plot(tdata, z_half, 'k')
    tdata = s_prof.variables['nh_pressure_b'][:].data.transpose()
    tdata = tdata[:,121:181].mean(axis=1)
    print tdata
    ax.plot(tdata, z_half, 'b')
    tdata = s_prof.variables['nh_pressure_w1'][:].data.transpose()
    tdata = tdata[:,121:181].mean(axis=1)
    ax.plot(tdata, z_half, 'r--')
    tdata = s_prof.variables['nh_pressure_w2'][:].data.transpose()
    tdata = tdata[:,121:181].mean(axis=1)
    ax.plot(tdata, z_half, 'r:')

    plt.savefig(path+'/Visualization/pz_first2-3hr.pdf')
    plt.close('all')


if __name__ == '__main__':
    main()
