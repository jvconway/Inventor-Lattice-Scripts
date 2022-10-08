############################################
##  
##  DrawLattice - Link - Master.py
##  Joe Conway (Xelera Research) 2022
##  
##  Read *.layout_table file (.csv format) exported from Bmad
##  and place .blend model files in correct location in space.
##  
##  
##  
##  
##  
##  
## 
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

## Subroutine to assign values in *.layout_table file to variables
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

##Subroutine to check for missing catalog models
def check_for_missing(lat, catalog):
    print('=============CHECK FOR MISSING CATALOG FILES==================')
    for ele in lat:  #for each element in the lattice
        
        elename = ele['key'] + str(floor(1000*ele['L']))  #derive element name based on convention "key" + floor(length)
        file_path = os.path.join(catalog, elename + '.blend') #create file path
        
        inner_path = 'Object'
        p = Path(file_path)
        if ele['L'] == 0:  #if the element length is 0 skip
            continue
        elif ele['key'] == "Pipe": #Pipes will be generated, do not need a catalog model
            continue
        elif ele['key'] == "Drift": #Drifts will be generated, do not need a catalog model
            continue
        elif p.exists() == False: #if the .blend file does not exist, log missing element name
            print('MISSING: ' + elename + '  ID: ' + str(ele['index']) + '  ' + ele['name'])        
        else: 
            continue
        return
    print('=============END CHECK==================')
    
## Subroutine for creating drift and pipe models
def Drift_Pipe(lat):
    elename = ele['key'] + str(floor(1000*ele['L']))  #derive element name based on convention "key" + floor(length)
       
    inner_path = 'Object'
    p = Path(file_path)
    if ele['L'] == 0:  #if the element length is 0 skip
        continue
    elif p.exists() == True:
        continue
    elif ele['key'] == 'Drift': or ele['key'] == 'Pipe'
    
        L = ele['L']
        
        bpy.ops.mesh.primitive_cylinder_add(radius=0.019, depth=L-(.012*2), enter_editmode=False, align='WORLD', location=(0, 0, 0), rotation=(0, 1.5708, 0), scale=(1, 1, 1))
        obj = bpy.context.object
#        mat = bpy.data.materials['Steel']
#        obj.data.materials.append(mat)

        bpy.ops.mesh.primitive_cylinder_add(radius=0.035, depth=.012, enter_editmode=False, align='WORLD', location=((L/2)-(0.012/2), 0, 0), rotation=(0, 1.5708, 0), scale=(1, 1, 1))
        obj = bpy.context.object
#        mat = bpy.data.materials['Steel']
#        obj.data.materials.append(mat)

        bpy.ops.mesh.primitive_cylinder_add(radius=0.035, depth=.012, enter_editmode=False, align='WORLD', location=(-((L/2)-(0.012/2)), 0, 0), rotation=(0, 1.5708, 0), scale=(1, 1, 1))
        obj = bpy.context.object
#        mat = bpy.data.materials['Steel']
#        obj.data.materials.append(mat)
        
        print(elename)
        bpy.ops.wm.save_as_mainfile(filepath=filepath)
                
    else: 
        continue
    return




if __name__ == "__main__":

    ## Define path to catalog models
    ## Change to dialog box
    catalog = 'C:/Users/Josep/Dropbox (Xelera)/Cooler Technical/Blender/Catalog'
    ## Define path to *.layout_table file
    ## Change to Dialog Box
    f = open("C:/Users/Josep/Desktop/cesr/bmad_12wig_20050626.layout_table", 'r')

    bpy.ops.wm.console_toggle()
    
    ###Open and read layout table file using subroutine
    header=f.readline()
    lat = [map_table_dict(line) for line in f]
    f.close()
    
    ## Run subroutine to check for missing
    check_for_missing(lat, catalog)
    ## print 'The above elements do not have catalog files'
    ## ask to continue and create black boxes y/n
    ## if no, ask to continue without creating black boxes y/n
    
    ## loop through layout_table file
    ## if L=0 skip
    ## if catalog model exists, link model (suppress warning message)
    ## if drift or pipe, subroutine to create drift or pipe
    ## otherwise, subroutine to create black box 
    for ele in lat:  #for each element in the lattice
        elename = ele['key'] + str(floor(1000*ele['L']))  #derive element name based on convention "key" + floor(length)(in mm)
        disp_name = ele['name'] + '_' + str(ele['index'])
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
        
        
                
        inner_path = 'Collection'
        collection_name = 'Collection'
        p = Path(file_path)
        if ele['L'] == 0:  #if the element length is 0 skip
            continue
        elif p.exists() == False: #if the .blend file does not exist skip and print name of missing element in system console
            #print('MISSING: ' + elename + ' ID: ' + str(ele['index']))
            continue        
        else: 
        #this code opens the .blend catalog file and goes through the file structure to link the collection to the current file
            bpy.ops.wm.link(
                filepath=os.path.join(file_path, inner_path, collection_name),
                directory=os.path.join(file_path, inner_path),
                filename=collection_name
                )
            #make just placed object active
            if len(bpy.context.selected_objects):
                bpy.context.view_layer.objects.active = bpy.context.selected_objects[0]
    #            active_object = bpy.context.active_object
            
            #Rename object something recognizable
            bpy.context.active_object.name = disp_name
            
            #Move object to correct location
            bpy.context.object.location[0] = ele['z']
            bpy.context.object.location[1] = ele['x']
            bpy.context.object.location[2] = ele['y']
            bpy.context.object.rotation_euler[2] += ele['theta']
            bpy.context.object.rotation_euler[1] += -ele['phi']
            bpy.context.object.rotation_euler[0] += ele['psi']
            
            print(elename + ' ID: ' + str(ele['index']))
    
    
    print('=============FINISHED PLACING ELEMENT MODELS==================', datetime.datetime.now())
    
    ## Finished Sound
    frequency = 2500  # Set Frequency To 2500 Hertz
    duration = 500  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)
    
    
    