init python: # Magmalink required!
    def tt_bryce1_link(ml):
        ml.find_label('waitmenu') \
            .hook_call('tt_bryce1_variablesetup') \
            .search_menu("Nothing yet. I'll have something later, I think.") \
            .add_choice("Water for me.", jump='tt_bryce1_drink1_waterforme', condition='True') \
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
                        .add_choice("I don't drink", jump='tt_bryce1_drink2_pushy', condition='True') \
                        .add_choice("No.", jump='tt_bryce1_drink2_no', condition='True') \
            .search_say("You know what, why don't we have ourselves a drinking contest?") \
            .link_from('tt_bryce1_canon_return_contest') \
            .search_menu("I would, but I don't think I can beat someone like you.") \
            .add_choice("No. Light drinking, please.", jump='tt_bryce1_drink2_light', condition='True')
    tt_bryce1_link(magmalink())

label tt_bryce1_variablesetup:

default tt_bryce1_water = False
default tt_bryce1_dontdrink = False
default tt_bryce1_drinkincident = None

python:
    tt_bryce1_water = False
    tt_bryce1_dontdrink = False
    tt_bryce1_drinkincident = None
call tt_bryce1_minigame_variable_setup
return

label tt_bryce1_chapterover_teetotaller:
    if persistent.c1teetotaler == False and not beer:
        python:
            persistent.c1teetotaler = True
            achievement.grant("Teetotaler")
            persistent.achievements += 1
            # renpy.pop_call()
        call syscheck
        play sound "fx/system.wav"
        if system=="normal":
            s "You rejected Bryce's invitations to drink!"
        elif system=="advanced":
            s "You rejected Bryce's invitations to drink. That was harsh."
        else:
            s "You rejected Bryce's invitations to drink. I hear you're missing out."
label tt_bryce1_chapterover:
    $ brycescenesfinished = 1
    jump _mod_fixjmp

# Linked to `c "I really think I should be going."` by the linkup scripts.
jump tt_bryce1_canon_return_leave

label tt_bryce1_drink1_waterforme:
    if brycemood >= 1:
        $ brycemood = 0
        Br brow "I suggested talking over a beer at the station and you said you'd have three. What happened to that? You're just having water?"
    else:
        Br brow "You're at a bar and you're getting water? You're not going to live even a little?"
    menu:
        "Yep.":
            $ tt_bryce1_water = True
            c "Why, is that a problem?"
            $ brycemood -= 1
            Br "I suppose not."
            show bryce normal with dissolve
        "I don't drink.":
            call tt_bryce1_dontdrink_callsite
            $ tt_bryce1_water = tt_bryce1_dontdrink
        "I need a clear head to be an ambassador.":
            c "How would your people look at mine if they see me drunkenly stumbling about?"
            Br stern "Fair enough. But that's a difficult position to be in, never letting yourself off the clock."
            Br normal "As the chief of police, I am responsible for your safety. That includes making sure you get home tonight without making a fool of yourself."
            Br smirk "You sure you don't want anything?"
            menu:
                "I'll have what you're having.":
                    Br laugh "There we go."
                    show bryce normal with dissolve
                "Maybe I'll just pass on drinking anything.":
                    $ brycemood -= 1
                    show br stern with dissolve
                "Just water, thanks.":
                    $ tt_bryce1_water = True
                    Br normal "If you insist."
        "I'm worried about my injuries.":
            c "Maverick knocked me over pretty hard the other night. Alcohol has a mild blood thinning effect, so I'd just like to play it safe in case anything's still tumbled about in my insides."
            $ tt_bryce1_water = True
            $ brycemood -= 1
            Br stern "I see."
        "Changed my mind. What Bryce is having.":
            $ brycemood += 1
            $ beer = True
            show bryce smirk with dissolve
        "Changed my mind. Nothing for now.":
            c "I might have something later, I think."
            show bryce normal with dissolve
    
    if tt_bryce1_water == True:
        Br normal "Well, the usual for me and water for [player_name]."

# Linked to `Wr "Noted. I'll be right back."` by the linkup scripts.
jump tt_bryce1_canon_return_noted_brb

