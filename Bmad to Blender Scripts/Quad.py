import bpy
import bmesh
import os, sys
import re
from mathutils import Matrix, Vector
from math import sin, cos, pi, sqrt, floor
from pathlib import Path
import winsound

## Define path to catalog models
catalog = 'C:/Users/Josep/Dropbox (Xelera)/Cooler Technical/Blender/Catalog/HSR/'
layout = 'C:/Users/Josep/Documents/GitHub/eic-cooler/blender/hsr/hsr.layout_table'

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

## Open and read layout table file using subroutine
f = open(layout, 'r') 
header=f.readline()
lat = [map_table_dict(line) for line in f]
f.close()

print('=============CREATE DRIFT .BLEND FILES==================')

for ele in lat:  #for each element in the lattice
    elename = ele['key'] + str(floor(1000*ele['L']))  #derive element name based on convention "key" + floor(length)
    print(ele['index'])
    
    file_path = os.path.join(catalog, elename + '.blend') #create file path
    
    inner_path = 'Object'
    p = Path(file_path)
    if ele['L'] == 0:  #if the element length is 0 skip
        continue
    elif p.exists() == True:
        continue
    elif ele['key'] == 'Quadrupole':
    
        bpy.ops.object.select_all(action='SELECT')
        bpy.ops.object.delete() 
        
        L = ele['L']
        filepath = catalog + elename + '.blend'

        bpy.ops.mesh.primitive_cylinder_add(radius=0.6096, depth=L, enter_editmode=False, align='WORLD', location=(0, 0, 0), rotation=(0, 1.5708, 0), scale=(1, 1, 1))
        #bpy.ops.object.shade_smooth()
        obj = bpy.context.object
        mat = bpy.data.materials['Quad Blue Paint']
        obj.data.materials.append(mat)

        print(elename)
        bpy.ops.wm.save_as_mainfile(filepath=filepath)
                
    else: 
        continue
    
print('=============FINISHED CREATE==================')

frequency = 2500  # Set Frequency To 2500 Hertz
duration = 200  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)