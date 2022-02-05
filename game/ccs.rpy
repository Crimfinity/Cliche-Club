label modthing:
    $ s_name = "Sayori"
    $ m_name = "Monika"
    $ n_name = "Natsuki"
    $ y_name = "Yuri"
    stop music
    scene bg room_night
    "I wake up with a jump."
    mc "Wow that sure was a wacky dream!"
    "Something about that dream doesn't sit well with me."
    "Especially after hearing Sayori talk about her depression yesterday…"
    label checkchoice:
    menu:
        "I wonder if I should go check on her…"
        "Go back to sleep.":
            if wrongs == 0:
                "I'm probably just imagining things."
                "I should just go back to sleep."
                show monika forward vang om oe at t11 zorder 2
                m "Fucking really!?"
                m ce "You bring me back here and do some stupid shit like this?"
                m "Do you just want to see what happens?"
                m oe "Here, take a look!"
                show monika lean anno om oe 
                show sayori hang at l33 zorder 2
                m "She dies."
                show monika forward angr rhip
                m "Just pick the {i}obviously{/i} right answer."
                $ wrongcheck = True
            if wrongs == 1:
                show monika at thide
                hide monika
                show sayori at lhide
                hide sayori
                "I'm probably just imagining things."
                "I should just go{nw}"
                show monika forward angr cm oe at t11 zorder 2 
                pause 1
                m om "Seriously?"
                m ce "Is this fun for you?"
                m lean anno om ce "Do you get satisfaction from this?"
                m cm "..."
                m om oe "Why are you like this?"
                m "The only reason this is here is because not only did everyone who playtested this go back to bed."
                show monika forward vang cm oe lpoint at f11
                m om "{b}THEY ALL TRIED PRESSING IT AGAIN.{/b}"
                m oe ldown"EVERY SINGLE PERSON!"
                m rhip "And I'm the bad guy?"
                show monika at t11
                m dist ce "I'm obviously not letting you go back to bed. Just pick the other option."
                show monika anno cm oe
            if wrongs == 2:
                show monika rdown
                pause 1 
                show monika ce
                pause 1 
                m om "{i}Fuck you."
                show monika cm
            if wrongs ==3:
                m om "You aren't getting a reaction from me anymore."
                show monika cm
            if wrongs == 4:
                show monika at s11
                m "..."
            if wrongs == 5:
                m om "Last warning..."
                show monika cm
            if wrongs == 6:
                window hide
                pause 1
                show monika angr oe cm
                pause 2
                show monika lpoint
                pause 1.5
                $ renpy.quit()



            $ wrongs += 1
            jump checkchoice
        "Check on Sayori.":
            if wrongcheck == True:
                show monika at thide
                hide monika
                if wrongs == 1:
                    show sayori at lhide
                    hide sayori
            "I may be crazy considering it's 2:35 in the morning, but I can't shake the feeling that something’s wrong."
            "I think I should go see if she’s okay."
            "I briefly get changed into some scruffy clothes, and head to Sayori’s place."
            scene bg house_night with wipefast
            "As I step out of my house, the cold air sends a few shivers through me." 
            "I approach Sayori’s house and open the front door with the spare key that she left in the lock."
            scene black with wipefast
            "I choose not to question that for now, and head inside." 
            "Yeah, a person sneaking into your home at 2 in the morning totally isn't terrifying."
            "Thankfully, since I've been here so often, I can make my way through the downstairs with little trouble, {w=.5}even without the ligh{nw}"
            play sound "sfx/fall2.ogg"
            "*THUMP*"
            "I trip over a chair and fly headfirst into a table."
            mc "Owwww~"
            "Well, that wasn’t ideal."
            "I get up and climb the stairs."
            "I feel another shiver."
            "Something just feels so wrong about this place." 
            "Why now of all times?"
            "Oh that's why!"
            scene bg entn with wipeleft_scene
            "I run downstairs and close the front door, before heading back outside Sayori’s room."
            scene black with wipeleft_scene
            "Ahh... That's better."
            "It seems as if her light is still on…"
            "Well, let's hope I don't end up on a sex offender list for this."
            "(Or find her hanging…)"
            "I GENTLY open the door."
            mc "Sayo-{nw}"
            scene bg sayori nroom with dissolve
            "Huh, seems like she's not here."
            "I hear rustling coming from under her sheets."
            "Is she trying to hide from me?"
            "You'd think she’d get better at hide and seek someday..."
            "WAIT!" 
            "Why are her lights on if she’s in bed?"
            "Also, who turns on the light in the room they hide in?"
            "I gently approach the bed…"
            mc "Sayo-{nw}"
            show sayori pjs rup turned pani om ce at hf11 zorder 2
            s "AAAAAAAAHHHHH!!!"
            play music t2 fadein 1
            "Sayori jumps and I feel something wrap around my neck. Tugging me onto the bed."
            show sayori curi om oe
            mc "Hey! Hey! It’s me!"
            show sayori at t11 
            "I feel the grip loosen."
            show sayori worr 
            s awkw "Oh... [player]... What are you doing here?"
            s ce rdown "You scared me really bad!"
            show sayori cm nobl
            mc "Sorry, just felt like something was wrong so I figured I'd come over."
            "I remove whatever was around my neck."
            show sayori rnoose
            "It's… A noose?"
            "Huh?"
            mc "Sayori… Why do you have a noose?!"
            show sayori curi om oe 
            s "Huh?"
            show sayori happ at f11
            s "Oh! This is my trusty self defense noose!"
            s nerv awkw "It's also a backup in case my other one breaks or someone randomly throws it out like my mom did last time..."
            show sayori cm at t11
            mc "What do you mean \"other one\"?"
            show sayori rup n1
            "Sayori points towards the ceiling."
            stop music fadeout 1
            "Wait!"
            "WHY IS THERE A NOOSE ON THE CEILING?"
            "AND A CHAIR BELOW IT!"
            mc "Sayori…. Were you going to….?"
            s om "Ehehe…" 
            show sayori rdown at s11
            s "Well…" 
            s ce n4 "There’s no getting out of this one... is there?" 
            show sayori cm
            "A silence follows."
            show sayori sad oe n1 at t11
            mc "I mean not really."
            "Alright, time for an emotional heart to heart or something."
            play music t9 fadein 1.5
            mc "Look, Sayori, I’d be really sad if you died."
            mc "Like… Really sad…"
            show sayori anno    
            mc "It would suck."
            mc "And everyone else in the club would be sad too."
            "Sayori looks at me, with slight annoyance in her eyes." 
            s om "You don’t get it."
            show sayori cm
            mc "Look, I can't promise I know what's going on in your head…"
            show sayori sad 
            mc "But we all care about you."
            mc "Sayori, listen to me."
            mc "I'm not letting you go."
            mc "Please don't do this. Let us talk it out."
            mc "This isn't a solution. This isn't how your story ends."
            mc "We all love you, Sayori."
            mc "We’ll always be here for you." 
            show sayori cry cm
            "Sayori launches forward at me, gently wrapping her arms around me."  
            "I follow suit, and she begins crying."  
            s om "I’m… Sorry.. [player]..." 
            "She has trouble speaking, through her tears."
            s "I was so selfish…"
            show sayori cm
            mc "It's okay Sayori. I'm just glad you're still here with me."
            "Sayori wipes her tears off of her cheek." 
            mc "Sayori… Can I ask something of you?"
            s sad om oe "Yeah… What is it?"
            show sayori cm
            mc "You mind if I sleep on the couch tonight?"
            s nerv om "Why not in my bed?"
            show sayori cm  
            mc "Because we aren't far enough in this mod for a commitment like that."  
            s worr om e1a "Huh?"
            show sayori cm
            mc "I dunno but I'm gonna head downstairs."
            mc "See you tomorrow!"
            stop music 
            scene black
            play sound "sfx/fall2.ogg"
            "I fall down the stairs." 
            mc "Fuck, that hurt."
            "I crawl to the couch and pass out."
            #(Mc wakes up)
            pause 3
            scene bg residential_day with dissolve
            play music t2 
            "It's time for the festival."
            "I go to my house and grab whatever I helped with over the weekend."
            "It sure looks great!" 
            $ sref()
            "I think everyone will like it!" 
            show sayori turned happ om oe lup at t11 zorder 2
            s "You ready to go, [player]?"
            show sayori ldown cm
            mc "You know it!"
            mc "I'm sure nothing will go wrong!"
            window hide
            pause 2
            stop music
            scene bg fireclub
            window show 
            play sound "mod_assets/fire.mp3"
            "It did not go well, ladies and gentlemen."
            stop sound fadeout .5
            play music t3 fadein 1
            scene bg club_day with wipeleft_scene 
            "I show up to the clubroom, the {i}atmosphere{/i} and tray of cupcakes in hand!"
            "Man it sure was great I was able to help everyone on the weekend!"
            show monika forward om oe rhip happ at t11 zorder 2
            m "Hello, [player]!"  
            m lpoint "I'm sure the festival is going to be amazing!" 
            m lean "Just imagine that we're {b}hanging{b} out!"       
            show layer master:
                subpixel True
                truecenter
                parallel:
                    ycenter 360
                    easein 1 zoom 1.5 ycenter 500
            show monika forward lpoint rdown happ e1e om  at i11
                #subpixel True
                #easein 1.0 ycenter 350 zoom 1.5
            pause .2
            show monika oe
            m "(Also, good job for not leaving her hanging.)" 
            show monika cm
            "Monika shoots me finger guns."
            "Huh, that was strange…"
            show monika at thide
            hide monika
            scene bg club_day:
                subpixel True
                zoom 1
            show yuri turned happ ldown rup oe cm at t22 zorder 2
            "Yuri and I set up the banner in the clubroom." 
            show sayori turned lup rup lsur om oe at h21 zorder 2 
            s "Wow, that looks so cool!" 
            show sayori cm
            show yuri om at f22
            y "Thank you Sayori."
            show yuri cm at t22
            show sayori at thide
            hide sayori
            show yuri at thide
            hide yuri
            show sayori turned rup ldown e2c cm at l31
            "I turn my focus on the cupcakes that are left out."
            show sayori rup ldown e2c cm at t32
            "Sayori is attempting to snatch one of them because of course she is."
            show natsuki turned vang ldown rdown cm oe at t33
            show sayori shoc lup rup om oe at h32
            pause .3
            show natsuki at f33
            n om "Sayori!"
            show natsuki cm at t33
            show sayori at f32
            s vsur om oe "Aaah!"
            show sayori at lhide
            hide sayori
            show natsuki om at f33
            n "{b}Get back here!{nw}"
            show natsuki at lhide
            hide natsuki
            pause .24
            "At this time, students begin to pour into the classroom."
            "Shortly after, Monika addresses them."
            show monika lean happ om oe at f11 zorder 2
            m "Hello, everyone!"
            m "Welcome to the Literature Club!"
            m "For our club's performance, we are going to be reading poetry!"
            m "I hope you all enjoy, and that it shows you a new world of writing!"
            show monika forward happ om oe lpoint rhip
            m "I'll be sharing my poem first, it's called {i}Help, I'm stuck in a video game!"
            show monika cm ldown rdown at t11
            "Monika's voice carries across the room, her poise clear as she reads her poem."
            "Her inflection is pristine."
            "All eyes are on her as she reads her poem."
            show monika lean
            "As she finishes, a round of applause echoes throughout the room." 
            #"Wow, Monika's really epic"
            show monika at thide
            hide monika
            show sayori turned happ lup rdown ce mc at l11 zorder 2
            "Next up is Sayori, who bounces to the podium." 
            "No hanging around for her, am I right?"
            s om oe nerv ldown "Ok, my poem is called um..."
            s happ ce"{i}The Osaka Weather Report!"
            #this the weather report for osaka japan at 144 am 9/13 2020 pst
            s oe "Today will be partly cloudy with a high of 85 degrees and a-" 
            show sayori lsur at s11
            s "Oh, where was I?"
            show sayori ce lup rup happ at h11
            s "Oh, right!" 
            show sayori ldown oe rdown ldown at h11
            s "It's currently 80 degrees with a low of 71 for today."
            show sayori rup at f11
            s "But for the next three days, it's gonna be sunny!" 
            s ce "That means no rainclouds!" 
            show sayori oe mc at t11 zorder 2
            "Sayori hops a little bit, content."
            show sayori at thide
            hide sayori 
            "It seems that nobody is paying attention anymore." 
            show natsuki cross anno cm oe at t11 zorder 2
            n "Hmph."
            "I hear Natsuki mumble."
            show natsuki at thide
            hide natsuki
            "My blood boils as I see cupcake wrappers littering the floor."
            show yuri turned rup lup dist cm at t11 zorder 2
            "After she sits down, Yuri cautiously approaches the front of the room."
            y om "H-Hello, my name is Yuri and…"
            show yuri shy sad ce at s11
            y "Uuuuu-"
            show yuri
            #y "I cut myself--"
            y turned sad lup rup om oe "M-my poem is called {i}The After-{nw}"
            show yuri cm ce at falldown
            hide yuri
            play sound fall
            "Yuri collapses out of fear."
            "I can hear other students snickering for a bit before laughter erupts in the classroom." 
            show natsuki cross vang oe cm at t11 zorder 2
            stop music 
            play music t7
            "Natsuki storms up from her seat." 
            #"Oi met ill fockin nok ye blok off ye wee cunt, ye hear me?
            show natsuki turned ldown rhip om
            n "EXCUSE ME?" 
            show natsuki cm ce
            "Rage drips from her normally-cutesy face."
            show natsuki at f11
            n om "Someone could've died, and you fucking laugh?"
            n "If you're gonna laugh at someone for sharing something they care about, you should head out the door you came in!"
            show natsuki cross cm at t11
            b "We were only here for the cupcakes anyway!"
            "Everyone beelines for the door, leaving a fuming Natsuki alone with us."  
            "Perhaps they, too, were scared of the little-pink gremlin."
            "Silence and tension fill the room, as only the Club members remain."
            n om angr "(Assholes…)"
            show natsuki turned rdown cm 
            "I hear Natsuki mutter something under her breath." 
            "..." 
            "After a wait that feels like a century, Monika speaks up."
            show natsuki at t22
            show monika forward worr ldown rdown om oe at t21 
            m "Well…"
            show monika cm
            "She has a look of anguish painted onto her face." 
            m ce "..." 
            n lhip rhip om ce "We failed, didn't we?" 
            show natsuki sad ldown rdown at s22
            n "What else is there to it?"
            show natsuki cm 
            m om "N-Natsuki, I-"
            show monika dist ce cm at s21 
            "Monika sighs, deeply." 
            "It seems as if she is having to hold back tears." 
            m om oe "We didn't fail, failure is not learning from your mistakes; we can learn from this and do better next time." 
            show natsuki doub om oe at f22
            n "Next time?"  
            show natsuki ldown rdown cm at t22
            stop music fadeout 1
            play music t9 fadein 1
            m om rhip "I didn't prepare you guys at all, up until a few days before. If it's anyone's fault, it's mine." 
            show monika cm at t21
            mc "Monika…" 
            show monika curi rdown
            "She turns to look at me." 
            mc "It wasn't your fault - we did the best we could."
            m om pout "...You're right." 
            show monika cm
            show natsuki cross om ce
            "Natsuki huffs, and sits down at one of the desks." 
            show natsuki at thide
            hide natsuki
            show monika at thide
            hide monika
            "I walk over to Yuri, who is still on the floor." 
            "I lightly tap her face." 
            show yuri turned lsur ldown rdown cm ce at t11 zorder 2
            mc "Wake up, Yuri." 
            mc "It's me, [player]. Are you alive?" 
            "Yuri shifts."
            show monika forward cm oe neut at t41 
            "Monika appears next to me. She hoists Yuri onto her arm, and sits her down at a desk." 
            show monika at thide
            hide monika
            show yuri e2b
            "Yuri's eyes flutter."
            show yuri om oe shoc rup lup at h11 
            y "W-What happened…?" 
            y dist "My head… Hurts…" 
            show yuri cm
            mc "You passed out after walking to the podium." 
            show yuri shy neut cm oe
            mc "Are you okay, though, Yuri?" 
            show yuri bful at s11
            "Yuri buries her face in her hands."  
            y n4 oe om "I guess that's why we're the only ones in here, then…" 
            "I begin to hear sniffles."
            show monika forward ldown rdown dist om oe at t22
            show yuri at t21
            m "No, it's not your fault."
            show monika cm 
            show yuri turned cry om oe rup ldown at t21
            y "How…?" 
            m n2 om worr "Well… You were nervous, and your body can't control what it does in those situations…" 
            m "Not only that, I didn't prepare you well enough…" 
            #m "(In Spinjitzu…)"
            show monika cm ce at s22
            "Monika huffs." 
            show monika at thide
            hide monika
            show yuri at thide
            hide yuri
            "I begin to clear up cupcake wrappers." 
            "The air gets heavier as the others follow suit."  
            "In a short while, the room is clear."
            show monika forward om oe worr ldown rdown at t11 
            m "Well… I'm sorry that this didn't turn out as planned.."
            show monika cm at t22
            show sayori turned om oe rup ldown laug at t21 
            s "It's okay Monika."
            s "We did our best and that's all that matters!"
            show sayori cm
            stop music
            mc "As Natsuki said, {i}People can try, and that's about it." 
            m dist "..." 
            m om nerv"I guess so… " 
            show sayori at thide
            hide sayori
            show monika at t11
            play music t5
            m happ lpoint rhip "...Okay, Everyone... I think it's best we get out of here for a little while."
            m lean happ om oe "I'll see you all here tomorrow!"
            scene bg corridor with wipeleft_scene
            "And with that, we all leave the club." 
            "I tell you what…" 
            "We need a route choice just about now."
            menu: 
                "So I think that…"
                "Yuri is nice":
                    $ y_route = True
                    call yol
                "Monika is nice":  
                    "Lol nice try."
                    $ m_route = True
                    call mchoice
                "Natsuki.": 
                    pass
                    $ n_route = True
                    call nol
                "Sayori is nice":
                    $ s_route = True
                    call sol
            jump indentocd1
