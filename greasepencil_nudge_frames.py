bl_info = {
    "name": "Nudge Grease Pencil Frames",
    "Description": "Shorten (D) or Extend (F) the duration of the current Grease Pencil frame",
    "blender": (2, 80, 0),
    "category": "Animation",
    "author": "bergamote"
}

import bpy


def selectFrames():
    bpy.ops.action.select_leftright(mode="LEFT", extend=False)
    bpy.ops.action.select_all(action='INVERT')


class ExtendGpFrame(bpy.types.Operator):
    """Extend the current Grease Pencil keyframe"""
    bl_idname = "action.extend_gp_frame"
    bl_label = "Extend frame"
    bl_options = {'REGISTER', 'UNDO'}


    def execute(self, context):
        if bpy.context.area.type == 'DOPESHEET_EDITOR':
            selectFrames()
            bpy.ops.transform.transform(mode='TIME_TRANSLATE', value=(1,0,0,0))

        return {'FINISHED'}

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


addon_keymaps = []

def register():
    bpy.utils.register_class(ExtendGpFrame)
    bpy.utils.register_class(ShortenGpFrame)
    wm = bpy.context.window_manager
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

if __name__ == "__main__":
    register()


# Based on the tutorial at https://docs.blender.org/manual/en/latest/advanced/scripting/addon_tutorial.html
