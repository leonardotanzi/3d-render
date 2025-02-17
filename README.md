# 3d-render

# Exploiting Deep Learning and Augmented Reality in Fused Deposition Modeling: a focus on positioning

This folder contains the tools to produce an artificial dataset of a 3D model with different rotations as explained in the paper: *Exploiting Deep Learning and Augmented Reality in Fused Deposition Modeling: a focus on positioning*

One can both download the Blender file by decompressing the BlenderFile.rar archive or separately importing the 3D components in the SingleComponents.rar archive and associate them with the *script.py*.

The Blender script will generate a sample with a random background for each interval of rotations along the three axes chosen.
The background dataset has to be downloaded [here](https://groups.csail.mit.edu/vision/SUN/hierarchy.html) and, once downloaded, the RGB images have to be moved to a *Background* folder in the home directory.

The output images will be saved in a folder RENDER_FILES in the home directory together with a tag file containing all the rotations for each image.
