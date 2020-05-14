# Python Rubik's Cube
The purpose of this python module is to create a representation of a Rubik's
cube that can be manipulated and eventually integrated with a Blender rig.

## Cube Design
* Faces are named after the color of the center sticker, as no side rotation
can displace the center sticker. 
* This cube representation is red-centric, meaning the UV map of the cube
has red at the center with the other colors branching off of it, as follows:
```
             _ _ _ 
            |G|G|G|
            |G|G|G|
            |G|G|G|
             ¯ ¯ ¯ 
     _ _ _   _ _ _   _ _ _   _ _ _ 
    |Y|Y|Y| |R|R|R| |W|W|W| |O|O|O|
    |Y|Y|Y| |R|R|R| |W|W|W| |O|O|O|
    |Y|Y|Y| |R|R|R| |W|W|W| |O|O|O|
     ¯ ¯ ¯   ¯ ¯ ¯   ¯ ¯ ¯   ¯ ¯ ¯ 
             _ _ _ 
            |B|B|B|
            |B|B|B|
            |B|B|B|
             ¯ ¯ ¯ 
```