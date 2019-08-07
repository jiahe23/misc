import numpy as np
import masking

def get_updmask(dataobj, z_half):
    c_srf = dataobj.groups['fields'].variables['c_srf_15'][:].data
    c_srf_2d = masking.reshape_var(c_srf)
    ql_2d = dataobj.groups['fields'].variables['ql'][:].data
    ql_2d = masking.reshape_var(ql_2d)
    w2d_full = dataobj.groups['fields'].variables['w'][:].data
    w2d_full = masking.reshape_var(w2d_full)
    w2d_half = masking.interpolate_w(w2d_full)
    cb_idx, ct_idx = masking.calculate_cloud_base_top(ql_2d)
    mask2d = masking.updraft_env_mask(c_srf_2d, w2d_half, ql_2d, cb_idx, ct_idx, z_half)
    return mask2d['updraft'].reshape(c_srf.shape[0],c_srf.shape[1],c_srf.shape[2])

def scalar_ddz_upd(dataobj, varname, mask3d, dz, alpha0):
    var = dataobj.groups['fields'].variables[varname][:].data
    ddz = np.zeros_like(var)
    for k in np.arange(1, var.shape[2]-1):
        ddz[:,:,k] = 0.5*(alpha0[k+1]*var[:,:,k+1]-alpha0[k-1]*var[:,:,k-1])/float(dz)
    return np.ma.masked_where(mask3d, ddz).reshape(ddz.shape[0]*ddz.shape[1],ddz.shape[2]).mean(axis=0)

def get_a_upd(mask3d):
    return 1-mask3d.sum(axis=0).sum(axis=0)/float(mask3d.shape[0]*mask3d.shape[1])
