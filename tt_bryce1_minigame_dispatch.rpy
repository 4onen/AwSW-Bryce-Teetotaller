init python in tt_bryce1_minigame:
    skipdialogue = True
    talk_played = False
    tv_played = False
    darts_played = False
    darts_suggested = False
    jukebox_played = False
    jukebox_suggested = False

    wake_salt = False
    wake_pepper = False
    wake_slap = 0
return

label tt_bryce1_minigame_mood:
    if brycemood >= -1:
        show bryce normal with dissolve
    else:
        show bryce stern with dissolve
    return

label tt_bryce1_minigame_dispatch_init:

Br "What now? My plan was to come here and burn a few brain cells, but since we're not doing that..."

c "I'm sure that's not the only thing we can do in here."

label tt_bryce1_minigame_dispatch:

python in tt_bryce1_minigame:
    options_played = sum([darts_played, jukebox_played, talk_played, tv_played])

if tt_bryce1_minigame.options_played > 2:
    jump tt_bryce1_minigames_over
elif sum([tt_bryce1_minigame.jukebox_suggested, tt_bryce1_minigame.darts_suggested, tt_bryce1_minigame.talk_played, tt_bryce1_minigame.tv_played]) > 3:
    jump tt_bryce1_minigames_badend

if tt_bryce1_minigame.skipdialogue == False:
    if brycemood > -1:
        show bryce normal with dissolve
        Br "That was something. What next?"
    else:
        show bryce stern with dissolve
        Br "What brilliant diversion do you have planned next?"
$ tt_bryce1_minigame.skipdialogue = False

menu:
    "[[Ask about the jukebox in the corner.]" if tt_bryce1_minigame.jukebox_suggested == False:
        c "Hey, waiter?"
        show waiter flip at Position(xpos=0.1) with easeinleft
        Wr "Yes?"
        c "That's a jukebox over there, right?"
        Wr "Yes. It is a jukebox."
        c "That's something."
        $ tt_bryce1_minigame.jukebox_suggested = True
        Br brow "Dancing? You expect me to be able to dance?"
        c "We could also just listen."
        show waiter with dissolve
        $ renpy.pause (0.3)
        hide waiter with easeoutleft

        if brycemood < -2:
            Br stern "No. I can tell you're going to try to trick me into dancing. I do not need that staining my reputation."
            c "But--"
            Br "No buts. I'm calling veto. Choose something else to do."
            $ tt_bryce1_minigame.skipdialogue = True
            jump tt_bryce1_minigame_dispatch
        # This line written by GitHub Copilot
        Br "I'm not sure what you're trying to do, but I'm not sure I like it."
        $ tt_bryce1_minigame.jukebox_played = True
        jump tt_bryce1_minigame_jukebox
    "[[Inquire about the pin on the wall behind you.]" if tt_bryce1_minigame.darts_suggested == False:
        c "Hey, waiter?"
        show waiter flip at Position(xpos=0.1) with easeinleft
        Wr "Yes?"
        c "That pin, on the wall behind me..."
        Wr "It is used for hanging dartboards."
        c "I knew it. Could we get one hung up?"
        $ tt_bryce1_minigame.darts_suggested = True

        if brycemood < -3:
            Br brow "Are you serious?"
            c "Sure."
            Br stern "Does it look like I can hold a dart? Much less throw one accurately? With what I've been drinking?"
            c "I'm not sure. Maybe you could grip it with your teeth?"
            Br "I'm not going to be your entertainment. Pick something else."
            $ tt_bryce1_minigame.skipdialogue = True
            jump tt_bryce1_minigame_dispatch
        elif brycemood < -1:
            Br stern "A game of dexterity."
            c "Sure."
            Br "Fine. But don't expect me to be happy about it."
            Br laugh "Or, for that matter, to do well."
            show bryce stern with dissolve
        else:
            show bryce brow with dissolve
        jump tt_bryce1_minigame_darts
    "[[Look for a sports TV.]" if tt_bryce1_minigame.tv_played == False:
        $ tt_bryce1_minigame.tv_played = True
        jump tt_bryce1_tv
    "We could chat." if tt_bryce1_minigame.talk_played == False:
        $ tt_bryce1_minigame.talk_played = True
        jump tt_bryce1_minigame_talk
    "Well, we could still have that drinking contest..." if beer:
        jump tt_bryce1_minigame_drinking

    $ renpy.error("tt_bryce1_minigame_dispatch menu should always jump somewhere, but didn't!")





