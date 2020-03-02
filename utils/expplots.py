from data_postprocess import *
import matplotlib.pyplot as plt

class lesplots:
    def __init__(self, lesobj):
        self.data = lesobj

    def plot_profile(self, varname, t1, t2):
        t = self.data.stats('timeseries','t')
        # TODO: Need to check if default z ref is z_full
        z = self.data.stats('reference','z')
        tidx = np.where( (t>=t1) & (t<=t2) )
        profdata = self.data.stats('profiles', varname)
        profdata = profdata[tidx,:].squeeze().mean(axis=0)
        fig, ax = plt.subplots(1,1, figsize=(6,8))

        ax.plot(profdata, z, 'k')
        ax.set_xlim([profdata.min()-0.1*0.1*(profdata.max()-profdata.min()), profdata.max()+0.1*(profdata.max()-profdata.min())])
        ax.set_ylim([0, z.max()])
        ax.set_title('LES: '+varname)

    def plot_tz(self, varname):
        t = self.data.stats('timeseries','t')
        z = self.data.stats('reference','z')
        profdata = self.data.stats('profiles', varname)

        fig, ax = plt.subplots(1,1, figsize=(12,6))
        C = ax.contourf(t, z, profdata.transpose(), cmap='RdBu_r')
        plt.colorbar(C)
        ax.set_xlabel('t')
        ax.set_ylabel('z')
        ax.set_title('LES: '+varname)


class scmplots:
    def __init__(self, scmobj):
        self.data = scmobj

    def plot_profile(self, varname, t1, t2):
        t = self.data.stats('timeseries','t')
        # TODO: Need to check if default z ref is z_full
        z = self.data.stats('reference','z')
        tidx = np.where( (t>=t1) & (t<=t2) )
        profdata = self.data.stats('profiles', varname)
        profdata = profdata[tidx,:].squeeze().mean(axis=0)

        fig, ax = plt.subplots(1,1, figsize=(6,8))
        ax.plot(profdata, z, 'k')
        ax.set_xlim([profdata.min()-0.1*0.1*(profdata.max()-profdata.min()), profdata.max()+0.1*(profdata.max()-profdata.min())])
        ax.set_ylim([0, z.max()])
        ax.set_title('SCM: '+varname)

    def plot_tz(self, varname):
        t = self.data.stats('timeseries','t')
        z = self.data.stats('reference','z')
        profdata = self.data.stats('profiles', varname)

        fig, ax = plt.subplots(1,1, figsize=(12,6))
        C = ax.contourf(t, z, profdata.transpose(), cmap='RdBu_r')
        plt.colorbar(C)
        ax.set_xlabel('t')
        ax.set_ylabel('z')
        ax.set_title('SCM: '+varname)


class lesVSscm_plots:
    def __init__(self, lesobj, scmobj):
        self.les = lesobj
        self.scm = scmobj

    def plot_profile(self, varles, varscm, t1, t2):
        tles = self.les.stats('timeseries','t')
        tscm = self.scm.stats('timeseries','t')

        # TODO: Need to check if default z ref is z_full
        zles = self.les.stats('reference','z')
        zscm = self.scm.stats('reference','z')
        tidxles = np.where( (tles>=t1) & (tles<=t2) )
        tidxscm = np.where( (tscm>=t1) & (tscm<=t2) )
        profles = self.les.stats('profiles', varles)
        profscm = self.scm.stats('profiles', varscm)
        profles = profles[tidxles,:].squeeze().mean(axis=0)
        profscm = profscm[tidxscm,:].squeeze().mean(axis=0)

        fig, ax = plt.subplots(1,1, figsize=(6,8))
        ax.plot(profles, zles, 'k')
        ax.plot(profscm, zscm, 'b')
        datamin = min(profles.min(), profscm.min())
        datamax = max(profles.max(), profscm.max())
        ax.set_xlim([datamin-0.1*(datamax-datamin), datamax+0.1*(datamax-datamin)])
        ax.set_ylim([0, max(zles.max(),zscm.max())])
        ax.set_title(varles)
        ax.legend(['LES','SCM'])

    def plot_tz(self, varles, varscm):
        tles = self.les.stats('timeseries','t')
        tscm = self.scm.stats('timeseries','t')

        # TODO: Need to check if default z ref is z_full
        zles = self.les.stats('reference','z')
        zscm = self.scm.stats('reference','z')
        profles = self.les.stats('profiles', varles)
        profscm = self.scm.stats('profiles', varscm)

        fig, ax = plt.subplots(2,1, figsize=(12,12))
        C = ax[0].contourf(tles, zles, profles.transpose(), cmap='RdBu_r')
        plt.colorbar(C, ax=ax[0])
        ax[0].set_xlabel('t')
        ax[0].set_ylabel('z')
        ax[0].set_title('LES: '+varles)
        C = ax[1].contourf(tscm, zscm, profscm.transpose(), cmap='RdBu_r')
        plt.colorbar(C, ax=ax[1])
        ax[1].set_xlabel('t')
        ax[1].set_ylabel('z')
        ax[1].set_title('SCM: '+varscm)
