init python:
    import os
    newversion=["0.12.6","0.12.7","0.12.8"]
    #假设现在为老版本
    p_is_old_ver = True

    for x in newversion:
        if renpy.config.version == x and not renpy.android:
            p_is_old_ver = False
            os.remove(renpy.config.basedir + "/game/Submods/Dialogue Packs/mas_after125_topics"),
