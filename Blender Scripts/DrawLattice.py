############################################
##  
##  DrawLattice.py
##  Joe Conway (Xelera Research) 2022
##  
##  Read *.layout_table file (.csv format) exported from Bmad
##  and place .blend model files in correct location in space.
##  
##  
##  Run CheckForMissing.py first to check for models missing from catalog
##  
##  Run with System Console open to see start and end messages and times
##  
##  This version "appends" the catalog model into the current .blend file which
##  can result in large file sizes.  "Linking" the catalog model results in
##  smaller file sizes but so far I have experienced the links breaking when
##  sharing the file with others.
##  
############################################

import bpy
import bmesh
import os, sys
import re
from mathutils import Matrix, Vector
from math import sin, cos, pi, sqrt, floor
from pathlib import Path
import datetime
import winsound

## Define path to catalog models
catalog = 'C:/Users/Josep/Dropbox (Xelera)/Cooler Technical/Blender/Catalog'

## Subroutine to assign values in *.layout_table file to variables
def map_table_dict(line):
#    print('map_table_dict: ', line) #print lines in system console to debug which line breaks
    d = {}
    vals = line.split(',')[0:14]
    #d['layer']  = vals[0].strip() 
    d['name']   = vals[0].strip()
    d['index']  = int(vals[1])
    d['x']      = float(vals[2])
    d['y']      = float(vals[3])
    d['z']      = float(vals[4])
    d['theta']  = float(vals[5])
    d['phi']    = float(vals[6])
    d['psi']    = float(vals[7])
    d['key']    = vals[8].strip()
    d['L']      = float(vals[9])  
    if d['key']=='SBEND':
        d['angle'] = float(vals[10]) 
        d['e1'] = float(vals[11]) 
        d['e2'] = float(vals[12])  
    if d['key']=='PIPE':
        d['radius_x'] =  float(vals[10])  
        d['radius_y'] =  float(vals[11])
        d['thickness'] =  float(vals[12])  
    if d['key']=='WIGGLER':
        d['radius_x'] =  float(vals[10])  
        d['radius_y'] =  float(vals[11])
        d['xray_line_len'] =  float(vals[12])          
    d['descrip'] = vals[13]  
    return d

###Open and read layout table file using subroutine
f = open("C:/Users/Josep/Documents/GitHub/eic-cooler/blender/cooler/cooler.layout_table", 'r')
header=f.readline()
lat = [map_table_dict(line) for line in f]
f.close()

print('=============PLACE ELEMENT MODELS==================', datetime.datetime.now())

for ele in lat:  #for each element in the lattice
    elename = ele['key'] + str(floor(1000*ele['L']))  #derive element name based on convention "key" + floor(length)(in mm)
#    print(elename)

    ## We currently have 4 Quad types and don't use the standard naming convention for them
    if ele['key'] == 'Quadrupole':
            if floor(1000*ele['L']) == 200:
                elename = 'QuadrupoleW5'
            if floor(1000*ele['L']) == 100:
                elename = 'QuadrupoleS4'
            if floor(1000*ele['L']) == 60:
                elename = 'QuadrupoleS2s'
            if floor(1000*ele['L']) == 120:
                elename = 'QuadrupoleS2l'
    
    file_path = os.path.join(catalog, elename + '.blend') #create file path
    
    
            
    inner_path = 'Object'
    p = Path(file_path)
    if ele['L'] == 0:  #if the element length is 0 skip
        continue
    elif p.exists() == False: #if the .blend file does not exist skip and print name of missing element in system console
        #print('MISSING: ' + elename + ' ID: ' + str(ele['index'])) #missing elements are written in CheckForMissing.py so not necessary here
        continue        
    else: 
        #this code opens the .blend catalog file and goes through the file structure to get the actual 3D model and append it to the current file
        #find all pieces (objects) in .blend file
        with bpy.data.libraries.load(file_path, link=False) as (data_from, data_to):    
            onames = [name for name in data_from.objects if True]
            data_to.objects = data_from.objects
        
        for ob in onames:
            object_name = ob
            #append objects to this file (change "append" to "link" to link files, see note at top)
            bpy.ops.wm.append(
                filepath=os.path.join(file_path, inner_path, object_name),
                directory=os.path.join(file_path, inner_path),
                filename=object_name
                )
            #make just placed object active
            if len(bpy.context.selected_objects):
                bpy.context.view_layer.objects.active = bpy.context.selected_objects[0]
            
            #Rename object something recognizable
            bpy.context.active_object.name = elename
            
            #Move object to correct location
            bpy.context.object.location[0] = ele['z']
            bpy.context.object.location[1] = ele['x']
            bpy.context.object.location[2] = ele['y']
            bpy.context.object.rotation_euler[2] += ele['theta']
            bpy.context.object.rotation_euler[1] += ele['psi']
            bpy.context.object.rotation_euler[0] += -ele['phi']
            
            print(elename + ' ID: ' + str(ele['index']))
            
print('=============FINISHED PLACING ELEMENT MODELS==================', datetime.datetime.now())


frequency = 2500  # Set Frequency To 2500 Hertz
duration = 500  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)
