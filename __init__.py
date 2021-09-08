from modloader.modclass import Mod, loadable_mod

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