label tt_bryce1_minigame_talk:
    Br brow "Chat?"
    c "Talk. Like regular people."
    call tt_bryce1_minigame_mood
    Br "About?"
    c "I'd like to get to know you better. I assume this isn't all you do in your free time. After all, unless I'm mistaken, happy hour is only an hour long."
    if brycemood >= -2:
        show bryce laugh with dissolve
        $ renpy.pause (0.7)
        Br stern "Well, no, happy hour is actually usually two to three hours, most places."
        c "I knew that, but it still perplexes me why they call it an hour, then."
        Br normal "You have a point there."
    else:
        show bryce stern with dissolve
        m "My attempt to lighten Bryce's dark mood fell completely flat. After a long moment, he took a breath and answered my implied question."
        $ renpy.pause (0.7)

    Br "No, this isn't all I do in my free time. Though I wouldn't say my other free time activities are something to share on a first night out, or with a fancy ambassador."
    c "Fancy?"
    if tt_bryce1_dontdrink == True:
        Br brow "Trying to find another way to word dry. Anti-alcohol."
        c "I just don't want any."
    else:
        Br smirk "Sipping at your alcohol instead of slamming a few back."
        # c "That just doesn't sound like a fun evening."

    $ renpy.pause (0.8)

    Br normal "Anyways, how do you like it here so far? I mean, compared to wherever it is that you came from."
    menu:
        "I'm having a night out at a bar with a dragon. I'd say that alone is worth it.":
            $ brycemood += 1
            $ renpy.pause (0.5)
            Br smirk "Glad to hear you're enjoying it, at least."
        "It's alright. Certainly a nice change from what I'm used to.":
            Br "Good to hear. Maybe next time we'll send a dragon over to your world."
            c "That could be... interesting."
        "To be honest, I think I'd rather be home.":
            $ brycemood -= 1
            $ renpy.pause (0.5)
            show bryce brow with dissolve
            Br "Can't fault you for that. Home is where the heart is, after all."

    m "While we'd talked, Bryce had finished his drink."
    $ tt_bryce1_brycedrinks += 1
    Br laugh "Waiter, another round."
    show bryce normal with dissolve
    Wr "Coming right up."
    show bryce normal at right with ease
    show waiter flip at left with easeinleft

    play sound "fx/2glasses.wav"

    if beer:
        m "I hadn't gotten far enough in my current drink to warrant a refill."
    else:
        if tt_bryce1_water == True:
            Wr "Another water, [player_name]?"
            c "Sure."
        else:
            Wr "Would you like anything now, [player_name]?"
            menu:
                "Water.":
                    $ tt_bryce1_water = True
                "No, thanks.":
                    pass
    
    if tt_bryce1_water == True:
        show waiter
        $ renpy.pause (0.3)
        hide waiter with easeoutleft
        $ renpy.pause (1.5)
        show waiter flip at left with easeinleft
        play sound "fx/glasses.wav"
        Wr "Call if you'd like anything else."
    show waiter
    $ renpy.pause (0.3)
    hide waiter with easeoutleft
    
    $ renpy.pause (0.9)
    show xith normal flip at Position(xpos=0.165) with easeinleft
    $ renpy.pause (0.3)
    if beer:
        Xi "Bryce, is your drinking partner tonight really taking it that slowly?"
    else:
        Xi "Bryce, is your drinking partner tonight really not drinking?"
    c "Why is everyone making a big deal out of this?"
    Br brow "You are at a bar right now."
    Xi "I have to say, that's new for you, Bryce."
    c "Me being human isn't the more interesting part?"
    Xi "It is different. I just find the lack of quickly flowing drinks moreso."
    $ renpy.pause (0.2)
    show xith normal with dissolve
    Xi "Have fun, you two."
    $ renpy.pause (0.3)
    hide xith with easeoutleft
    $ renpy.pause (0.3)
    show bryce at center with ease
    Br normal "I won't deny talking kills some time, but I'd like to move on."
    c "Okay."

    jump tt_bryce1_minigame_dispatch

