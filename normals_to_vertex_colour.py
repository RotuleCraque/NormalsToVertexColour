bl_info = {
    "name": "Normals to Vertex Colour",
    "category": "Object",
    "blender": (3, 0, 0),
    "author": "Alo",
}




import bpy
import mathutils
from random import uniform



class NormalsToVertexColour(bpy.types.Operator):
    """Bake face normals in vertex colour rgb and a random numder in alpha"""
    bl_idname = 'object.normals_to_vertex_colour'
    bl_label = 'Normals to Vertex Colour'
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        normals_to_vertex_colour()
        return {'FINISHED'}


def normals_to_vertex_colour():
    bpy.ops.object.mode_set(mode='OBJECT')

    # selected object
    obj = bpy.context.active_object
    mesh = obj.data

    # objects needs a vertex color layer
    vertex_colours = mesh.vertex_colors
    if len(vertex_colours) == 0:
        vertex_colours.new()
        
    # get colour layer
    colour_layer = vertex_colours.active

    i = 0
    # for every vertex of every face, write face normal to vertex colour
    for face in mesh.polygons:
        faceNorm = face.normal
        
        # convert normal to [0,1] range
        faceNorm = (faceNorm + mathutils.Vector([1.0, 1.0, 1.0])) * mathutils.Vector([0.5, 0.5, 0.5])
        
        # compute random in [0,1] range to store in alpha
        rand = uniform(0.0, 1.0)
        
        
        for idx in face.loop_indices:
            # set normal to colour
            colour_layer.data[i].color = mathutils.Vector([faceNorm.x, faceNorm.y, faceNorm.z, rand])
            i += 1
            
            
            
def menu_func(self, context):
    self.layout.operator(NormalsToVertexColour.bl_idname)
            
def register():
    bpy.utils.register_class(NormalsToVertexColour)
    bpy.types.VIEW3D_MT_object.append(menu_func)
    
def unregister():
    bpy.utils.unregister_class(NormalsToVertexColour)
    bpy.types.VIEW3D_MT_object.remove(menu_func)
    
    
if __name__ == "__main__":
    register()