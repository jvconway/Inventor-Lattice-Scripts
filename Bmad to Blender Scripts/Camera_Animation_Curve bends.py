#Create path of beam for camera animation
#in bmad tao run command show -write filename lat sbend::* -att s@f15.9 -floor -no_tail_lines -no_label_lines -no_slaves to output file



import bpy
import bmesh
import os, sys
import re
from mathutils import Matrix, Vector
from math import sin, cos, pi, sqrt, floor
from pathlib import Path
import datetime
import winsound
from mathutils import Vector



def map_table_dict(line):
#    print('map_table_dict: ', line) #print lines in system console to debug which line breaks
    d = {}
    vals = line.split#(',')[0:10]
    print(vals)
    d['x']      = float(vals[5])
    d['y']      = float(vals[6])
    d['z']      = float(vals[7])
    return d

###Open and read layout table file using subroutine
f = open("C:/Users/josep/Desktop/bends4.csv", 'r')
header=f.readline()
lat = [map_table_dict(line) for line in f]
f.close()

print('=============Create Curve==================', datetime.datetime.now())

coords_list = []


for ele in lat:
    X = ele['x']
    Y = ele['y']
    Z = ele['z']
    coords_list.append([X,Y,Z])


# make a new curve
crv = bpy.data.curves.new('crv', 'CURVE')
crv.dimensions = '3D'

# make a new spline in that curve
spline = crv.splines.new(type='NURBS')

# a spline point for each point
spline.points.add(len(coords_list)-1) # theres already one point by default

# assign the point coordinates to the spline points
for p, new_co in zip(spline.points, coords_list):
    p.co = (new_co + [1.0]) # (add nurbs weight)

# make a new object with the curve
obj = bpy.data.objects.new('Path', crv)
bpy.context.scene.collection.objects.link(obj)

print('=============Curve Creation Finished==================', datetime.datetime.now())



#frequency = 2500  # Set Frequency To 2500 Hertz
#duration = 500  # Set Duration To 1000 ms == 1 second
#winsound.Beep(frequency, duration)