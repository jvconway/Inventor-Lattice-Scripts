import bpy
import bmesh
import os, sys
import re
from mathutils import Matrix, Vector
from math import sin, cos, pi, sqrt, floor
from pathlib import Path
import winsound

catalog = 'C:/Users/Josep/Dropbox (Xelera)/Cooler Technical/Blender/Catalog'


def map_table_dict(line):
#    print('map_table_dict: ', line)
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

###Open and read layout table file
f = open("C:/Users/Josep/Documents/GitHub/eic-cooler/blender/cooler/cooler.layout_table", 'r') 
header=f.readline()
lat = [map_table_dict(line) for line in f]
f.close()
print('=============NEW CHECK FOR MISSING ELEMENT .BLEND FILES==================')

for ele in lat:  #for each element in the lattice
    elename = ele['key'] + str(floor(1000*ele['L']))  #derive element name based on convention "key" + floor(length)
#    print(elename)

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
    elif p.exists() == False: #if the .blend file does not exist, log missing element name
        print('MISSING: ' + elename + '  ID: ' + str(ele['index']) + '  ' + ele['name'])
        #continue        
    else: 
        continue
    
print('=============END CHECK==================')


frequency = 2500  # Set Frequency To 2500 Hertz
duration = 200  # Set Duration To 1000 ms == 1 second
winsound.Beep(frequency, duration)