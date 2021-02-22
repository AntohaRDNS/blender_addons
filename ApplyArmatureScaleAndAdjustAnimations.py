import bpy

# ----------------------------------------------------------------
# Apply Scale of Selected Armature and adjust its actions
# ----------------------------------------------------------------

# armature object
arm_object = bpy.context.object

# get object uniform scale
uniform_scale = bpy.context.object.scale.x

# target actions array & prefix (actions with same prefix as armature)
target_actions = []
target_actions_prefix = ''

# reset view
def reset():
    bpy.context.area.type = 'GRAPH_EDITOR'
    bpy.context.space_data.dopesheet.filter_text = ""
    
    bpy.context.area.type = 'VIEW_3D'
    bpy.ops.object.editmode_toggle()
    bpy.ops.object.editmode_toggle()
    bpy.context.area.type = 'TEXT_EDITOR'
    
# filter only target actions
for act in bpy.data.actions:
    if target_actions_prefix in act.name:
         target_actions.append(act)

# for each target action 
for act in target_actions:
        
    # assign target action from array
    arm_object.animation_data.action = act
      
    # change area to 3D View & apply scale
    bpy.context.area.type = 'VIEW_3D'
    bpy.ops.object.editmode_toggle()
    bpy.ops.object.editmode_toggle()
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)

    # change mode to Pose & select all bones
    bpy.ops.object.posemode_toggle()
    bpy.ops.pose.select_all(action='SELECT') 

    # change area to Graph Edito r, filter only 'location curves' & select all visible curves
    bpy.context.area.type = 'GRAPH_EDITOR'
    bpy.context.space_data.dopesheet.filter_text = "location"
    bpy.ops.graph.select_all(action='SELECT')

    ## reset 2D cursor loaction & set it as transform pivot 
    bpy.context.scene.frame_current = 0
    bpy.context.space_data.cursor_position_y = 0
    bpy.context.space_data.pivot_point = 'CURSOR'

    # scale all 'location' curves by uniform scale value
    bpy.ops.transform.resize(value=(1, uniform_scale, 1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, True, False), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

    bpy.ops.graph.select_all(action='DESELECT')

# reset all windows
reset()




