from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

# https://matplotlib.org/basemap/

def map1():
    # Using the miller projection.
    m = Basemap(projection='mill',llcrnrlat=-90,urcrnrlat=90,\
                llcrnrlon=-180,urcrnrlon=180,resolution='c')
    m.drawcoastlines()
    m.fillcontinents()
    #m.drawcountries()
    #m.drawstates()
    m.drawmapboundary()
    plt.title("Quick basemap example")
    plt.savefig('map1.png')
    plt.show()

def map2():
    m = Basemap(projection='mill',llcrnrlat=-60,urcrnrlat=90,\
                llcrnrlon=-180,urcrnrlon=180,resolution='c')
    m.drawcoastlines()
    m.fillcontinents(color='#072b57',lake_color='#FFFFFF') # blue continents, white lakes
    #m.drawcountries()
    #m.drawstates()
    m.drawmapboundary(fill_color='#FFFFFF')
    plt.title("Quick basemap example 2")
    plt.savefig('map2.png')
    plt.show()

def map3():
    m = Basemap(projection='mill',llcrnrlat=-60,urcrnrlat=90,\
                llcrnrlon=-180,urcrnrlon=180,resolution='c')
    m.drawcoastlines()
    #m.drawcountries()
    #m.drawstates()
    m.drawrivers()
    m.fillcontinents(color='#04BAE3',lake_color='#FFFFFF')

    m.drawmapboundary(fill_color='#FFFFFF')
    #m.topography()
    #m.shadedrelief()
    #m.bluemarble()
    plt.title("World rivers")
    plt.savefig('map3.png')
    plt.show()



def map4():
    # Using the miller projection.
    m = Basemap(projection='mill',llcrnrlat=20,urcrnrlat=50,\
                llcrnrlon=-130,urcrnrlon=-60,resolution='c')
    m.drawcoastlines()
    m.drawcountries()
    m.drawstates()
    m.fillcontinents(color='#04BAE3',lake_color='#FFFFFF')
    m.drawmapboundary(fill_color='#FFFFFF')
    # Houston, Texas
    lat,lon = 29.7630556,-95.3630556
    x,y = m(lon,lat)
    m.plot(x,y, 'ro', label='Houston, Texas')
    lon, lat = -104.237, 40.125 # Location of Boulder
    xpt,ypt = m(lon,lat)
    m.plot(xpt,ypt, 'go', label='Boulder')
    plt.title("Geo Plotting")
    plt.legend(loc=0)
    plt.savefig('Texas.png')
    plt.show()

def map5():
    m = Basemap(projection='mill',llcrnrlat=20,urcrnrlat=50,\
                llcrnrlon=-130,urcrnrlon=-60,resolution='c')
    m.drawcoastlines()
    m.drawcountries()
    m.drawstates()
    m.fillcontinents(color='#04BAE3', lake_color='#FFFFFF')
    m.drawmapboundary(fill_color='#FFFFFF')
    lat = 30,31,34,33,32
    lon = -103,-110,-107,-111,-115
    lat2 = 40,33,44,31,30
    lon2 = -113,-100,-102,-111,-112
    x,y = m(lon,lat)
    m.plot(x,y,'ro',markersize=20,alpha=.5)
    x,y = m(lon2,lat2)
    m.plot(x,y,'go',markersize=20,alpha=.5)
    plt.title('Geo Plotting')
    plt.show()

#map1()
#map2()
#map3()
#map4()
#map5()

import numpy as np
# set up orthographic map projection with
# perspective of satellite looking down at 50N, 100W.
# use low resolution coastlines.
map = Basemap(projection='ortho',lat_0=45,lon_0=-100,resolution='l')
# draw coastlines, country boundaries, fill continents.
map.drawcoastlines(linewidth=0.25)
map.drawcountries(linewidth=0.25)
map.fillcontinents(color='coral',lake_color='aqua')
# draw the edge of the map projection region (the projection limb)
map.drawmapboundary(fill_color='aqua')
# draw lat/lon grid lines every 30 degrees.
map.drawmeridians(np.arange(0,360,30))
map.drawparallels(np.arange(-90,90,30))
# make up some data on a regular lat/lon grid.
nlats = 73; nlons = 145; delta = 2.*np.pi/(nlons-1)
lats = (0.5*np.pi-delta*np.indices((nlats,nlons))[0,:,:])
lons = (delta*np.indices((nlats,nlons))[1,:,:])
wave = 0.75*(np.sin(2.*lats)**8*np.cos(4.*lons))
mean = 0.5*np.cos(2.*lats)*((np.sin(2.*lats))**2 + 2.)
# compute native map projection coordinates of lat/lon grid.
x, y = map(lons*180./np.pi, lats*180./np.pi)
# contour data over the map.
cs = map.contour(x,y,wave+mean,15,linewidths=1.5)
plt.title('contour lines over filled continent background')
plt.show()


