# ---------------------------------------------------------------------------------------
# Written by: Alvaro Sanchez
#
# The following code takes an indefinite number of rasters and multiplies them. 
# These rasters correspond to probability distributions (Numbers between 0 and 1). 
# It also takes a line shapefile. This corresponds to a route of a vehicle or person 
# throughout the area delimited by the rasters. It graphs the values of the raster 
# throughout the line. This is relevant to determine which parts of a route are more 
# dangerous than others, if the probability rasters correspond to individual 
# probabilities of a negative event to occur, like homicide probability (homic_prob) 
# or drug dealing probability (drug_prob)
# ---------------------------------------------------------------------------------------

import os
import rasterio
import numpy as np
import matplotlib.pyplot as plt
import shapely.geometry
from shapely.geometry import LineString 
import fiona

# Paths to the files needed for the analysis. 
# These are paths to the rasters with the probabilities
homicPath = "test files/homic_prob.tif"
drugsPath = "test files/drug_prob.tif"

# This is a path to the polyline shapefile
routePath = "test files/route.shp"

# Load the rasters from the files specified above using the function created below
rasterList = load_rasters(homicPath,drugsPath)

# Load the shapefile of the route
routeShp = load_polyline_from_shp(routePath)

# Compute the result.tif with the multiplication of the rasters
multiply_rasters(rasterList)

#obtain the graph values for the plot
graph = probabilityLine(routeShp,"result.tif")

# Plots the graph values. 2nd argument is the size of the points
plot_points(graph,2)


# This function multiplies rasters cell by cell. It assumes cells 
# have the same extent and resolution.
# If this is not the case, the input rasters must be edited. 
def multiply_rasters(rasters):
    result = None
    for raster in rasters:
        if result is None:
            result = raster.read(1)
        else:
            result = np.multiply(result, raster.read(1))
    with rasterio.open("result.tif", "w", driver="GTiff",
                       height=result.shape[0],
                       width=result.shape[1],
                       count=1, dtype=result.dtype,
                       crs=rasters[0].crs,
                       transform=rasters[0].transform) as dst:
        dst.write(result, 1)

# Function receives inputs in projected coordinate system
def probabilityLine(route, rasterProb):
    graphValues = []
    # Transform the route from src_crs to tgt_crs
    # route = transform_polyline(route,src_crs,tgt_crs)
    with rasterio.open(rasterProb) as src:
        # Loading the array
        arr = src.read(1)
        
        # Get the line length
        line = LineString(route)
        length = line.length
        
        # Get x and y values of points along the line
        step = length / 1000.0
        distance = 0
        for i in np.arange(0, length, step):
            # This gets the coordinates at specified distances
            point = line.interpolate(i)
            x, y = point.x, point.y
            # Get the corresponding cell value from the raster. This will prevent errors due to being out of bounds 
            try:
                row, col = src.index(x, y)
                if row > 0 and col > 0 and row < src.width and col < src.height:
                    cell_value = arr[row][col]
                    graphValues.append([distance, cell_value])
                distance += step                
            except IndexError:
                distance += step
                continue
    return graphValues

# Loads a line feature from a file path
def load_polyline_from_shp(file_path):
    with fiona.open(file_path) as src:
        polyline = shapely.geometry.shape(src[0]['geometry'])
    return polyline

# Load rasters and returns a list of rasterio features
def load_rasters(*input_paths):
    rasters = []
    for path in input_paths:
        rasters.append(rasterio.open(path))
    return rasters

# Same as previous but deletes the inputs
def load_rasters_and_delete(*input_paths):
    rasters = []
    for path in input_paths:
        rasters.append(rasterio.open(path))
        os.remove(path)
    return rasters

# Function created to plot the points on an x,y cartesian plot
def plot_points(points, point_size = 10):
    x = [p[0] for p in points]
    y = [p[1] for p in points]
    plt.plot(x, y, 'ro', markersize = point_size)
    plt.show()

# Function to display the rasters. 
def display_raster(raster):
    fig, ax = plt.subplots()
    ax.imshow(raster.read(1), cmap='gray')
    ax.set_axis_off()
    plt.show()