label tt_bryce1_minigame_drinking:
    Br smirk "That's what I like to hear."
    Br brow "Although, was this your plan? To have me take a headstart?"
    menu:
        "You bet. I've been planning this all along.":
            if brycemood > -2:
                python:
                    brycemood += 1
                    renpy.pause(0.5)
                Br laugh "I knew it!"
                Br smirk "It's not going to work, though. I won't lose to someone calling themselves a lightweight."
            else:
                Br stern "That was rude. That was... extremely rude."
                Br brow "But if you think it's going to stop me from winning, clearly you don't know me."
        "Nope.":
            c "Though, I guess it could be construed as advantageous."
            Br smirk "Planned or not, it won't work. I won't lose to someone calling themselves a lightweight."
    
    $ renpy.error("TODO: Transition the drinking game back into canon whenever possible.")

label tt_bryce1_minigames_badend:
    if beer:
        menu:
            "[[Admit you're out of ideas.]":
                pass
            "Well, we could still have that drinking contest...":
                jump tt_bryce1_minigame_drinking
    
    c "I'm out of ideas."
    Br brow "Are you, now?"
    if brycemood < -1:
        Br stern "Frankly, I'm glad you are. Humoring you has taken a lot of effort I could have put toward draining these bowls."
        Br "You've been full of bad ideas and jabs at my drinking since we got here."
        Br "I'm done with it."
        jump tt_bryce1_ending_badevening

    Br smirk "I'm so disappointed."
    c "Okay. Say it."
    Br "Burning a few brain cells {i}would{/i} have been a better way to spend the evening."
    Br brow "Since you're not intent on joining me for that, though, I guess I'll have to do that by myself."
    Br "You can find your way back to your apartment?"
    c "Yeah."
    Br normal "Good. Do that."

    scene black with dissolve
    stop music fadeout 1.0
    python:
        brycebar = False
        brycestatus = "bad"

    jump tt_bryce1_chapterover_teetotaller

