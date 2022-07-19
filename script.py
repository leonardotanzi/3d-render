# Camera location (0, -1.32, 0.18) rotation (90, 0, 0)
# Prusa (0, 0, 0 ) and (0, 0, 0)


import bpy
import math
import os
import fnmatch
from random import randint
from glob import glob
import random


start_cam = bpy.data.objects["Camera"].location.copy()
start_loc = bpy.data.objects["Prusa3D"].location.copy()
start_rot = bpy.data.objects["Prusa3D"].rotation_euler.copy()

    
S = 0
T = 0
    

def scale_view(S): 
    
    bpy.ops.object.select_all(action='DESELECT')
    cam_object = bpy.data.objects["Camera"].select_set(True)
    bpy.context.view_layer.objects.active= bpy.data.objects["Camera"]

    if S == 0:    
        n_scale_y = 0    
    
    if S == 1:    
        n_scale_y = randint(-100, -50) / 200
        
    if S == 2:    
        n_scale_y = randint(-50, 50) / 200
        
    if S == 3:    
        n_scale_y = randint(50, 100) / 200

    bpy.ops.transform.translate(value=(0, n_scale_y, 0), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
   
   
def translate_cam(T):
    bpy.ops.object.select_all(action='DESELECT')
    cam_object = bpy.data.objects["Camera"].select_set(True)
    bpy.context.view_layer.objects.active= bpy.data.objects["Camera"]
    
    if T == 0:
        n_translate_x = 0
        n_translate_z = 0
        
    if T == 1:
        n_translate_x = randint(-15, -10)/ 200
        n_translate_z = randint(-15, -10)/ 200
        
    if T == 2:
        n_translate_x = randint(-10, 10)/ 200
        n_translate_z = randint(-10, 10)/ 200
        
    if T == 3:
        n_translate_x = randint(10, 15)/ 200
        n_translate_z = randint(10, 15)/ 200

    bpy.ops.transform.translate(value=(n_translate_x, 0, n_translate_z), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
    
    
def light_change():
    
    n_angle = randint(0, 10)
    n_strength = randint(-2, 5)
    
    bpy.context.view_layer.objects.active= bpy.data.objects["Sun.001"]
    bpy.context.object.data.angle = start_light_angle + n_angle
    bpy.context.object.data.energy = start_light_strength + n_strength
    
    
def occlusion():   # inserting fake occlusions
    
    for tool in tool_list:
    
        move_x = randint(-10, 10)
        move_y = randint(-10, 10)
        move_z = randint(-200, 200)
        r_x= randint (0, 30)
        r_y= randint (0, 30)
        r_z= randint (0, 30)
        
        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects[tool].select_set(True)
        bpy.context.view_layer.objects.active= bpy.data.objects[tool]
        bpy.ops.transform.translate(value=(move_x, move_y, move_z), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(True, True, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)   
        
        bpy.ops.transform.rotate(value=r_x, orient_axis='X', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
        bpy.ops.transform.rotate(value=r_y, orient_axis='Y', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
        bpy.ops.transform.rotate(value=r_z, orient_axis='Z', orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
                
   
if __name__ == "__main__":

    scene = bpy.context.scene

    blend_file_path = bpy.data.filepath
    directory = os.path.dirname(blend_file_path)

    # name of the directory where it will save the images and rotations tag
    file_dir = 'RENDER_FILES'
    tag_file_name = 'rotations.tag'

    save_folder = os.path.join(directory, file_dir)
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)  # if you don't run blender as admin I have to create by hand the folder


    f = open(os.path.join(directory, tag_file_name), "w")
    
    # backgrounds
    bgfiles = []
    for img_path in glob(os.path.join(directory, "Backgrounds\\") + "*.jpg"):
        bgfiles.append(img_path) 
    
    background_n = len(bgfiles)
    print(background_n)
    
    count = 0
    total_step = 0
    
    for step_x in range(-10, 31):
        for step_z in range(-60, 61):
            random_list = random.sample(range(-30, 31), 20)
            total_step += 1
            for step_y in range(-30, 31):
        
                if step_y in random_list:
                    
                    # both the transformation are not needed for this task
                    # light_change()
                    # occlusion()
                    
                    x = math.radians(step_x)
                    y = math.radians(step_y)
                    z = math.radians(step_z)
                    bpy.ops.object.select_all(action='DESELECT')
                    bpy.data.objects["Prusa3D"].select_set(True)
                    bpy.context.view_layer.objects.active= bpy.data.objects["Prusa3D"]
                    # how much rotate the object
                    bpy.context.active_object.rotation_euler[0] = x 
                    bpy.context.active_object.rotation_euler[1] = y
                    bpy.context.active_object.rotation_euler[2] = z
                                                 
                    background_index = randint(0, background_n - 1)
                    bg = bgfiles[background_index]
                    print(bg)
                    new_img = bpy.data.images.load(filepath = bg)
            
                    bpy.context.scene.world.node_tree.nodes["Image Texture"].image = new_img
                    bpy.context.scene.world.node_tree.nodes["Image Texture"].image.reload()
                                        
                    
                    img_name = os.path.join(save_folder, 'PRusa_rgb_' + str(count) +'.jpg')
                    print("%s, %f, %f, %f" % ('PRusa_rgb_' + str(count) +'.jpg', x, y, z), file=f)
                    print("S:{}, T:{}".format(S, T))
                    
                    bpy.context.scene.eevee.use_gtao = True
                    bpy.context.scene.render.filepath = img_name
                    # waits until the writing is finished before moving on to the next render
                    bpy.ops.render.render(write_still = True)  
                    bpy.data.images.remove(new_img)
                    
                    count += 1
                    
                    # Restoring the initial positions of objects
                    bpy.data.objects["Camera"].location = start_cam
                    bpy.data.objects["Prusa3D"].rotation_euler = start_rot
                    bpy.data.objects["Prusa3D"].location = start_loc

    f.close()
