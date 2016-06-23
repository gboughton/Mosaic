
# coding: utf-8

# In[2]:

import os
import sys
import glob
import argparse
import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt


#parser = argparse.ArgumentParser(description ='Run sextractor on mosaics')
#parser.add_argument('--d',dest = 'd', default =' ~/github/HalphaImaging/astromatic', help = 'Locates path of config files')
#args = parser.parse_args()
#os.system('cp ' +args.d + '/default.* .')


hafiles = glob.glob('*_ha*')
hafiles = set(hafiles) - set(glob.glob("*.*"))
for it in hafiles:
    t = it.split('_')
    print "Running Sextractor on",t[0]
    ir = t[0]+'_R'
    os.system('/usr/bin/sextractor ' + it + '.coadd.fits -c default.sex.hdi -CATALOG_NAME ' + it + '.cat')
    os.system('/usr/bin/sextractor ' + it + '.coadd.fits,' + ir + '.coadd.fits -c default.sex.hdi -CATALOG_NAME ' + ir + '.cat')
# Catalogs made

cluster = "A1367"
hacat = glob.glob(cluster + "_ha*.cat")
rcat = glob.glob(cluster + "_R.cat")
try:
    hacat = hacat[0]
    rcat = rcat[0]
except IndexError:
    print "No catalogs found"
    sys.exit(0)
hadat = fits.getdata(hacat,2)
rdat = fits.getdata(rcat,2)
haflux = hadat["FLUX_AUTO"] #Not right column name
rflux = rdat["FLUX_AUTO"]
hflags = hadat["FLAGS"]
rflags = rdat["FLAGS"]
print "Number of Points found:",len(rflags)
keepflag = np.ones(len(rflags),dtype = bool)
for i in range(len(hflags)-1):
    if (rflags[i]+hflags[i])>0:
        keepflag[i] = False
rgflx = rflux[keepflag]
hagflx = haflux[keepflag]
print "Number of Uncompromised Points:",len(rgflx)
dflux = hagflx-rgflx
plt.hist(dflux)
plt.title("Halpha Flux - R Flux")
plt.xlabel("Difference")
plt.ylabel("Amount")




