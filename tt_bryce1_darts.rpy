
init:
    python:
        class tt_BlueMap(im.MatrixColor):
            """
            Retints the image so that blues remap to the target
            color while grey shades map to themselves.
            """
            def __init__(self, im, color, **properties):
                c = renpy.easy.color(color)
                self.color = c

                rgb = c.rgb

                matrix = renpy.display.im.matrix(1-rgb[0], 0, rgb[0], 0, 0,
                                                1-rgb[1], 0, rgb[1], 0, 0,
                                                1-rgb[2], 0, rgb[2], 0, 0,
                                                        1, 0,      0, 1, 0)
                super(tt_BlueMap, self).__init__(im, matrix, **properties)

        def tt_player_dart_displayable(_displaytime, _anydisplaytime, imagename, flip=False):
            if flip:
                return (tt_BlueMap(im.Flip(imagename,horizontal=True),persistent.playercolor),None)
            else:
                return (tt_BlueMap(imagename,persistent.playercolor),None)
    
    image tt_bryce1_dart blue = "dartboard/dart.png"
    image tt_bryce1_dart brown = tt_BlueMap("dartboard/dart.png", "#8B4513") # Bryce
    image tt_bryce1_brycedart = 'tt_bryce1_dart brown'
    image tt_bryce1_playerdart = DynamicDisplayable(tt_player_dart_displayable,"dartboard/dart.png")

    image tt_bryce1_darthit brown = tt_BlueMap("dartboard/darthit.png", "#8B4513") # Bryce
    image tt_bryce1_brycedarthit = 'tt_bryce1_darthit brown'
    image tt_bryce1_playerdarthit = DynamicDisplayable(tt_player_dart_displayable,"dartboard/darthit.png")

    image tt_bryce1_darthit right brown = tt_BlueMap("dartboard/darthit2.png", "#8B4513") # Bryce
    image tt_bryce1_brycedarthit right = 'tt_bryce1_darthit right brown'
    image tt_bryce1_brycedarthit left = im.Flip('tt_bryce1_darthit right brown',horizontal=True)
    image tt_bryce1_brycedarthit fall:
        'tt_bryce1_brycedart'
        size (50,150)
        alignaround(0.5,0.5)
        xanchor 0.5
        yanchor 0.5
        parallel:
            easeout_quad 1.5 yoffset 2000
        parallel:
            linear 0.4 rotate 360
            rotate 0
            linear 0.1 rotate 90
            linear 0.2 rotate 180
    image tt_bryce1_playerdarthit right = DynamicDisplayable(tt_player_dart_displayable,"dartboard/darthit2.png")
    image tt_bryce1_playerdarthit left = DynamicDisplayable(tt_player_dart_displayable,im.Flip("dartboard/darthit2.png",horizontal=True))
    image tt_bryce1_playerdarthit fall:
        'tt_bryce1_playerdart'
        size (50,150)
        alignaround(0.5,0.5)
        xanchor 0.5
        yanchor 0.5
        parallel:
            easeout_quad 1.5 yoffset 2000
        parallel:
            linear 0.4 rotate 360
            rotate 0
            linear 0.1 rotate 90
            linear 0.2 rotate 180

    image bg tt_bryce1_dartwall = "dartboard/dartboard_nohanger.png"
    image bg tt_bryce1_dartwall hanger = "dartboard/dartboard_hanger.png"

    image tt_bryce1_board a = "dartboard/boarda.png"
    image tt_bryce1_board b = "dartboard/boardb.png"
    image tt_bryce1_board c = "dartboard/boardc.png"

    image bryce back flip = "cr/bryce_back_flip.png"

    python in tt_bryce1_minigame_darts_store:
        import random
        import math
        def shudder_mouse(drunkedness=1):
            currposition = renpy.get_mouse_pos()
            tpos = (960, 540)
            dir = ((currposition[0] - tpos[0]), (currposition[1] - tpos[1]))
            dirmagnitude = math.sqrt(dir[0]*dir[0] + dir[1]*dir[1])
            if dirmagnitude < 60:
                dir = (dir[0]/dirmagnitude, dir[1]/dirmagnitude)
            else:
                dir = (0,0)
            adjust = drunkedness*random.randint(-4,4), drunkedness*random.randint(-4,4)
            renpy.set_mouse_pos(currposition[0] + 4*dir[0] + adjust[0], currposition[1] + 4*dir[1] + adjust[1])

        class ReturnMousePos(renpy.ui.Action):
            alt = "Throw Dart"

            def __call__(self):
                return renpy.get_mouse_pos()

    screen tt_bryce1_minigame_dart_targeting(drunkedness=0, is_debug=False):
        key "mousedown_1" action tt_bryce1_minigame_darts_store.ReturnMousePos()
        if not is_debug:
            key "game_menu" action [Return(False)]
            timer 0.034 repeat True action Function(tt_bryce1_minigame_darts_store.shudder_mouse,drunkedness)
    
    python in tt_bryce1_minigame_darts_store:
        @renpy.pure
        def hit_target(x,y):
            return (x-960)**2 + (y-540)**2 < (280)**2

        @renpy.pure
        def get_dart_state(xy):
            x,y = xy
            if hit_target(x,y):
                # Hit the board
                return ("left" if x < 820 else ("right" if x > 1100 else "")),x,y

            if x < 860:
                if 230 <= x:
                    return "fall",x,y
                if 190 < x < 230:
                    x = 190
                return ("left" if x < 820 else ""),x,y
            elif 1060 < x:
                if x <= 1690:
                    return "fall",x,y
                if 1690 < x < 1730:
                    x = 1730
                return ("right" if x > 1100 else ""),x,y
            else:
                return "",x,y

        T = renpy.curry(renpy.display.transform.Transform)
        @renpy.pure
        def render_player_dart(click_xy):
            dart_state,x,y = get_dart_state(click_xy)
            if dart_state == "fall":
                renpy.show('tt_bryce1_playerdarthit fall',[T(xpos=x,ypos=y)])
            elif dart_state == "left":
                renpy.show('tt_bryce1_playerdarthit left',[T(xpos=x,ypos=y,xanchor=1.0,yanchor=0.5)])
            elif dart_state == "right":
                renpy.show('tt_bryce1_playerdarthit right',[T(xpos=x,ypos=y,xanchor=0.0,yanchor=0.5)])
            else:
                renpy.show('tt_bryce1_playerdarthit',[T(xpos=x,ypos=y,xanchor=0.5,yanchor=1.0)])
            return dart_state,x,y

        @renpy.pure
        def render_bryce_dart(click_xy):
            dart_state,x,y = get_dart_state(click_xy)
            if dart_state == "fall":
                renpy.show('tt_bryce1_brycedarthit fall',[T(xpos=x,ypos=y)])
            elif dart_state == "left":
                renpy.show('tt_bryce1_brycedarthit left',[T(xpos=x,ypos=y,xanchor=1.0,yanchor=0.5)])
            elif dart_state == "right":
                renpy.show('tt_bryce1_brycedarthit right',[T(xpos=x,ypos=y,xanchor=0.0,yanchor=0.5)])
            else:
                renpy.show('tt_bryce1_brycedarthit',[T(xpos=x,ypos=y,xanchor=0.5,yanchor=1.0)])
            return dart_state,x,y

        @renpy.pure
        def score_boarda(x,y):
            if y>abs(x/4):
                return 2
            elif y<-abs(x/2):
                if (-y-28)**2+x*x < 40*40:
                    return 3
                elif (-y-168)**2+x*x < 90*90:
                    return 2
            return 1

        @renpy.pure
        def score_boardb(x,y):
            if y*y+x*x < 60*60:
                return 3
            elif (y>x) == (y>-x):
                return 2
            else:
                return 1

        @renpy.pure
        def score_boardc(x,y):
            if (44.8-y)**2+x*x < 40*40:
                return 3
            elif (67.2-y)**2+x*x < 113*113:
                return 2
            elif (33.6-y)**2+x*x < 180*180:
                return 2
            elif (0-y)**2+x*x < 247*247:
                return 1
            renpy.error("Unexpected dart landing location %f %f"%(x,y))

        # dart states:
        # -3 dart knocked down board
        # -2 dart hit drywall
        # -1 dart fell off the wall
        # 0  dart hit target, missed scoring zones
        # 1  dart hit target, scored 1
        # 2  dart hit target, scored 2
        # 3  dart hit target, scored 3
        @renpy.pure
        def render_and_score_dart(click_xy,board,renderfn):
            dart_state,x,y = renderfn(click_xy)
            if dart_state == "fall":
                return -1
            elif not hit_target(x,y):
                # TODO: check for board knock down
                return -2
            else:
                im = renpy.load_surface('dartboard/board%s.png'%chr(board+ord('a')))
                px = im.get_at((x-624,y-204))
                if px[2] > (px[0]+px[1])/1.5:
                    # Hit scoring zone; determine which one for the board
                    if board == 0:
                        return score_boarda(x-960,y-540)
                    elif board == 1:
                        return score_boardb(x-960,y-540)
                    elif board == 2:
                        return score_boardc(x-960,y-540)
                    else:
                        renpy.error("Unexpected board number: %r"%board)
                else:
                    # Hit target, missed scoring zone
                    return 0

        def player_throw():
            _return = False
            while not _return:
                _return = renpy.call_screen('tt_bryce1_minigame_dart_targeting')
            return render_and_score_dart(_return,boardup,render_player_dart)
        
        bryce_practice_targets = {
            0: [(923, 677), (931, 672), (1161, 738), (953, 633), (988, 646), (999, 684), (1057, 721), (879, 684), (1107, 596), (1092, 640), (877, 547), (1031, 672), (1101, 716), (899, 639), (803, 643), (1132, 731), (908, 650), (852, 652), (990, 797), (837, 693)],
            1: [(925, 676), (970, 639), (1058, 569), (979, 770), (953, 612), (984, 746), (996, 806), (1006, 284), (951, 697), (941, 705), (923, 696), (982, 681), (997, 478), (968, 786), (960, 705), (954, 598), (947, 656), (878, 613), (894, 616), (921, 748)],
            2: [(903, 526), (960, 545), (1058, 582), (689, 590), (889, 577), (1019, 593), (1123, 544), (880, 509), (908, 620), (752, 536), (989, 524), (1006, 556), (1182, 546), (1148, 507), (946, 621), (1171, 538), (973, 538), (997, 561), (1143, 623), (1048, 489)]
        }
        def bryce_throw(goal_score=None, cheat=False):
            # Goal_score 1 is illegal. Bryce doesn't go for 1s.
            renpy.show('bryce back flip',at_list=[renpy.python.store_dicts['store']['left']])
            renpy.with_statement(renpy.python.store_dicts['store']['dissolve'])
            renpy.pause (0.5)
            if goal_score is None:
                tgt = bryce_practice_targets[boardup][funplayed*3+throwcount]
                return render_and_score_dart((int(tgt[0]),int(tgt[1])),boardup,render_bryce_dart)
            else:
                return render_and_score_dart((950,700),boardup,render_bryce_dart)


