from modloader.modclass import Mod, loadable_mod
import jz_magmalink as ml

def tt_bryce1_link():
    ( ml.find_label('bryce1')
        .search_if('persistent.bryce1skip == True')
        .branch()
        .search_menu("Yes. I want to skip ahead.")
        .branch()
        .hook_to('tt_bryce1_skip_menu')
    )

    contest = ml.find_label('waitmenu') \
        .search_menu("Nothing yet. I'll have something later, I think.") \
        .add_choice("Water for me.", jump='tt_bryce1_drink1_waterforme') \
        .search_say("Noted. I'll be right back.") \
        .link_from('tt_bryce1_canon_return_noted_brb') \
        .search_say("It wasn't long before the waiter returned with a drinking bowl as wide as it was tall, filled to the brim with a foam-topped, dark amber liquid. Carefully, he set it down in front of Bryce, who didn't hesitate to take a big gulp.") \
        .search_if("beer == True") \
        .add_entry("tt_bryce1_water == True", jump='tt_bryce1_drink1_waterarrives', after="beer == True") \
        .search_say("There you go. Just call me if you need anything.") \
        .link_from('tt_bryce1_canon_return_afterdrink1') \
        .search_say("Here you go.",depth=300) \
        .search_if("beer == False",depth=20) \
        .add_entry("tt_bryce1_dontdrink == True", jump='tt_bryce1_drink2_dontdrink', before="beer == False") \
        .add_entry("tt_bryce1_water == True", jump='tt_bryce1_drink2_watered_down', before="beer == False") \
        .branch("beer == False") \
            .search_menu("Not really. I guess I can stay for a little while.") \
            .branch() \
                .search_menu("I don't really drink, though.") \
                .branch() \
                    .search_menu("I'll try it just for you.") \
                    .add_choice("I don't drink", jump='tt_bryce1_drink2_pushy') \
                    .add_choice("No.", jump='tt_bryce1_drink2_no') \
        .search_say("You know what, why don't we have ourselves a drinking contest?") \

    contest.search_menu("[[Leave.]") \
        .branch() \
        .search_say("No, thanks. I'm not interested.") \
        .link_from('tt_bryce1_canon_return_leave')

    contest \
        .link_from('tt_bryce1_canon_return_contest') \
        .search_menu("I would, but I don't think I can beat someone like you.") \
        .add_choice("No. Light drinking, please.", jump='tt_bryce1_drink2_light') \
        .search_menu("Maybe. Having a lil' fun doesn't hurt, right?",depth=250) \
        .link_behind_from('tt_bryce1_canon_return_midcontest') \
        .search_menu("Put some pepper on his nose.",depth=250) \
        .branch() \
            .search_say("(Huh... that was actually the salt, not the pepper. Let's try that again.)") \
            .link_behind_from('tt_bryce1_pepperwake_canon') \
            .search_say("That's the best you could come up with?") \
            .hook_to('tt_bryce1_pepperwake',condition='tt_bryce1_minigame.wake_pepper')

@loadable_mod
class AWSWMod(Mod):
    name = "Teetotaller"
    version = "v0.9"
    author = "4onen"
    dependencies = ["MagmaLink"]

    @staticmethod
    def mod_load():
        tt_bryce1_link()

    @staticmethod
    def mod_complete():
        pass