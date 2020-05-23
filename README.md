# Greasepencil Nudge Frames


This is very simple Add-on for [Blender](http://blender.org), to speed up modifying the length of Greasepencil frames.  
It adds two keyboard shortcuts to the Dopesheet, `D` to shorten and `F` to extend, the duration of the currently displayed keyframe by 1 frame.

Pressing `D` does the same thing as typing `[`, `Ctrl+I`, `G`, `-`, `1` and `Enter`.  
Pressing `F` does the same thing as typing `[`, `Ctrl+I`, `G`, `1` and `Enter`.

To install it, got to `Edit > Preferences > Add-ons > Install...`, select `greasepencil_nudge_frames.py` and confirm, then enable it by ticking the checkbox.


### Notes

- The shortcuts change the length of the displayed frame for **every** unlocked layers. Make sure you isolate the layer you want to affect, or lock the ones you want to keep in place.
- This is my first add-on for Blender so most likely badly written and possibly buggy. Use at your own risks and all that.


### To do

- Save keyframe selection before the operation and get back to that selection after the operation is done.
