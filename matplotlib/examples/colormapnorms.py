"""
Colormap Normalization
======================

Objects that use colormaps by default linearly map the colors in the
colormap from data values *vmin* to *vmax*.  For example::

    pcm = ax.pcolormesh(x, y, Z, vmin=-1., vmax=1., cmap='RdBu_r')

will map the data in *Z* linearly from -1 to +1, so *Z=0* will
give a color at the center of the colormap *RdBu_r* (white in this
case).

Matplotlib does this mapping in two steps, with a normalization from
[0,1] occurring first, and then mapping onto the indices in the
colormap.  Normalizations are classes defined in the
:func:`matplotlib.colors` module.  The default, linear normalization is
:func:`matplotlib.colors.Normalize`.

Artists that map data to color pass the arguments *vmin* and *vmax* to
construct a :func:`matplotlib.colors.Normalize` instance, then call it:

.. ipython::

   In [1]: import matplotlib as mpl

   In [2]: norm = mpl.colors.Normalize(vmin=-1.,vmax=1.)

   In [3]: norm(0.)
   Out[3]: 0.5

However, there are sometimes cases where it is useful to map data to
colormaps in a non-linear fashion.

Logarithmic
-----------

One of the most common transformations is to plot data by taking
its logarithm (to the base-10).  This transformation is useful to
display changes across disparate scales.  Using :func:`colors.LogNorm`
normalizes the data via :math:`log_{10}`.  In the example below,
there are two bumps, one much smaller than the other. Using
:func:`colors.LogNorm`, the shape and location of each bump can clearly
be seen:
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors

N = 100
X, Y = np.mgrid[-3:3:complex(0, N), -2:2:complex(0, N)]

# A low hump with a spike coming out of the top right.  Needs to have
# z/colour axis on a log scale so we see both hump and spike.  linear
# scale only shows the spike.
Z1 = np.exp(-(X)**2 - (Y)**2)
Z2 = np.exp(-(X * 10)**2 - (Y * 10)**2)
Z = Z1 + 50 * Z2

fig, ax = plt.subplots(2, 1)

pcm = ax[0].pcolor(X, Y, Z,
                   norm=colors.LogNorm(vmin=Z.min(), vmax=Z.max()),
                   cmap='PuBu_r')
fig.colorbar(pcm, ax=ax[0], extend='max')

pcm = ax[1].pcolor(X, Y, Z, cmap='PuBu_r')
fig.colorbar(pcm, ax=ax[1], extend='max')
fig.show()