label tt_bryce1_minigame_darts:
    python in tt_bryce1_minigame_darts_store:
        funplayed = 0
        throwcount = 0
        # Sourshot:
        # 0: untriggered
        # 1: Bryce landed a 3
        # 2: Player landed next shot
        sourshot = 0

        # Realgame:
        # 0: untriggered
        # 1: Player throw 1
        # 2: Player throw 2
        # 3: Player throw 3
        realgame = 0

        player_score = 0
        bryce_score = 0

        player_misses = 0
        player_drinks = 0

        boarda_available = True
        boarda_picked = False
        boardb_available = True
        boardb_picked = False
        boardc_available = True
        boardc_picked = False
        # Boardup enumeration:
        # 0: Board A
        # 1: Board B
        # 2: Board C
        # None: No board is up
        boardup = None
        boards_fallen = 0
        renpy.pause (0.5)

    scene bg tt_bryce1_dartwall at Pan((0, 460), (0,0), 4.0) with Fade(0.5,0.0,2.0)
    $ renpy.pause(2.7)

    label tt_bryce1_minigame_darts_boardselect:
    scene bg tt_bryce1_dartwall at top with dissolve

    if tt_bryce1_minigame_darts_store.funplayed > 2:
        show bryce brow at right with dissolve
        Br "Not that this isn't mildly amusing, but are we going to play seriously?"
        c "What do you mean?"
        Br normal "We haven't been tracking points so far. Normally this is a competitive game."
        menu:
            "I've been having fun.":
                $ renpy.pause (0.3)
                Br brow "Well, I prefer to have a little bit of challenge to it, rather than just throwing darts at a wall."
                Br normal "Are you sure I can't convince you to play for real?"
                menu:
                    "Yes, I'm sure.":
                        $ renpy.pause (0.3)
                        $ brycemood -= 1
                        Br stern "If you say so. In that case, I'd prefer to move to something else."
                        c "Alright."
                        $ renpy.pause (0.8)
                        jump tt_bryce1_minigame_darts_packup
                    "I guess I can play for real.":
                        $ renpy.pause (0.3)
            "Sure. Let's play for real.":
                $ renpy.pause (0.3)
        Br smirk "That's the spirit."
        jump tt_bryce1_minigame_darts_competitive_boardselect

    if tt_bryce1_minigame_darts_store.boards_fallen < 2:
        Br "Which dartboard do you want to play on?"

    menu:
        "Board A" if tt_bryce1_minigame_darts_store.boarda_available:
            $ tt_bryce1_minigame_darts_store.boardup = 0
        "Board B" if tt_bryce1_minigame_darts_store.boardb_available:
            $ tt_bryce1_minigame_darts_store.boardup = 1
        "Board C" if tt_bryce1_minigame_darts_store.boardc_available:
            $ tt_bryce1_minigame_darts_store.boardup = 2
        "PointPicker" if False:
            jump tt_bryce1_minigame_darts_pointpicker
        "I'm done with this." if any((tt_bryce1_minigame_darts_store.boarda_picked,tt_bryce1_minigame_darts_store.boardb_picked,tt_bryce1_minigame_darts_store.boardc_picked)):
            label tt_bryce1_minigame_darts_donewiththis:
            $ brycemood -= 2
            Br stern "Well, I'm not going to keep doing it if you aren't."
            scene bare with fade
            show bryce stern at center with dissolve
            jump tt_bryce1_minigame_dispatch

    hide bg tt_bryce1_dartwall
    show bg tt_bryce1_dartwall hanger at top
    if tt_bryce1_minigame_darts_store.boardup == 0:
        show tt_bryce1_board a at truecenter with dissolve
        if not tt_bryce1_minigame_darts_store.boarda_picked:
            $ tt_bryce1_minigame_darts_store.boarda_picked = True
            show bryce normal at Position(xpos=0.85) with dissolve
            Br "Well, that's one of the more complex boards."
            Br "Top and bottom are two points, left and right are one, and the dot in the middle is three."
            Br laugh "I mostly aim for the bottom. It's the best I can manage, really."
            show bryce normal with dissolve
            if tt_bryce1_minigame_darts_store.boardup in [0, 1] and all([tt_bryce1_minigame_darts_store.boarda_picked,tt_bryce1_minigame_darts_store.boardb_picked]):
                c "I think I'm seeing a pattern here. The top and bottom versus left and right, it's like the head and body versus shoulders of someone standing upright."
                show bryce brow with dissolve
                c "Then the middle is the neck or clavicle."
                $ brycemood += 1
                Br laugh "I can't say I've ever looked at it that way."
                Br normal "These board designs are all over the place. They've been around for ages, so no telling what whoever invented them meant for them to look like."
    elif tt_bryce1_minigame_darts_store.boardup == 1:
        show tt_bryce1_board b at truecenter with dissolve
        if not tt_bryce1_minigame_darts_store.boardb_picked:
            $ tt_bryce1_minigame_darts_store.boardb_picked = True
            show bryce normal at Position(xpos=0.85) with dissolve
            Br "This board looks simple, but it's not all created equal."
            Br "The usual scoring is that the top and bottom are two points, left and right are one, and the center is three."
            Br brow "That dot in the middle is deceptively hard to hit. At least after a few drinks."
            c "Got it."
            show bryce normal with dissolve
            if tt_bryce1_minigame_darts_store.boardup in [0, 1] and all([tt_bryce1_minigame_darts_store.boarda_picked,tt_bryce1_minigame_darts_store.boardb_picked]):
                c "I think I'm seeing a pattern here. The top and bottom versus left and right, it's like the head and body versus shoulders of someone standing upright."
                show bryce brow with dissolve
                c "Then the middle is the neck or clavicle."
                $ brycemood += 1
                Br laugh "I can't say I've ever looked at it that way."
                Br normal "These board designs are all over the place. They've been around for ages, so no telling what whoever invented them meant for them to look like."
    elif tt_bryce1_minigame_darts_store.boardup == 2:
        show tt_bryce1_board c at truecenter with dissolve
        if not tt_bryce1_minigame_darts_store.boardc_picked:
            $ tt_bryce1_minigame_darts_store.boardc_picked = True
            show bryce stern at Position(xpos=0.85) with dissolve
            Br "This one."
            c "Not a fan?"
            Br brow "There's nowhere really to aim on it that you can miss by a bit and still be sure to score."
            Br "Still, if you want to give it a shot..."
            Br normal "Outermost ring is one point, innermost circle is three, the other two are two points."
            c "Good to know."

    menu tt_bryce1_minigame_darts_playmenu:
        "Maybe a different board." if tt_bryce1_minigame_darts_store.boards_fallen < 2:
            jump tt_bryce1_minigame_darts_boardselect
        "I'm done with this.":
            jump tt_bryce1_minigame_darts_donewiththis
        "Toss a few darts for fun?":
            Br normal "Sure."
            if tt_bryce1_minigame_darts_store.funplayed == 0:
                Br laugh "If I can hit the board, anyway."
            Br "You go first."
            label tt_bryce1_minigame_darts_funtoss:
            hide bryce with dissolve
            python in tt_bryce1_minigame_darts_store:
                funplayed += 1
                throwcount = 0

            while tt_bryce1_minigame_darts_store.throwcount < 3:
                python in tt_bryce1_minigame_darts_store:
                    throwcount += 1
                    s = player_throw()
                    renpy.pause(0.5)
                if tt_bryce1_minigame_darts_store.sourshot == 1:
                    $ tt_bryce1_minigame_darts_store.sourshot = 3
                    if tt_bryce1_minigame_darts_store.s == -3:
                        jump tt_bryce1_minigame_darts_boardfall
                    elif tt_bryce1_minigame_darts_store.s < 0:
                        show bryce smirk at right with dissolve
                        Br "You missed the board."
                        c "I noticed."
                        Br laugh "What was that about all luck?"
                        c "Yeah, yeah."
                        $ brycemood += 1
                        show bryce normal with dissolve
                        hide bryce normal with dissolve
                    elif tt_bryce1_minigame_darts_store.s in [0,1,2]:
                        show bryce normal at right with dissolve
                        c "Swing and a miss."
                        Br smirk "Harder than you thought, huh?"
                        c "A little bit."
                        hide bryce with dissolve
                    elif tt_bryce1_minigame_darts_store.s == 3:
                        show bryce stern at right with dissolve
                        c "See. That's skill."
                        $ brycemood -= 1
                        Br brow "That's you having real hands. Plus you haven't had nearly as much to drink as I have."
                        c "And the fact remains I made that shot on command."
                        Br stern "..."
                        hide bryce with dissolve
                else:
                    if tt_bryce1_minigame_darts_store.s == 3:
                        Br "Good throw."
                    elif tt_bryce1_minigame_darts_store.s <= 0:
                        Br "Miss. Ouch."
                    elif tt_bryce1_minigame_darts_store.s == -3:
                        jump tt_bryce1_minigame_darts_boardfall
                    elif tt_bryce1_minigame_darts_store.s in [1, 2]:
                        pass
                    else:
                        Br "Oops."
                        $ renpy.error("Impossible score: %u"%tt_bryce1_minigame_darts_store.s)

                python in tt_bryce1_minigame_darts_store:
                    if sourshot > 0:
                        sourshot = 4
                    renpy.pause (0.5)
                    s = bryce_throw()
                    renpy.pause (0.8)
                if tt_bryce1_minigame_darts_store.s == 3:
                    $ brycemood += 1
                    if tt_bryce1_minigame_darts_store.sourshot == 0:
                        Br laugh flip "Damn! That was a lucky throw."
                        menu:
                            "Luck is all it was.":
                                $ brycemood -= 1
                                $ renpy.pause (0.8)
                                show bryce brow flip with dissolve
                                Br "If you're so confident, let's see you hit that score next throw."
                                $ tt_bryce1_minigame_darts_store.sourshot = 1
                                if not tt_bryce1_minigame_darts_store.throwcount < 3:
                                    $ tt_bryce1_minigame_darts_store.throwcount = 2
                            "Nice.":
                                $ brycemood += 1
                            "[[Say nothing.]":
                                pass
                        $ renpy.pause (0.5)
                    else:
                        Br laugh flip "Another three-pointer. Maybe this isn't so bad."
                elif tt_bryce1_minigame_darts_store.s == -3:
                    Br "Oops. That came a little close to knocking the board down."
                    # $ brycemood -= 1
                elif tt_bryce1_minigame_darts_store.s <= 0:
                    Br "Damn."
                elif tt_bryce1_minigame_darts_store.s in [1,2]:
                    pass
                else:
                    Br "Oops."
                    $ renpy.error("Impossible score: %u"%tt_bryce1_minigame_darts_store.s)
                hide bryce with dissolve

            if tt_bryce1_minigame_darts_store.funplayed < 3:
                show bryce normal flip at left with dissolve
                Br "Another board?"
                menu:
                    "Sure, I could go for something different.":
                        hide bryce with dissolve
                    "I'd like a few more throws on this one.":
                        Br "Sure."
                        jump tt_bryce1_minigame_darts_funtoss
            jump tt_bryce1_minigame_darts_boardselect
        "Best out of three throws?":
            show bryce smirk at Position(xpos=0.85) with dissolve
            Br "You want to make this a real game? I'll give you three throws." # Second half of this line brought to you by GitHub Copilot.
            Br "Are you sure this is the board you want to play me on?"
            menu:
                "Actually, let's play with the other boards a little more.":
                    Br laugh "Sure thing."
                    jump tt_bryce1_minigame_darts_boardselect
                "Yep.":
                    pass
            jump tt_bryce1_minigame_darts_realgame0