label tt_bryce1_dontdrink_callsite(tt_bryce1_talked_about_reza=False):
    Br brow "Just flat don't? Ever?"
    if brycemood>0:
        $ brycemood = 0
        Br stern "What was that back at the station, then? I suggested talking over a beer and you said you wanted three."
        c "A joke?"
        Br brow "A confusing one without the right context."
    $ renpy.pause (0.8)
    Br "Can I ask you why?"
    menu:
        "No.":
            $ tt_bryce1_dontdrink = True
            c "You can't ask."
            $ brycemood -= 2
            Br stern "I see."
        "Medical reasons.":
            $ tt_bryce1_dontdrink = True
            c "I don't want to get too much into it. Put simply: I can't."
            Br sad "Damn. I'm sorry to hear that."
            c "Let's just move on."
        "Personal reasons.":
            $ tt_bryce1_dontdrink = True
            c "It's... complicated, and not exactly material for your first night out with someone."
            Br smirk "Not without enough alcohol?"
            c "No. That's... no."
            Br sad "Ah. Sorry. I crossed a line, didn't I?"
            c "Let's just move on."
        "My faith prohibits it.":
            $ tt_bryce1_dontdrink = True
            Br "Your faith in what?"
            c "Humanity has a large number of religions, most describing some god or gods that created our world."
            c "I believe in one of these. And, in my religion's history, our creator sent us a message that we should not partake in alcohol consumption."
            if tt_bryce1_talked_about_reza == False:
                c "Human religion can get really complicated. I could spend hours explaining the few I know about, but I think talking about Reza is going to be more important to both of us."
            else:
                c "Human religion can get really complicated. I could spend hours explaining the few I know about. I'm sure that's not what you came here for tonight."
            Br normal "It sure sounds complicated. Hundreds? How can you even be sure you've picked the right one?"
            Br laugh "And if you didn't, why bother with the rules?"
            show bryce smirk with dissolve
            c "That's a good question. But the point of religion is to have faith in whichever path you pick. Believing in something means following its rules, among other things."
            Br normal "I see."
        "Don't like it.":
            c "I just don't want to drink. Is that so weird?"
            Br normal "It kinda is. I can't say I've ever met anyone who didn't drink at least a little who didn't have some reason."
            Br laugh "Just try a little? Even if you don't like beer, you haven't had one like this before."
            menu:
                "Okay. I'll try it just for you.":
                    $ beer = True
                    Br "You're doing yourself a favor."
                "No, thanks.":
                    $ tt_bryce1_dontdrink = True
                    $ brycemood -= 1
                    Br stern "Suit yourself."
                "[[Leave.]":
                    $ renpy.pop_call()
                    jump tt_bryce1_canon_return_leave
        "Drinking is abhorrent.":
            if tt_bryce1_talked_about_reza == False:
                c "The only reason I'm here is to tell you about Reza. As soon as I'm done, you can do whatever the hell you want to yourself. Not that you'll probably even remember what I tell you."
            else:
                c "I honestly don't know why I'm still here. I've already told you what I know about Reza, not that you'll probably even remember."
            Br stern "Excuse me?"
            c "Did I misspeak? Or are you already mishearing me from accumulated liver damage?"
            Br "Damn. That's it. If you're so upset being here, you should leave."
            if tt_bryce1_talked_about_reza == False:
                c "So you dragged me out here and won't even do your job? What was all that about my knowledge of Reza being helpful?"
                Br brow "I made clear I was off the clock when I left my badge at the station, didn't I?"
                Br stern "I was going to be happy to pass along whatever you had to tell me."
                Br "But if it's so difficult for you to be here, you can tell someone else tomorrow."
                label tt_bryce1_ending_badevening:
                Br "Now get out, before you ruin anyone else's evenings."
            scene black with dissolve
            stop music fadeout 1.0

            nvl clear
            window show
            n "Without another word, I got up from my seat and left."
            n "Luckily, I didn't have much trouble finding my way back alone. I certainly couldn't stand spending any more time with someone like Bryce."
            n "Needless to say, I didn't regret leaving him behind."
            window hide
            nvl clear

            python:
                nodrinks = True
                brycebar = False
                brycestatus = "bad"

            jump tt_bryce1_chapterover_teetotaller
    return

label tt_bryce1_drink1_waterarrives:
    m "He brought my water as well, provided in a glass that seemed more appropriate for my kind."
# Linked to `Wr "There you go. Just call me if you need anything."` by the linkup scripts
jump tt_bryce1_canon_return_afterdrink1


label tt_bryce1_drink2_watered_down:
    Br brow "So you're serious about sticking to water tonight?"
    menu:
        "Yeah. Just water.":
            $ renpy.pause (0.5)
            Br stern "That's hardly a way to enjoy an evening out."
            c "Well, I'm not exactly looking for an evening I can't remember."
            jump tt_bryce1_drink2_lightordry
        "Maybe a little drink won't hurt.":
            python:
                tt_bryce1_water = False
                tt_bryce1_dontdrink = False
                beer = True
            c "I mean, I guess I'm in another world and I'm already at the bar. If not tonight, am I going to keep making excuses?"
            Br smirk "That's the spirit."
            # Br laugh "Waiter, bring us another beer."
            # c "Not as big as yours!"
            # Br normal "Of course not. He knows to scale things by body mass."
            # Br smirk "Although..."

# Linked to `Br "You know what, why don't we have ourselves a drinking contest?"` by the linkup scripts.
jump tt_bryce1_canon_return_contest

