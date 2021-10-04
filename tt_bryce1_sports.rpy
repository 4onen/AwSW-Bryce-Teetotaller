init:
    image tt_bryce1_waiter_barcut = "cr/zhong_serv_b_barcut.png"
    
    transform tt_bryce1_waiter_barcut_transform:
        alignaround (0,0)
        pos (1469,437)
        size (248,284)

    image bare tt_bryce1_tvoff = "bg/in/baretv.png"
    image bare tt_bryce1_tvon = "bg/in/baretvon.png"

    image tt_bryce1_tvimage dergfootball = "sportstv/dergfootball.png"

    image tt_bryce1_tvimage horrible = "sportstv/horrible.png"

    image tt_bryce1_tvimage select:
        block:
            choice:
                "tt_bryce1_tvimage dergfootball"
            choice:
                "tt_bryce1_tvimage horrible"
        block:
            choice:
                pause 2.0
            choice:
                pause 3.0
            choice:
                pause 4.0
        repeat

    transform tt_bryce1_tvimage:
        alignaround (0, 0)
        pos (1359, 624)
        size (94, 68)

        block:
            block:
                choice:
                    linear 0.3 alpha 0.8
                choice:
                    linear 0.5 alpha 0.8
                choice:
                    linear 0.7 alpha 0.7
            block:
                choice:
                    linear 0.7 alpha 1.0
                choice:
                    linear 1.0 alpha 1.0
                choice:
                    linear 1.3 alpha 1.0
                choice:
                    linear 1.5 alpha 1.0
            repeat

