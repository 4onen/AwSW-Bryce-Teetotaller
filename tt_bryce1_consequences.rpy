init python:
    def tt_bryce1_consequences_link(ml):
        ml.find_label('chapter2chars') \
            .search_if('brycestatus == "good"') \
            .search_if('brycestatus == "good"') \
            .branch() \
            .search_if('bryce3unplayed == False') \
            .branch_else() \
            .search_if('bryce1unheard == True') \
            .branch() \
            .search_python('renpy.pause (0.5)') \
            .hook_to('tt_bryce1_c2_answ_fix') \
            .search_say("I think you had some fun too, but I also wanted to show you there's more to me than that.") \
            .link_from('tt_bryce1_c2_answ_fix_end')
        ml.find_label('chapter3chars') \
            .search_if('brycestatus == "good"') \
            .search_if('brycestatus == "good"') \
            .branch() \
            .search_if('bryce3unplayed == False') \
            .branch_else() \
            .search_if('bryce1unheard == True') \
            .branch() \
            .search_python('renpy.pause (0.5)') \
            .hook_to('tt_bryce1_c3_answ_fix') \
            .search_say("I think you had some fun too, but I also wanted to show you there's more to me than that.") \
            .link_from('tt_bryce1_c3_answ_fix_end')
        ml.find_label('chapter4chars') \
            .search_if('brycedead == False') \
            .search_if('brycedead == False') \
            .branch() \
            .search_if('brycestatus == "good"') \
            .branch() \
            .search_if('bryce3unplayed == False') \
            .branch_else() \
            .search_if('bryce1unheard == True') \
            .branch() \
            .search_python('renpy.pause (0.5)') \
            .hook_to('tt_bryce1_c4_answ_fix') \
            .search_say("I think you had some fun too, but I also wanted to show you there's more to me than that.") \
            .link_from('tt_bryce1_c4_answ_fix_end')
    tt_bryce1_consequences_link(magmalink())

label tt_bryce1_c2_answ_fix:
    Br "Hey. I was just thinking about last time. I know I got a little close to blackout drunk, but I still thought that was kinda fun."
    jump tt_bryce1_c2_answ_fix_end
label tt_bryce1_c3_answ_fix:
    Br "Hey. I was just thinking about last time. I know I got a little close to blackout drunk, but I still thought that was kinda fun."
    jump tt_bryce1_c3_answ_fix_end
label tt_bryce1_c4_answ_fix:
    Br "Hey. I was just thinking about last time. I know I got a little close to blackout drunk, but I still thought that was kinda fun."
    jump tt_bryce1_c4_answ_fix_end