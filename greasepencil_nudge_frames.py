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

def checkSelObject(context):
    '''Make sure only 1 GPENCIL object is selected'''
    obj = context.selected_objects
    if len(obj) > 1:
        print('More than one object selected')
        return False
    else:
        if obj[0].type == 'GPENCIL':
            return obj[0]
        else:
            return False

def layerUnlocked(obj):
    '''Make sure active gp layer isn't locked'''
    layer_ready = False
    if obj:
        active_layer = obj.data.layers.active_note
        if active_layer:
            if obj.data.layers[active_layer].lock == False:
                layer_ready = True
    return layer_ready

class ExtendGpFrame(bpy.types.Operator):
    """Extend the current Grease Pencil keyframe"""
    bl_idname = "action.extend_gp_frame"
    bl_label = "Extend frame"
    bl_options = {'REGISTER', 'UNDO'}


    def execute(self, context):
        if bpy.context.area.type != 'DOPESHEET_EDITOR':
            return {'CANCELLED'}
        if context.space_data.ui_mode != 'GPENCIL':
            return {'CANCELLED'}

        obj = checkSelObject(context)
        if obj and layerUnlocked(obj):
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
        if bpy.context.area.type != 'DOPESHEET_EDITOR':
            return {'CANCELLED'}
        if context.space_data.ui_mode != 'GPENCIL':
            return {'CANCELLED'}

        obj = checkSelObject(context)
        if obj and layerUnlocked(obj):
            cur_fra = context.scene.frame_current
            layers = bpy.data.objects[obj.name].data.layers
            keyframes = []
            for layer in layers:
                if layer.lock == False:
                    if layer.active_frame:
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
