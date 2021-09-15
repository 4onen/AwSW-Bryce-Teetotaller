label tt_bryce1_minigame_variable_setup:
default tt_bryce1_minigame.skipdialogue = True
default tt_bryce1_minigame.talk_played = False
default tt_bryce1_minigame.tv_played = False
default tt_bryce1_minigame.darts_played = False
default tt_bryce1_minigame.darts_suggested = False
default tt_bryce1_minigame.jukebox_played = False
default tt_bryce1_minigame.jukebox_suggested = False

python in tt_bryce1_minigame:
    skipdialogue = True
    talk_played = False
    tv_played = False
    darts_played = False
    darts_suggested = False
    jukebox_played = False
    jukebox_suggested = False
return

label tt_bryce1_minigame_mood:
    if brycemood >= -1:
        show bryce normal with dissolve
    else:
        show bryce stern with dissolve
    return

label tt_bryce1_minigame_dispatch_init:
call tt_bryce1_minigame_variable_setup

Br "What now? My plan was to come here and burn a few brain cells, but since we're not doing that..."

c "I'm sure that's not the only thing we can do in here."

label tt_bryce1_minigame_dispatch:

python in tt_bryce1_minigame:
    options_played = sum([darts_played, jukebox_played, talk_played])

if tt_bryce1_minigame.options_played > 1:
    jump tt_bryce1_minigames_over
elif sum([tt_bryce1_minigame.jukebox_suggested, tt_bryce1_minigame.darts_suggested, tt_bryce1_minigame.talk_played]) > 2:
    jump tt_bryce1_minigames_badend

if tt_bryce1_minigame.skipdialogue == False:
    if brycemood >= -1:
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
    
    if beer:
        jump tt_bryce1_chapterover_teetotaller
    else:
        jump tt_bryce1_chapterover
    # TODO: Definitely borked this ending somehow -- what's brycebar again?