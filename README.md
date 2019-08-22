# Codes

## {FEniCS on Colab}
<pre>!apt-get install fenics
from google.colab import files

import platform, sys
python_version=platform.python_version()
from distutils.version import LooseVersion, StrictVersion

if ( LooseVersion(python_version) < LooseVersion("3.0.0")):
    print("Python3 is needed!");
    print("How to fix: Runtime/Change_runtime_type/Python 3");
    sys.exit()
try:
    from dolfin import *; from mshr import *
except ImportError as e:
    !apt-get install -y -qq software-properties-common python-software-properties module-init-tools
    !add-apt-repository -y ppa:fenics-packages/fenics
    !apt-get update -qq
    !apt install -y --no-install-recommends fenics
    from dolfin import *; from mshr import *
    
import matplotlib.pyplot as plt;
from IPython.display import clear_output, display; import time; import dolfin.common.plotting as fenicsplot 
import time

import os, sys, shutil

dolfin_version = dolfin.__version__
print ('dolfin version:', dolfin_version)

!rm -rf * # clean up all files</pre>

## {Unique for Abaqus Numpy}
<pre>def unique(arr):
    k=0
    while k < arr.shape[0]:
        x = arr[k]
        barr = (x==arr).all(1)
        barr[np.where(barr==True)[0][0]] = False
        arr = np.delete(arr, np.where(barr==True), 0)
        k+=1
    return arr</pre>

## {Particles!}
<pre>import numpy as np
from math import sqrt
from scipy.spatial.distance import euclidean

class particle:
    def __init__(self, position, radius):
        self.pos = position
        self.radius = radius

n_particles = 10
default_radius = 0.2
all_particles = []
x_lim = np.array([0,2])
y_lim = np.array([0,2])

def newpos():
    return [np.random.uniform(x_lim[0]+default_radius, x_lim[1]-default_radius),np.random.uniform(y_lim[0]+default_radius, y_lim[1]-default_radius)]   

for n in range(n_particles):
    pos = newpos()
    try:
        mindist = euclidean(sorted(all_particles, key = lambda p: euclidean(p.pos, pos))[0].pos, pos)
        while mindist <= 2*default_radius:
            pos = newpos()
            mindist = euclidean(sorted(all_particles, key = lambda p: euclidean(p.pos, pos))[0].pos, pos)
    except: pass
    all_particles.append(particle(pos, default_radius))
    
plt.figure(figsize=(4,4))
for ptc in all_particles:
    circle = (ptc.pos[0] + ptc.radius * np.sin([x for x in np.linspace(0,2*np.pi,100)]), ptc.pos[1] + ptc.radius * np.cos([x for x in np.linspace(0,2*np.pi,100)]))
    plt.plot(*circle)
plt.axis('equal')</pre>