label tt_bryce1_minigame_darts_boardfall:
    show bg tt_bryce1_dartwall
    show tt_bryce1_playerdarthit fall
    with None
    show tt_bryce1_board:
        parallel:
            easeout_quad 1.5 yoffset 2000
        parallel:
            choice:
                linear 3.0 rotate 180
            choice:
                linear 3.0 rotate -180
    $ renpy.pause(2.5)
    hide tt_bryce1_board with None
    python in tt_bryce1_minigame_darts_store:
        boards_fallen += 1
        if boardup == 0:
            boarda_available = False
        elif boardup == 1:
            boardb_available = False
        elif boardup == 2:
            boardc_available = False
    if tt_bryce1_minigame_darts_store.boards_fallen == 1:
        show bryce stern at Position(xpos=0.85) with dissolve
        Br "Did you do that on purpose?"
        menu:
            "No! That was a complete accident.":
                $ brycemood += 1
                Br laugh "Heck of an accident! Damn. Let me go talk to the waiter."
            "I wanted to see if I could.":
                $ brycemood -= 2
                Br brow "Well, you could."
                Br stern "That's not something to be proud of. The material these boards are made out of isn't exactly durable."
                Br "Let me go talk to the waiter."
        show bryce stern flip with dissolve
        $ renpy.pause (0.3)
        hide bryce with easeoutright
        m "He spoke a few moments with the waiter, then both of them returned."
        show waiter at right with easeinright
        Wr "I will have to take this board out of rotation until I can inspect it."
        c "Makes sense."
        show waiter flip with dissolve
        $ renpy.pause (0.3)
        hide waiter with easeoutright
        jump tt_bryce1_minigame_darts_boardselect
    elif tt_bryce1_minigame_darts_store.boards_fallen == 2:
        show bryce brow at Position(xpos=0.85) with dissolve
        $ renpy.pause (0.8)
        Br "Again?"
        menu:
            "I swear that was an accident.":
                $ brycemood -= 1
                Br stern "Well, let me take it over to the waiter."
            "Sure. Why not?":
                $ brycemood -= 3
                Br stern "You saw \"why not\" with the last one."
                Br "I'm not gonna risk any more of his equipment. Put your dart back in the case."
                menu:
                    "I'm sorry.":
                        $ brycemood += 2
                        Br "..."
                    "...":
                        pass
                    "No.":
                        c "We've got one board left. Let's keep playing."
                        if brycemood >= 0:
                            Br brow "I can't believe I'm saying this, but fine. One more game."
                        else:
                            label tt_bryce1_minigame_darts_boardfall_noplay:
                            stop music fadeout 3.0
                            Br stern "I'm not asking, [player_name]."
                            c "Are you about to threaten a human ambassador?"
                            if tt_bryce1_minigame_darts_store.boards_fallen < 3:
                                Br brow "Are you {i}really{/i} going to play that card over a game of darts?"
                                c "I was having fun. Let's put up the last board."
                            else:
                                Br brow "How immature are you?"
                            Br stern "Hand the dart over. Your diplomatic duties ended when you finished telling me about Reza."
                            Br brow "This was me attempting to be friendly with you. But you make that very difficult."
                            m "I turned to leave."
                            Br stern "[player_name]!"
                            scene black with dissolve
                            nvl clear
                            window show
                            n "He didn't follow me out the door of the bar. I made my way home in the darkness without him."
                            n "If his pushing me to drink was his way of manipulating his way close to me, I could stand to live without him."
                            n "And my throws were impressive. If he couldn't see that, that was his problem."
                            n "I had better things to do with my time here."
                            window hide
                            nvl clear
                            python:
                                nodrinks = True
                                brycebar = False
                                brycestatus = "bad"
                            jump tt_bryce1_chapterover_teetotaller
        show bryce stern flip with dissolve
        $ renpy.pause (0.3)
        hide bryce with easeoutright
        jump tt_bryce1_minigame_darts_boardselect
    elif tt_bryce1_minigame_darts_store.boards_fallen == 3:
        $ brycemood -= 1
        show bryce stern at Position(xpos=0.85) with dissolve
        Br "Well, that's the end of that."
        menu:
            "I could go for doing that again.":
                $ brycemood -= 2
                Br brow "Damaging the bar's property? I'd prefer if you didn't."
            "...":
                pass
            "Sorry.":
                Br brow "Then why'd you do it?"
        Br stern "Put your dart back in the case and head back to the table. I'll bring it all back to the waiter and cover your bills from that."
        menu:
            "[[Put the dart away.]":
                pass
            "No.":
                jump tt_bryce1_minigame_darts_boardfall_noplay
        show bryce stern flip with dissolve
        $ renpy.pause (0.3)
        hide bryce with easeoutright
        $ renpy.pause (0.5)
        jump tt_bryce1_minigame_darts_packup