label tt_bryce1_tv:
    python in tt_bryce1_minigame:
        sporttalk_count = 0
        sporttalk_soccer = False
        sporttalk_runnerball = False
        sporttalk_toss = False
        sporttalk_quidditch = False
        sporttalk_stuntflying = False

    Br laugh "Hey, waiter?"
    show bryce normal with dissolve
    show waiter flip at Position(xpos=0.1) with easeinleft
    Wr "Yes?"
    Br normal "You had a TV set up during the celebration of the other human arriving, right?"
    Wr "I did."
    Br normal "Could you set it up again? The human wants to see the sports culture channel."
    c "Sports culture?"
    Br laugh "Only channel we have that shows sports all the time."
    show bryce normal with dissolve
    Wr "Of course. I'll pull it out."
    show waiter with dissolve
    $ renpy.pause (0.3)
    hide waiter with easeoutleft
    show tt_bryce1_waiter_barcut at tt_bryce1_waiter_barcut_transform with dissolve
    $ renpy.pause (0.6)
    show bare tt_bryce1_tvoff with dissolve
    $ renpy.pause (0.4)
    play sound "fx/flicker.wav"
    show tt_bryce1_tvimage horrible at tt_bryce1_tvimage with dissolve
    show bryce normal flip with dissolve
    $ renpy.pause (0.3)
    hide tt_bryce1_waiter_barcut with dissolve
    Br "Well, there you are. Sports. {w=2.0}Any questions?"
    $ renpy.pause (0.8)
    c "Huh. I think we have that sport back home. Though obviously we don't have any flying."
    Br "What's it called there?"
    # c "Derby Football. It's a game where you try to get the ball to the other team's goal." # Co-pilot, what is this line?
    c "Some people call it soccer, some people call it football."
    Br brow flip "Really? We call it soccer."
    Br laugh flip "Weird coincidence."
    c "I mean, considering that we have the same language, not all that weird."
    show bryce normal flip with dissolve
    c "What other kinds of sports do you have?"
    Br brow flip "I don't exactly study the area, so I don't have anything like a complete list. But, ah..."
    show tt_bryce1_tvimage dergfootball with dissolve
    c "Hold on, it just switched cameras and the picture quality dropped."
    Br normal flip "Oh that's normal. Arts and Culture doesn't see the largest budget, and sports is just a small part of it. I'm actually surprised they had that higher quality camera."
    $ renpy.pause (0.8)
    c "Sorry, that's just hard to process. Sports was a massive industry in my world."
    Br "I figured, from the hundreds of thousands of teams."
    Br laugh flip "Why?"
    show bryce normal flip with dissolve
    menu:
        "Entertainment.":
            c "We had a lot of downtime back home in the past. People were looking for something to do."
            show tt_bryce1_tvimage horrible
            show bryce brow flip
            with dissolve
            Br "I see."
        "Tribalism.":
            c "Humans naturally separate into groups, a sort of us versus them. Sports let us do that in a way that didn't hurt anybody -- at least not usually."
            c "There were the occasional accidents in post-game celebrations. Sometimes riots when local teams lose."
            show tt_bryce1_tvimage horrible
            show bryce brow flip
            with dissolve
            Br "I see."
        "It just is.":
            c "Everyone just kinda... does sports because we always have. Basically as far back as we have records, we have history of doing sports. The sports have changed over time of course, but that's just how it's been."
            show tt_bryce1_tvimage horrible
            show bryce brow flip
            with dissolve
            Br "I see. That's interesting, because as far as I know, that's why we play sports too. But that never led to a big thing involving nearly everyone, like you described."
            c "Maybe there's something we're just missing that's different."
    $ renpy.pause (1.0)
    Br stern flip "Uh oh."
    c "What's wrong?"
    Br brow flip "The goalie on the left. That's a flyer."
    c "And?"
    Br stern flip "That's a dangerous position for anyone with wings to play. People kick and whip the ball at the highest speeds when shooting for the goal."
    Br "Wing injuries from that aren't pretty. And she's nothing but wings."
    show tt_bryce1_tvimage select with dissolve
    Br brow flip "I'm surprised nobody discouraged her from playing that position."
    show bryce stern flip with dissolve
    menu:
        "Who says they didn't?":
            c "Maybe that flyer just really feels strongly for achieving in that sport, and is willing to take the risk. Many humans feel the same way in similarly dangerous sports. Rock climbing, skydiving..."
            $ brycemood -= 1
            Br brow flip "She's putting herself in harm's way for no reason."
            Br "Consider what happens if she is hurt. Then she has to be treated at their local healthcare facilities."
            Br "While she's being treated, she's not contributing to her job. That's assuming she'll ever fully recover and be the productive member of society she was in the first place."
            Br "It's a waste."
            show bryce stern flip with dissolve
            m "Bryce nosed down into his drinking bowl, finishing up what remained."
            $ tt_bryce1_brycedrinks += 1
            play sound "fx/gulp2.wav"
            $ renpy.pause (4.0)
        "I see.":
            pass
        "[[Say Nothing.]":
            pass
    $ renpy.pause (0.8)
    m "After letting Bryce brood a moment, I tried to move the conversation back to other parts of their sports world."

    c "So I assume soccer isn't the only sport your people play. What other kinds of sports do your people have?"
    Br normal flip "I don't exactly study the topic, so let me see what I remember."
    $ renpy.pause(0.5)
    Br stern flip "Soccer, Runnerball, Toss, Quidditch, and stunt flying, off the top of my head."
    c "Hm."
    python in tt_bryce1_minigame:
        sporttalk_count = 0
    label tt_bryce1_tv_sportsmenu:
    menu:
        c "Tell me a little more about..."
        "Soccer." if tt_bryce1_minigame.sporttalk_soccer == False:
            $ tt_bryce1_minigame.sporttalk_soccer = True
            c "I noticed you had flying in soccer. Humans can't fly, so I'm curious how else the rules might differ."
            Br normal flip "Well, let me think a minute."
            Br "You've got two teams, each with a goal and a goalie. The goalies on each team are the only ones who are allowed to grab the ball."
            Br "Everyone else tries to hit it through the goal. Kicks, slaps, tail whacks, it's all legal. You just can't hold it, like for a throw."
            c "That's interesting. We don't allow anything but kicks. Nothing above the waist at all, really, except chest and head bumps."
            c "What about boundaries? Kicking the ball out of bounds?"
            Br "The team not responsible for kicking it out of bounds sends someone to kick it back in-bounds."
            Br laugh flip "Can't see how that's going to differ."
            show bryce normal flip with dissolve
            c "We actually bring the whole game to a halt, have someone -- anyone -- place it on the edge of the field, then let the team not responsible kick it back in from there."
            Br brow flip "Why would you do it that way?"
            c "Fairness. Not all of the out-of-bounds locations are as advantageous."
            Br normal flip "I suppose that makes sense. I'd prefer to stay in the game, though."
        "Runnerball." if tt_bryce1_minigame.sporttalk_runnerball == False:
            $ tt_bryce1_minigame.sporttalk_runnerball = True
            c "It sounds like it's for runners specifically, but what is it about?"
            Br laugh flip "Runners running with a ball!"
            Br normal flip "I've had the rules to me explained once or twice, but I don't get them."
            Br "They've got this oblong ball, like an egg but symmetrically..."
            show bryce stern flip with dissolve
            if tt_bryce1_brycedrinks > 3:
                play sound "fx/chair.ogg"
                m "He lifted a paw to gesture with, then stumbled to catch himself as he bumped into a chair."
            elif tt_bryce1_brycedrinks > 1:
                m "He gestured with a paw, swaying slightly from his alcohol consumption."
            else:
                m "He gestured with a paw, struggling to form his claws into the shape he was conveying."
            Br "Kinda pointy on both ends. And the runners tackle each other over it, while trying to carry it to opposite ends of the field."
            c "Wait, this sounds exactly like one of our sports. When they get it to the ends of the field, do they call it a \"touchdown\"?"
            Br normal flip "Yeah. Think so."
            c "We call that sport \"football.\""
            Br brow flip "What, like that other name you've got for soccer?"
            Br laugh flip "What's that even got to do with feet?"
            $ brycemood += 1
            c "No idea. That's just what it's called."
            Br normal flip "Alright. That's something."
        "Toss." if tt_bryce1_minigame.sporttalk_toss == False:
            $ tt_bryce1_minigame.sporttalk_toss = True
            Br stern flip "This sport is more for people like me."
            c "You don't look happy about that."
            Br brow flip "Thing is, it messes up our backs. There's this saying we have. Don't know if you have it: \"Lift with your legs.\""
            Br stern flip "We quadrupeds can't do that when we're grabbing things with our forelegs."
            Br "Yet, the sport pops up and people want to play it."
            c "What... is it, exactly?"
            # Br normal flip "It's a game where you throw a ball into the air, and it's up to you to catch it." # Cute, but no.
            Br normal flip "You take a tree trunk, all debranched and stuff, usually straight up and down."
            Br smirk flip "And throw it, end over end."
            Br normal flip "Score is based on distance, number of times it flips over, how straight you throw it, and whether you make sure it falls away from you when it finally hits the ground -- toward you is less points."
            Br stern flip "It's definitely cool to watch, but in my opinion the health risks outweigh the cool factor."
            c "The health risks of... throwing an entire tree?"
            menu:
                "Throwing a tree does sound crazy.":
                    $ renpy.pause (0.5)
                    $ brycemood -= 1
                    Br "Exactly why I don't like it too much."
                "I think I've heard of that...":
                    Br brow flip "Really?"
                    c "Yeah. Humans have a sport called \"Caber Toss\" that's a lot like that. Almost exactly like that, now that I think about it."
                    Br normal flip "Interesting."
        "Quidditch." if tt_bryce1_minigame.sporttalk_quidditch == False:
            $ tt_bryce1_minigame.sporttalk_quidditch = True
            c "So, this name is really close to a name of a fictional human sport, but I'll let you explain it first."
            Br "Well, it's easier to start from something else. Have you heard about Ixomen Spheres since you arrived here?"
            if persistent.ixomenassembled == True or renpy.python.store_dicts['store'].get("ixomenunread", True) == False:
                c "Yeah, I've heard some things. But how is that relevant? What does it do for the game?"
            else:
                c "Can't say that I have."
            # Br normal "Ixomen Spheres are a magical sphere that can be used to create a magical force field around you." # Cute, but no.
            Br normal flip "Well, it's a pretty expensive piece of tech. But the relevant part here is the tech inside it that makes it float."
            c "What, just hover in the air?"
            Br brow flip "And fly around under its own power. I haven't seen one operating, but that's about it."
            Br normal flip "Anyway. In Quidditch, they've got a few balls with that tech inside, so it's really a flyer sport."
            Br stern flip "It's also a really expensive sport, so only very rarely done."
            c "I see. So I'm guessing it's only for flyers."
            Br normal flip "Yeah. Not that they'd exclude someone else, but it's not exactly possible for someone stuck on the ground to deal with hoops way up in the air."
            Br "Oh, yeah, hoops, balls..."
            $ renpy.pause (0.8)
            Br stern flip "Okay. So I'm pretty fuzzy on any of the rules or terms."
            Br brow flip "But it's annoying because there's one ball that if a flyer catches it, it's basically guaranteed the game ends in that team's favor."
            c "Yeah, that's exactly how our version goes."
            Br "So you have some way to fly?"
            c "Well, no. This sport was described in our fiction. There are approximations to play on the ground, but they're not even close to the flying version."
            Br normal flip "So you've got legends about us, huh?"
            menu:
                "I'm not sure.":
                    c "The sport was described by a fiction author, who was trying to invent a sport from whole-cloth. I don't think she based it on anything."
                    Br "I see."
                "Sure, something like that.":
                    c "We have plenty of legends about dragons, yeah. I wouldn't have guessed Quidditch was connected before, but after hearing this I'd definitely want to look into it."
                    $ brycemood += 1
                    Br smirk flip "I see. Well, take a look at that when you get back to your side."
        "Stunt Flying." if tt_bryce1_minigame.sporttalk_stuntflying == False:
            $ tt_bryce1_minigame.sporttalk_stuntflying = True
            Br normal flip "Now for one I've seen in person."
            c "So, what is it? Are there specific stunts that they need to perform, like an obstacle course?"
            Br brow flip "No. That would be too dangerous for the flyers, and somewhat unfair. It'd force different flyers with different body shapes through one activity."
            Br stern flip "If people failed, they could get hurt. If everyone succeeds, it's boring -- they're all almost the same."
            c "I see. So it's more freeform?"
            Br normal flip "Pretty much. Every contestant knows their limits, so they do the most extravagant tricks they can perform. Tricks that one flyer can perform, another can't. So there's really an aspect of competition in showing off to the judges."
            c "Showing off to judges. Okay, so a bit like our gymnastics competitions. They're doing the most impressive things they can to impress, to earn a high score."
            Br "Sounds similar, yeah."
        "I think that sates my curiosity." if tt_bryce1_minigame.sporttalk_count > 0 and tt_bryce1_minigame.sporttalk_count < 3:
            if tt_bryce1_minigame.sporttalk_count == 1:
                Br brow flip "Really? After asking me about one sport."
                c "Yeah. I think this deserves a more serious review than idle bar conversation."
                $ brycemood -= 1
                Br "If you say so."
            jump tt_bryce1_tv_sportsmenu_over

    python in tt_bryce1_minigame:
        sporttalk_count = sum([sporttalk_soccer, sporttalk_quidditch, sporttalk_runnerball, sporttalk_stuntflying, sporttalk_toss])

    if tt_bryce1_minigame.sporttalk_count == 1:
        Br "Any other questions?"
        jump tt_bryce1_tv_sportsmenu
    elif tt_bryce1_minigame.sporttalk_count == 2:
        Br brow flip "Anything else?"
        jump tt_bryce1_tv_sportsmenu
    elif tt_bryce1_minigame.sporttalk_count == 3:
        Br laugh flip "Are you going to ask me about every one of these sports?"
        menu:
            "Yes.":
                show bryce stern flip with dissolve
                c "I don't mean to monopolize the evening, but this is all very interesting, and useful in the name of interspecies understanding."
                $ brycemood -= 1
                Br "Okay, fine. I'll let you pick my brain on one more. You want to dig deeper than that goes, you'll have to go to the library or binge the sports culture channel or something."
                jump tt_bryce1_tv_sportsmenu
            "No.":
                show bryce normal flip with dissolve
                $ renpy.pause (0.5)
                Br normal flip "Then I hope you don't mind me asking you to move things along now."
                Br "Our sports may be fascinating to you, but they're pretty dull for me."
                c "Oh, alright. Sure."
    else:
        pass

    label tt_bryce1_tv_sportsmenu_over:
        $ renpy.pause (0.5)
        Br "Alright, I think it's time to pack up the TV. Don't want to spend all the bar's electricity."
        Br laugh "Waiter?"
        show bryce normal with dissolve
        show zhong serv b flip at left with easeinleft
        m "The waiter appeared, replacing Bryce's once-again empty drink. Before he could leave, Bryce caught him."
        $ tt_bryce1_brycedrinks += 1
        Br "If you'd like to put the TV away, I think the ambassador's finished."
        Wr shy b flip "I am slightly busy at the moment. But thank you. I will put it away when I have time."
        show zhong serv b at left with dissolve
        $ renpy.pause (0.3)
        hide zhong with easeoutleft
        $ renpy.pause (0.3)
        show tt_bryce1_waiter_barcut at tt_bryce1_waiter_barcut_transform with dissolve
        hide tt_bryce1_tvimage with dissolvemed
        hide tt_bryce1_waiter_barcut with dissolve


    jump tt_bryce1_minigame_dispatch