label tt_bryce1_drink2_no:
    Br stern "So you came out to a bar to not have anything? Just give it a try."
    m "Having made my decision clear, I'm not sure what else to do to get through to him. I waited in silence until the waiter arrived with the drink."
    $ renpy.pause (0.3)
    show bryce normal at right with ease
    show waiter flip at left with easeinleft
    play sound "fx/glasses.wav"
    $ renpy.pause (0.2)
    show waiter
    menu:
        "[[Pour your drink into Bryce's.]":
            stop music fadeout 2.0
            $ renpy.pause (0.3)
            play sound "fx/pour.ogg"
            show bryce brow with dissolve
            python:
                tt_bryce1_drinkincident = "pour"
                brycemood -= 1
                renpy.pause (1.0)
            show waiter flip at left with dissolve
            $ renpy.pause (3.0)
            stop sound fadeout 0.1
            $ renpy.pause (0.1)
            play sound "fx/glassdown.wav"
            m "The amber liquid from my glass overfilled the edges of Bryce's drinking bowl, seeping down the sides."
        "[[Knock your drink off the table.]":
            stop music fadeout 2.0
            play sound "fx/glassdown.wav"
            queue sound "fx/silence.ogg"
            queue sound "fx/silence.ogg"
            queue sound "fx/glassimpact2.ogg"
            $ renpy.pause(0.2)
            show waiter flip
            show bryce brow
            with dissolve
            python:
                tt_bryce1_drinkincident = "knock"
                brycemood -= 2
                renpy.pause(0.8)
        "I don't want to drink.":
            show waiter flip with dissolve
            python:
                tt_bryce1_drinkincident = None
                renpy.pause(0.5)
        "[[Say nothing.]":
            hide waiter with easeoutleft
            show bryce at center with ease
            Br smirk "I don't see you complaining now."
            jump tt_bryce1_canon_return_contest
    c "I said I didn't want to drink tonight."
    c "Why is this so hard for you to understand?"
    stop music fadeout 2.0
    if brycemood <= -3:
        # Player said they needed a clear head to be an ambassador,
        #  chose not to drink anything, then shoved their drink off
        #  a table. Bryce is not impressed.
        Br stern "That's how you behave as an ambassador with a clear head?"
        label tt_bryce1_drink2_no_pushuncalled:
        c "You're the one putting alcohol I didn't ask for in front of me!"
        Br brow "Then you could have ignored it. Pushing it off the table was uncalled for."
        c "Your pushiness was uncalled for. Why is it that the chief of police is more interested in drowning everyone in alcohol than having a conversation?"
        Br stern "Maybe you're right. Maybe you have already had enough, without having any yet."
        jump tt_bryce1_ending_badevening
    elif brycemood <= -1:
        # Player did something untoward with their drink rather than
        #  make their position clear again.
        if tt_bryce1_drinkincident == "knock":
            Br stern "You actually just did that?"
            jump tt_bryce1_drink2_no_pushuncalled

        Br "..."
        Br stern "I get it. You don't want to drink tonight. Fine."
        if tt_bryce1_drinkincident == "pour":
            Br brow "You could have at least waited for me to make more room."
            Br stern "It's going to be hard for me to pretend that immature act wasn't your response."
            c "You're the one putting alcohol I didn't ask for in front of me!"
            Br sad "..."
        else: # tt_bryce1_drinkincident == None
            Br stern "You could have said something earlier."
            c "I told you repeatedly. You kept pushing."
            Br sad "..."
    elif brycemood <= 0 and tt_bryce1_drinkincident == None:
        # Player has walked a thin line since the start of the encounter.
        Br brow "..."
        $ renpy.pause (0.5)
        Br sad "Ah. Damn. I assumed you... damn."
        $ renpy.pause (0.3)
        Br "You hadn't said anything earlier in the night, I just thought..."
        c "I don't drink, Bryce."
    else:
        # Player said they'd have three at the station -- not addressed.
        Br brow "It's hard to understand because you said at the station you wanted three beers to my offer of one."
        c "It's called a joke?"
        Br stern "A poor one."
        $ brycemood = -1

    play music "mx/clouds.ogg" fadein 1.0
    if tt_bryce1_drinkincident != "knock":
        play sound "fx/glasses.wav"
        Wr "I'll take this back, then."
        show waiter
        $ renpy.pause (0.3)
        hide waiter with easeoutleft
        show bryce at center with ease
    Br brow "So... drinking."
    call tt_bryce1_dontdrink_callsite(tt_bryce1_talked_about_reza=True)
    if beer == True:
        jump tt_bryce1_canon_return_contest
    jump tt_bryce1_drink2_dontdrink