label tt_bryce1_minigame_darts_competitive_boardselect:
    if tt_bryce1_minigame_darts_store.boards_fallen < 2:
        menu:
            Br "Which dartboard should we pick up with?"
            "Board A" if tt_bryce1_minigame_darts_store.boarda_available:
                $ tt_bryce1_minigame_darts_store.boardup = 0
            "Board B" if tt_bryce1_minigame_darts_store.boardb_available:
                $ tt_bryce1_minigame_darts_store.boardup = 1
            "Board C" if tt_bryce1_minigame_darts_store.boardc_available:
                $ tt_bryce1_minigame_darts_store.boardup = 2
    else:
        Br stern "Well, you haven't exactly left us with a lot of choice with which board to finish the game on."
        python in tt_bryce1_minigame_darts_store:
            boardup = [boarda_available,boardb_available,boardc_available].index(True)

    hide bg tt_bryce1_dartwall
    show bg tt_bryce1_dartwall hanger at top
    if tt_bryce1_minigame_darts_store.boardup == 0:
        show tt_bryce1_board a at truecenter with dissolve
    elif tt_bryce1_minigame_darts_store.boardup == 1:
        show tt_bryce1_board b at truecenter with dissolve
    elif tt_bryce1_minigame_darts_store.boardup == 2:
        show tt_bryce1_board c at truecenter with dissolve

    python in tt_bryce1_minigame_darts_store:
        renpy.jump("tt_bryce1_minigame_darts_realgame%u"%realgame)



