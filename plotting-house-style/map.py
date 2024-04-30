"""
Code for plotting pretty maps. Requires geopandas and matplotlib.
"""

try:
    import geopandas as gpd
    from shapely import box
except ImportError as exc:
    raise ImportError(
        "Can't import plotting_house_style.map as some dependencies are missing. "
        'Run `pip install "plotting_house_style[map]"` to fix.'
    ) from exc

from .colours import *
from typing import Optional

def get_world_map(continent:Optional[str] = None):
    """
    Returns a geodataframe with the world borders. If a continent is specified, only the countries
    on that continent are returned.
    inputs:
        continent: continent to return the countries for
    returns:
        geodataframe with the world borders
    """
    world=gpd.read_file(gpd.datasets.get_path("naturalearth_lowres"))
    if continent:
        return world[world.continent == continent]
    return world

def plot_pretty_basemap(base,gdf,ax):
    """
    Plots a pretty, minimal basemap. Turns tick labels off, plots the landmass white on a 
    babyblue background. The outline of the landmass is black, the country borders within are
    light gray. Crops to the extent of the geodataframe gdf.
    inputs:
        base: geodataframe with the world borders
        gdf: geodataframe to crop the basemap to, the data you want to plot
        ax: axis to plot on

    side effects:
        plots the basemap on the axis
        removes axes
    """
    # crop the map to the extent of the data, so not the whole basemap is plotted
    xMin, yMin, xMax, yMax = gdf.total_bounds
    base_box = gpd.GeoDataFrame(geometry=[box(xMin-5, yMin-5, xMax+5, yMax+5)], crs=base.crs)
    base_box.plot(ax=ax, color=BABYBLUE, zorder=0,edgecolor='black',linewidth=0.6)

    # backgrund blue, land white with grey country borders
    base.plot(ax=ax, color='white',edgecolor='gray',zorder=1,linewidth=0.6)

    # color the outline of the landmass black
    polygon= base.geometry.unary_union
    gdf_bounds=gpd.GeoDataFrame(geometry=[polygon], crs=base.crs)
    gdf_bounds.plot(ax=ax, edgecolor='black',linewidth=0.6,facecolor='none',zorder=2)

    # remove axes
    ax.set_axis_off()