label tt_bryce1_drink2_pushy:
    Br smirk "Right. So you came out to a bar to not have anything? Just give it a try."
    c "No, I'm being serious. I don't drink."
    m "What I was saying finally seemed to process for him."
    call tt_bryce1_dontdrink_callsite(tt_bryce1_talked_about_reza=True)
    if beer == True:
        jump tt_bryce1_canon_return_contest
    jump tt_bryce1_drink2_dontdrink

label tt_bryce1_drink2_dontdrink:
    Br brow "So you really don't drink? Not even on special occasions?"
    c "Nope."
    Br stern "Do you have a problem with other people drinking?"
    menu:
        "Not at all.":
            jump tt_bryce1_author_tract
        "Your body, your choices.":
            $ brycemood -= 1
            c "I'm not a fan, but I'm not going to stand in anyone's way."
            label tt_bryce1_author_tract:
            c "I'd be pretty upset if someone else stood between me and something I wanted."
            c "It's my thing with my body. Everyone else can do what they'd like."
            Br normal "That's a good way of thinking about it."
            Br brow "Still, dry is hardly a way to enjoy an evening out at a bar."
            c "Well, I'm not exactly looking for an evening I can't remember."
        "I'd like to avoid it.":
            $ nodrinks = True
            $ brycemood -= 1
            Br brow "Does that mean you want to leave now?"
            Br normal "I was hoping we could still salvage something of the evening, even if you do want it dry."
            menu:
                "[[Leave.]":
                    c "No, thanks."
                    Br sad "Fair enough."
                    scene black with dissolvemed
                    stop music fadeout 4.0
                    nvl clear
                    window show
                    n "I got up and left."
                    n "Much as Bryce seemed like an alright person, he was too pushy with the alcohol. It just wasn't a situation I wanted to be in."
                    n "If he didn't want to do anything else, he should have found another drinking buddy."
                    window hide
                    nvl clear
                    python:
                        nodrinks = True
                        brycebar = False
                        brycestatus = "neutral"
                    jump tt_bryce1_chapterover_teetotaller
                "I guess I can stay for a little while.":
                    pass
                "I'll stick around for you.":
                    show bryce brow with dissolve
                    $ renpy.pause (0.7)
            Br normal "Alright."
    jump tt_bryce1_drink2_lightordry

label tt_bryce1_drink2_light:
    c "I don't drink that often. Who knows what a mess I'd be if I went that heavy?"
    Br normal "Are you sure? We can scale things back for your mass."
    c "Yes, I'm sure."
    Br "Alright."

label tt_bryce1_drink2_lightordry:
    $ renpy.pause (0.7)
    Br brow "Was telling me all the stuff about Reza the only reason you wanted to meet with me?"
    menu:
        "It was.":
            $ renpy.pause (0.5)
            Br stern "If that's the case, then I don't want to force you to be here."
            Br "I should probably let you go home to rest, in case the department needs to call on your help again."
            menu:
                "[[Leave.]":
                    c "Sure, thanks."
                    Br sad "Fair enough."
                    scene black with dissolvemed
                    stop music fadeout 4.0
                    nvl clear
                    window show
                    n "I got up and left."
                    n "Much as Bryce seemed like an alright person, he had a point. If there wasn't anything for me there, it just wasn't a situation I wanted to be in."
                    window hide
                    nvl clear
                    python:
                        brycebar = False
                        brycestatus = "neutral"
                    jump tt_bryce1_chapterover_teetotaller
                "I'd rather stay.":
                    Br brow "Why?"
                    c "Our misunderstanding with drinking aside, this has been a nice evening."
                    Br normal "Ah, good."
        "Well, it doesn't hurt to have friends in high places.":
            $ brycemood -= 2
            $ renpy.pause (0.5)
            if brycemood <= -3:
                Br stern "You won't find one here."
                c "Excuse me?"
                Br "If all you wanted was to follow me out here and to try to get into my good graces, you're doing a pretty poor job."
                if beer:
                    Br brow "I'd have expected you to play along with the drinking game at least a little."
                else:
                    Br brow "I'd have expected you to play along with the drinking at least a little."
                Br stern "But I'm not one for hanging around someone who tells me they want to manipulate me. I don't like mind games."
                jump tt_bryce1_ending_badevening
            else:
                Br stern "I see."
                $ renpy.pause (0.8)
        "Maybe. Having a little fun doesn't hurt, right?":
            $ brycemood += 1
            $ renpy.pause (0.5)
            Br flirty "A little fun?"
            Br normal "I'm not used to hearing that without a few drinks on both sides."
            if beer == True:
                Br smirk "You've only finished the one."
                c "Well, I'm not feeling a buzz yet, so take that as you will."
            else:
                c "Well, I'm not drinking tonight, so take that as you will."
            $ renpy.pause (0.8)

    jump tt_bryce1_minigame_dispatch_init