label tt_bryce1_minigame_darts_realgame0:
    play music "mx/archaic.ogg" fadein 1.0
    ### THROW ONE ###

    if beer == True:
        Br smirk "Let's make this at least a little interesting."
        c "What did you have in mind?"
        Br "Miss the board and you have to drain a glass."
        c "I thought we were trying to avoid heavy drinking?"
        Br laugh "Oh come on. You're barely even buzzed; you'll be fine."

    Br normal "Go ahead, go first."
    if tt_bryce1_minigame_darts_store.funplayed > 0:
        c "Didn't I go first during practice?"
        Br "What's the problem? Didn't you get a good enough idea of how I throw during practice?"
        c "Alright then."
    else:
        c "Alright. If you say so."

    if False:
        label tt_bryce1_minigame_darts_realgame1:
        play music "mx/archaic.ogg" fadein 1.0
        Br "Alright. Want to try that throw again?"



    $ renpy.pause (0.5)
    play sound "fx/woosh3.ogg"
    show round1 at Pan ((-500, -200), (0, -200), 1.0) with wiperight
    $ renpy.pause (2.0)
    hide round1 with wiperight



    hide bryce with dissolve
    python in tt_bryce1_minigame_darts_store:
        realgame = 1
        s = player_throw()
        renpy.pause(0.5)
        player_score += s if s > 0 else 0

    if tt_bryce1_minigame_darts_store.s == -3:
        jump tt_bryce1_minigame_darts_boardfall
    elif tt_bryce1_minigame_darts_store.s <= 0:
        $ tt_bryce1_minigame_darts_store.player_misses += 1
        show bryce smirk flip at left with dissolve
        Br "You missed."
        c "I can see that."
        if beer == True:
            Br laugh flip "Maybe I underestimated how buzzed you were."
            show bryce normal flip with dissolve
            menu:
                "I'm not turning this into a drinking game.":
                    $ brycemood -= 3
                    Br stern "Have it your way."
                "[[Take your drink.]":
                    $ brycemood += 1
                    play sound "mx/gulping.wav"
                    $ renpy.pause (0.5)
                    $ tt_bryce1_minigame_darts_store.player_drinks += 1
                    Br laugh flip "Waiter, [player_name] is going to need another round!"
                    show bryce normal flip with dissolve
    elif tt_bryce1_minigame_darts_store.s <= 2:
        pass
    elif tt_bryce1_minigame_darts_store.s == 3:
        show bryce stern flip at left with dissolve
        Br "A three right out of the gate. Already showing off."
        c "Hey, I want to win, right?"
    else:
        Br "Oops."
        $ renpy.error("tt_bryce1_minigame_darts_realgame1 impossible score.")
    
    python in tt_bryce1_minigame_darts_store:
        renpy.pause(0.5)
        s = bryce_throw(3 if s > 2 else 2)
        renpy.pause(0.5)
        bryce_score += s if s > 0 else 0
    if tt_bryce1_minigame_darts_store.s < 0:
        $ brycemood -= 1
        Br "Damn it."
        menu:
            "You've still got the rest of the game.":
                $ brycemood -= 1
            "[[Say nothing.]":
                pass
        Br "Let me just finish this off."
        $ tt_bryce1_brycedrinks += 1
        play sound "fx/gulp2.wav"
        $ renpy.pause (4.0)
    elif tt_bryce1_minigame_darts_store.s == 0:
        Br "..."
        menu:
            "Ouch.":
                $ brycemood -= 1
                Br "Oh shut it."
            "Well, you hit the board.":
                Br "I suppose that's a good sign."
            "[[Say nothing.]":
                pass
    else: # 1 <= tt_bryce1_minigame_darts_store.s:
        if tt_bryce1_minigame_darts_store.s < 3:
            Br "Oh."
        else:
            Br smirk "Ha!"
        menu:
            "Nice.":
                $ brycemood += 1
            "Damn.":
                $ brycemood -= 1
                Br "Oh don't pretend that makes this any harder for you."
            "[[Say nothing.]":
                pass

    Br "Well, your throw."
    hide bryce with dissolve

    ### THROW TWO ###

    
    if False:
        label tt_bryce1_minigame_darts_realgame2:
        play music "mx/archaic.ogg" fadein 1.0
        Br "Alright. Want to try that throw again?"

        
    python in tt_bryce1_minigame:
        darts_played = True

    hide tt_bryce1_playerdarthit
    hide tt_bryce1_brycedarthit
    with dissolve


    $ renpy.pause (0.5)
    play sound "fx/woosh3.ogg"
    show round2 at Pan ((-500, -200), (0, -200), 1.0) with wiperight
    $ renpy.pause (2.0)
    hide round2 with wiperight



    python in tt_bryce1_minigame_darts_store:
        realgame = 2
        s = player_throw()
        renpy.pause(0.5)
        player_score += s if s > 0 else 0
    if tt_bryce1_minigame_darts_store.s == -3:
        jump tt_bryce1_minigame_darts_boardfall
    elif tt_bryce1_minigame_darts_store.s <= 0:
        $ tt_bryce1_minigame_darts_store.player_misses += 1
        if beer == True:
            if tt_bryce1_minigame_darts_store.player_drinks > 0:
                show bryce brow flip at left with dissolve
                Br "You okay, there?"
                c "Nothing I can't handle."
                play sound "fx/gulp2.wav"
                $ brycemood += 1
            elif tt_bryce1_minigame_darts_store.player_misses > 1 and tt_bryce1_minigame_darts_store.player_drinks == 0:
                show bryce stern flip at left with dissolve
                Br stern "..."
                menu:
                    "Okay, okay. I'll drink for it.":
                        $ brycemood += 1
                        play sound "fx/gulp2.wav"
                        $ renpy.pause(5.0)
                        $ tt_bryce1_minigame_darts_store.player_drinks += 1
                    "[[Say nothing.]":
                        pass
            else:
                menu:
                    "I'm not turning this into a drinking game.":
                        $ brycemood -= 3
                        Br stern "Have it your way."
                    "[[Take your drink.]":
                        $ brycemood += 1
                        play sound "mx/gulping.wav"
                        $ renpy.pause (0.5)
                        $ tt_bryce1_minigame_darts_store.player_drinks += 1
                        Br laugh flip "Waiter, [player_name] is going to need another!"
                        show bryce normal flip with dissolve
        else:
            if tt_bryce1_minigame_darts_store.s < 0:
                show bryce brow flip at left with dissolve
                Br "You're kidding, right?"
                c "Maybe it's a good thing I'm not drinking, then. Aim that bad on alcohol, I could have hit another patron."
                Br laugh flip "Fair enough."
                show bryce normal flip with dissolve
            else: # tt_bryce1_minigame_darts_store.s == 0:
                show bryce brow flip at left with dissolve
                if tt_bryce1_minigame_darts_store.bryce_score > 1:
                    Br "Hm. Miss. That's going to be tough to make up."
                else:
                    Br stern flip "You don't have to miss to keep our scores even."
                    menu:
                        "I was {i}so{/i} close.":
                            $ brycemood += 1
                            Br smirk flip "If you say so."
                        "That wasn't on purpose.":
                            Br normal flip "If you say so."
                        "Sorry.":
                            $ brycemood -= 2
                            Br stern flip "Just don't. No pity shots."
    elif tt_bryce1_minigame_darts_store.s <= 2:
        pass
    elif tt_bryce1_minigame_darts_store.s == 3:
        if tt_bryce1_minigame_darts_store.player_score > 3 and tt_bryce1_minigame_darts_store.bryce_score < 3:
            show bryce sad flip at left with dissolve
            c "You okay?"
            Br stern flip "Fine. This game's far from over."
        else:
            show bryce stern flip at left with dissolve
            Br "Good throw."
            c "Thanks."
    else:
        Br "Oops."
        $ renpy.error("tt_bryce1_minigame_darts_realgame2 impossible score.")

    c "Your turn."

    python in tt_bryce1_minigame_darts_store:
        renpy.pause(0.5)
        s = bryce_throw(3 if s > 2 else 2)
        renpy.pause(0.5)
        bryce_score += s if s > 0 else 0
    if tt_bryce1_minigame_darts_store.s < 0:
        hide bryce with dissolve
        $ tt_bryce1_brycedrinks += 1
        play sound "fx/gulp3.wav"
        $ renpy.pause (6.0)



    if tt_bryce1_minigame_darts_store.player_score > tt_bryce1_minigame_darts_store.bryce_score:
        if tt_bryce1_minigame_darts_store.player_score - tt_bryce1_minigame_darts_store.bryce_score > 3:
            $ brycemood -= 1
            show bryce stern flip at left with dissolve
            Br "Now we know this game is over."
            c "What, you're giving up?"
            Br brow flip "There's nothing to give up. I can't win."
            c "Oh. Huh. Guess I do win, then."
            Br stern flip "Maybe this was a bad idea to begin with."
            label tt_bryce1_minigame_darts_brycegiveup:
            Br "I'll pack up. You head back to the table."
            hide bryce with dissolve
            $ renpy.pause(0.5)
            jump tt_bryce1_minigame_darts_packup
        else:
            if brycemood > 0:
                show bryce laugh flip at left with dissolve
            else:
                show bryce brow flip at left with dissolve
            Br "Guess I'm not doing so well."
            menu:
                "You're still in the running.":
                    Br normal "Suppose so."
                "You're doing really well, considering.":
                    $ brycemood -= 1
                    Br stern "Considering the alcohol, or the lack of hands?"
                    Br "Forget it. Let's just play the last throw."
                "On way more alcohol than me, though.":
                    $ brycemood += 1
                    Br laugh flip "Very true!"
                    Br normal flip "So. Last throw."
    elif tt_bryce1_minigame_darts_store.player_score == tt_bryce1_minigame_darts_store.bryce_score:
        $ brycemood += 1
        show bryce smirk flip at left with dissolve
        Br "Neck and neck, huh?"
        if tt_bryce1_minigame_darts_store.player_score == 0:
            c "I'm not sure neck and neck at zero is that intense."
            Br laugh flip "I'm not sure either."
            Br normal flip "Funny though. So, last throw?"
        else:
            c "Anything can happen."
    else: # bryce_score > player_score
        if tt_bryce1_minigame_darts_store.bryce_score - tt_bryce1_minigame_darts_store.player_score > 3 or tt_bryce1_minigame_darts_store.player_score < 2:
            $ brycemood -= 1
            show bryce brow flip at left with dissolve
            Br "You threw the game."
            c "Sorry?"
            if tt_bryce1_minigame_darts_store.bryce_score - tt_bryce1_minigame_darts_store.player_score > 3:
                Br stern flip "There's no way I'm beating you and your hands by more than three points without you trying not to win."
            elif tt_bryce1_minigame_darts_store.player_misses > 1:
                Br stern flip "There's no way you and your hands missed the board both throws."
            else:
                Br stern flip "There's no way you and your hands just chose to score that low."
            menu:
                "I played badly on purpose.":
                    c "I thought it would cheer you up to win at this."
                    show bryce brow flip
                    $ renpy.pause (0.5)
                    Br "It's not fun if we're counting points and pretending to play when we both know who's going to win."
                "[[Say nothing.]":
                    $ brycemood -= 1
                "That totally wasn't on purpose.":
                    Br brow flip "I don't buy that."
                    if beer == True:
                        c "Maybe it was the alcohol."
                    else:
                        c "I don't know what happened."
                    c "But I didn't mean to throw the game."
                    if tt_bryce1_minigame_darts_store.player_misses > 1:
                        Br stern flip "Well, it wasn't fun to watch you miss the board that much."
                    elif tt_bryce1_minigame_darts_store.player_score < 1:
                        Br stern flip "Well, it wasn't fun to watch you miss the scoring zones every time."
                    elif tt_bryce1_minigame_darts_store.player_score < 2:
                        Br stern flip "Well, it wasn't fun to watch you miss, or aim for low-point zones."
                    else:
                        Br stern flip "Well, it wasn't fun to watch you miss the high-score zones as if it was intentional."
                    c "Sorry."
            Br "I'll pack up. You head back to the table."
            hide bryce with dissolve
            $ renpy.pause(0.5)
            jump tt_bryce1_minigame_darts_packup
        else:
            $ brycemood += 1
            show bryce laugh flip at left with dissolve
            Br "How am I winning?"
            menu:
                "I'm a lightweight." if beer == True:
                    c "I'm going to guess the alcohol hits me harder than it hits you."
                    Br smirk flip "Maybe. That works for me."
                "I'm at a complete loss.":
                    show bryce brow flip with dissolve
                    $ renpy.pause (0.8)
                "Your darts are different from the ones back home.":
                    show bryce normal flip with dissolve
                    c "Why is there a fin in the middle of the dart like this?"
                    $ brycemood += 1
                    Br laugh flip "More surface for dragons like me to hold it."
                    c "Huh."
            Br normal flip "Alright. Last throw."


    ### THROW THREE ###

    hide tt_bryce1_playerdarthit
    hide tt_bryce1_brycedarthit
    with dissolve

    $ renpy.pause (0.5)
    play sound "fx/woosh3.ogg"
    show round3 at Pan ((-500, -200), (0, -200), 1.0) with wiperight
    $ renpy.pause (2.0)
    hide round3 with wiperight
    hide bryce with dissolve

    python in tt_bryce1_minigame_darts_store:
        realgame = 3
        s = player_throw()
        renpy.pause(0.5)
        player_score += s if s > 0 else 0
    if tt_bryce1_minigame_darts_store.s == -3:
        jump tt_bryce1_minigame_darts_boardfall
    elif tt_bryce1_minigame_darts_store.s < 1:
        show bryce stern flip at left with dissolve
        if tt_bryce1_minigame_darts_store.s < 0:
            Br "You missed the board entirely. On the last throw."
        else:
            Br "You missed any scoring zone. On the last throw."
        $ brycemood -= 1
        if tt_bryce1_minigame_darts_store.player_drinks > 0:
            play sound "fx/gulp2.wav"
            $ brycemood += 1
            Br normal flip "Fair enough."
        elif beer and tt_bryce1_minigame_darts_store.player_misses < 1:
            menu:
                "I'm not turning this into a drinking game.":
                    $ brycemood -= 3
                    Br stern "Have it your way."
                "[[Take your drink.]":
                    play sound "fx/gulp2.wav"
                    Br brow flip "Drinking now doesn't exactly help explain how you missed then."
                    menu:
                        "Misses happen.":
                            c "What are the scores?"
                        "I messed up to make you feel better.":
                            $ brycemood -= 2
                            Br stern "I'm pretty sure I asked you not to take any pity shots."
                            c "Well, too bad."
                            Br "If you were planning this from the start, this whole thing was a stupid idea."
                            c "Hey, I was trying to make this night better for you."
                            Br brow "And you thought winning unfairly at darts would provide that for me?"
                            jump tt_bryce1_minigame_darts_brycegiveup
        elif beer:
            $ brycemood -= 1
        else:
            if tt_bryce1_minigame_darts_store.s < 0:
                Br "You have hands. How could you fail at this?"
                c "Maybe it's not as easy as it looks?"
                Br brow flip "With {i}fingers{/i}?"
                c "Look, stop freaking out about it and check our scores."
                Br "..."
            else:
                Br "You have hands. How could you miss this?"
                c "I was trying! Look how close I got it."
                show bryce back flip with dissolve
                m "Bryce inspected the board for a long moment, then pawed his head as he considered the scores."





    if tt_bryce1_minigame_darts_store.player_score - tt_bryce1_minigame_darts_store.bryce_score > 3:
        show bryce stern flip at left with dissolve
        Br "And that's the game."
        c "I mean, we don't have to skip your last turn. Let's at least see how close you got, right?"
        Br back flip "..."
        python in tt_bryce1_minigame_darts_store:
            renpy.pause(0.5)
            s = bryce_throw(2,True)
            renpy.pause(0.5)
            bryce_score += s if s > 0 else 0
        c "You just aimed for a two again?"
        Br brow flip "I told you that's the best I can usually do."
        c "Fair. Still, one more throw and I think you could tie me up."
        Br stern flip "Not how the game works, unfortunately. Still..."
    elif tt_bryce1_minigame_darts_store.player_score - tt_bryce1_minigame_darts_store.bryce_score >= 2:
        show bryce stern flip at left with dissolve
        if tt_bryce1_minigame_darts_store.player_score - tt_bryce1_minigame_darts_store.bryce_score == 3:
            Br "Damn this. There's no way I make that shot to tie."
        else: # == 2
            Br "Damn this. There's no way I make that shot to win. Not even sure I can tie."
        c "You miss 100%% of the shots you don't take."
        Br back flip "..."
        m "Bryce stared down the board for a long, long moment, then threw."
        python in tt_bryce1_minigame_darts_store:
            renpy.pause(1.5)
            s = bryce_throw(player_score - bryce_score,True)
            renpy.pause(0.5)
            bryce_score += s if s > 0 else 0
        $ brycemood += 3
        Br laugh flip "I made it!"
        c "You made it!"
        Br flirty flip "Holy heck. That was close. And yet I tied up you and your hands."
        c "Yeah, that was awesome."
        show bryce smirk flip with dissolve
        c "Wait, what?"
    else: # tt_bryce1_minigame_darts_store.player_score - tt_bryce1_minigame_darts_store.bryce_score < 2:
        if tt_bryce1_minigame_darts_store.player_score - tt_bryce1_minigame_darts_store.bryce_score < 1:
            Br brow flip "I score even a one, I'm going to win."
        else:
            Br stern flip "Gotta make a two."
        c "All up to you."
        Br back flip "..."
        m "Bryce stared down the board for a long, long moment, then threw."
        python in tt_bryce1_minigame_darts_store:
            renpy.pause(1.5)
            s = bryce_throw(2,True)
            renpy.pause(0.5)
            bryce_score += s if s > 0 else 0
        $ brycemood += 1
        c "You hit it!"
        Br normal flip "I did."
        Br brow flip "Not as satisfying as I thought it would be."
        c "Well, enjoy it. Next time I'll practice more."
        Br normal flip "Maybe I will too."
    Br normal flip "This was pretty fun. Let me pack up and I'll see you back at the table."
    c "Sure."
    hide bryce with dissolve
    jump tt_bryce1_minigame_darts_packup

