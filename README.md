# Greasepencil Nudge Frames


This is very simple Add-on for [Blender](http://blender.org), to speed up modifying the length of Greasepencil frames.  
It adds two keyboard shortcuts to the Dopesheet, `D` to shorten and `F` to extend, the duration of the currently displayed keyframe by 1 frame.

Pressing `D` does the same thing as typing `[`, `Ctrl+I`, `G`, `-`, `1` and `Enter`.  
Pressing `F` does the same thing as typing `[`, `Ctrl+I`, `G`, `1` and `Enter`.

To install it, got to `Edit > Preferences > Add-ons > Install...`, select `greasepencil_nudge_frames.py` and confirm, then enable it by ticking the checkbox.


### Notes

- Pressing `D` is a **destructive** operation! If the playhead is on top of a keyframe, it will get shortened until the next keyframe along ends up taking its place, erasing it in the process. 
- The shortcuts move the frames from **every** layers, so make sure you lock the layers you want to keep in place.
- This is my first add-on for Blender, so most likely badly written and possibly buggy Use at your own risks and all that.


### To do

- Make it impossible to accidently erase a keyframe. ie: if the current keyframe only lasts 1 frame, do nothing.
- Save which keyframes were selected before the operation and get back to that selection after the operation is done. That means the previous 'To do' needs to be done, to guarantee there's the same number of keyframes before and after.
- Assign the keymap to the Grease Pencil Dopesheet (right now it's assigned to `Window`, then `bpy.context.area.type` is checked for `DOPESHEET_EDITOR` before operation)

