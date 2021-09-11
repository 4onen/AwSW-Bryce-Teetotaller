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
                pause 1.0
            choice:
                pause 2.0
            choice:
                pause 3.0
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
    m "You take a look around the bar, but don't spot any TVs."
    Br brow "What are you looking for?"
    c "Where I'm from, most bars have a TV or two tuned to a sports channel."
    Br "Sports?"
    c "Yeah. You know, stadiums? Usually a bunch of people chasing after a ball."
    Br laugh "I know what you're talking about, except for the stadium thing."
    Br normal "But why would anyone come to a bar to watch sports?"
    c "Cheering on your favorite team?"
    Br brow "Favorite team?"
    c "We had hundreds of teams, across dozens of sports, and that was just counting the professional leagues. I think the academic leagues had thousands of sports teams."
    c "Most people would just support the teams in their areas. Some people grow attached to their teams and keep supporting them, even if they move or the team moves."
    Br normal "Sounds complicated."
    Br normal "But if that's what humans do out at a bar."
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
    $ renpy.pause (0.3)
    hide tt_bryce1_waiter_barcut with dissolve
    show bryce normal flip with dissolve
    m "TODO: Real scene"
    m "TV off"
    show tt_bryce1_tvimage dergfootball at tt_bryce1_tvimage with dissolve
    m "TV dergfootball"
    show tt_bryce1_tvimage horrible at tt_bryce1_tvimage with dissolve
    m "TV horrible"
    show tt_bryce1_tvimage select at tt_bryce1_tvimage with dissolve
    m "TV select"
    hide tt_bryce1_tvimage with dissolve
    m "TV off"
    $ renpy.error ("TODO: Sportstalk scene")