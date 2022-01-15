# NormalsToVertexColour
Blender add-on to bake face normals into vertex colour and a random number in vertex alpha.

![Screenshot](/Snapshot_Doc_01.png)

Note: 

Normals will be converted from the [-1,1] range to the [0,1] range for storage, and you will need to be convert them back to [-1,1] before use (normal * 2 - 1).

Result can be viewed from the vertex painting mode, or by using a material which base colour comes from vertex colour.