label tt_bryce1_minigames_over:
    m "Looking around the bar, I realized Bryce and I were the only two patrons still here."
    if tt_bryce1_brycedrinks < 4:
        if brycemood > 0:
            Br brow "Oh. Damn. It got late fast."
            c "Yeah, that can happen when you're having a good time."
            if brycemood > 3:
                Br normal "Guess so."
            else:
                Br laugh "Was that what that was?"
                c "Ouch. Low blow."
                Br normal "Nah. You were trying. It wasn't too bad."
        else: # brycemood <= 0:
            Br brow "Guess that's the end of one dull evening."
            c "Hey, I was trying."
            Br stern "Not very well."

        if tt_bryce1_brycedrinks >= 2:
            play sound "fx/chair.ogg"
            show bryce at Position(xpos=0.45,xanchor='center') with ease
            m "Bryce stood, knocking into a couple chairs as he made his way out toward the aisle."
            Br "Well, let's get you home."
            menu:
                "Are you sure?":
                    c "Kinda seems like you might need more help getting home."
                    if brycemood > 1:
                        Br flirty "Is that you asking to come over to my place?"
                        menu:
                            "Uh.":
                                show bryce smirk with dissolve
                            "No.":
                                show bryce brow with dissolve
                                $ brycemood -= 2
                            "Maybe.":
                                pass
                            "Huh?":
                                $ brycemood -= 2
                                Br brow "Oh. Nevermind."
                        Br "You might be right, though. Normally I go a little heavier than this and I'm not even sure how I get home."
                        c "Well, you're gonna have to lead the way."
                        Br normal "Sure."
                        jump tt_bryce1_apartment
                "Can you even find my home right now?":
                    $ brycemood -= 2
                    Br stern "Ha. Very funny."
                    Br "Now come on."
                "Sure.":
                    pass
        else:
            show bryce at Position(xpos=0.45,xanchor='center') with ease
            Br "Well, let's get you home."
            if brycemood > 2:
                menu:
                    "Are you sure I can't come back to your place?":
                        Br flirty "Oh?"
                        Br laugh "Not a chance. That's a diplomatic incident waiting to happen. At least right now."
                        Br normal "Come on."
                    "Sure.":
                        pass
    else:
        play sound "fx/impact3.ogg"
        hide bryce with easeoutbottom
        m "When I looked back, Bryce had fallen under the table, spilling the bowl he'd been drinking from."
        if brycemood > 0:
            c "Bryce!"
        c "(Oh man. How much did he have?)"
        menu:
            "[[Leave him.]":
                show zhong normal b flip at left with easeinleft
                Wr "Wait a minute."
                c "What?"
                Wr "It's kind of an unspoken rule here that whoever is his drinking buddy helps Bryce home."
                menu:
                    "Not my problem.":
                        if beer:
                            c "I told him I'd only be drinking light today. If he didn't want to scale his consumption, that's his problem."
                        else:
                            c "I told him I wouldn't be drinking today. If he didn't want to scale his consumption, that's his problem."
                        jump tt_bryce1_soberleave
                    "Okay, sure.":
                        $ brycemood += 1
                    "If I have to...":
                        pass
                    "[[Leave.]":
                        c "Heck, no."
                        label tt_bryce1_soberleave:
                        Wr "That's not very nice of you."
                        c "Too bad. He's a big drinker. He can deal with it."

                        scene black with fade
                        nvl clear
                        window show
                        n "Without looking back, I got up and left for my apartment."
                        n "When I finally arrived, I was glad to fall into bed and sleep away the unnecessarily late evening."
                        window hide
                        nvl clear
                        $ leftbryce = True
                        $ brycebar = False
                        $ brycestatus = "bad"
                        jump tt_bryce1_chapterover_teetotaller
                show zhong serv b with dissolve
                $ renpy.pause (0.3)
                hide zhong with easeoutleft
            "[[Wake him up.]":
                pass
        
        c "Come on. Let's get you home."
        m "Bryce is still unconscious."
        label tt_bryce1_wakemenu:
        menu:
            m "Bryce is still unconscious."
            "Put some salt on his nose." if wake_salt:
                $ tt_bryce1_minigame.wake_salt = False
                c "(Right. It'll be like smelling salts.)"
                play sound "fx/salt.ogg"
                $ renpy.pause (1.5)
                c "(Nothing happened.)"
                c "(Maybe that's why smelling salts differ from table salt.)"
                jump tt_bryce1_wakemenu
            "Put some pepper on his nose.":
                $ wake_pepper = True
                jump tt_bryce1_pepperwake_canon
                label tt_bryce1_pepperwake:
                c "Uh."
                $ brycemood -= 1
                Br stern "Eugh. Okay. Let's just... er..."
                c "Let's get you home."
                Br "Sure. That."
            "Dump water on his face.":
                c "This should do the trick."
                play sound "fx/splash.wav"
                $ renpy.pause (2.0)
                show bryce brow with dissolve
                Br "Wha? 's that you, [player_name]? Where am I?"
                c "Still in the bar. Come on, let's get you home."
            "Slap him.":
                play sound "fx/slap1.wav"
                $ tt_bryce1_minigame.wake_slap += 1
                if tt_bryce1_minigame.wake_slap == 1:
                    c "(Nope. Nothing.)"
                    jump tt_bryce1_wakemenu
                elif tt_bryce1_minigame.wake_slap == 2:
                    c "Wake up!"
                    Br stern "Mmph."
                else: # tt_bryce1_minigame.wake_slap >= 3:
                    c "C'mon, Bryce."
                    show bryce brow with dissolve
                    Br "What? Is that you, [player_name]?"
                    menu:
                        "[[Keep slapping.]":
                            play sound "fx/slap2.wav"
                            $ renpy.pause (0.5)
                            show bryce laugh with dissolve
                            $ brycemood += 1
                            Br "Stop it! I'm awake already!"
                            c "Sorry."
                            Br brow "Damn. Didn't think you had it in you to slap me."
                        "[[Stop.]":
                            pass
                    Br "Where am I?"
                    c "Still in the bar."
                    show bryce stern with dissolve
                    Br "Ugh..."
                    c "Come on. Let's get you home."
            "Poke him with a dart." if tt_bryce1_minigame.darts_suggested:
                $ brycemood -= 1
                play sound "fx/chair3.ogg"
                show bryce brow with dissolve
                Br "Ow! Hey! What was that?"
                c "One of the dartboard darts."
                Br stern "Dang. Those are sharp."
                Br "Urgh. Where am I?"
                c "Still at the bar. Come on. Let's get you home."
        jump tt_bryce1_apartment

    scene black with fade
    nvl clear
    window show
    if beer or tt_bryce1_brycedrinks >= 2:
        n "The walk home was uneventful, but for a few trips and stumbles."
    else:
        n "The walk home was uneventful and peaceful, just the crunch of gravel between us."
    n "Before long, we arrived at my apartment door and Bryce bid me a good night."
    window hide
    nvl clear
    $ brycestatus = "neutral"
    $ brycebar = False
    jump tt_bryce1_chapterover_teetotaller

