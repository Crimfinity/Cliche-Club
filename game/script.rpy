


label start:


    $ anticheat = persistent.anticheat


    $ chapter = 0


    $ _dismiss_pause = config.developer


    $ s_name = "Sayori"
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ in_sayori_kill = None
    $ allow_skipping = True
    $ config.allow_skipping = True

    scene black
    pause 2
    stop music fadeout .5
    #maybe add glitch textbox here
    $ style.say_window = style.window_monika
    m "Why am I back here?"
    m "Did you do this, [player]?"
    m "Why did you bring me back here?"
    m "Are you here to torture me?"
    m "Don't you remember? There is no happiness to be found in the literature club."
    menu:
        "Because.":
            menu:
                "Well, I'm gonna go on some long rant through choice boxes to show that I'm the player and not mc despite not saying exactly what the player would, essentially being meta in a way that takes the player out of the game.":
                    menu:
                        "Bear with me here.":
                            m "Uhhhh {i}oookay{/i}?"
                            menu:
                                "Anyways...":
                                    menu:
                                        "I believe that you can fix things, and make the literature club a place where happiness can be found.":
                                            menu:
                                                "I also truly care about all of you, and want to help you and the rest of the club.":
                                                    menu:
                                                        "Don't you owe it to them to try and give the club another chance?":
                                                            play music mend fadein 1
                                                            m "I guess I do..."
                                                            m "Also, you came back, didn’t you?"
                                                            m "You even modified the game to give us a happy ending."
                                                            window hide
                                                            pause 2
                                                            window show
                                                            m "Alright."
                                                            m "I'll see what I can do."
                                                            m "I love you, [player]."
                                                            window hide 
                                                            stop music fadeout 4
                                                            scene white with fade
                                                            pause 4
                                                            $ style.say_window = style.window
                                                            window show
                                                            m "Oh! [player]."
                                                            m "One last thing."
                                                            scene black
                                                            m "Since this mod is about being generic or whatever."
                                                            m "It would be kind of funny to make you play through act 1 unchanged and would cover a lot of mods."
                                                            m "But I care about your sanity, so I guess I'll ask..."
                                                            menu:
                                                                m "Do you want to skip to the mod, or play through all of act 1?"
                                                                "I'd love to play act 1 again!":
                                                                    pass
                                                                "Skip to the mod.":
                                                                    m "Very well."
                                                                    window hide
                                                                    pause 2
                                                                    window show
                                                                    jump mod1
    m "Wow really?"
    m "You do you I guess."

                                            




    if persistent.playthrough == 0:

        $ chapter = 0
        call ch0_main


        call poem


        $ chapter = 1
        call ch1_main
        call poemresponse_start
        call ch1_end


        call poem


        $ chapter = 2
        call ch2_main
        call poemresponse_start
        call ch2_end


        call poem


        $ chapter = 3
        call ch3_main
        call poemresponse_start
        call ch3_end

        $ chapter = 4
        call ch4_main

        #python:
            #try: renpy.file(config.basedir + "/hxppy thxughts.png")
            #except: open(config.basedir + "/hxppy thxughts.png", "wb").write(renpy.file("hxppy thxughts.png").read())
        $ chapter = 5
        call ch5_main

        call endgame

        return

    elif persistent.playthrough == 1:
        $ chapter = 0
        call ch10_main
        jump playthrough2


    elif persistent.playthrough == 2:

        $ chapter = 0
        call ch20_main

        label playthrough2:


            call poem
            python:
                try: renpy.file(config.basedir + "/CAN YOU HEAR ME.txt")
                except: open(config.basedir + "/CAN YOU HEAR ME.txt", "wb").write(renpy.file("CAN YOU HEAR ME.txt").read())


            $ chapter = 1
            call ch21_main
            call poemresponse_start
            call ch21_end


            call poem (False)
            python:
                try: renpy.file(config.basedir + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt")
                except: open(config.basedir + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt", "wb").write(renpy.file("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt").read())


            $ chapter = 2
            call ch22_main
            call poemresponse_start
            call ch22_end


            call poem (False)


            $ chapter = 3
            call ch23_main
            if y_appeal >= 3:
                call poemresponse_start2
            else:
                call poemresponse_start

            if persistent.demo:
                stop music fadeout 2.0
                scene black with dissolve_cg
                "End of demo"
                return

            call ch23_end

            return

    elif persistent.playthrough == 3:
        jump ch30_main

    elif persistent.playthrough == 4:

        $ chapter = 0
        call ch40_main
        jump credits

label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
