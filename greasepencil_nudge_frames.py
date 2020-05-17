bl_info = {
    "name": "Nudge Grease Pencil Frames",
    "Description": "Shorten (D) or Extend (F) the duration of the current Grease Pencil frame",
    "blender": (2, 80, 0),
    "category": "Animation"
}

import bpy


def selectFrames():
    bpy.ops.action.select_leftright(mode="LEFT", extend=False)
    bpy.ops.action.select_all(action='INVERT')


class ExtendGpFrame(bpy.types.Operator):
    """Extend the current Grease Pencil keyframe"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "action.extend_gp_frame"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Extend frame"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.


    def execute(self, context):        # execute() is called when running the operator.
        if bpy.context.area.type == 'DOPESHEET_EDITOR':
            selectFrames()
            bpy.ops.transform.transform(mode='TIME_TRANSLATE', value=(1,0,0,0))

        return {'FINISHED'}            # Lets Blender know the operator finished successfully.

class ShortenGpFrame(bpy.types.Operator):
    """Shorten the current Grease Pencil keyframe"""
    bl_idname = "action.shorten_gp_frame"
    bl_label = "Shorten frame" 
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if bpy.context.area.type == 'DOPESHEET_EDITOR':
            selectFrames()
            bpy.ops.transform.transform(mode='TIME_TRANSLATE', value=(-1,0,0,0))

        return {'FINISHED'}

# store keymaps here to access after registration
addon_keymaps = []

def register():
    bpy.utils.register_class(ExtendGpFrame)
    bpy.utils.register_class(ShortenGpFrame)
    # handle the keymap
    wm = bpy.context.window_manager
    # Note that in background mode (no GUI available), keyconfigs are not available either,
    # so we have to check this to avoid nasty errors in background case.
    kc = wm.keyconfigs.addon
    if kc:
        km = wm.keyconfigs.addon.keymaps.new(name='Window', space_type='EMPTY')
        kmi = km.keymap_items.new(ExtendGpFrame.bl_idname, 'F', 'PRESS')
        addon_keymaps.append((km, kmi))
        kmi = km.keymap_items.new(ShortenGpFrame.bl_idname, 'D', 'PRESS')
        addon_keymaps.append((km, kmi))


def unregister():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    bpy.utils.unregister_class(ExtendGpFrame)
    bpy.utils.unregister_class(ShortenGpFrame)

# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()