label indentocd1:
    stop music fadeout .5
    scene bg residential_day with wipeleft_scene
    play music t2 fadein .5
    show sayori turned neut cm e1b ldown rdown at t11 zorder 2
    "It's mostly silent as Sayori and I walk home."
    "Finally, Sayori speaks up."
    s om oe "Soo…"
    if s_route == True:
        call sas1
    else:
        call ynas1  
    "We part ways and I enter my house."
    scene bg room_night with fade 
    "I am incapable of doing anything interesting without someone else that surrounds it plot wise, so I go straight to bed."
    scene black with fade 
    stop music fadeout 1
    pause 1   
    #Crimsin realizes his Mic was on in his Team's call
    #"A gunshot rings out, they're dead."
    #c "Not really, but I just said that out loud while writing this before I realized I wasn't muted on my school's teams call and now want to die."
    #c "Anyways, please kill me, carry on with the mod."  
    jump day2

label day2:
    #day 2
    scene bg bedroom with fade
    play sound alarm
    "I awaken to a very annoying alarm mp3."
    stop sound 
    "Groggily climbing out of my bed, I get dressed and head downstairs to get some food."
    scene bg kitchen with wipeleft_scene
    "It's always empty in my house since my parents are always out on {i}business trips{/i}™."
    "I do pretty good for myself, but it gets kinda lonely sometimes."
    if n_route == True:
        "Also, I have a convenient extra bedroom in case anyone needs a place to stay."
    scene bg residential_day with dissolve
    "Stepping out of my house, I'm excited for a great day of {s}school{/s} club!"
    "I am reminded of the time on Sunday that happened." 
    "Yeah, that was pretty neat." 
    "It sure was great that I helped everyone!"
    play music t2 fadein 1
    show sayori turned happ om ce lup rup at f11 
    s "Hey, [player]!"
    show sayori cm oe ldown rdown at t11
    "My mind is brought back to reality by a cheery voice."
    if s_route == True: 
        mc "Heyo, Sayo!"
    else:
        mc "Why hello, character that maintains plot relevance no matter the mod."
        show sayori curi om at f11
        s "Huh?"
        show sayori cm at t11
        mc "Nothing. Good to see you."
    show sayori happ om at f11
    s "Ready to head to school?"
    show sayori at t11
    mc "You know it."
    stop music
    scene bg club_day with fade
    "School didn't happen, and now we're at the club."
    play music t3 fadein 1 
    show monika forward happ om oe ldown rhip at f11
    m "Hey, [player]! Good to see you again."
    show monika forward cm rdown at t11
    mc "You too, Monika." 
    "Wow, she is so popular and cool."
    show monika anno 
    c "But we can save time writing by not making her a route." 
    show monika rhip  
    so "Can't we just say it got cancelled?"
    show monika lpoint
    c "Well…{w=.33}{nw}"
    #$ srf = screenshot_srf()
    show layer screens:
        truecenter
        zoom 1.00
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    hide screen tear
    stop sound
    hide monika 
    $ del _history_list[-3:]
    #delete history here
    "As I look around the clubroom, it appears everyone is here already."
    show yuri turned ldown rdown flus e1a n3 at f11
    y "G-G-G-G-G-G-G-G-G-Good to see y-y-you again [player]."
    show yuri shy neut om oe n5 at s11
    y "UUuuuuuuuuuuuuuuuuuuuuuuuu...-"
    #maybe make a shudder movement here
    y "D-Do you want some t-t-t-t-ea?"
    "Yuri stammers out that question, like a lawn mower with a faulty start line."
    show yuri cm at t21
    show natsuki cross anno ce om at f22
    n "Ugh, welcome back, I guess, dummy."
    show natsuki cm at t22 
    "The word 'Dummy' resonates in my head."
    show yuri at t32
    show natsuki at t33
    show sayori turned happ ldown rup om oe at l31
    s "Hiiii, [player]!"
    show sayori cm 
    mc "Good to see you all again too."
    #if y_route == False: 
        #y "Give me your liver, [player]-sama!" 
        #rewind the text or however the fuck you're meant to do that idk
    mc "So what all have you guys been reading?"
    show natsuki turned lhip rdown om oe worr at f33
    n "Well I've been reading manga as usual."
    show natsuki vang cm at t33
    show yuri turned lup rdown anno om oe at f32
    y "He asked what you were {i}reading{/i}, Natsuki."
    show yuri cm at t32 
    #"The pinkheart looks infuriated."
    show natsuki at f33
    n om "Manga is literature!" 
    show sayori neut
    n cross ce flus "Nn--"
    show natsuki at thide
    hide natsuki
    "Defeated, Natsuki marches off to her corner of the clubroom."
    show yuri at thide
    hide yuri 
    show sayori at thide
    hide sayori 
    "The rest follow suit, going off to do their own thing."
    #y "Yo anyone wan some fokin t?"
    if m_route == True:
        "I think about speaking with Monika, but I guess I could just talk to someone in my league."
    stop music fadeout .5
    play music t6 fadein 1    
    if s_route == True:
        jump sroutestart
    if n_route == True:
        jump nroutestart 
    if y_route == True:
        jump yroutestart 
    #HAHA i don't have to code monika route      

label mroute:
    stop music fadeout 1 
    scene bg club_day
    show monika forward happ cm ldown rdown oe at i11 
    with fade 
    show monika at f11 
    m om "Hey [player]."
    show monika cm at t11 
    mc "Hi Monika! What's up?"
    show monika om at f11 
    m "Something really cool just happened. Want to hear about it?"
    show monika cm at t11 
    mc "Of course!"
    show screen dialog("Unfortunately, due to unforseen circumstances, development on the Monika route is now on an indefinate hiatus. We thank you for your understanding.", ok_action=Jump("gameend"))#Quit(confirm=None))
    $ renpy.pause(hard=True)
label gameend:
    $ renpy.quit()


    

    





        

            

                




            







            




