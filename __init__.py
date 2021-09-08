from modloader.modclass import Mod, loadable_mod

#### Utilities

# def find_say_in_file(needle,filename):
#     """Find a :class:`renpy.ast.Say` node based on what is said and in what file

#     This searches the entire AST tree for the specified statement.

#     Args:
#         needle (str): The statement to search for
#         filename (str): The rpy file to search in, from the game root

#     Returns:
#         A :class:`renpy.ast.Node` node
#     """
#     for node in renpy.game.script.all_stmts:
#         if isinstance(node, ast.Say) and node.filename == filename and node.what == needle:
#             return node
#     return None

# def format_node(node):
#     if node is not None:
#         return "%s %s:%u: %s"%(str(node.__name__),node.filename,node.linenumber,node.get_code())
#     return "None"

# def debugPrint(msg):
#     debug = True
#     if debug:
#         modloader.modgame.sprnt(msg)

# def tterr(msg):
#     renpy.error("Teetotaller mod: "+msg)

# def call_if_renpy_global(node, dest, global_name, return_node=None):
#     if isinstance(dest,str):
#         dest_node = modast.find_label(dest)
#     else:
#         if not isinstance(dest,ast.Node):
#             renpy.error("Non-node, non-label passed to call_if_renpy_global destination!")
#             return None
#         else:
#             dest_node = dest

#     def call_function(hook):
#         if renpy.python.store_dicts["store"][global_name]:
#             label = renpy.game.context().call(dest_node.name,
#                 return_site=hook.old_next.name if return_node is None else
#                 return_node.name)
#             hook.chain(label)

#     return modast.hook_opcode(node,call_function)

# def sayCondition(words):
#     return (lambda n: (isinstance(n,ast.Say) and n.what==words))

# #### Linkups

# def bryce1_menu_descent_into_madness(bryce1_drink2_if_playernodrink):
#     if1_block = None
#     for cond, block in bryce1_drink2_if_playernodrink.entries:
#         if cond == 'beer == False':
#             if1_block = block
#             break
#     if if1_block is None:
#         tterr("Unable to descend into Bryce1 menu madness: 'beer == False' gone from If")

#     bryce1_menu_stayalittle = modast.search_for_node_type(if1_block[0],ast.Menu)
#     if bryce1_menu_stayalittle is None:
#         tterr("Unable to descend into Bryce1 menu madness: stay a little menu missing.")
#     bryce1_say_guessicanstay = ml.get_menu_hook(bryce1_menu_stayalittle).get_option_code("Not really. I guess I can stay for a little while.")[0]
    
#     bryce1_menu_tryalittle = modast.search_for_node_type(bryce1_say_guessicanstay,ast.Menu)
#     if bryce1_menu_stayalittle is None:
#         tterr("Unable to descend into Bryce1 menu madness: try a little menu missing.")
#     bryce1_say_idontdrinktho = ml.get_menu_hook(bryce1_menu_tryalittle).get_option_code("I don't really drink, though.")[0]
#     if bryce1_say_idontdrinktho is None:
#         tterr("Unable to descend into Bryce1 menu madness: \"I don't really drink, though.\" missing from menu2.")

#     bryce1_menu_tryalittle = modast.search_for_node_type(bryce1_say_idontdrinktho,ast.Menu)
#     if bryce1_say_idontdrinktho is None:
#         tterr("Unable to find menu in Bryce1 menu madness: \"I'll try it just for you,\" menu missing from \"I don't really drink, though.\"")
#     bryce1_menu_tryalittle_hook = ml.get_menu_hook(bryce1_menu_tryalittle)
#     bryce1_menu_tryalittle_hook.add_item("I don't drink.",modast.find_label('tt_bryce1_drink2_pushy'))
#     bryce1_menu_tryalittle_hook.add_item("No.",modast.find_label('tt_bryce1_drink2_no'))



# def bryce1_tt():
#     bryce1_waitmenu = modast.find_label('waitmenu')
#     modast.call_hook(bryce1_waitmenu,modast.find_label('tt_bryce1_variablesetup'),None)
#     bryce1_drink1_menu_node = modast.search_for_node_type(bryce1_waitmenu,ast.Menu)
#     bryce1_drink1_menu = ml.get_menu_hook(bryce1_drink1_menu_node)
#     bryce1_drink1_menu.add_item("Water for me.",modast.find_label('tt_bryce1_drink1_waterforme'))
#     bryce1_drink1_say_notedbrb = modast.search_for_node_with_criteria(bryce1_drink1_menu_node,sayCondition("Noted. I'll be right back."))
#     modast.find_label('tt_bryce1_canon_return_noted_brb').chain(bryce1_drink1_say_notedbrb)

#     bryce1_drink1_arrives = modast.search_for_node_with_criteria(bryce1_drink1_say_notedbrb,sayCondition("It wasn't long before the waiter returned with a drinking bowl as wide as it was tall, filled to the brim with a foam-topped, dark amber liquid. Carefully, he set it down in front of Bryce, who didn't hesitate to take a big gulp."))
#     call_if_renpy_global(bryce1_drink1_arrives,'tt_bryce1_drink1_waterarrives','tt_bryce1_water')

#     bryce1_drink2_arrives = modast.search_for_node_with_criteria(bryce1_drink1_arrives,sayCondition("Here you go."),max_depth=300)
#     bryce1_drink2_if_playernodrink = modast.search_for_node_type(bryce1_drink2_arrives,ast.If,max_depth=20)
#     bryce1_drink2_if_playernodrink.entries.insert(0,('tt_bryce1_water and not tt_bryce1_dontdrink',[modast.find_label('tt_bryce1_drink2_watered_down')]))
#     bryce1_drink2_if_playernodrink.entries.insert(0,('tt_bryce1_dontdrink',[modast.find_label('tt_bryce1_drink2_dontdrink')]))
#     bryce1_menu_descent_into_madness(bryce1_drink2_if_playernodrink)

#     bryce1_drinkingcontest = modast.search_for_node_with_criteria(bryce1_drink2_arrives,sayCondition("You know what, why don't we have ourselves a drinking contest?"))
#     modast.find_label('tt_bryce1_canon_return_contest').chain(bryce1_drinkingcontest)

@loadable_mod
class AWSWMod(Mod):
    @staticmethod
    def mod_info():
        return ("Teetotaller", "v0.2", "4onen", False)

    @staticmethod
    def mod_load():
        pass # bryce1_tt()

    @staticmethod
    def mod_complete():
        pass