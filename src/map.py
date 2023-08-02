"""_summary_

Doc: https://matplotlib.org/basemap/
"""

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np


def map1(m) -> None:
    # Using the miller projection.

    m.drawcoastlines()
    m.fillcontinents()
    m.drawmapboundary()

    plt.title("Quick basemap example")
    plt.savefig('figs/map1.png')
    plt.show()


def map2(m, VERY_DARK_BLUE, WHITE) -> None:
    m.drawcoastlines()

    # blue continents, white lakes
    m.fillcontinents(color=VERY_DARK_BLUE, lake_color=WHITE)
    m.drawmapboundary(fill_color=WHITE)

    plt.title("Quick basemap example 2")
    plt.savefig('figs/map2.png')
    plt.show()


def map3(m, VIVID_CYAN, WHITE) -> None:
    m.drawcoastlines()
    m.drawrivers()
    m.fillcontinents(color=VIVID_CYAN, lake_color=WHITE)
    m.drawmapboundary(fill_color=WHITE)
    # m.topography()
    # m.shadedrelief()
    # m.bluemarble()

    plt.title("World rivers")
    plt.savefig('figs/map3.png')
    plt.show()


def map4(m, VIVID_CYAN, WHITE) -> None:
    m.drawcoastlines()
    m.drawcountries()
    m.drawstates()
    m.fillcontinents(color=VIVID_CYAN, lake_color=WHITE)
    m.drawmapboundary(fill_color=WHITE)
    lat, lon = 29.7630556, -95.3630556
    x, y = m(lon, lat)
    m.plot(x, y, 'ro', label='Houston, Texas')
    lon, lat = -104.237, 40.125  # Location of Boulder
    xpt, ypt = m(lon, lat)
    m.plot(xpt, ypt, 'go', label='Boulder')

    plt.title("Geo Plotting")
    plt.legend(loc=0)
    plt.savefig('figs/Houston_Texas.png')
    plt.show()


def map5(m, VIVID_CYAN, WHITE) -> None:
    m.drawcoastlines()
    m.drawcountries()
    m.drawstates()
    m.fillcontinents(color=VIVID_CYAN, lake_color=WHITE)
    m.drawmapboundary(fill_color=WHITE)
    lat = 30, 31, 34, 33, 32
    lon = -103, -110, -107, -111, -115
    lat2 = 40, 33, 44, 31, 30
    lon2 = -113, -100, -102, -111, -112
    x, y = m(lon, lat)
    m.plot(x, y, 'ro', markersize=20, alpha=.5)
    x, y = m(lon2, lat2)
    m.plot(x, y, 'go', markersize=20, alpha=.5)

    plt.title('Geo Plotting')
    plt.show()


def map6(m) -> None:
    # set up orthographic map projection with
    # perspective of satellite looking down at 50N, 100W.
    # use low resolution coastlines.
    map = Basemap(projection='ortho', lat_0=45, lon_0=-100, resolution='l')
    # draw coastlines, country boundaries, fill continents.
    map.drawcoastlines(linewidth=.25)
    map.drawcountries(linewidth=.25)
    map.fillcontinents(color='coral', lake_color='aqua')
    # draw the edge of the map projection region (the projection limb)
    map.drawmapboundary(fill_color='aqua')
    # draw lat/lon grid lines every 30 degrees.
    map.drawmeridians(np.arange(0, 360, 30))
    map.drawparallels(np.arange(-90, 90, 30))
    # make up some data on a regular lat/lon grid.
    nlats = 73
    nlons = 145
    delta = 2. * np.pi / (nlons - 1)
    lats = .5 * np.pi - delta * np.indices((nlats, nlons))[0, :, :]
    lons = delta * np.indices((nlats, nlons))[1, :, :]
    wave = .75 * (np.sin(2. * lats) ** 8 * np.cos(4. * lons))
    mean = .5 * np.cos(2. * lats) * ((np.sin(2. * lats)) ** 2 + 2.)
    # compute native map projection coordinates of lat/lon grid.
    x, y = map(lons * 180. / np.pi, lats * 180. / np.pi)
    # contour data over the map.
    map.contour(x, y, wave + mean, 15, linewidths=1.5)

    plt.title('contour lines over filled continent background')
    plt.show()


def main() -> None:

    m_1 = Basemap(projection='mill', llcrnrlat=-90, urcrnrlat=90,
                llcrnrlon=-180, urcrnrlon=180, resolution='c')

    m_2 = Basemap(projection='mill', llcrnrlat=-60, urcrnrlat=90,
                llcrnrlon=-180, urcrnrlon=180, resolution='c')

    m_3 = Basemap(projection='mill', llcrnrlat=20, urcrnrlat=50,
                llcrnrlon=-130, urcrnrlon=-60, resolution='c')

    WHITE = '#FFFFFF'
    VERY_DARK_BLUE = '#072b57'
    VIVID_CYAN = '#04BAE3'

    map1(m_1)
    map2(m_2, VERY_DARK_BLUE, WHITE)
    map3(m_2, VIVID_CYAN, WHITE)
    map4(m_3, VIVID_CYAN, WHITE)
    map5(m_3, VIVID_CYAN, WHITE)
    map6(m_3)


if __name__ == '__main__':
    main()
