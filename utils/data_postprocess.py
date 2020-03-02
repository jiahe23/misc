'''
module for pycles postprocess
data import
'''
import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt

class lesdata:
    def __init__(self, datapath, expname):
        self.datapath = datapath
        try:
            self.statsobj = nc.Dataset(self.datapath+'/stats/Stats.'+expname+'.nc','r')
        except:
            print 'stats data loading failure'
            exit(0)

    def fields(self, tt, varname):
        try:
            self.fieldobj = nc.Dataset(self.datapath+'/comb_fields/'+str(tt)+'.nc','r')
        except:
            print 'field data loading failure'
            exit(0)
        try:
            return  self.fieldobj.groups['fields'].variables[varname][:].data
        except:
            print 'cannot get '+varname+' in fields'

    def stats(self, grouptype, varname):
        if grouptype == 'profiles':
            return self._getProfiles(varname)
        elif grouptype == 'reference':
            return self._getReferece(varname)
        elif grouptype == 'timeseries':
            return self._getTimeseries(varname)
        else:
            exit(grouptype+' is not a valid group in stats data')

    def _getProfiles(self, varname):
        try:
            return self.statsobj.groups['profiles'].variables[varname][:].data
        except:
            print 'cannot get '+varname+' in profiles'
            return

    def _getReferece(self, varname):
        try:
            return self.statsobj.groups['reference'].variables[varname][:].data
        except:
            print 'cannot get '+varname+' in reference'
            return

    def _getTimeseries(self, varname):
        try:
            return self.statsobj.groups['timeseries'].variables[varname][:].data
        except:
            print 'cannot get '+varname+' in timeseries'
            return

class scmdata:
    def __init__(self, datapath, expname):
        self.datapath = datapath
        try:
            self.statsobj = nc.Dataset(self.datapath+'/stats/Stats.'+expname+'.nc','r')
        except:
            print 'stats data loading failure'
            exit(0)

    def stats(self, grouptype, varname):
        if grouptype == 'profiles':
            return self._getProfiles(varname)
        elif grouptype == 'reference':
            return self._getReferece(varname)
        elif grouptype == 'timeseries':
            return self._getTimeseries(varname)
        else:
            exit(grouptype+' is not a valid group in stats data')

    def _getProfiles(self, varname):
        try:
            return self.statsobj.groups['profiles'].variables[varname][:].data
        except:
            print 'cannot get '+varname+' in profiles'
            return

    def _getReferece(self, varname):
        try:
            return self.statsobj.groups['reference'].variables[varname][:].data
        except:
            print 'cannot get '+varname+' in reference'
            return

    def _getTimeseries(self, varname):
        try:
            return self.statsobj.groups['timeseries'].variables[varname][:].data
        except:
            print 'cannot get '+varname+' in timeseries'
            return
