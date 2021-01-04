bl_info = {
    "name": "Nudge Grease Pencil Frames",
    "author": "Pevin Kinel (bergamote)",
    "blender": (2, 80, 0),
    "location": "Dopesheet > Grease Pencil > Keyboard D and F",
    "description": "Shorten (D) or extend (F) the current GP frame",
    "category": "Animation",
}

import bpy


def selectFrames():
    '''Select every keyframe to the right of current frame'''
    bpy.ops.action.select_leftright(mode="LEFT", extend=False)
    bpy.ops.action.select_all(action='INVERT')

def checkContext(context):
    valid = False
    if (bpy.context.area.type == 'DOPESHEET_EDITOR' and
        context.space_data.ui_mode == 'GPENCIL'):
        valid = True
    return valid

def checkSelObject(context):
    '''Make sure at least 1 GPENCIL object is selected'''
    valid = False
    obj = context.selected_objects
    gp_objs = []
    if obj:
        gp_objs = []
        for sel_obj in obj:
            if sel_obj.type == 'GPENCIL':
                valid = True
                gp_objs.append(sel_obj)
    else:
        return False
    return gp_objs

class ExtendGpFrame(bpy.types.Operator):
    """Extend the current Grease Pencil keyframe"""
    bl_idname = "action.extend_gp_frame"
    bl_label = "Extend frame"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        if checkContext(context) and checkSelObject(context):
            selectFrames()
            bpy.ops.transform.transform(mode='TIME_TRANSLATE', value=(1,0,0,0))
            return {'FINISHED'}
        else:
            return {'CANCELLED'}


class ShortenGpFrame(bpy.types.Operator):
    """Shorten the current Grease Pencil keyframe"""
    bl_idname = "action.shorten_gp_frame"
    bl_label = "Shorten frame"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        cur_fra = context.scene.frame_current
        objects = checkSelObject(context)
        if checkContext(context) and objects:
            for obj in objects:
                layers = bpy.data.objects[obj.name].data.layers
                for layer in layers:
                    keyframes = []
                    if layer.lock == False and layer.active_frame:
                        cur_fra == layer.active_frame.frame_number
                        for i in layer.frames:
                            if i.frame_number not in keyframes:
                                keyframes.append(i.frame_number)

                    if (cur_fra in keyframes) and (cur_fra + 1) in keyframes:
                        # frame would be overwritten
                        return {'CANCELLED'}

            selectFrames()
            bpy.ops.transform.transform(mode='TIME_TRANSLATE', value=(-1,0,0,0))

            return {'FINISHED'}
        else:
            return {'CANCELLED'}


addon_keymaps = []

def register():
    bpy.utils.register_class(ExtendGpFrame)
    bpy.utils.register_class(ShortenGpFrame)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = wm.keyconfigs.addon.keymaps.new(name='Animation', space_type='EMPTY')
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