label tt_bryce1_minigame_darts_packup:
    if tt_bryce1_minigame_darts_store.realgame > 0:
        play music "mx/clouds.ogg" fadein 1.0
    $ renpy.pause(0.5)
    scene bare with fade
    jump tt_bryce1_minigame_dispatch

label tt_bryce1_minigame_darts_pointpicker:
    scene bg tt_bryce1_dartwall hanger at top
    menu:
        "PointPicker Root"
        "Board A":
            $ tt_bryce1_minigame_darts_store.boardup = 0
            show tt_bryce1_board a at truecenter with dissolve
        "Board B":
            $ tt_bryce1_minigame_darts_store.boardup = 1
            show tt_bryce1_board b at truecenter with dissolve
        "Board C":
            $ tt_bryce1_minigame_darts_store.boardup = 2
            show tt_bryce1_board c at truecenter with dissolve
        "Return":
            jump tt_bryce1_minigame_darts

    python in tt_bryce1_minigame_darts_store:
        _return = True
        while _return:
            _return = renpy.call_screen('tt_bryce1_minigame_dart_targeting')
            playerdartpos = renpy.get_mouse_pos()
            print(playerdartpos,render_and_score_dart(playerdartpos,boardup,render_player_dart))
    
    play sound "fx/system3.wav"
    jump tt_bryce1_minigame_darts_pointpicker
