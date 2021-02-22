# blender_addons
addons-helpers


Goal: A simple script that applies the scale of the armature and adjusts all its animations.

Problem: When you apply a scale to an armature, all of its animations break.

Usage:

      1. Download & Open sctipt file (apply_armature_scale_and_adjust_animations.py) in Blenders Text Editor
      2. Change raw: "target_actions_prefix = ''"   
                     
                     If you want ALL the animations in the file to be adjusted, use:
                     target_actions_prefix = ''   
                      
                     If you want ONLY animations with a specific name to be adjusted:
                     target_actions_prefix = 'you_custom_animation_prefix'
                     
      3. Select Armature in Oject Mode & Play Script
