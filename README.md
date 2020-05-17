Greasepencil Nudge Frames
=========================

This is very simple Add-on for [Blender](http://blender.org), to speed up modifying the length of Greasepencil frames. It adds two keyboard shortcuts to the Dopesheet, `D` to shorten and `F` to extend, the currently displayed keyframe.

Pressing `D` does the same thing as typing `[`, `Ctrl+I`, `G`, `-`, `1` and `Enter`.
Pressing `F` does the same thing as typing `[`, `Ctrl+I`, `G`, `1` and `Enter`.

To install it, got to `Edit > Preferences > Add-ons > Install...`, select `greasepencil_nudge_frames.py` and confirm, then enable it by ticking the checkbox.

**Note:** Pressing `D` is a destructive operation! If the playhead is on top of a keyframe, it will get shortened until the next keyframe along ends up taking its place. 

