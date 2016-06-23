
# coding: utf-8

# In[2]:

import os
import sys
import glob
import argparse
import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt


# In[3]:

#parser = argparse.ArgumentParser(description ='Run sextractor on mosaics')
#parser.add_argument('--d',dest = 'd', default =' ~/github/HalphaImaging/astromatic', help = 'Locates path of config files')
#args = parser.parse_args()
#os.system('cp ' +args.d + '/default.* .')


# In[4]:

hafiles = glob.glob('*_ha*')
hafiles = set(hafiles) - set(glob.glob("*.*"))
for it in hafiles:
    print it
    t = it.split('_')
    ir = t[0]+'_R'
    print '/usr/bin/sextractor ' + it + '.coadd.fits -c default.sex.hdi -CATALOG_NAME ' + it + '.cat'
    print ""
    os.system('/usr/bin/sextractor ' + it + '.coadd.fits -c default.sex.hdi -CATALOG_NAME ' + it + '.cat')
    print ""
    print "/usr/bin/sextractor " + it + '.coadd.fits, ' + ir + '.coadd.fits -c default.sex.hdi -CATALOG_NAME ' + ir + '.cat')"
    print ""
    os.system('/usr/bin/sextractor ' + it + '.coadd.fits, ' + ir + '.coadd.fits -c default.sex.hdi -CATALOG_NAME ' + ir + '.cat')
# Catalogs made


# In[9]:

cluster = ""
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


# In[ ]:

hafiles = ['it_ha.cat','this_ha.cat','no_ha.cat']
rfiles = []
for it in hafiles:
    print it
    t = it.split("_")
    print t
    rfiles.append(t[0]+"_R.cat")
print rfiles


# In[25]:

rflags = [0,0,2,3,2,1,0,0,2,0]
hflags = [1,0,3,2,0,1,1,0,0,0]
hd = np.array([3,2,5,5,2,6,8,3,1,6])
rd = np.array([4,1,7,2,7,9,5,2,5,3])
keepflag = np.ones(len(rflags),dtype = bool)
for i in range(len(rflags)):
    if (rflags[i]+hflags[i])>0:
        keepflag[i] = False

#keepflag[rflags<1]=False
#print keepflag
#keepflag[hflags>0]=False
print keepflag
print hd[keepflag]
print rd[keepflag]
# Should be [False, True, False, False, False, False, False, True, False, True]


# In[6]:

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
hadat.columns


# In[8]:

for i in range(4):
    print i


# In[10]:

rflags = rdat["FLAGS"]
rflags[6]


# In[11]:

print len(hflags)
print len(rflags)


# In[ ]:



