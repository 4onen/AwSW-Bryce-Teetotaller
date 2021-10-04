init:
    image tt_bryce1_apartment_night = "bg/in/apts/pad_night.png"

init python:
    tt_bryce1_apartment_floor = False


label tt_bryce1_apartment:
    scene black with dissolvemed
    $ renpy.pause(0.5)
    stop music fadeout 1.0
    nvl clear
    window show
    if tt_bryce1_brycedrinks >= 3:
        n "Bryce needed quite a bit of help remaining on course for the walk home, as he bumped into me and a few walls."
    else:
        n "The walk back to Bryce's was uneventful, but for a few trips and stumbles."

    if beer == True:
        n "I was glad I hadn't let myself drink any closer to excess tonight. The cool night air helped keep both of us awake."
    else:
        n "I was glad I didn't drink, as it let me be there to catch him, and kept me from having any falls myself. The cool night air also helped keep him awake."

    play sound "fx/door/open.wav"
    n "I got the door for him, wanting to avoid worsening the clawmarks I could see around the handle from previous late-night entries."
    $ renpy.pause(0.5)
    n "Then..."

    window hide
    nvl clear

    show tt_bryce1_apartment_night at Pan((0,260),(0,360),2.0) with dissolve
    c "H-Hey!"
    play sound "fx/door/doorclose3.wav"
    m "Bryce finished shoving me through the door, then closed it behind himself and plopped down in front of it."
    $ tt_bryce1_blanketoncouch = True
    $ tt_bryce1_minigame.wake_slap = 0
    if tt_bryce1_brycedrinks >= 4:
        m "He was asleep a moment later."
        c "(Not again.)"
        m "Bryce is still unconscious."
        label tt_bryce1_apartment_wakemenu:
        menu:
            m "Bryce is still unconscious.{fast}"
            "Slap him.":
                play sound "fx/slap1.wav"
                $ tt_bryce1_minigame.wake_slap += 1
                if tt_bryce1_minigame.wake_slap == 1:
                    c "(Well, gentle isn't going to work. He's already well out of it.)"
                    jump tt_bryce1_apartment_wakemenu
                elif tt_bryce1_apartment_wakemenu == 2:
                    c "Bryce?"
                    $ renpy.pause (0.5)
                    c "(Still nothing.)"
                    jump tt_bryce1_apartment_wakemenu
                elif tt_bryce1_apartment_wakemenu == 3:
                    m "I tried a little more force this time."
                    c "Hey, Bryce. Need you to move."
                    Br laugh "Mnh."
                    c "(Nope. Still out of it.)"
                    jump tt_bryce1_apartment_wakemenu
                elif tt_bryce1_apartment_wakemenu >= 4:
                    $ brycemood -= 1
                    m "I put a lot more of my arm into this one, and it showed in his response."
                    pass
            "Kick him.":
                play sound "fx/hit1.ogg"
                $ brycemood -= 2
                pass
            "Drape his blanket over him." if tt_bryce1_blanketoncouch == True:
                $ tt_bryce1_blanketoncouch = False
                c "(Well, he looks a little more peaceful like that.)"
                jump tt_bryce1_apartment_wakemenu
            "Sleep on Bryce's couch.":
                c "(If he's going to trap me in here, might as well take the most comfortable furniture.)"
                $ renpy.pause (0.6)
                c "(I'm going to reek of alcohol and dragon in the morning. Hope that doesn't raise uncomfortable questions...)"
                $ tt_bryce1_apartment_floor = False
                jump tt_bryce1_apartment_morning
            "Sleep on the floor.":
                c "(That couch reeks of alcohol and dragon. Guess if I'm trapped here, I might as well sleep on the floor.)"
                $ tt_bryce1_apartment_floor = True
                jump tt_bryce1_apartment_morning
        
        show bryce stern dk at center with dissolve
        Br "Urgh."
        Br "What, exactly, was that for?"

    show bryce stern dk with dissolve

    menu:
        "What's the big idea!?":
            $ brycemood -= 1
            c "Why are you trying to lock me in here?!"
            show bryce brow dk with dissolve
            $ renpy.pause(0.5)
        "Bryce, you're drunk. We shouldn't do anything we'll regret." if tt_bryce1_brycedrinks < 4:
            Br laugh dk "No, no."
            Br smirk dk "'s not what this is about."
            show bryce normal dk with dissolve
        "I, uh, need you to move to go home.":
            Br "Sorry, [player_name]. Can't do that."

    Br "You're my responsibility right now. And with Reza, we can't be sure he won't target you if you're on your own, late at night."
    Br "It's my fault, for not being sober enough to walk you to your own apartment."
    Br stern dk "But it's for your own protection."

    menu:
        "I respectfully decline.":
            c "Let me go."
            Br brow dk "I implore you to reconsider."
            label tt_bryce1_apartment_bullshit:
            menu:
                "I respectfully decline.":
                    c "Let me go."
                    Br "I implore you to reconsider."
                    jump tt_bryce1_apartment_bullshit
                "Fine. Where do I sleep?":
                    pass
        "That's bullshit.":
            Br "It's the facts of the situation as we know them."
            Br brow dk "I'm not going to let you go."
            c "You're worried I'm going to collude with Reza somehow."
            $ brycemood -= 1
            Br stern dk "I can't say the possibility hasn't crossed my mind."
            Br brow dk "The more you fight against it, the harder that possibility gets to rule out."
            menu:
                "Fine. Where do I sleep?":
                    pass
                "So I sleep in your house, or you lock me up as a suspect?":
                    $ brycemood -= 2
                    Br stern dk "It's not like that, [player_name]."
                    c "Says the alcoholic trying to keep me in his house."
                    Br brow dk "I'm going to give you one chance to walk that back."
                    menu:
                        "Fine. Whatever. Where do I sleep?":
                            pass
                        "Isn't that true, though?":
                            $ brycemood -= 1
                            Br brow dk "You go drinking with me one night, and that's the impression you walk away with?"
                            Br stern dk "You need to work on your learning to judge people."
                            c "..."
                            menu:
                                "Fine. Where do I sleep?":
                                    pass
                                "Get out of my way.":
                                    jump tt_bryce1_apartment_bullshit2
                        "Or what?":
                            label tt_bryce1_apartment_bullshit2:
                            stop music fadeout 1.0
                            m "Bryce lifted his butt off the ground, taking a few threatening steps forward. I backed further into his room."
                            Br stern dk "[player_name], how is it this difficult for you to understand? People are {i}dead{/i}, and you're the closest person to the lone suspect."
                            Br "I'm in no state to walk you home, so I'm asking you to make the best of things we both--"
                            m "Taking my opportunity, I ran around the couch, making it to the door before he could get turned around to follow."
                            show bryce angry dk with vpunch
                            Br "[player_name]!"
                            scene black with fadequick
                            m "I bolted down the stairs and away from the apartment."
                            play sound "fx/door/doorclose3.wav"
                            queue sound "fx/runstumblefall3.ogg"
                            m "Bryce followed, tripping his way down with a tremendous crash."
                            m "Not stopping to see if the drunkard police chief was okay, I barely even slowed until I was most of the way home."
                            $ brycestatus = "bad"
                            $ brycebar = False
                            $ renpy.pause(0.8)
                            jump tt_bryce1_chapterover_teetotaller
        "Where do I sleep?":
            pass
        "Reza wouldn't do that.":
            $ brycemood -= 1
            Br brow dk "We also thought Reza wouldn't kill people."
            $ renpy.pause (1.0)
            c "Fine. Where do I sleep?"
        "That makes sense. Thanks.":
            show bryce normal dk with dissolve
            $ brycemood += 1

    Br "The couch is the only thing close to a bed in here. Feel free to take that. I'll be over here on the floor."
    c "(Barring the door with his body, obviously.)"

    m "As soon as you approach the couch, you discover it positively reeks of alcohol and dragon."
    menu:
        "I'm not sleeping on that.":
            $ brycemood -= 1
            Br brow dk "Then take the floor. That's really the best I can do."
            $ tt_bryce1_apartment_floor = True
        "Thanks...?":
            Br normal dk "Sure. Don't mention it."
            $ brycemood += 1
            $ tt_bryce1_apartment_floor = False

    scene black with dissolvemed




label tt_bryce1_apartment_morning:
    scene black with dissolvemed
    $ renpy.pause (1.5)
    scene pad at Pan ((0, 0), (0,360), 5.0) with dissolveslow
    play music "mx/campfire.ogg" fadein 2.0
    if tt_bryce1_apartment_floor == True:
        m "I awoke looking at an unfamiliar ceiling. For a moment, I wondered where I was before the events of last night all came back to me. As I got up and looked around, I realized that I'd apparently slept on the floor."
        show black with dissolve
        $ renpy.pause (0.5)
        show cgbryce with dissolvemed
        $ renpy.pause(2.0)
        hide cgbryce with dissolve
        hide black
        show bryce laugh at Position(xpos=0.45,xanchor='center',ypos=1.0,yanchor='bottom'):
            ypos 1.2
        with dissolvemed
        m "Apparently Bryce had moved from the door, when it was clear I wasn't going anywhere."
    else:
        m "I awoke looking at an unfamiliar ceiling. For a moment, I wondered where I was before the events of last night all came back to me. As I sat up and looked around, I realized the thick scent of alcohol had wafted off the couch with me."
        show bryce laugh at right:
            ypos 1.2
        with dissolvemed
        m "Bryce was still passed out by the door."

    c "Hey, Bryce."

    menu:
        "Guess I smell like you, now." if tt_bryce1_apartment_floor == False:
            $ brycemood += 1
            m "The dragon moved and let out a groan before he opened his eyes."
            show bryce brow with dissolve
            Br "Do you? Damn."
        "You are salivating." if tt_bryce1_apartment_floor == True:
            m "The dragon moved and let out a groan before he opened his eyes."
            show bryce brow with dissolve
            Br "Just as you do, occasionally, I bet."
        "Wake up, fattie.":
            $ brycemood -= 1
            m "The dragon moved and let out a groan before he opened his eyes."
            show bryce stern with dissolve
            c "(That got him.)"
            Br "For your information, my kind does tend to look a little bigger than the others, but it also makes us the strongest."
            show bryce brow with dissolve
        "Good morning, sunshine":
            $ brycemood += 1
            m "The dragon moved and let out a groan before he opened his eyes."
            show bryce brow with dissolve
            $ renpy.pause (1.0)

    if tt_bryce1_brycedrinks < 4:
        show bryce normal with dissolve
        show bryce:
            ease 2.0 xanchor 0.5 xpos 0.5 yanchor 1.0 ypos 1.0
        with ease
        Br normal "[player_name], you're here. Sorry about last night, I didn't mean to trap you."
        menu:
            "You literally did mean it, though.":
                c "Something about not getting me murdered by Reza?"
                $ brycemood -= 1
                Br stern "Can't you accept an apology and move on?"
                c "An apology for an action you don't regret?"
                Br "I regret that I brought you back to my apartment instead of to your own, where that wouldn't be necessary. Isn't that sufficient?"
                c "I'll think about it."
            "Don't worry about it.":
                c "I've slept in worse places. At least your apartment doesn't have bugs or stains."
                $ brycemood += 1
    else:
        Br "Daaamn, my head. Why are you even here?"
        c "You trapped me here, remember?"
        Br stern "Not all that clearly."
        c "Well, you were pretty insistent."
        Br "Huh."
        Br brow "You didn't do anything funny while I was out, did you?"
        show bryce stern with dissolve
        m "The dragon rose with a nice morning stretch, rubbed his eyes, then held his head high as he let out a grunt and a big yawn."
        show bryce at center with ease


    if brycemood <= -2:
        if tt_bryce1_brycedrinks >= 4:
            Br stern "Crap. Now I remember. You wanted to go through that night barely drinking."
        Br "Let's put this mess of an evening behind us. It's clear we don't get along outside professional settings."
        c "Clear, huh? And who complained the entire time, just because I wasn't getting drunk with them?"
        Br brow "I remember being considerate. {i}You{/i} were glaring at me over every drink."
        c "Because we're going to trust the memory of the guy who was drinking heavily."
        Br stern "It's daytime out. Maybe you should be leaving."
        c "Yeah, I guess I should."
        play sound "fx/door/doorclose3.wav"
        scene black with dissolve
        stop music fadeout 1.0
        jump tt_bryce1_chapterover_teetotaller
    elif brycemood <= 2:
        if tt_bryce1_brycedrinks >= 4:
            Br stern "Damn, now I remember."
        Br normal "I'll admit it. That's normally not often how I spend evenings, but it wasn't terrible."
        Br "If you can forgive me the apartment sleepover thing, then we can definitely consider something else with a less spur-of-the-moment plan."
        c "Deal."
        show bryce brow with dissolve
        Br "Wait... what time is it?"
        c "Ugh..."
        Br "Damn, I should really get going, or I'll be late for work. You know how to get back to your apartment from here, right?"
        c "I think so."
        show bryce normal with dissolve
        Br "Guess you should be going as well, kiddo. Maybe I'll see you some other time."
        stop music fadeout 1.0
        $ brycestatus = "neutral"
        $ persistent.bryce1skip = True
        jump tt_bryce1_chapterover_teetotaller
    else:
        if tt_bryce1_brycedrinks >= 4:
            Br laugh "Damn, now I remember."
        Br normal "That evening wasn't half bad. Now I'm especially sorry I messed it up with that forced sleepover."
        c "Well, you didn't force me to walk you home. I could have left for my apartment from the bar."
        Br "Can I get away with you pretending that didn't happen?"
        if tt_bryce1_apartment_floor == True:
            c "I guess..."
        else:
            c "If you can explain the smell on my clothes."
            Br laugh "Maybe. Hopefully nobody will notice."
            show bryce normal with dissolve
        Br laugh "Maybe I should invite you over some other time, show you that there's more to the chief of police than getting drunk and dragging you home?"
        c "Wouldn't that be dragging me over to your place anyway?"
        Br smirk "I guess that depends on whether you want to come over."
        if tt_bryce1_brycedrinks < 4:
            Br flirty "I seem to remember a certain someone asking to come over to my place."
            c "I'm not sure we remember that the same way."
        else:
            c "I guess it does."
        $ renpy.pause (0.5)
        stop music fadeout 2.0
        $ brycestatus = "good"
        $ persistent.bryce1skip = True
        jump tt_bryce1_chapterover_teetotaller