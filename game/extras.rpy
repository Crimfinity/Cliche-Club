label mchoice:
    menu:
        "Who should I {i}actually{/i} play the route of?"
        "Yuri is nice.":
            $ y_route = True
            call yol from _call_yol
        "Natsuki.":
            $ n_route = True
            call nol from _call_nol
        "Sayori nice.":
            $ s_route = True
            call sol from _call_sol
    return

label nol:
    show natsuki turned happ ldown rdown cm oe zorder 2 at t11
    mc "Natsuki."
    n lhip curi om "What do you want?"
    show natsuki cm
    "Did I say that out loud?"
    n anno om "Uh… Earth to [player]?"
    n doub "You gonna keep staring at me or what?"
    show natsuki cm
    "Looks like I did."
    mc "Sorry. Just thinking out loud is all."
    n neut om ldown "Oh okay."
    n worr "Wait."
    n cross angr "What were you thinking about me?"
    show natsuki cm
    mc "Eh, nothing."
    n turned doub ldown rdown om ce "Well it better not have been anything rude!"
    n pout oe "Or gross…"
    show natsuki cm at s11
    mc "Don't worry about it."
    "I escape from that awkward situation as quickly as possible."
    return

label yol:
    show yuri turned cm oe happ ldown rdown zorder 2 at t11
    mc "Yuri is nice."
    y lsur om "...[player]?"
    show yuri cm
    mc "Yeah, what's up?"
    show yuri shy happ om ce at s11
    y "You… said my name."
    show yuri cm
    "Huh, I think I said that out loud."
    mc "...Did I? Nah…"
    show yuri turned dist lup rup at t11
    y om oe "Perhaps I'm just imagining things…"
    show yuri cm
    "Well I sorta dodged a bullet with that one."
    "Gotta learn to not speak aloud like that."
    "I should write a book about getting out of that situation."
    "I'll call it {i}Gaslighting 101."
    "{i}A Sosiopath's Wet Dream."
    pause 2
    "On second thought, maybe I shouldn't become an author."
    "I mean I misspelt my book title in my head. How does someone even do that?"
    "I decide it's best to distance myself from Yuri on the way out after what I said earlier."
    return

label sol:
    show sayori turned happ cm oe ldown rdown zorder 2 at t11
    mc "Sayori is nice."
    s laug om lup awkw "Huh? Uh... thanks, [player]."
    show sayori nobl cm
    mc "I uh… said that out loud didn't I?"
    s om ce ldown "Ehehe, yup!"
    show sayori at thide
    hide sayori
    "The Bun prances away, giggling."
    "Even though we were supposed to walk home together."
    return
label sas1:
    show sayori at f11
    s happ n3 "What made you want to compliment me so bad?~"
    show sayori cm n1 at t11
    "Oh no."
    "I feel my face grow red."
    mc "Well, I just figured maybe acknowledging why I enjoy being around you would be kinda helpful for… Y'know."
    s curi om lup "...For what…?"
    show sayori cm
    mc "Y'know, the whole overused raincloud metaphor thing."
    show sayori at f11
    s happ ldown ce om "Oh! Right!"
    s oe "Well, thanks, [player]!"
    show sayori cm
    "The girl with the cinnamon bun-like hair wraps my arm in a hug."
    "I feel a certain {i}something{/i} against my arm…"
    "..."
    mc "Ahaha… Thanks, Say Say."
    "I have now officially created the worst nickname of all time."
    show sayori at t11
    "She releases her grip on me."
    if persistent.ynas1 == True:
        s om "So, did you try to help with my {i}rainclouds{/i} in any other route?"
        show sayori cm
        mc "Nope."
        show sayori at s11
        s om dist "Oh..."
        show sayori cm
        mc "...Back to the script!"
        s nerv om "Oh yeah, right."
    show sayori happ cm oe ldown rdown at t11
    "Shortly after, we arrive at my house."
    mc "See ya Sayori!"
    s ce om "Byeee~"
    if persistent.key1 == True:
        show sayori at thide
        hide sayori
        "Wait..."
        "Wasn't I missing a key on the other routes?"
        "Oh well, doesn't matter for the plot I guess."
    return



label ynas1:
    show sayori lup sedu mb at f11
    if y_route == True:
        s "What were you thinking about Yuri for?~"
    if n_route == True:
        s "What were you thinking about Natsuki?~"
    show sayori cm at t11
    mc "Huh?!"
    "I feel my face go red."
    "I've got to get out of this somehow!"
    mc "Where did you hear that?!"
    show sayori laug ce ldown
    "I can see Sayori trying to hold in her laughter. She ends up giggling at my expense anyway."
    show sayori om oe
    if n_route == True:
        s "I heard you talking to Natsuki in the corridor."
    if y_route == True:
        s "I heard you talking with Yuri in the corridor."
    show sayori tap oe om nerv
    s "I was right next to you, y'know~"
    s "So... lemme ask again."



    show sayori at f11
    s "What were ya' thinkin' about?"
    show sayori turned happ cm oe at t11
    "Her voice is mocking."
    mc "N-Nothing I just…"
    "My face grows hotter than the sun."
    mc "Why do you want to know so much?"
    show sayori lup om ce
    s "Because it seems interesting!"
    show sayori cm
    "I see my house in the distance."
    mc "Oh hey, Sayori, looks like we're home."
    mc "We'll have to continue this conversation later!"
    scene bg house with dissolve
    "I briskly walk to the front door and turn the handle."
    "Locked."
    $ persistent.key1 = True
    "I may or may not have left my key inside my living room before heading out this morning..."
    "Well, I only have one hope of getting in my house."
    mc "{b}Sayori?{/b}"
    s "Yeah?"
    "Sayori's voice can be heard off in the distance."
    mc "Do you still have my spare key?"
    s "Uh, I think so. Why?"
    mc "I'm kinda locked out of my house."
    s "Oh one sec!"
    window hide
    pause 2
    window show
    show sayori turned ldown rdown neut ce cm n2 at l11

    "Sayori returns, out of breath."
    show sayori om at s11
    "She holds up a key."
    show sayori turned e1d worr e1d at t11
    s "I've......haah."
    show sayori ce at s11
    pause .5
    show sayori om lup at t11
    s "...Got it."
    show sayori cm oe
    mc "Thanks Sayori, you're a lifesaver."
    s mb e1d "Not so fast!"
    if n_route == True:
        s "You have to tell me what's up with you and Natsuki first."
    if y_route == True:
        s "You have to tell me what's up with you and Yuri first."
    show sayori ma
    mc "Do I have to?"
    show sayori at f11
    s mb ce ldown "Yup!"
    show sayori happ n1 cm oe at t11
    mc "I…"
    mc "..."
    "I have trouble speaking."

    mc "I picked their route for this mod."
    s lsur om oe "Huh?"
    show sayori me e1d
    mc "Uh I meant…"
    mc "I really like her."
    show sayori md
    if y_route == True:
        mc "She's nice."
    if n_route == True:
        mc "She's nice.{w=.3}{nw}"
        mc "She's.{fast}"
    show sayori at f11
    s om happ lup rup e1b "Uwoah! That's so cool!"
    s om happ oe "You two would be a super cute couple."

    if n_route == True:
        show sayori cm
        "A distant growl echoes through the neighborhood."
        show layer master:
            subpixel True
            truecenter
            zoom 1.1
            block:
                dizzy(3, 0.01)
                time .3
            block:
                dizzy(1.5, 0.01)
                time .3
            block:
                dizzy(.2, 0.01)
                time .5
        n "{b}I'M NOT CUTE!!!!{/b}"

        "Yep, knew this cliche mod wasn't gonna be able to escape that line…"
    show sayori cm ldown rdown at t11
    mc "Woah, let's not get ahead of ourselves here."
    mc "I just think she's pretty neat, you know…?"
    s b1d om "Sure, [player]."
    show sayori cm
    mc "Alright, can I get my key now?"
    s nerv om lup -b1d "Yeah, I guess."
    show sayori cm happ
    "Sayori hands me the spare key."
    $ persistent.ynas1 = True
    return


label ss1:
    "I decide to go see what Sayori is up to."
    show sayori turned ldown rdown oe om vsur at t11
    "It appears she's currently 'Uwaa~'-ing in a loop."
    show monika forward anno cm oe ldown rdown at l31
    pause .2
    show monika lpoint at t31
    pause .2
    show layer screens:
        truecenter
        zoom 1.00
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    hide screen tear
    stop sound
    hide monika
    hide sayori
    show sayori turned ldown rdown happ om oe at f11
    s "Oh hey [player], what's up?"
    show sayori cm at t11
    mc "Not much, just wanted to see what you were up to."

    show sayori om at f11
    s "Oh I'm just..."
    show sayori lsur
    s "Oh I'm just...{fast} I forgot."
    show sayori cm zorder 2 at t11
    "How did she-"
    "Right. Cliche mod."
    mc "Well, how are you feeling?"
    window hide
    show sayori laug cm oe lup rup zorder 2 at f11
    stop music fadeout 1
    play music livereport fadein 1
    show weather1 zorder 1:
        subpixel True
        xoffset -1200
        easein_bounce 3 xoffset 0
    show stand onlayer screens:
        subpixel True
        xoffset -300
        yoffset 300
        easeout 2 yoffset -200
    pause 2
    window show
    show sayori at t11
    "Where is this going?"
    show sayori happ om ce at f11
    s "Well I'm glad you asked!"
    s oe rdown "I'm weatherette Sayori with channel 9 news!"
    show weather2 zorder 1.5
    hide weather1
    stop music fadeout 1
    show sayori ldown anno cm at t11
    mc "There is no way that's a real term.{fast}"
    pause 0.5
    mc "Okay, okay… fine."
    s om "Partly cloudy."
    play sound "mod_assets/slide.wav"
    window hide
    show stand onlayer screens:
        subpixel True
        xoffset -470
        yoffset -700
        rotate 0
        parallel:
            ease 2.5 yoffset -2500
        parallel:
            block:
                easeout 4.5 rotate 3000
    show sayori cm
    show weather2 zorder 1:
        subpixel True
        xoffset 0
        ease 3 xoffset -1700
    pause 3
    window show
    "Huh."
    show sayori n2 nerv om oe at f11
    play music t2 fadein 1.5
    s "Anyways, can you buy me a cookie?"
    show sayori cm at t11
    mc "Uh… Sure."

    show sayori happ om ce lup rup n1 at hf11
    s "Yay!{nw}"
    show sayori oe
    s "Yay!{fast}{w=.15} Thanks [player]!"
    show sayori ce at h11
    pause .2
    show sayori at h11
    pause .2
    show sayori cm oe at t11
    "Sayori jumps up and down as she wraps her arms around me in a bear hug."
    mc "Alright, alright."
    show sayori tap nerv om oe at s11
    s "Ehehehehehehehehehhehehe sorry~"
    scene bg corridor with wipeleft
    show vending with dissolve:
        truecenter
        zoom 0.6
        block:
            ease 3 yoffset 25
            ease 3 yoffset -25
            repeat

    "We step out of the clubroom and are greeted by a vending machine."
    mc "Hold on, since when did vending machines float?"
    show sayori turned ldown rdown om oe neut at f31
    s "I dunno."
    show sayori cm at t31
    "Sayori shrugs."


    m "Sorry, guys!"
    "I hear a distant shout from the clubroom."
    pause .5
    show sayori vsur at h31
    hide vending with wipeleft
    m "...Aaaand there!"
    show sayori lsur om lup at f31
    s "Where'd it go?"
    s tap pout om oe "I wanted a cookie…"
    show sayori turned ldown rdown e2c cm lsur at t31
    "Suddenly, the vending machine reappears against the wall."
    show sayori om at f31
    s "Huh?"
    show sayori cm at t31
    "Without questioning it, I slide an unnamed currency into the slot."
    "Is it Yen? Is it Dollars?{i} Maybe one of those 'Quids'?{/i}"

    "Guess we'll never know."
    show sayori e2d neut om


    "Sayori's eyes widen as I conjure up a chocolate chip cookie."

    mc "'Tis magic, my dear."
    show sayori laug e1h at f31
    s "It's beautiful…"
    show sayori cm at t31
    mc "Alright then."
    "I toss Sayori the cookie and she finishes it in seconds."
    show sayori at f31
    s om "Sho good! Thank you [player]!"
    show sayori cm at t31
    mc "What did I say about finishing eating before you talk?"
    show sayori nerv oe om n2 at s31
    s "Shorry!"
    show sayori happ cm nobl
    mc "Alright, you ready to walk home?"
    show sayori om rdown at t31
    s "Sure."
    return


label ys1:
    "I decide to go see what Yuri is doing."
    show yuri turned neut lup rup e1b cm at t11
    "It appears she's reading a familiar book."
    "It has a distinct eye on the cover with the title Portrait of Markov."

    "Putting my hand on her shoulder, she jumps."
    show yuri shoc rup om oe at h11
    y "Aahh-!{nw}"
    window hide 
    stop music fadeout .2 
    show yuri at boing
    $ renpy.pause(delay=.9, hard=True)
    play sound thud 
    show yuri with hpunch
    $ renpy.pause(delay=6, hard=True)
    play music t6 fadein 3
    "Surprised, Yuri hops out of her chair and drops 'gracefully' towards floor headfirst."
    "I make an attempt to catch her, but my hands don't compromise."
    "She bursts through the floor and lands on the ground of the first story."
    mc "...Sorry."
    "I offer her a hand."
    "Pulling herself off the ground, Yuri reaches to grab it, but comes up short."
    "Now how can I get her up here?"
    show sayori turned lup rnoose happ om oe at l31
    s "Sayori to the rescue!!!"
    show sayori cm
    "I turn to see Sayori, holding a noose."
    show sayori ce om ldown at f31
    s "The self defence noose is multipurposed!"
    show sayori cm oe rdown at t31
    "She unties her 'self defense' noose and hands it to me."
    show sayori laug rup om at f31
    s "I'll even let ya have a free trial."
    show sayori cm at t31
    mc "Uh... Thanks Sayori."
    show sayori happ om ce at hf31
    s "No worries."
    s "I'm selling them for $19.99!"
    show sayori pout e1a
    s "But wait! Theres more."
    s "Call or text {i}(503)839-9667{/i} now and we'll throw in a self defence landmine too!"
    show sayori cm at t31
    mc "Who is 'we'?"
    show sayori tap nerv om oe
    s "Well I thought you'd be willing to invest in my company..."
    show sayori turned anno cm oe
    mc "Nope."
    mc "Besides, who would that pitch be towards if not me?"
    s nerv om "Ehehe I guess you're right."
    show sayori sad e1b cm at t31
    "Okay. time to set Yuri free from the depths of the teachers lounge."
    mc "Alright Yuri, grab on!"
    y "Hm?"
    "She looks up and the rope."
    y "Oh, alright."
    show yuri neut cm oe at rise
    "She grabs onto the rope and hauls herself up."
    y turned happ om oe "Thank you, [player], you're very kind."
    y rdown ce "Your generosity is effervescent."
    show yuri cm
    show sayori at thide
    hide sayori
    "I have no clue what that last word means."
    show yuri oe
    mc "N-no problem, Yuri."
    show yuri curi
    mc "So… Painting of Mark?" with dissolve
    hide yuri
    show yuri turned curi om oe at i11
    y "Huh?"
    show yuri cm at t11
    "She looks at me with a dire and confused expression, it's like she's been offended."
    "Oh no."

    show yuri rup om dist at f11
    y "It's… Portrait of Markov…"
    show yuri ldown cm rdown happ ce at t11
    "She lightly chuckles."
    mc "Yeah, that one."
    show yuri shy neut om oe
    y "W-w-w-w-would you like to read with me, today?"
    show yuri cm happ
    mc "Sure, why not?"
    "I sit down next to the purple woman."
    scene y_cg1_base
    with dissolve

    "She fidgets a little bit before settling, then slides the book between us."
    "We read for a while, our shoulders pressed together, her lavender scent filling my nostrils."
    "Eventually, Yuri speaks up."
    show y_cg1_exp1
    show y_cg1_exp2
    with dissolve
    y "Would you like some tea, [player]?"
    mc "Uh, yeah. Alright."
    hide y_cg1_exp1 with dissolve
    play sound crash 
    show tea at tealikenises with vpunch
    "All of a sudden, Yuri's tea set crashes through the closet door."
    "Natsuki lets out a yelp from near the closet where the teaset was resting."
    "I turn around in shock."
    "It beelines out of the clubroom door."
    "Huh. That's new."
    scene bg club_day
    show monika forward lpoint rdown anno om oe at f21
    show yuri turned lsur rup lup at t22
    m "Yuri, again?!"
    show monika cm at t21
    "Monika glares at Yuri."
    show yuri shoc om at f22
    y "W-Wha-?"
    y shy neut om oe "I'm- I'm sorry… Monika."
    y turned rdown ldown om oe neut "It won't happen again."
    show yuri neut cm at t22
    show monika ce om ldown at f21
    m "You know, I believe in you, Yuri."
    m oe "You can be the strong, independent girl that you want to be."
    m neut "Even if that involves controlling your telekinesis."
    show yuri happ ce
    m "You are enough, Yuri. I promise."
    m lean happ om oe "Now, back to literature!"
    hide monika
    "Monika seems to disappear."
    show yuri at t11
    "Following that... strangely motivational disciplining, I turn my attention back to Yuri."
    mc "So, when did you learn telekinesis?"
    show yuri oe om at f11
    y "Good question, my mother learned it on one of her business trips!"
    y dist rup "Before she died..."
    y happ "Pretty neat, huh?"
    show yuri rdown cm at t11
    mc "Awesome!"
    pause .3 
    show tea2 at rise:
        zoom .08
        xoffset 400
    "The tea set floats back to us, the cups entirely filled."
    show yuri neut rdown
    "I grab one and take a sip."
    "It tastes like a taste."
    hide tea2 with dissolve
    show yuri lsur
    mc "This is great, Yuri, thanks!"
    show yuri om oe
    y "Y-You really mean that?"
    mc "Yup."
    show yuri mb dist at f11
    y "Ah… Thank you [player]."
    show yuri happ cm oe
    mc "So where did you get the tea set?"
    show yuri happ om oe at f11
    y "Good question, my mother brought it back for me on one of her business trips!"
    y dist rup "Before she died..."
    y happ "Pretty neat, huh?"
    show yuri cm at t11
    mc "Awesome!"
    pause .3 
    show monika forward happ om oe lpoint rhip at l31
    m "Okay, everyone! Time for you to leave."
    show monika cm
    "That's a bit more forward than I remember it being."
    show yuri at thide
    hide yuri
    show monika at thide
    hide monika
    "I say my goodbyes and exit the club with Sayori."






    return
label ns1:


    "I decide to go see what Natsuki is doing."
    scene bg closet with dissolve
    show natsuki turned flus ldown rhip cm oe at f11:
        yoffset 550
        hopfocus(640,.25)
        pause 2
        repeat
    "She appears to be jumping up and down, trying to grab a box of manga."
    show natsuki rdown ce at s11
    "After about a minute or so, she surrenders. Placing her hands on her knees while breathing heavily."
    show natsuki angr ce om at t11
    n "Keeps moving my fucking manga…"
    show natsuki oe
    n "Monik{nw}"
    show natsuki pani at hf11
    n "Gah!{w=.1}{nw}"
    pause .15
    show natsuki e1a at t11
    "Natsuki spins around and only just now realizes I was standing behind her."
    show natsuki cm
    mc "Sorry."
    show natsuki cross om ce angr at f11
    n "Don't go around scaring people like that, dummy!"
    show natsuki turned lhip rhip cm at h11
    "She punches my arm."
    show natsuki om anno at f11
    n "Anyways…"
    show natsuki cm oe at t11
    mc "You need help getting your manga?"
    show natsuki cross ce om angr at f11
    n "I can do it myself."
    show natsuki turned ldown rdown vang cm oe at t11
    mc "And that went so well last time…"
    show natsuki at lhide
    hide natsuki
    "Natsuki storms off and grabs a stool and heads back towards the closet."
    show natsuki turned curi ldown rdown oe cm at r11
    mc "Hold on."
    show natsuki rhip om at f11
    n "Huh? What do you want?"
    show natsuki cm lsur at t11
    mc "Use this."
    "I conjure a trampoline."
    "Where from? Who knows."
    show natsuki om at f11
    n "Wha?"
    show natsuki curi rdown cm at t11
    mc "Don't question it."
    show natsuki worr om at s11
    n "Uh… alright."
    show natsuki neut cm at t11
    "I give Natsuki the mini trampoline."
    show natsuki rhip e1b at s11
    "As she bends over to set it up, I simply grab the manga myself."
    show natsuki om rdown at f11
    n "Where'd it…"
    show natsuki angr om oe
    n "Dummy, I told you I don't need any help!"
    show natsuki at h11
    "She punches me in the arm. Again."
    show natsuki cross vang cm at f11
    n "Grr."
    show natsuki turned anno lhip at t11
    mc "So, you want to read some manga?"
    show natsuki worr om at f11
    n "Y-yeah, I guess."
    show natsuki neut cm at t11
    mc "Sweet!"
    scene n_cg1_bg
    show n_cg1_base
    show n_cg1_exp5
    with dissolve_cg
    "We both sit up against the wall and Natsuki rests the manga between us."
    "The two of us sit bunched together reading."
    "It's mostly silent except for when Natsuki complains about her dad or something."
    "I dunno what it's really about, since I'm focusing on this manga."
    "I really like it now or something."
    hide n_cg1_exp5 wih dissolve_cg
    n "Hey, [player]?"
    mc "What's up?"
    show n_cg1_exp2 with dissolve_cg
    n "I kinda… Need a place to stay for a while."
    n "So I was wondering if I could live at your place."
    n "B-but don't get the wrong idea, b-baka!"
    show n_cg1_exp5
    hide n_cg1_exp2
    with dissolve_cg
    "Well I'll have to sacrifice the ball pit room."
    "But hey, I'm going to be living with a cute anime girl."
    mc "Sure, I have a spare room you can stay in."
    hide n_cg1_exp5 with dissolve_cg
    n "Really?"
    show n_cg1_exp5 with dissolve_cg
    mc "Yeah why not? I've known you for a whole eight days."
    hide n_cg1_exp5 with dissolve_cg
    n "T-thank you."
    show n_cg1_exp1 with dissolve_cg
    n "You don't know how much this means to me."
    hide n_cg1_exp1 with dissolve_cg
    n "But... Why are you so nice to me?"
    show n_cg1_exp5 with dissolve_cg
    mc "Because that's one of my only defining character traits."
    hide n_cg1_exp5
    show n_cg1_exp2
    with dissolve_cg
    n "Oh..."
    hide n_cg1_exp2
    with dissolve_cg
    n "Alright, well, you okay if I come over in a week?"
    show n_cg1_exp5
    with dissolve_cg
    "I shrug."
    mc "Fine by me."
    hide n_cg1_exp5
    show n_cg1_exp1
    with dissolve_cg
    n "Great!"
    hide n_cg1_exp1
    show n_cg1_exp3
    n "I mean... That's cool."
    n "..."
    scene bg club_day
    show natsuki turned dist oe cm at t11
    show monika forward lpoint rhip om oe happ at f31
    play music t5
    m "Okay everyone!"
    m "I think that we're out of time for today."
    show monika lean happ om oe
    m "So I'll see you all tomorrow."
    show monika forward om oe happ lpoint rdown at f31
    m "Don't forget, we aren't doing poems anymore."
    show natsuki at thide
    hide natsuki
    show monika at thide
    hide monika
    "I say my goodbyes and make my way out of the club."
    "Before I can get through the doorway, I feel a soft tug at my sleeve."
    show natsuki turned pout ldown rdown at f11
    n "Don't forget what you said earlier, okay?"
    show natsuki happ cm at t11
    mc "I won;t. Promise."
    window hide
    scene black with dissolve
    pause 2
    window show
    return







label ynas2:
    stop music fadeout .5 
    scene bg residential_day with wipeleft_scene
    play music t2 fadein .2  
    show sayori turned happ cm ce ldown rdown at t11
    "We walk in silence for a while until Sayori finally speaks up."
    s nerv om "So…"
    if y_route == True:
        s tap nerv om oe "You were looking at Yuri's {i}Painting{/i}, huh?"
    else:
        s tap nerv om oe "You read with Natsuki, huh?"
    mc "And what of it?"
    show sayori turned happ cm ce
    "She giggles."
    show sayori om oe at f11
    s "Nothin'~"
    s sedu rup mb "It's just that you two are so cute together~"
    "I feel my face redden a little."
    show sayori cm at t11
    mc "Thanks, Sayori."
    show sayori nerv om
    s "She's totally into you y'know…"
    show sayori happ lup at f11
    s "You should ask her out!"
    show sayori cm neut at t11
    mc "As if I'd be so bold."
    s om "C'mon, [player]..."
    if y_route == True:
        mc "Maybe someday. But only after the scene where we go to a cafe and say it's not a date while nervously holding hands."
    else:
        mc "Maybe someday, but only after she moves in with me."
    show sayori lsur cm oe
    pause .1
    show sayori ce
    pause .1 
    show sayori oe
    "Sayori blinks a little."
    s rdown "Oh… Alright."
    show sayori curi om ldown at f11
    s "And how long will that take?"
    show sayori cm at t11
    "I shrug."
    if y_route == True:
        mc "Eh. I dunno."
    if n_route == True:
        mc "Not too long..."
        show sayori rup worr e1a at f11
        s "Really? You've only known eachother for like a week."
        show sayori cm at t11
        mc "Eight days, Sayori. Eight days."
        s om "..."
    mc "Alright, looks like this is where we part ways."
    show sayori happ om oe ldown rdown at f11
    s "Bye [player]!"





















    show sayori cm at t11
    mc "See ya."
    stop music fadeout 1 
    scene bg bedroom with fade
    "I stand around in my bedroom for a little while."
    mc "Man, still nothing any girls have done that makes the afternoon plot relevant?"
    window hide 
    scene black with fade
    pause 3 
    return


label ns2:
    # day 3
    play music t3 
    scene bg corridor with dissolve_scene_full
    "Alright, time for the club."
    "I wonder what's going to greet me today."
    "I {i}gently open the door{/i} and step inside."
    scene bg club_day with wipeleft
    show monika lean om oe happ at f11 
    m "Hey [player], how's it hangin'?"
    show monika cm at t11 
    mc "Hey Monika. Surprised you're here on time."
    show monika forward lpoint happ om oe 
    m "Well, not much else to distract me these days."
    show monika cm 
    mc "That's good."
    mc "Anyways, I'm going to go talk to Natsuki now."
    show monika doub om 
    m "Of course you are."
    scene bg closet with wipeleft
    "I walk across the class to Natsuki, who seems to be speaking with Yuri."
    play music t7
    show natsuki cross angr ce om at f22
    show yuri turned rup dist e1b at t21 
    n "It's like I told you yesterday, MANGA IS LITERATURE!"
    #y "Mate mate you come to Birmingham mate I'll fuckin bite your face off and shove it up your asshole you little dickhead, you little fucking knob. You were talking about the whispering maybe you should stop whispering yourself first you little fucking mommy's boy now shut your mouth and fuck off dickhead. You know something you little fucking muppet I'll tell you where I live, I live in FUCKING Birmingham, Smethwick, you little fucking bic-dickhead FIND OUT WHERE IT IS, YEAH. COME BIRMINGHAM and I'll BITE YOUR FUCKING FACE OFF. I WILL FUCK YOU UP DICKHEAD I WILL FUCK YOU UP YOU LITTLE KNOB YOU SENT ME THE FIRST MESSAGE. I'M A FUCKING BIG MAN YOU LITTLE FUCKING DICKHEAD. I'M COMING FOR YOU, BIG MAN SIX FOOT, BIG ASS STOCKY MAN, SO COME SMETHWICK, AND I'LL BITE YOUR FUCKING FACE OFF. YOU SENT ME THE FIRST MESSAGE, SO NEXT TIME CHECK YOUR MESSAGES YOURSELF YOU FUCKING DICKHEAD What did i fucking shout at you down the mic for, playing your fucking mouth, mate, to my bro man. You sent me a message first, yeah. I live in Smethwick Birmingham if you want to FUCKING brawl. COME down, Smethwick, ask for Danny G, I'LL COME OUT MY HOUSE, AND I'LL BREAK YOUR FUCKING LEGS! YOU LITTLE PRICK! HEAR WHAT I'M SAYING?! HEAR WHAT I'M, FUCKING SAYING?! COME BIRMINGHAM AND I WILL FUCK YOU UP, COME BIRMINGHAM NOW, AND I WILL FUCK YOU UP! I TOLD YOU WHERE I LIVE, YOU WANT TO KNOW WHERE I LIVE?! I LIVE IN FUCKING SMETHWICK, NOW COME, AND I'LL KILL YAH. What's my problem? What's my problem? You, is my fucking problem. Shut your fucking mouth I'LL FIND OUT WHERE YOU LIVE AND I WILL COME AND FUCK YOU UP IN YOUR OWN HOUSE. SHUT THE FUCK UP YOU DON'T KNOW WHO I AM GEEZER, I AM A FUCKING MONSTER. DON'T FUCK ME ABOUT AND I'LL COME TO YOUR HOUSE AND I WILL FUCK YOU UP IN YOUR OWN HOUSE. I TOLD YOU WHERE I LIVE. COME TO MY HOUSE, SMETHWICK, COME TO MY HOUSE AND WE'LL SEE WHO KNOCKS WHO OUT MATE I'LL BREAK YOUR FUCKING FACE. SERIOUSLY MATE I'LL BREAK YOUR FACE, I WILL BREAK YOU OPEN, I SWEAR TO GOD YOU LITTLE PRICK. YOU SOUND LIKE YOU'RE 17 YOU LITTLE KNOBHEAD. I'VE GOT FUCKING KIDS OLDER THAN YOU MAN, I GOT KIDS THAT WILL FUCK YOU UP YOU DICKHEAD."
    show yuri -e1b angr om lup at f21 
    show natsuki turned ldown rdown angr cm oe at f22
    y "Tell me, Natsuki, do you look at a drawing with a caption and think \"This is literature\"?"
    show yuri cm at t21 
    "Man, looks like they're really going at it..."
    n ce "Nn--" 
    show natsuki om n2 at f22
    n "I wasn't the one whose boobs magically grew a size bigger as soon as [player] started showing up!!"
    #y "Jumbo \nMass = Large. \nVery bigg."
    show natsuki shoc -n2 at h22 
    show yuri om rdown at f21
    y "Okay, Flat Stanley." 
    show yuri cm at t21 
    show natsuki vang
    "Natsuki looks mortified as she inhales, preparing to scream." 
    show natsuki flus e1b at h22 
    show yuri vsur at h21 
    stop music fadeout 5 
    mc "Both of you! Stop!"
    "The girls turn around in shock, only just now realizing I was present." 
    show yuri sad 
    show natsuki sad om e1b n3 at f22 
    n "[player]?"
    show natsuki fs sad ce om -e1b 
    n "I..."
    show natsuki at lhide 
    hide natsuki 
    show yuri shoc 
    "Natsuki then bolts past me out of the clubroom." 
    show yuri at t11 
    y ce "Natsuki-"
    show yuri shy sad om oe 
    y "I..."
    show yuri ce at s11 
    y "I didn't mean it..."
    "Welp, guess it's my time to shine."
    #Hero complex, initializing. 
    scene bg corridor with wipeleft 
    show natsuki turned zorder 1 at t11 
    show vending zorder 2:
        truecenter
        zoom 0.6
        block:
            ease 3 yoffset 25
            ease 3 yoffset -25
            repeat
    with dissolve
    "As I exit the club room, I find Natsuki crawling under a nearby vending machine." 
    #smolsuki 
    #i write in lowercase because im a #lofi producer babay
    "How she fits underneath it, I'm not sure."
    "Maybe she really is Flat Stanley..."
    mc "Natsuki."
    show natsuki at hf11
    n "Ah! [player]!"
    n "Go away-!"
    show natsuki at t11 
    "Natsuki grits her teeth and clenches her uniform as she looks away."
    mc "Hey... It's okay."
    mc "I'm sorry Yuri was giving you a hard time."
    show natsuki at f11
    n "Yeah, well... It's no big deal. I'm fine."
    show natsuki at t11 
    "The stray tears falling down Natsuki's face show she is not indeed \'fine\'."
    play music t9 fadein 4 #haha GET IT BECAUSE NATSUKI IS INTERPOLATING "MY FEEL" FROM PINK EYES SO i PLAY MY FEELINGS BECAUSE I'M SO FUCKING CLEVER IMA A GENIUS BIG BRAIN GOD I'M SO COOL AND DEFINITLY NOT SO, SO, alone.
    mc "Hey, Natsuki..." 
    "I rest my hand on her shoulder."
    "Well, as much as I can while she's under a vending machine."
    show natsuki at f11 
    n "Why are you helping me, [player]? My chest really is flat… Yuri was right…"
    show natsuki at t11 
    mc "Well that isn't important."
    mc "Besides..."
    "I feel my face grow red."
    mc "Isn't that what friends are for?"
    show natsuki at f11 
    n "But you're not denying it!!" 
    show natsuki fs sad cm oe at t11 
    "She whines."
    #"I begin lightly singing the DK Crew Rap."
    mc "Here, come sit."
    "Natsuki then pushes herself out from underneath like a car mechanic."
    show vending:
        parallel:
            ease 1 yoffset -250 xoffset 2000
        parallel:
            rotate 0
            linear .5 rotate 360 
            repeat 

    "I guide her to a nearby bench, where she nearly collapses."
    "Beginning to lean onto my shoulder, she starts crying harder than before." 
    n ce om "O Lord, why must I be cursed with a chest Oh-So flat-!" 
    n cry "When all I want to do is hit my friend Yuri, with a bat." 
    n oe "People are mean, [player]!" 
    n "They make me want to just yell at them.." 
    n "You're the only person in this cruel world that is nice to me!" 
    n "Why…?" 
    #play lit(var) depression edition 
    #OR lit(var)(var) AKA lit(var) Natsuki-is-my-hashtag-bae edition
    show natsuki cm n3
    mc "Well... I just enjoy spending time with you."
    n ff lsur e1g om "You... you mean that?"
    show natsuki cm 
    mc "Yup."
    show natsuki -e1g e1a 
    n "..."
    show natsuki om dist -e1a 
    n "[player]..." 
    n "Can I ask a question?" 
    show natsuki cm
    mc "Sure."
    show natsuki worr om at f11 
    n "Why do {i}certain boys{/i} make my heart flutter?" 
    show natsuki cm at t11 
    show natsuki cry n2 -n3
    stop music 
    mc "Maybe you have some kind of illness."
    mc "Might want to go see a doctor."
    mc "I hear heart-disease is rife this time of year!"
    show natsuki at f11
    n lsur om rhip "Huh? I-"
    n anno ce -n2 "Sure. Whatever."
    show natsuki cm at t11 
    "A silence then falls upon us."
    "I get the feeling I'm missing something here…" 
    "Eventually, I speak up."
    mc "Alright, you ready to head back inside?"
    "Natsuki sniffles as she softly nods."
    show natsuki at f11 
    n e1g happ om "Y-yeah..."
    show natsuki cm at t11 
    "I help Natsuki to my feet as we walk back into the clubroom together."
    play music t3 
    scene bg club_day with wipeleft_scene
    show monika forward happ cm oe at t21 
    show natsuki turned neut cm oe rhip at t22 
    "Upon our entrance, Monika is the first to notice us."
    show monika rhip om at f21 
    m "Hey Natsuki, feeling any better?"
    show monika cm at t21  
    show natsuki rdown om e1a at f22 
    n "Y-yeah..."
    show natsuki pout -e1a n4 cm at t22 
    "Natsuki then turns to look at me."
    show natsuki pani om at hf22 
    show monika ce 
    n "But not because of him or anything-!!"
    show monika lean happ om oe at f21
    show natsuki cm lsur at t22 
    m "Ha. I'm sure it has nothing at all to do with him."
    show monika cm at t21 
    show natsuki cross vang om ce at f22 
    n "Shut up, Monika." 
    show natsuki turned angr ce cm at t22 
    show monika forward happ om ce lpoint at f21 
    m "Alright, alright." 
    show monika at thide 
    hide monika 
    show yuri turned sad om oe rup at f21
    show natsuki lsur oe at h22  
    y "Natsuki..."
    show yuri cm at t21 
    "With that, Natsuki flinches."
    show natsuki anno om rhip at f22 
    n "What do {i}you{/i} want Yuri?"
    show natsuki -n3 -n4 n2 neut cm at t22  
    show yuri worr n4 om at f21  
    y "I-I... wanted to apologize for my previous remarks." 
    show yuri -n4 dist 
    y "I should give you the respect you deserve." 
    show yuri cm at t21 
    show natsuki ce dist 
    n "..."
    show natsuki om -n2 at f22 
    n "I'm sorry too."
    n sad "I shouldn't have yelled at you like I did."
    show natsuki cm at t22
    show yuri dist om rdown lup at f21  
    y "Well, if it will make you feel better..."
    show yuri cm ce at t21 
    "Yuri inhales deeply." 
    show yuri neut ldown om oe at f21 
    y "I shall read one of your \'manga\'."
    show yuri cm at t21 
    show natsuki happ om ce at f22 
    n "Sweet!"
    n oe "Does this mean I have to read a fancy book?"
    show natsuki neut cm at t22 
    show yuri anno om at f21
    y "Yes..."
    show yuri cm neut cm at t21 
    show natsuki neut om at f22 
    n "Well, I guess it won't hurt..."
    show natsuki cm at t22
    "Yuri then beams at Natsuki."
    show yuri ce om at f21 
    y "Excellent!"
    show yuri oe cm at t21 
    show natsuki curi om lhip at f22 
    n "What was it you said you read? {w}The 'Painting of Mark' or something, right?"
    #OH LOOK, A REFERENCE TO THE YURK ANGLE!!!!!!
    show natsuki cm at t22 
    show yuri anno om at f21 
    y "Portrait of Markov..."
    show yuri neut cm at t21 
    show natsuki happ om at f22
    n "Yeah, that!"
    show natsuki flus n3 at t33 
    show yuri vsur n3 om at t31 
    show sayori turned lup rup happ ce om at f11
    s "You two are so cute!"
    show yuri at f31 
    show natsuki at f33 
    show sayori cm oe at t11 
    ny "Huh?"
    show yuri at thide
    show natsuki at thide
    show sayori at thide
    hide natsuki 
    hide sayori 
    hide yuri 
    show monika forward happ ce om lpoint rhip at l11 
    play music t5 
    m "Okay, everyone!"
    show monika oe at f11 
    m "I think it's time we end the meeting for today."
    m ldown rdown "I'll see you all tomorrow~"
    show monika cm 
    "We say our goodbyes and all leave the club." 
    stop music fadeout 1.5 
    scene bg room_night with dissolve_scene_full
    "As I lay in bed, my mind wanders about the events from earlier today."
    show corridor 
    show natsuki turned n3 worr om oe at t11 
    with dissolve 
    n "Why do {i}certain boys{/i} make my heart flutter?" 
    hide corridor 
    hide natsuki 
    with dissolve 
    "What could she have meant with that?"
    "Is she sick? Is she going to die?"
    "I also never asked her why she was under a vending machine in the first place."
    #u/thisismypr0naccount0 coming with that one teaser xDDD
    "My mind is in a million different places."
    "Oh well, I need to get some sleep so I can be ready for tomorrow."
    stop music fadeout .7
    scene black with fade 
    return 
label nh1:
    
    #six day time skip baby 
    play music t8 fadein 1 
    scene bg residential_day 
    show sayori turned rup om oe at f11 
    with fade 
    s "...So that's why unicorns are definitely real!"
    show sayori cm at t11 
    mc "Uh huh. You drive a compelling argument Sayori."
    show sayori rdown om ce happ  at f11 
    s "Ehehehehehehe thanks!"
    show sayori cm at t11 
    pause .6
    show sayori om oe neut at t11 
    s "Well, guess this is our stop! See ya tomorrow [player]!"
    mc "Yep."
    show sayori at thide 
    hide sayori 
    "Alright, time to get home and watch some anime."
    scene bg house 
    stop music 
    show natsuki turned rhip neut om oe at if11  
    n "Hey."
    show natsuki cm at t11 
    mc "What are you doing here?"
    show natsuki lhip curi om 
    n "Moving in?"
    show natsuki angr cm 
    mc "That was today?"
    show natsuki ldown om ce at f11 
    n "Yes! Dummy!"
    n oe "I even told you multiple times not to forget."
    show natsuki cm at t11 
    mc "Oh yeah..."
    show natsuki worr om 
    n "Ugh, are you going to let me in or what?"
    show natsuki cm 
    mc "Y-yeah!"
    "Scared of Natsuki punching me again, I swiftly unlock the front door."
    mc "Welcome uh... home?"
    n om ce "Yeah, whatever."
    show natsuki cm 
    "That's pretty cold for free rent."
    "Oh well, I sure don't have the backbone to stop her."

    play music t6 fadein 2 
    scene bg lrd with dissolve
    show natsuki turned curi om oe lhip rdown at f11 
    n "Uh... dude?"
    show natsuki cm at t11 
    mc "Yeah?"
    show natsuki om 
    n "Why do you have a body pillow laying on the couch?"
    show natsuki cm 
    mc "W-well, I forgot you were coming over today so I kinda..."
    show natsuki anno 
    mc "Left it out."
    "...Hope she doesn't notice the stains."
    show natsuki ldown ce vang om at hf11 
    n "Gross!"
    show natsuki angr oe 
    n "You really need to clean up after yourself, [player]!"
    show natsuki cross anno 
    n "This place is disgusting."
    show natsuki doub cm at t11 
    mc "Well if you gave me some time to clean it, the pillow would be a little more presentable."
    show natsuki turned anno om at f11 
    n "You're a pig."
    show natsuki cm at t11 
    mc "I'm sorry..."
    show natsuki om 
    n "I hope you don't expect me to sleep on the couch."
    show natsuki cm 
    mc "No... it's fine. You can take my bed."
    mc "We can share if you wanted t{nw}"
    n doub om "No."
    show natsuki cm 
    mc "Figured."
    show natsuki om at f11 
    n "You can sleep with your girlfriend down here."
    n angr "And you're room better not be dirtier than this living room."
    show natsuki cm at t11 
    mc "I don't think it is."
    "Oh god what have I left out upstairs?"
    "Uh let's see... there's... lots of manga, but I guess she wouldn't be disappointed by that."
    "Well, nothing else I can do. Might as well just accept my punishment."
    show natsuki om rhip at f11
    n "Here's the deal, you clean up this disgusting house, and I make us some food."
    show natsuki cm 
    mc "Yes ma'am."
    show natsuki happ lhip ce om at f11 
    n "That's more like it!"
    n om "Now, off you go."
    scene black with fade 
    "I frantically toss my body pillowcase in the laundry and run upstairs to clean up the rest of my room and hide whatever {i}unsavory{/i} things may be strewn about."




    scene bg kitchen with dissolve_scene_full 
    show natsuki turned cm oe neut casual at t11 
    mc "This looks pretty good, thanks Natsuki."
    show natsuki ce om anno at f11 
    n "It would've been better if you had more food in your kitchen."
    show natsuki dist cm oe at t11 
    mc "Yeah I guess."
    "It probably would be good to buy something other than chips more often."
    "The two of us eat in silence other than Natsuki grumbling about the many issues of my house."
    "We finish up and place our dishes in the sink."
    show natsuki neut ldown rhip om oe at f11 
    n "I'm gonna hit the hay, I'm pretty drained from not being at home, y'know?"
    show natsuki cm at t11 
    mc "Yeah, I get it."
    mc "Fifty-fifth door on the left."
    "I gesture upstairs."
    show natsuki curi om 
    n "Okay... Wait, Fifty-fifth?"
    show natsuki cm 
    mc "Yeah, I have a lot of doors."
    show natsuki lsur om at f11 
    n "Okaaay then. Guess I'll start my journey."
    show natsuki cm 
    "Natsuki heads towards the stairs."
    show natsuki happ om at f11 
    n "Thank you, by the way."
    n "This means a lot to me."
    show natsuki neut cm at t11 
    mc "No problem, I only exist to help people with their struggles."
    mc "Goodnight!"
    scene black  
    stop music fadeout 1.5 
    "With that, I turn around and flick off the light, plopping down on the couch."
    "I pull my body pillow into a tight embrace."
    "Now, to get some much needed sleep."
    #fade out and pause/ all that good shit
    return 
label nh2:
    pause .7
    scene bg lrd with dissolve 
    play music t5 
    "I awake to the sound of sizzling."
    mc "Hm?"
    "What could be sizzling? Did I leave the stove on?"
    "The sound of humming fills the room."
    "Oh yeah."
    scene bg kitchen 
    show natsuki turned casual neut e1a cm at t11 
    with wipeleft 
    mc "Morning, Natsuki."
    show natsuki pani -e1a at hf11
    n om "Ah!"
    n anno ce "Quit sneaking up on me like that!"
    show natsuki ce 
    mc "Sorry, sorry."
    mc "Anyways, how'd you sleep?"
    show natsuki om oe 
    n "Fine."
    show natsuki rhip at f11 
    n curi n2 "But does a boy really need that much hentai?"
    show natsuki -n2 cm at t11  
    "I blush profusely."
    "Quick, change the subject!"
    mc "Uh... uh! {w=.7}...Whatcha makin'?"
    show natsuki neut om 
    n "Eggs and bacon, just something simple."
    show natsuki cm 
    mc "Oh that's cool, I didn't know I had either of those."
    show natsuki cross om doub casual at f11  
    n "You didn't, I had to walk all the way to town to get them."
    n turned rdown ldown casual neut  "Hope you didn't mind I spent your money on groceries."
    show natsuki cm at t11 
    mc "Eh, it's fine, as long as I get some food."
    play music t2 
    show layer master at vpunch 
    show sayori turned rup lup casual yand om oe zorder 5:
        rotate 180
        zoom 1.45
        xoffset -325
        yoffset -2000
        block:
            ease 1 yoffset -800
    s "DID SOMEONE MENTION FOOD!?"
    show sayori cm 
    mc "Jesus fuck!"
    show sayori nerv om rdown 
    s "Ehehe..."
    s "Sorry about that."
    show sayori cm:
        parallel:
            ease 2 yoffset 1500
        parallel:
            block:
                rotate 180 
                linear 3 rotate 540 
                repeat 
    pause 1 
    hide sayori 
    show natsuki worr at t21 
    show sayori turned casual happ ce cm lup at ir22 
    #sayori drops from the ceiling 
    #quick pause for her to look around
    pause 3.5
    show sayori oe 
    pause .3 
    show sayori curi 
    pause .4
    show sayori om at f22
    s "Why is Natsuki here?"
    show sayori lsur cm at t22 
    mc "She lives here now?"
    show sayori om at f22 
    s "Huh???"
    show sayori curi 
    s "But why?"
    show sayori cm at t22 
    mc "I dunno, she just asked."
    show natsuki lhip om at f21  
    n "Yeah... Just kinda felt like it, I guess."
    show natsuki cm at t21 
    "Natsuki sways a little while observing the floor."
    show natsuki sad 
    show sayori neut om lup at f22 
    s "So... food?"
    show sayori happ cm at t22 
    mc "Yeah, Natsuki is making eggs and bacon I guess."
    show sayori om ce rup at f22 
    s "Ooh! I'll help!"
    show sayori oe cm at t22 
    mc "No!"
    show sayori sad om at f22 
    s "Why?"
    show sayori cm at t22 
    mc "Because of that one time you almost burned my house down cooking."
    show sayori anno om at f22 
    s "[player], that was ten years ago."
    s doub ldown rdown "And you bring it up almost every day."
    show sayori cm at t22 
    mc "Do I?"
    show natsuki neut ldown om at f21  
    n "Yeah, not the first time I've heard you mention it."
    show natsuki cm at t21 
    "..."
    show sayori happ 
    mc "Well, I guess you can help."
    scene black 
    stop music 
    "The three of us then finish cooking, as surprisingly nothing burns to the ground."
    "The worst that happened was me mixing up salt and sugar."
    "It happens a lot, surprisingly."
    "Huh? Why was that last scene change so jarring?"
    "Well because the rest of it isn't interesting, and I can't be fucked to come up with a good bridge."
    "Time for a time skip~"
    window hide 
    pause 1.5 
    return 
label nh3:
    #day 6 (Week 3 Monday(Including Base game))
    play music t8
    "And just like that, the weekend flies by."
    "Guess I have to go wake Natsuki up."
    "I climb up the stairs and swing open the door to my old room."
    mc "Natsuk{nw}"
    stop music 
    scene bg bedroom 
    show natsuki turned towel ldown rdown pani ce om at h11 
    #natsuki towel sprite and mc room with wipeleft
    n "AH!"
    scene black with vpunch
    play sound "sfx/fall.ogg"
    "Natsuki roundhouse kicks me in the chest before slamming the door shut."
    "Well that was a little uncalled for."
    n "WHAT ARE YOU DOING, PERV?!"
    mc "I'm sorry! I was just waking you up for school."
    n "I've been up for an hour, I even made you breakfast!"
    mc "Oh..."
    mc "Sorry."
    n "Just learn to knock next time."
    mc "Yeah, got it."
    mc "Guess I'll just... Wait for you?"
    n "Duh!"
    n "You're lucky I didn't buy that self defence claymore Sayori was trying to pitch to me!"
    mc "Hold on... the what?"


    play music t6
    scene bg residential_day with dissolve_scene_full 
    show natsuki turned rhip curi om oe at f11 
    n "Say, where's Sayori? Doesn't she normally walk with you?"
    show natsuki neut cm at t11 
    mc "Eh, doesn't matter."
    mc "I'm sure her depression doesn't exist anymore."
    n shoc rdown om "Her what?!"
    show natsuki worr cm  
    mc "Doesn't exist anymore. It's fine."
    n om "Oh... okay."
    show natsuki cm 
    "The two of us proceed to walk to school in silence."
    stop music fadeout .5
    return 
label trip:
    if persistent.routes != 0:
        call screen dialog("You've already seen this scene, click skip if you don't feel like replaying it.", ok_action=Return())
    scene bg club_day with wipeleft_scene 

    play music t5 
    mc "Howdy!"
    show monika forward om oe happ lpoint at f11 
    m "Oh, hey [player]."
    show monika nerv 
    m "I've been uh..."
    m happ "Waiting for you."
    m rhip ce "We decided we would go on a field trip today!"
    m lean happ om oe "Since now that you're in a relationship, the club isn't really relevant anymore."
    m forward ldown rdown "So we're giving you one last hurrah!"
    m rhip "But first, poem sharing!"
    m "Get ready to write!"
    call poem
    play music t5
    scene bg club_day 
    show monika forward neut om oe at t11
    with fade  
    m n2 "Yeah... thought so."
    m lean happ om oe  "Oh well, it's picnic time!"
    show monika cm 
    mc "Hold on, I never agreed to this."
    scene park 
    show monika lean om oe at i11
    m "But can you stop me?"
    show monika forward happ cm ce 
    mc "{i}...Fair.{i}"
    "Monika smiles, taunting me."
    show monika oe lpoint om at f11 
    m "Okay, everyone!"
    m oe "I think it's time we eat!"
    show monika cm at t21 
    show sayori turned happ ce om rup at f22  
    s "Yay! I'm so hungry!"
    show sayori cm 
    "Is she ever not hungry?"
    show monika om ldown at f21 
    m "I brought us all sandwiches, what all did you bring?"
    show monika cm at t31 zorder 2
    show sayori at t11 zorder 2 
    show natsuki turned neut om oe at f33 zorder 3
    n "Cupcakes, what else would I bring?"
    show natsuki cm at t33 zorder 2
    show monika om at f31 zorder 3
    m "And what about you Sayori?"
    show sayori tap nerv om oe at f11 zorder 3
    show monika cm neut at t31 zorder 2
    show natsuki anno 
    s "I uh... forgot to bring anything."
    show monika ce om at f31 zorder 3
    show sayori cm at t11 zorder 2
    m "Oh well."
    show monika happ rhip oe 
    m "That just leaves you, Yuri."
    show monika cm at t31 zorder 2
    show natsuki neut 
    mc "What about me?"
    show monika anno rdown om at f31 zorder 3
    m "You don't matter."
    show monika neut 
    m "Now, Yuri?"
    show monika cm at t41 zorder 2
    show sayori at t42 
    show natsuki at t43 
    show yuri turned shoc lup rdown om oe n2 at f44 zorder 3
    y "Ah! Y-y-y-y-yes..."
    show yuri dist cm -n2 at t44 zorder 2
    "Yuri gingerly pulls out a bottle of wine."
    show sayori turned vsur lup rup om at f42 zorder 3
    show natsuki curi rhip 
    s "Uwaaa~"
    show sayori cry ldown 
    s "Yuri, alcohol is bad or something."
    show sayori sad cm at t42 zorder 2
    show yuri sad ldown om at f44 zorder 3
    y "I'm sorry..."
    show yuri cm at t44 zorder 2
    show monika neut om at f41 zorder 3
    m "As much as I'd love to take a drink, this is still official club business."
    show monika lpoint 
    call updateconsole ("No more wine")
    pause .3 
    hide console_bg
    hide console_caret 
    hide console_text
    hide ctext
    show yuri shoc om rup at f44 zorder 3
    show monika ldown at t41 zorder 2
    y "Huh? Where did my precious elixir disappear to?"
    show natsuki lhip rhip om neut at f43 zorder 3
    show yuri cm zorder 2
    n "Okay 'Thesaurus Lady', can we just eat?"
    show natsuki cm 
    y shy n5 neut om oe "Uuuuuuuuuuuuuuuuuuuuuuuuuuuu{nw}"
    y turned om oe ldown rdown neut "Alright.{fast}"
    stop music fadeout 1 
    return 
label nh3_2: #because I didn't seperate this from the picnic like a dumbass
    scene bg lrn with dissolve_scene_full
    play music t8 
    mc "Man, what a day!"
    show natsuki turned casual happ om oe lhip rhip at f11 
    n "I'll say!"
    show natsuki cm at t11 
    mc "So...you thinkin what I'm thinkin?"
    show natsuki neut at t11  
    n "..."
    n curi om ldown "{i}Parfait Girls{/i}?"
    show natsuki cm happ 
    mc "Of course! What else would I be thinking of?"
    n ce om "Exactly."
    stop music fadeout 1
    scene bg room_night with wipeleft_scene 

    
    "The two of us hike up the stairs to what is now Natsuki's room."
    "Upon entering, she walks triumphantly over to her parfait girls box and slides out the volume we left on."
    "Volume number...{w} 1468."
    "Wow, that's a lot."
    "Almost like the writers couldn't think of anything more original for us to do or bond through."
    "Except for baking, of course. But we've covered that one plenty already."
    "{i}Probably{/i}."
    "Shaking that thought, I refocus my attention on Natsuki."
    "She pats my old bed, beckoning me over."
    "I oblige and climb into the bed."
    "She opens the manga and we begin to read."
    "After a few minutes, I feel a bit more weight slump onto me."
    "Natsuki fell asleep on top of me. Oh no! What a wacky dilemma!"
    "Should I get up and risk waking her up from her sleep, or should I suffer in her warm embrace?"
    "..."
    "Yeah, think I'm gonna stay in bed."
    "A little while won't hurt."
    scene black with fade 
    window hide 
    pause .8
    window show 
    "Yeah..."
    window hide 
    pause 2.5
    return 
label nh4:
    #Day 7
    scene bg bedroom with dissolve
    "I awaken to the sun shining through the window."
    show natsuki turned casual neut ce cm at t11 
    "Groggily, I notice that unlike usual, I'm not alone."
    mc "Natsuki?"
    show natsuki om 
    n "G'morning."
    show natsuki cm 
    "She's not mad at me? Score!"
    "I live to see another day."
    mc "So, should we get up?"
    show natsuki om 
    n "Can we just stay like this?"
    n anno "Only for a bit longer... Baka."
    show natsuki happ cm 
    mc "Alright."
    "The two of us lay in our bed for a couple hours, despite it being a tuesday."
    "School doesn't matter for the plot anymore, and we can use the excuse of time skips or something."
    "Eventually, Natsuki releases her grip on me and hops out of bed."
    show natsuki lhip happ om oe at f11
    n "Alright, breakfast time!"
    show natsuki cm at t11 
    "Oh no." 
    "More cooking scenes."
    show natsuki at lhide 
    hide natsuki 
    "Thankfully, Natsuki runs downstairs without forcing me to help."
    "Which means that I get to sleep in."
    "Shortly after her departure, I decide to join her downstairs."
    scene bg kitchen 
    show natsuki turned sedu casual om oe rhip at f11 
    with wipeleft
    n "Well, well, well. Look who finally showed up!"
    n happ "Perfect timing, I just finished breakfast."
    show natsuki cm at t11 
    mc "Epic!"
    "Natsuki slides the eggs and bacon onto two plates."
    show natsuki ce om at f11
    n "Here you go. Eat up."
    show natsuki cm
    mc "Thanks, I appreciate it."
    show natsuki flus om oe 
    n "Y-you don't have to thank me or anything..."
    show natsuki lsur cm 
    play music t10 
    mc "Well, I want to."
    "Alright, it's time for another heart to heart or something."
    mc "To be honest, this house is so much more..."
    mc "Alive."
    mc "When you're around."
    mc "It's been some of the best three days of my life with you here, Natsuki."
    mc "You truly make me happy."
    mc "Because I..."
    "Here goes nothing..."
    mc "I love you."
    show natsuki pani om oe n3 
    n "H-huh."
    show natsuki cm 
    "She seems stunned, like a deer in headlights."
    show natsuki dist om at s11 
    n "I-I uh..."
    n "{size=5}Love you too.{/size}"
    show natsuki cm 
    mc "What was that?"
    show natsuki angr om at f11 
    n "I love you too! Okay!?"
    show natsuki cm at t11 
    "Well that was one angry confession."
    show natsuki anno 
    mc "I heard you the first time."
    show natsuki om at f11 
    n "Dick."
    show natsuki cm at h11
    play sound "sfx/smack.ogg"
    stop music  
    show white:
        alpha 0 
        linear .1 alpha .25
        easeout .1 alpha 0
    "She kicks me in the aforementioned area."
    mc "Augh!"
    mc "Was that really necessary?"
    show natsuki rhip lhip doub om at f11 
    n "Well, yeah, you totally deserved it!"
    show natsuki neut cm at t11 
    mc "But it derailed my plans of kissing you!"
    show natsuki curi om 
    n "Oh, we were supposed to do that?"
    show natsuki cm 
    mc "Uh..."
    mc "I...{w=.4} guess?"
    n ldown happ om "Great!"
    scene black
    "We then kiss or something."
    "It's pretty cool."
    
    play music t6 
    scene bg kitchen  
    show natsuki turned casual lhip rdown curi om oe at i11
    n "So, should we like... go out or something?"
    show natsuki cm happ 
    mc "Sure, why not."
    show natsuki om at f11 
    n "Alright, let's hit the road!"
    scene bg rr with wipeleft_scene


    pause .2
    "Ah 'restaurant', my favorite place to take dates to."
    show natsuki turned casual neut cm oe at t11 
    "Natsuki and I both scan through our menus."
    show natsuki worr om 
    n "Yo [player], you sure you can afford all this?"
    show natsuki cm happ 
    mc "Don't worry about it."
    "My wallet is definitely going to feel this one..."
    "But I can worry about that later."
    "I have more distracting things to focus on."
    "Eventually, a waiter pops up and takes our orders."
    "After the waiter leaves, we wait."
    "Then we eat for like the fifth time this week."
    scene bg kitchen with fade

    show natsuki turned casual happ happ om oe at t11 
    n "Thanks for taking me out, [player]."
    show natsuki cm 
    mc "My pleasure!"
    stop music fadeout 4 
    show natsuki dist om 
    n "Can I uh..."
    show natsuki neut 
    n "Can I show you something?"
    show natsuki cm 
    mc "Hm?"
    mc "Alright."
    show natsuki doub ce om 
    n "Here goes nothing..."
    play music t9
    show natsuki cm at d11 
    "Natsuki lifts up her shirt to reveal dozens of bruises?"
    "(It would sure be cool if we could actually see them.)"
    mc "Huh!?"
    mc "Natsuki, what happened? Are you okay?"
    show natsuki dist om 
    n "I fell."
    show natsuki cm 
    "Huh, makes sense."
    "..."
    n om oe "My dad hit me."
    show natsuki cm 
    "Who the fuck hits their daughter?"
    show natsuki sad om 
    n "He used to be... normal."
    n "Until my mom died."
    show natsuki cry 
    n "Then he went downhill."
    show natsuki fs ce om cry 
    n "He lost his job a-and he started..."
    n oe "Hitting me."
    n "So that's why I had to get out, [player]."
    show natsuki cm 
    mc "Natsuki..."
    mc "Don't worry, you're safe with me."
    show natsuki om at f11 
    n "I still love him."
    n "Even if he isn't the best."
    show natsuki cm at t11 
    mc "Natsuki, he sounds like a pretty awful person."
    n ce om "Yeah..."
    n turned sad om oe "But he's still my dad."
    show natsuki cm 
    mc "Someone who lays a hand on you doesn't deserve you."
    mc "Now... You want to go to bed and relax?"
    show natsuki ff dist om at f11
    n "Y-yeah..."
    show natsuki cm 
    mc "Alright."
    stop music fadeout 1 
    return 

label std:
    scene bg club_day 
    show monika forward neut cm oe at t11 
    with dissolve_scene_full  
    play music t3 
    mc "Wh- how did I get here?"
    show monika doub om 
    m "You... walked here?"
    show monika cm 
    mc "Oh yeah."
    "Damn time skips."
    mc "So, what's the plan for today?"
    show monika lpoint om happ 
    m "Well, we need to cover our bases..."
    show monika at f11 
    m rhip ce "And that includes saving all the dokis!"
    m oe ldown rdown "So, let's start, shall we?"
    if n_route == True:
        m "You're already helping Natsuki, so focusing on everyone else should be fine."
    if s_route == True:
        m "You're already helping Sayori, so focusing on everyone else should be fine."
    if y_route == True:
        m "You're already helping Yuri, so focusing on everyone else should be fine."
    show monika cm at t11 
    mc "Uh... alright."
    show monika lean happ om oe at f11 
    m "Good luck!"
    show monika at thide 
    hide monika 
    if y_route == False:
        show yuri turned neut cm oe at t11 
        mc "Don't cut yourself lol."
        show yuri nerv om oe at f11 
        y "T-t-t-t-t-t-t-t-thank you [player]. I'm cured."
        show yuri at lhide 
        hide yuri 
    if n_route == False:
        show natsuki turned neut cm oe at t11 
        mc "Just kill your dad."
        show natsuki lsur om at f11 
        n "Damn, that's hardcore."
        n curi "But what if I still love him or something?"
        show natsuki cm at t11 
        mc "Well my dog died last summer, so there's a doghouse in my backyard with your name on it!"
        show natsuki lhip rhip neut om 
        n "Sure, works for me."
        show natsuki cm at thide 
        hide natsuki 
    if s_route == False: 
        show sayori turned neut cm oe at t11 
        mc "Don't be sad."
        show sayori tap nerv om oe 
        s "You know... I'd be a lot less sad if you invested in my business endeavors."
        show sayori turned anno cm  
        mc "Sorry, I'm not interested in buying any nooses anytime soon."
        show sayori om at f11 
        s "Meanie."
        show monika forward sad ce om at l31
        m "Fine, I'll just buy one instead."
        show monika cm 
        show sayori happ lup rup om ce at h11  
        s "Yay! Thanks Monika!"
        show sayori at thide
        hide sayori  
    show monika forward cm oe neut at t11 
    mc "So that should be about everyone, right?"
    show monika anno oe om at f11 
    m "Aren't you forgetting someone?"
    show monika cm 
    mc "I don't think so."
    show monika lean anno om oe 
    m "...Yeah. You're probably right."
    show monika cm 
    m "..."
    show monika forward neut om 
    m "...Okay,{w=.4} everyone."
    m "I think it's time to go."
    show monika cm 
    mc "Alright, see ya Monika."
    if n_route == True:
        show monika at thide 
        hide monika 
        show natsuki turned neut cm oe at t11 
        mc "Hey Nat, ready to walk home?"
        show natsuki rhip angr om at f11
        n "Nat!?"
        show natsuki cm 
        mc "Do you not want to be called that?"
        show natsuki dist
        n "..."
        show natsuki om at f11 
        n "I guess it's fine."
        show natsuki cm at t11 
        mc "Great, lets go!"
        show natsuki neut at t22 
        show sayori turned curi lup rdown om oe at l21 
        s "What about me?"
        show sayori cm 
        mc "You don't exist in the story anymore."
        show sayori sad om oe at f21 
        s "Oh... okay."
    return 
label nfd:
    stop music fadeout .3 
    scene bg residential_day with wipeleft_scene
    mc "So, Nat. I've been meaning to ask..."
    pause .7
    mc "...Nat?"
    play music t7 
    n "Aaaah!!!"
    n "Help me, [player]."
    show natsukidad 2m at t11 zorder 7 
    show natsuki turned pani ce om at t11:
        rotate 30 
        yoffset -60 
        xoffset 50
        block:
            dizzy(3, 0.01)
            repeat 
    with wipeleft
    "I whirl around to see a man with pink hair running away, carrying Natsuki over his shoulder."
    mc "Natsuki!!!"
    "Natsuki reaches out in a desperate attempt to reach me."
    "Her hand ends up nowhere close to mine."
    show natsukidad at thide 
    hide natsukidad 
    show natsuki at thide 
    hide natsuki 
    "In shock, I stand still as the two grow smaller and smaller in my view."
    "Eventually, I snap into action and run after them."
    scene bg house_night with wipeleft
    "I finally see the man dart into a house and slam the door shut behind him."
    "Shit, that's probably her dad she was talking about the other day."
    "With no other choice, I dart up the driveway and swing open the door."

    scene bg lra with wipeleft 
    show natsukidad 2f at f11 
    show natsuki turned cry cm oe at t41 
    nd "You must be the person Natsuki ran off with."
    nd 3f "You should really mind your own damn business."
    nd 3d "Like damn, let me beat my child in peace."
    show natsukidad 1a at t11
    mc "I can't really just let you do that."
    mc "You're sick."
    show natsukidad 1b at f11 
    nd "And what are you going to do about it?"
    show natsukidad 1a at t11 
    "I need to think carefully about this."
    "This could be a matter of life and death."
    stop music fadeout 15         
    "So..."
    menu:  
    



        "Right Choice":

            "Time to beat this bastard into a pulp."
            "I shift into my best attack stance, mimicking that one guy from that one movie."
            "Natsuki's father dashes at me."
            "He takes a swing at me, but misses completely."
            "Sensing the opportunity, I use my elbow to jab him in his rib."
            show natsukidad 1u at f11 
            nd "My McRib!"
            show natsukidad at t11 
            "His McDonalds product drops onto the carpet as he stares down in agony."
            "While he's distracted, {w=.6}{nw}"
            play sound gun 
            show white zorder 30:
                alpha 0 
                ease .1 alpha .25 
                easeout .2 alpha 0
            show natsukidad:
                subpixel True
                .2
                easeout 0.25 yalign -20.0
            extend "I whip out a desert eagle and blow his brains out."
            hide natsukidad 
            "Where from?{w=.6} Who knows."
            "Wonder if the police will be mad at me?"
            "Eh, probably not."
            show natsuki om at t11 
            n "[player]..."
            show natsuki ce happ cm at face 
            "Natsuki wraps me in a warm embrace."
            show natsuki om 
            n "You saved me..."
            show natsuki oe 
            n "T-thank you."
            show natsuki cm 
            mc "I'd do anything to keep you safe."
            mc "Now, what do you say we go home and become stuck in an eternal loop of reading parfait girls and baking cupcakes?"
            show natsuki rhip ce om at t11 
            n "Hell yeah!"
            if persistent.n_complete == False:
                $ persistent.routes += 1
                $ persistent.n_complete = True 
            



        "Wrong Choice":

            "Alright, I've got it!"
            "I pull out a five pound bag of flour and a copy of parfait girls."
            "Where from?"
            "I dunno."
            "But that's besides the point."
            "Now I can save Natsuki from her awful abusive father with {i}FORCED SYMBOLISM{/i}!!!"
            "I chuck the bag of flour as hard as I can."
            show natsukidad 1e zorder 10 
            "It sinks to the floor a foot and a half away from me."
            "...Maybe this book can help me."
            show natsukidad 1k 
            "Lets see..."
            #natsuki's dad slowly grows closer
            "I flip over to a random page."
            "Maybe I can find some wisdom in this thing."
            show natsukidad:
                ease 1 zoom .9 yoffset 20
            "Two households, both alike in dignity,{w=1}{nw}"
            show natsukidad:
                ease 1 zoom .95 yoffset 40
            "In fair Verona, where we lay our scene,{w=1}{nw}"
            show natsukidad:
                ease 1 zoom 1 yoffset 60
            "From ancient grudge break to new mutiny,{w=1}{nw}"
            show natsukidad:
                ease 1 zoom 1.05 yoffset 80
            "Where civil blood makes civil hands unclean.{w=1}{nw}"
            show natsukidad at face 
            "From forth the fatal loins of these two foes{w=1}{nw}"
            "A pair of star-cross'd lovers take th{nw}"
            window hide 
            pause 1
            show natsukidad 2m 
            pause .5
            play sound "sfx/slap.ogg" 
            scene black 
            pause .2 
            play sound fall 
            pause 4
            m "...Dumbass."
    #credits
    #Epic credit sequence, coupled with epic soundtrack
    return 
  
    
label sh1:
    
    scene bg residential_day
    show sayori turned uniform happ cm ce lup rup at t11:
        rotate 0
        linear 1 rotate 360
        repeat 
    with wipeleft_scene 
    play music t8 
    "Sayori (who is currently spinning for some reason) and I walk home." 
    "I get the urge to ask about her \'Uwaa-ing\' earlier, but I don't want to come off as intrusive." 
    "Instead, I decide to ask about her day." 
    mc "So.. How was your day?" 
    s om neut "61 degrees."
    show sayori cm 
    mc "Fahrenheit or celsius?"
    s ldown "Eh, I dunno."
    show sayori rdown cm 
    mc "Alright then."
    "We end up walking home in a calm silence."
    "Eventually we say our goodbyes, and enter our respective houses." 
    show sayori happ ce om at f11 
    s "See ya, [player]!" 
    mc "See you, Sayori." 
    stop music fadeout 1 
    scene bg bedroom with fade 
    "Welp, nothing relevant to do at home yet. Guess it's time to go to sleep."
    scene black 
    pause 2 
    scene bg bedroom 
    "Ah, morning!"
    "Time to go see what Sayori is up to!"
    "After all, she's the important one in this route."
    pause 1
    "...What's that?{w=.5} What about the club?"
    "That doesn't matter anymore, we only care about Sayori now!"
    if persistent.routes != 0:
        "Maybe only because I already played another route, but who cares?"
        if persistent.s_complete == True:
            "Or I only finished the Sayori route and for some reason played it again instead of trying to play another route."
            "...Which in practice a) circumvents the check set in place for the previous one line joke, and b) proves that I am a simp."
            "Where was I?"
            "Oh, right."
    "I get out of bed and tactically roll down my stairs."
    play music t2 
    scene bg kitchen 
    show sayori turned happ om oe casual lup rup at face 
    show layer master at vpunch 
    s "HI [player!u]!!!"
    show sayori cm
    mc "Gah! What are you doing in my house?"
    show sayori lup om at t11  
    s "I thought I would pay you a surprise visit! Just like when we were kids!"
    show sayori cm 
    mc "Ah, okay, makes sense."
    show sayori neut 
    mc "Hey, remember that one time we \[INSERT EVENT HERE\] when we were kids?"
    s rup ce om happ "Oh yeah! I totally do!"
    show sayori cm oe at t11
    mc "Fun times."
    show sayori yand oe cm:
        dizzy(.1,.1) 
    mc "So, want to get food or something?"
    s om "I love food!"
    show sayori:
        parallel:
            rotate 0 
            ease .3 rotate -360 
            repeat 
        parallel:
            ease .4 xoffset -2000
    pause .4 
    show layer master at hpunch 
    play sound crash 
    s "FOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOIDONOTRECOGNIZETHESTATEOFISREALOOOOOOOOOOOOOOOOO"
    "Guess I should follow her."
    scene bg rr with wipeleft_scene
    mc "So Sayori, how are you feeling today?"
    show sayori turned casual neut lup rdown casual om e3a at i11
    stop music 
    s "I am entirely motivated by food."
    show sayori at f11 
    play music t8 
    s yand om oe -e3a "So I'm great!"
    show sayori cm 
    mc "I'm glad to hear it."
    show sayori:
        ease 2.3 zoom .82
        ease 2.3 zoom .85
        repeat  
    "A pause comes over us as neither of us can think of what to say."
    "But it isn't awkward really, the two of us are just enjoying each other's presence and munching on fries."
    "It's quite nice, just the two of us sitting across from each other, me and my cute food vacuum waifu."
    "{i}Bet that's a phrase you never expected to hear.{/i}"
    mc "Hey Sayori, this reminds me of all the times we went to this restaurant as kids."
    show sayori happ ce om ldown rup at f11 
    s "Oh yeah!"
    show sayori cm dist at t11 
    mc "I still don't understand how you managed to burn down a restaurant you didn't work at."
    mc "Hell, it only reopened last week!"
    s doub oe om "Eh? Don't remind me, meanie!"
    show sayori cm 
    mc "Alright, alright. I'm sorry."
    show sayori happ om 
    s "No biggie, [player]."
    show sayori cm 
    stop music fadeout 3
    "Sayori killed twelve people that day."
    "I can still remember the screams reverberating throughout the smoldering Jack in the Box™."
    #Time skip
    scene black with fade 
    window hide 
    pause 1 
    scene bg rr
    show sayori turned casual happ ce cm at i11 
    with fade 
    play music t2 
    mc "Man I'm stuffed, what about you Sayori?"
    show sayori neut om oe at f11 
    s "My stomach is an abyss with infinite capacity for nutrients."
    show sayori cm 
    mc "Do you want me to like... buy you more fries?"
    show sayori happ om at t11 
    s "It's fine. I'll be a-okay!"
    show sayori cm 
    mc "If you say so."
    "It seems our lunch 'date' is coming to a close."
    "But there's still plenty of light out, so maybe we can find something else to do."
    show sayori neut 
    mc "Hey Say, did you want to take a stop at the park on the way back?"
    show sayori happ om at f11 
    s "That sounds like fun!"
    show sayori cm at t11 
    "With Sayori's approval, the two of us depart to go to the park."
    stop music fadeout 1.5 
    window hide 
    scene black with fade
    window hide 
    pause 1 
    scene park2 
    show sswing:
        truecenter
        yoffset -500
        zoom .8
        block:
            rotate 0
            linear .25 rotate 360 
            repeat  
    with fade 
    window hide 
    play music t6 
    pause 2 
    s "Wheeeeeeeeeeeeeeeeeeeeee!"
    "Man, I didn't know I could swing a swing so fast."
    "Is this like... safe? I won't like, turn her into a pancake or something?"
    "Great. Now I'm hungry again."
    "No! I have to focus on not letting my dearest friend, no, the love of my life, die via a concoction of centripetal force and woodchips."
    "Alright, I've got a plan."
    mc "Yo Sayori, let go of the swing!"
    "I have to shout for my voice to reach her in the heavens."
    s "Okay!"
    "With no hesitation, she lets go and is sent hurtling towards the sun."
    stop music fadeout 5 
    scene sky with dissolve 
    "Just gotta line this up..."
    play sound "mod_assets/whistle.mp3"
    pause 1.5   
    show white zorder 2:
        alpha 0 
        2
        ease 2 alpha 1
    pause 6 
    play sound "mod_assets/fire.mp3"
    scene white 
    scene parkfire 
    show schild zorder 1 at i11:
        zoom 1.6 #child sayori sprite
        dizzy(1,.001) 
    show parkfm zorder 2
    with dissolve 
    s "EVERYTHING WILL BURN."
    s "NOTHING IS FREE FROM THE HELL THAT I CAST UPON IT."
    s "YOU WILL ALL PERISH BENEATH ME."
    stop sound 
    scene park2 
    show sayori turned casual happ cm oe lup rup at i11 
    with wipeleft 
    "I'm starting to think this may be a problem of hers."
    show sayori nerv om 
    play music t8 
    s "Thanks for catching me ehehehehehe~"
    show sayori neut cm 
    mc "I guess you could say you've... fallen for me."
    s curi om rdown "I guess?"
    show sayori neut cm  
    mc "What do you say we call it a day? I can only take one near death experience per park trip."
    show sayori happ om ldown rdown at f11 
    s "Oh, like that time we met that weird football guy?"
    show sayori cm at t11 
    "I... don't know exactly what she's talking about, nor do I want to know."
    mc "Yeah, exactly like that."
    scene bg house_night with fade
    mc "So uh... see you tomorrow?"
    show sayori turned casual om oe at f11 
    s "Yeah, I had a great time! It's been a while since we last hung out like this."
    s sedu "When's the last time we spent time together outside of school anyways?"
    show sayori neut cm at t11 
    mc "Probably when you burned down that movie theatre."
    show sayori ce om lup rup at f11 
    s "Oh I remember now!"
    show sayori cm at t11 
    mc "I remember all too well."
    show sayori doub rdown om oe 
    s "Hey, don't judge me! They undercooked my popcorn."
    show sayori anno cm
    mc "Ah, you and your food."
    show sayori om ldown rdown 
    s "Yeah, yeah, laugh it up."
    stop music fadeout 2 
    show sayori cm 
    "A brief pause overcomes us as we take in the silence of our surroundings."
    show sayori dist n3 om at f11 
    s "Hey, [player], there's something you should know..."
    show sayori cm at t11 
    mc "Yeah, what is it?"
    show layer master:
        zoom 1 
        subpixel True 
        truecenter 
        ease 60 zoom 10 yoffset 900
    pause 60
    show layer master 
    #zoom out
    show sayori neut -n3 om 
    s "I love you."
    show sayori cm 
    mc "Wait, what?"
    "I thought this was gonna be another pitch for her self defence noose or whatever."
    show sayori anno om lup rdown 
    s "You heard me, meanie."
    show sayori cm at t11 
    mc "Uh, yeah, I did. You just caught me off guard."
    show sayori neut om at f11 
    s "Are you really that surprised? I mean we've basically known each other our whole lives."
    show sayori cm at t11 
    mc "Well yeah, that's basically the only thing we talk about."
    pause .2
    show sayori lsur 
    mc "I uh... love you too?"
    show sayori om lup rup 
    s "R-really?"
    show sayori cm at t11 
    mc "Didn't you just say it wasn't surprising you had feelings for me? What makes it different the other way around?"
    show sayori sad om n3 at f11 
    s "Well, yeah, but, it's {i}me{/i} we're talking about, I haven't even seen another guy in my life, and there's {s}three{/s} two cute girls you can go for in the club, wouldn't you rather be with either of them?"
    show sayori cm at t11 
    mc "I love {i}you{/i}, Sayori. and I wouldn't have it any other way."
    if persistent.routes != 0:
        if persistent.s_complete == True:
            pass 
        else:
            "I also already went through another route, but who am I to rain on her parade."
    scene black with close_eyes
    "We then kiss or something."
    "It's pretty cool."
    scene bg house_night
    show sayori turned happ lup rdown casual cm at t11  
    with fade 
    show sayori om at f11 
    play music t6 
    s "So, now that you're my boyfriend..."
    show sayori ce om lup rup at hf11
    s "You have to come help me make an ad for my self defence noose!"
    show sayori cm at t11 
    "I've been played."
    show sayori oe om rdown lup 
    s "Chop chop, [player], I've got the video camera set up in my living room!"
    #fade to residential day
    stop music fadeout 1 
    return
label ss2:
    window hide 
    scene black with fade 
    pause 1 
    scene bg residential_day with dissolve 
    play music t2 
    s "HEEEEY!"
    show sayori turned uniform happ cm ce lup rup at t11 
    mc "Oh hey Sayori, you're up early!"
    show sayori om oe at f11 
    s "You noticed~"
    s ce "It sure is a sunny day!"
    show sayori cm at t11 
    "I look up."
    mc "Yeah, it sure is."
    show sayori om neut oe
    s "I meant more metaphorically, but yeah."
    show sayori cm  
    mc "You know what metaphors are?"
    show sayori at hf11 
    s happ ce om "Nope!"
    show sayori cm at t11 
    mc "Oh."
    show sayori neut om oe ldown 
    s "So, did you wanna walk to school together?"
    show sayori cm 
    mc "Sure."
    show sayori happ ce om at f11 
    s "Yippie!"
    show sayori cm at t11 
    stop music fadeout .9
    scene bg club_day with fade 
    show sayori turned uniform happ om oe at f11 
    play music t6 
    #fade to club I guess 
    #show sayori 
    s "Hey everyone, I have an announcement to make!"
    show sayori cm at t42 zorder 10
    show yuri turned cm at t41 
    show monika forward cm at t44 
    show natsuki turned cm at t43  
    "All of the club members turn to address Sayori."
    show sayori ce om lup rup at f42 
    s "I am depression!"
    window hide 
    show sayori cm
    pause .3  
    show sayori at t42 
    show yuri dist 
    show natsuki curi 
    pause .5 
    show yuri om zorder 11 
    y "...Do you mean {i}have{/i} depression?"
    stop music 
    show yuri pani cm lup zorder 2 
    show sayori vang om oe at f11 zorder 1:
        zoom .8
        ypos 1.03
      
        ease .2 xoffset -300 rotate -15 yoffset 70 zoom .9
    show veins zorder 100 onlayer front
    show vignette zorder 99 onlayer front 
    show layer master:
        truecenter 
        ease_elastic .25 zoom 1.6 xoffset 400 yoffset 70  
    #zoom plus vignette focusing on sayori and Yuri
    s "DON'T RUIN THIS FOR ME, YURI."
    show sayori cm 
    show yuri om rup ce pani 
    "Yuri" "{size=8}\"{i}imsorry."#small text
    #effect ends abruptly
    play music t3
    show layer master:
        truecenter 
        zoom 1.6 
        xoffset 400 yoffset 70
        ease 6 zoom 2.4 xoffset 800 yoffset 140 
    pause 8 
    show layer master 
    hide veins onlayer front    
    hide vignette onlayer front
    hide natsuki 
    show yuri at i31 
    hide sayori 
    show sayori turned uniform neut cm oe at i11
    show monika anno om oe at i33
    m "{i}Ahem.{/i}{w} We're very proud of you for telling us and support you indefinitely."
    show monika neut cm at t33 
    show sayori curi om at t11 
    s "Even if I burn things to cope with my sadness?"
    show sayori cm at t11 
    show monika doub om 
    m "Yeah, sure, knock yourself out."
    show monika cm 
    mc "{i}Please don't encourage her.{/i}"
    show yuri at thide 
    hide yuri 
    show monika at thide 
    hide monika 
    show sayori yand om oe rup ldown at f11 
    s "The reckoning is nigh, [player]."
    s "The flames of cleansing will turn everything in this world to ash."
    "Writers, a little help here?"
    scene black
    stop music 
    window hide 
    pause 2 
    return
label sn1:
    #fade into picnic scene (already written in Nat route)

    scene bg house_night with fade 
    mc "Boy, what a day that was."
    show sayori turned nerv om oe lup rdown uniform at t11 
    s "Say, it's late, and our parents are not only not home, but basically nonexistent." 
    show sayori cm 
    mc "Yeah?"
    show sayori tap nerv om oe 
    s "{cps=14}Did you maybe wanna..."
    show sayori at f11 
    s "{cps=12}Buy a self defenc--{nw}"
    show sayori turned oe ldown rdown anno cm at t11 
    mc "Not interested."
    show sayori doub om rup ldown 
    s "Meanie."
    s "In that case, I'm going to sleep."
    show sayori cm 
    return
label send: 
    #fade into save the dokis scene (also from natsuki's scene but I'll have to write a few lines for Natsuki
    stop music fadeout 1 
    scene bg residential_day with fade 
    "Ah, the weekend~"
    "It's a nice day out, couldn't have asked for any better."
    "Say, I wonder what Sayori is up to on this fine afternoon."
    scene black with wipeleft_scene
    pause 1.5
    "Uhh...{w=.5} Why is her house so dark?"
    "It made sense when it was nighttime, but it's the middle of the afternoon."
    "Does she just not have windows?"
    "Or maybe this is just some kind of time or budget constrai--{w=.3}{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    hide screen tear
    "Lets go see what Sayori is up to."
    "I gently open the door, not because I really care about being sensitive, but because it feels right."
    play sound opend 
    scene bg sayori_bedroom 
    show sayori turned pjs dist rnoose ldown cm oe at i11 
    with wipeleft
    #sayori in suicide clothes with noose
    show sayori happ 
    mc "Hey Sayori."
    "Her eyes light up when she sees me."
    show sayori om at f11 
    s "Oh! Hiya [player]! It's great to see you."
    show sayori neut cm at t11 
    mc "Performing some R&D on your self-defence noose?"
    show sayori ce happ om at f11 
    s "You know it! Wanna help me test it?"
    show sayori sad cm at t11 
    mc "I'll pass, thank you very much."
    show sayori neut om oe
    s "Welp, looks like it's up to me."
    show sayori cm e2b at t21 
    "Sayori begins fastening the rope to her ceiling."
    show sayori at d21  
    "She then grabs a chair and slides it underneath."
    "Hey, wait a minute..."
    show sayori -e2b oe
    mc "Sayori, you aren't going to try killing yourself, are you?"
    show sayori happ ldown ce om 
    s "hehe, no silly~"
    s neut oe "It's not a matter of trying, I will succeed."
    show sayori cm 
    show vignette with dissolve
    "My heart rate accelerates."
    "Fuckfuckfuckfuck."
    "Sayori's life in danger right now."
    "What should I do?"
    #choice between right and wrong

    menu:
        "Right Choice":
            show sayori om at f21 
            s "Hey, could you step out for a second?"
            show sayori cm at t21 
            mc "When you're about to off yourself?"
            s nerv om "Well yeah, you don't want to see it happen, do you?"
            show sayori cm 
            play music t9 
            mc "I don't want it to happen in the first place!"
            s happ om "Relax, once I'm gone, there's three other people you can talk to."
            s neut "Actually there's only two worth talking to, but that's being nitpicky."
            show sayori cm 
            mc "But we all care about you, and I don't want to talk to any of them."
            mc "Hell, they're practically entirely ignored on this route."
            show sayori om ldown 
            s "I guess you have a point."
            show sayori angr om 
            s "But I would've wasted so much time!"
            s sad ce om "I made this whole business solely as a guise to hold onto a ton of nooses."
            show sayori cm 
            "Wow, she's a lot more clever than I have her credit for."
            "Even if that's way darker than this mod should be."
            show sayori doub om oe 
            s "It would be such a drag to {i}not{/i} kill myself at this point."
            show sayori cm neut at t21 
            mc "Okay, first, wouldn't you be wasting more time by just not living?"
            show sayori lsur 
            mc "Second, we don't have to waste the nooses, we could build a massive corporate empire."
            show sayori happ 
            mc "I'll help you sell all your nooses so you don't have to throw them out."
            "I sure hope people end up buying them because they're at a competitave price and not because they come pre-tied."
            show sayori om at f21 
            s "Alright, you've got a deal."
            s "Pleasure doing business with you."
            show sayori n3 cm at t21 
            "Sayori steps down from her chair and embraces me."
            scene black with fade
            stop music fadeout 2
            window hide  
            pause 1 
            mc "So, are you feeling a little better now?"
            s "One hundred degrees."
            mc "Wait, were the degrees just percentages the whole time?"
            if persistent.s_complete == False:
                $ persistent.routes += 1
                $ persistent.s_complete = True 
            return 
     

        "Wrong Chioce":
            show sayori neut om at f21 
            s "Hey, could you step out for a second?"
            show sayori cm at t21 
            mc "Huh? Uh, yeah, sure."
            show sayori  happ om #lup 
            s "Great! Thanks."
            play sound closed 
            scene black with wipeleft_door 
            s "Alright, now count to 30 and come back in."
            mc "Is this a game of hide and seek?"
            s "Sure is!"
            "I chuckle."
            "She really is childish. I mean, when was the last time we played hide and seek?"
            "Better get to counting."    
            jump counting
label send2: 
    mc "30!"
    mc "Ready or not, here I come!"
    "I excitedly gently open the door."
    play sound opend 
    scene bg sayori_bedroom
    show s_kill:
        truecenter 
        xoffset -400 yoffset 40 zoom .8 
    with wipeleft_door
    play sound sting  
    window hide 
    pause 4 
    play music t7
    #monika is behind the window, disappointed 
    "Oh wow, she killed herself."
    "I for one, am shocked."
    "And why is poem panic playing?"
    window hide 
    stop music fadeout 2 
    pause 2 
    "...That's better."
    "Hold on, there's a note clenched in her fist." 
    call showpoem(poem_s2)
    play sound "mod_assets/fire.mp3"
    "Of course."
    "But who's going to be selling the nooses if she's dead?"
    stop music 
    "Also, is something burning?"
    window hide 
    return 

label ys2:
    scene bg corridor with fade 
    window hide 
    pause .45
    "I approach the clubroom door, and hear voices going to and fro." 
    m "And then I said…" 
    m "That's not a hippo, that's my wife!" 
    #"A bit out of character, don't you think?" 
    #"Time to ping the creators of this mod on Discord!" 
    "I enter the club, really taking in the flooring joke Monika bestowed upon my ears."
    scene bg club_day 
    show sayori hang at i31 
    show monika forward laug om lpoint ce rhip at i22 
    with wipeleft_scene
    window hide  
    #show monika talking to a hanging sayori, realizing she's hanging, and bringing her back
    #closet bg
    pause .5 
    show monika happ cm oe ldown with dissolve 
    pause 1 
    show monika vsur at h22 
    pause 1.5   
    show monika ce lpoint 
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    hide s_kill 
    pause .25 
    hide screen tear 
    show monika at d22 
    show sayori turned cm neut ce at t21
    pause 1.5 
    show monika anno oe ldown rhip 
    show sayori lsur oe 
    pause .15 
    show sayori lsur ce 
    pause .15 
    show sayori oe 
    pause .15 
    show sayori ce 
    pause .15 
    show sayori oe 
    pause .5 
    scene bg closet
    show yuri turned dist oe cm lup rup at t11 
    show layer master:
        truecenter 
        zoom 1.7 
        yoffset 200 
    with wipeleft 

    "Looks like Yuri is over by the closet."
    "Should I go converse with her?" 
    "I know it's been like, what? A day?" 
    "But I think her eloquence is really rubbing off on me..." 
    "Now, not to be a filthy weeaboo protag or anything..." 
    "But damn does she look like an anime girl." 
    "Kawaii-desu if I do say so myself."
    pause 1
    "I'm sorry."
    pause .5  
    "Ahem, getting off track."
    "On the other hand..."
    show natsuki turned cm rhip ldown angr cm ce at i31:
        zoom .3
        
    show layer master:
        truecenter 
        subpixel True yoffset 200 zoom 1.7
        ease 3 yoffset -1620 xoffset 2500 zoom 7
    #pan to really tiny natsuki
    pause 3 
    "I don't really feel any of Natsuki's charm rubbing off on me."
    "Maybe if I was into children..."
    "But alas."
    n om lhip "...It's like I told you yesterday, MANGA IS LITERATURE!"
    show natsuki cm
    show layer master:
        truecenter subpixel True  
        yoffset -1620 xoffset 2500 zoom 7
        ease 2 zoom 1 yoffset 0 xoffset 0 
    show yuri anno rdown om ce 
    pause 1.3
    y "This again?" 
    show yuri oe cm 
    show natsuki angr om ldown rdown 
    n "Yes, this again, book girl."
    show natsuki neut cm oe 
    pause 1
    show natsuki angr om 
    n "Hey, Camera!{w} I'm down here!"
    show layer master:
        truecenter 
        subpixel True 
        easein_quint 1.5 yoffset -1620 xoffset 2500 zoom 7
    # zoom back to Natsuki
    show natsuki cm 
    pause 2  
    n doub ce om "It doesn't matter anymore, I already said what I wanted to say!"
    n anno oe "{i}Thanks for nothing.{/i}"
    show natsuki cm oe
    n angr om "What are you waiting for? Pan up so Yuri can respond!"
    show layer master:
        truecenter subpixel True xoffset 0 zoom 1.7 yoffset 200 
    with dissolve
    y happ om "Thank you, Natsuki."
    show yuri cm 
    pause .5 
    y doub ce om "Ahem,{w=.6} Natsu--{nw}"
    show yuri cm ce lsur zorder 3 
    show natsuki zorder 3 
    show sayori hang:
        xoffset -1000 
        ease 1.75 xoffset 1500 
    show yuri lsur oe 
    pause 1.5 
    #hanging sayori slides across the scene with monika chasing here
    s "{i}You can't catch me~~~~~{/i}{nw}"
    show monika forward vsur om oe at l31 
    m "How are you even moving!? Let me fix you!"
    show monika cm:
        easein_quint .4 xoffset 1500
    

    #zoom in on natsuki, hide monika and sayori
    pause .5
    "..."
    scene bg closet 
    show yuri turned cm dist oe lup rup at i22 
    show natsuki turned cm oe neut at i21 
    with dissolve_scene_full
    pause .5 
    show natsuki at f21 
    n lhip curi "So, where were we?"
    show natsuki cm at t21 
    show yuri om at f22 
    y "I'm... not really sure I have the urge to continue the debate on why you're wrong."
    #n "Jeez, no wonder you're…"
    #pause .5 
    #n "CAMERA, GET THE FUCK OVER HERE RIGHT THIS INSTANT."
    #zoom into natsuki
    show yuri cm at t22 
    
    #n "{b}As I was saying,{w}{/b} Yuri, are you really that spineless?"
    show natsuki cross ce om angr at f21 
    n "Jeez, are you really that spineless?"
    n anno "No wonder you don't have any friends."
    #camera slowly zooms out as yuri pauses before dipping
    show yuri cry ce om at s22 
    y "Uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu{nw}"
    show yuri cm:
        ease .5 xoffset 3000 
    show natsuki turned sad cm oe at t21 
    pause 1.5 
    show natsuki worr om at f21  
    n "...Too far?"
    show natsuki cm at t21 
    hide yuri 
    "I…{w} I should probably go comfort Yuri."
    #hallway bg 
    scene bg corridor with fade 
    mc "Yuri?"
    "Hmmmm... Calling her didn't work. Looks like I'm going to have to do some walking."
    mc "Maybe she's down these stairs."
    #immediate scene change to yuri cutting with ddlc+ stair bg
    scene vend 
    show yuri turned pani rcut lup om oe at h11 
    y "AAAAHH!!!"
    show yuri cm 
    mc "There you are!"
    mc "Oh jeez, that's a lot of blood!"
    mc "Are you on your period?"
    show yuri flus om at f11 
    y "Huh? Uhhhhhhhhhhh."
    show yuri cm at t11
    "Hold on…"
 
    pause 1     
    "Silly me! Periods don't make blood come from your arm!"
    "I would know, since I have one every month."
    "That's right! I, [player], am canonically a girl now!"
    "But only on the Yuri route."
    "I mean, you should have expected this from the name."
    y ce om rdown "I was j-j-j-j-j-j-j-j-j-j-j-j-j-just…"
    show yuri nerv oe at f11  
    y "Making tea!"
    y ce "That's right! Making tea, and nothing else."
    y nerv "I wasn't cutting myself or anything l-like that!"
    y laug "Why would I do something so strange?"
    show yuri cm lsur 
    mc "Oh, so that's what you were doing."
    show yuri at f11 
    y pani om "No! I-{nw}"
    show yuri dist cm oe at t11
    "Yuri pauses as she averts her gaze."
    y ce om "Yes, I was cutting myself."
    show yuri cm 
    "I was talking about the tea, but go off I guess."
    y oe om "I've been doing it for as long as I can remember."
    y sad ce "I understand if you hate me now. You don't have to talk to me anymore."
    show yuri worr cm oe 
    mc "Why would I hate you?"
    show yuri lup om at f11 
    y "Y-you don't?"
    show yuri cm curi at t11 
    mc "I think you're pretty poggers!"
    y neut om "I'm sorry, I'm not quite sure what that word meant. Give me a moment."
    show yuri cm book em
    
    "Yuri pulls out a dictionary and begins furiously flipping its pages."
    show yuri -book -em 
    mc "Forget it."
    mc "Cutting yourself probably isn't the most productive hobby, but it doesn't make you any less of a person."
    mc "So keep your chin up! You have the whole club to support you."
    show yuri dist rdown lup om
    y "B-b-b-b--b-b-b-b-b-b-b-b-b-b-b-b-b-b-b-b-b--bb--b-b"
    show yuri cry cm ce at s11 
    "Yuri has trouble speaking as tears begin forming around her eyes."
    show yuri om at t11 
    y "But they hate me."
    y oe "You heard what Natsuki said earlier!"
    show yuri cm 
    mc "That's just Natsuki being Natsfuki."
    "A half height banshee that really likes drawings of anime girls, that is."
    mc "She's just projecting her own feelings onto you since she felt attacked."
    #zoom 60
    #wait why the fuck would I zoom 60?
    #also mcs last line is fucking stupid
    #oh well, I don't care enough about this mod anymore
    y om "I see."
    show yuri sad ce 
    "Yuri wipes some tears from her cheek, getting blood on it."
    mc "You uh… may want to go wash off in the bathroom."
    mc "We can talk about getting you some help some other time."
    y nerv om "Alright. t-t-t-thank you, [player]."
    show yuri cm 
    mc "Anytime."
    mc "I'll walk you back to the club when you're ready."
    y neut om oe "Right."
    show yuri cm 
    scene corridor_r with dissolve 
    "This time, there were no voices inside the clubroom."
    "Just silence."
    mc "You ready?"
    #breath posing
    #yeah fuck that im lazy
    show yuri turned neut cm oe at t11 
    "She nods."
    scene club_r with wipeleft_scene
    "Hearing the door open, Natsuki gets up from the corner where she had been hunched up."
    show natsuki cross dist oe om at l21 
    n "...Hey."
    show natsuki turned dist oe cm  
    show yuri turned dist ldown rdown at t22 
    y "Hi."
    show yuri turned cm at t22 
    show natsuki curi om rhip ldown 
    n "So, the weather today..."
    show natsuki cm 
    show yuri happ ce om at f22 
    y "Indeed, it is quite pleasant."
    y oe "The clouds, with the hue of our uniforms, drifting across the sky."
    y neut "The rain, dropping peacefully to the ground."
    y curi "And who could forget the crackling that occasionally interrupts our speech?"
    play sound "mod_assets/thunder.mp3"
    show natsuki neut om at f21 
    show yuri cm at t22 
    n "Yuri, we're in a thunderstorm."
    show natsuki cm at t21 
    y dist om "...Right."
    show natsuki curi ldown rdown om at f21 
    show yuri cm 
    n "You find that pleasant?"
    show natsuki cm at t21
    show yuri shy om oe at f22 
    y "I do."
    show yuri cm at t22  
    show natsuki laug ce om at f21 
    n "Heh. You're so weird, Yuri!"
    show yuri om at s22  
    show natsuki cm oe neut at t21 
    y "Uuuuuuuuuuuuuuuuuuuuuuuuuuuuuu..."
    show yuri cm 
    show natsuki sad om at f21 
    n "I mean that in a good way. Like, {w=.5}I enjoy hearing you talk about things."
    n ce dist "Look, I'm sorry for being a bitch earlier."
    show natsuki cm at t21 
    show yuri turned dist om lup rup at f22
    y "I'm… also sorry. For not ever taking you seriously."
    show yuri cm at t22 
    n oe om "Thanks."
    show natsuki neut om lhip rdown at f21 
    n "So, we cool?"
    show natsuki cm at t21 

    #thunder 
    show yuri happ om at f22 
    y "Yes."
    show yuri cm at t22 
    show sayori turned happ ce om zorder 3 at h11 
    s "Hooray for friendship!"
    show sayori cm 
    "It seems the two of them made up for their quarrel from earlier."
    show sayori at thide 
    show yuri at thide 
    show natsuki at thide 
    hide sayori 
    hide yuri  
    hide natsuki 
    show monika lean happ om oe at t11 
    m "Okay, everyone!"
    show monika forward lpoint rhip happ ce om
    m "It's time for us all to head home."
    show monika cm oe neut at t22
    show natsuki turned lhip curi om oe at t21  
    "Natsuki" "\"Shouldn't we wait until this storm stops, {w=.1}{nw}"
    #monika disappears
    show monika:
        alpha 1 
        easeout_quint .3 alpha 0
    n "Shouldn't we wait until this storm stops, {fast}Monik--"
    show natsuki lsur cm at t11 
    n "..."
    show natsuki cross angr om ce at f11  
    n "Motherfuc--{nw}"
    scene black
    stop music 
    pause 1.5
    return
label ytp:
    scene forest with fade 
    pause 5 
    #zoom for 999 seconds
    "Where am I?{fast}"
    #"I barely leave my room, much less go exploring in a forest."
    "What the hell did Sayori put in that cookie she gave me earlier!?"
    "I should've known by the fact that she willingly gave up her food that there was something up."
    pause .5
    "I hear faint rusting in the distance as I take in my surroundings."
    "Oh god, am I going to get eaten by a bear?"
    "No, maybe it's Sayori. I mean I was with her before I fell asleep."
    "Hopefully she'll know how to get home."
    scene forest2 
    #show objects zorder 4
    show yuri turned dist ce cm at i11 zorder 5 
    #show objects as obj2 zorder 6 #ADD TRANSFORMS
    with wipeleft 
    mc "Oh, hi Yuri!"
    show yuri pani om oe at h11  
    show layer master at vpunch  
    y "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA{nw}"
    y vsur "[player]? What are you doing here?"
    y "This place is five hundred miles from civilization!"
    show yuri cm 
    mc "I dunno, I… walked?"
    show yuri om vsur at f11 
    y "We're on an island!"
    show yuri cm lsur at t11 
    mc "It seems I learned how to swim."
    "I'm completely dry though…"
    mc "Speaking of which, how did you get here then?"
    y neut om ldown "I can teleport."
    show yuri cm
    mc "You can? How'd you manage that?"
    show yuri oe om at f11
    y "Good question, my father learned it on one of his business trips!" 
    y dist rup "Before he died..."
    y happ "Pretty neat, huh?"
    show yuri rdown cm at t11
    "That sounds familiar…" 
    mc "Sorry if this sounds a little intrusive, but..."
    show vignette zorder 10 onlayer cover with dissolve  
    mc "How did your parents die?"
    show yuri happ om at f11 
    y "Good question." 
    show layer master:
        truecenter subpixel True
        parallel:
            easein 2.5 zoom 2 yoffset 250 
        parallel:
            ease 3 rotate 10 
       
          
    show yuri cm neut at t11 
    stop music
    pause 3 
    show layer master 
    hide vignette onlayer cover
    y happ om lup rdown "The trees here in this forest have such a pleasant forest verdant shade, do they not?"
    show yuri cm 
    mc "Sure?"
    mc "So anyways, telekinesis and teleportation, huh? That's pretty impressive."
    "Can she 'telephone' too?"
    "Or perhaps telescoping is an ability she possesses…"
    y happ om "Yes, I was just practicing before you arrived."
    show yuri cm 
    pause 1
    y nerv om  "And w-ww-w-w-w-w-well, I guess I still am practicing."
    #all the objects fall 
    y worr "Sorry."
    show yuri neut cm 
    mc "No worries."
    show yuri curi om at f11  
    y "Did you need help getting back home?"
    show yuri cm at t11 
    mc "I don't think I have enough energy to get back, so yes."
    y neut om "Understood. In that case, I will teleport you to your home."
    y "We need to make physical contact and then we'll be off."
    show yuri lsur cm 
    mc "Like a piggyback ride?"
    y flus om "I think just holding hands would be easier."
    show yuri cm at t11 
    mc "Oh, sounds good."
    show layer master:
        truecenter 
        ease 1.5 zoom 1.15 
    "I walk through the clearing and (after narrowly avoiding tripping over a branch,) grip Yuri's hand with my own." 
    y nerv om n3 "Uuuuuuuuu."
    show yuri cm -n3 
    mc "What's wrong?"
    show yuri lsur om at hf11 
    y "N-n-n-n-n-n-n-nothing! It's just… your… skin… is warm."
    show yuri cm at t11
    mc "Well yeah? All humans kinda are."
    show yuri laug om at f11 
    y "Ah. I've never actually touched one before."
    show yuri neut cm at t11 
    #"What's that supposed to mean?"
    mc "Sooooo...  teleporting?"
    y nerv om "Right, sorry. You probably think I'm weird now…"
    show yuri cm at t11 
    mc "It's like Natsuki said, only the good kind."
    show yuri dist 
    pause 1 
    show yuri mb 
    y "Thank you, [player]."
    y neut -mb om "Now, get ready to feel very dizzy."
    show yuri cm 
    mc "Huh? Wh--{nw}"
    show white zorder 10:
        alpha 0
        ease .3 alpha 1 
    pause .3 
    scene white 
    scene bg house_night 
    show layer master at anxiety 
    with Dissolve(5)
    #flash of white
    #anxiety transform on residential day
    "My blood sizzles as if I'm some kind of sentient soda."
    "But hey, looks like I'm back home."
    "I look around, but Yuri is nowhere to be found."
    "She probably teleported after me."
    "Welp, I need to have a chat with Sayori. But first, I need some sleep."
    scene black with fade
    show layer master 
    pause 1 
    return 
label yc:
    #afternoon 
    scene bg bedroom with fade 
    pause 1.5
    "It's a bright new day."
    "The sun is shining through the windows, and I texted Yuri and she agreed to come over this afternoon."
    "Just me and my supernatural goddess… what could go wrong?"
    "But before she comes, I should stop by Sayori's place and follow up about yesterday."
    scene bg residential_day 
    show yuri turned lsur casual cm oe at face 
    show layer master at vpunch 
    mc "Ah!"
    show yuri pani om lup rup at t11
    y "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    show yuri dist ce cm 
    mc "Oh! H-hi Yuri, you're… a little early."
    "Five hours early to be specific."
    show yuri flus om oe at hf11 
    y "I j-just thought I'd come sooner. As they say, the early bird gets the worm."
    show yuri worr cm at t11 
    mc "Does that make me a worm?"
    show yuri om pani at f11 
    y "Nnnno not at all! I'm sorry!"
    show yuri cm sad at t11 
    mc "Calm down, I'm just messing with you."
    show yuri sad om rdown lup  
    y "You are?"
    show yuri cm 
    mc "Yes?"
    y neut om "Oh."
    show yuri cm 
    mc "Well it's good to see you. What do you say we go get some food?"
    show yuri happ om ce at f11
    y "Ah, yes, a human bonding exercise."
    show yuri cm at t11 
    mc "Exactly."
    scene bg rr with fade 
    "Ah, here we are at this nondescript upscale cafe."
    "It definitely isn't a fast food restaurant that the developers were too lazy to grab a new background for to replace."
    "That would be blasphemy."
    "This is a high quality mod that hasn't been {i}mostly forgotten{/i} for 15 months!"
    "We would never stoop so low as to–{nw}"
    show yuri turned casual happ oe om at t11 
    y "This place seems very pleasant."
    show yuri cm 
    mc "Agreed."
    "The two of us sit in silence as we peer at the {a=https://www.variousartists.fun/menu}menu{/a}, trying to decide what scrumptious food we plan to devour."
    $ w_name = "Waiter"
    w "Can I get you two started on drinks tonight?"
    mc "Just water."
    w "And for you?"
    show yuri dist with dissolve
    pause 2
    mc "Uhh… Yuri?"
    "She doesn't respond."
    mc "I guess just water for her too?"
    w "Alright."
    "The waiter walks off."
    mc "Too shy to order?"
    show yuri anno om ce rup n3 at f11 
    y "I-I'm not just shy, I have a mortifying fear of waiters!"
    show yuri doub cm oe at t11 
    mc "Waiters specifically?"
    show yuri angr om lup rup 
    y "Yes! How they just stand there, looking down on you, their judgemental eyes, [player]. Those eyes are part of only the worst of my nightmares."
    y ce "Who knows what they're writing on their little notepads? What secrets lie on those pages? They could be cursing us for all we know."
    show yuri neut cm oe 
    mc "Huh. Well I think you're the only one in this building capable of cursing somebody."
    y ce dist om rdown -n3 "I suppose you're right."
    show yuri cm 
    mc "Do you want me to order for you?"
    show yuri pout om oe ldown rdown 
    y "I simply need to prepare myself."
    show yuri cm neut at t11     
    mc "I'll take your word for it."
    "We both return to our respective menus until the waiter returns."
    w "Are you two ready to order?"
    "Yuri nods her head."
    mc "I think so."
    w "What can I get you started with?"
    mc "Just water."
    w "...And for your meal?"
    mc "{i}Waters enough{/i}."
    w "Alright then."
    "The waiter turns to address Yuri."
    w "And for you?"
    show yuri ce at d11
    "Yuri musters all of her courage by taking a deep breath."
    show yuri om flus ce n3 at t11 
    y "Steak, please."
    show yuri lsur oe cm 
    w "And how would you like that cooked?"
    window hide 
    pause 3 
    scene bg house_night with fade 
    #long pause and fade to lack because I can't be fucked to continue this scene


    "After eating a delicious meal, Yuri kindly teleported me home."
    mc "Man, I'm stuffed. That was some great food."
    show yuri turned doub casual om oe ldown rdown at t11 
    y "All you had was water."
    show yuri cm curi 
    mc "If you drink enough water it's basically food."
    show yuri dist om rup n3 at f11 
    y "I'll… take your word for it."
    show yuri cm neut -n3 at t11 
    
    mc "Well, guess I'll see you at school."
    y nerv n3 om lup rup "Y-y-y-y-y-y-y-y-y-es."
    show yuri cm at t11 
    "Hmm."
    "I feel like there's something missing from this scene."
    "Oh, I got it!"
    scene black
    "We then kiss or something."
    "It's pretty cool."
    scene bg house_night 
    show yuri turned casual pani ce om n3 at i11 
    with fade 
    y "UUUUUUUwUUUUUUU."
    show yuri cm 
    mc "...So what's up with you and the letter u?"
    y neut om oe "It happens to be my favorite letter."
    show yuri cm 
    mc "Huh."
    return
label yend:
    scene fountain with fade 
    #"It's a nice afternoon, the air is fresh and my balls are fresher."
    "It's a nice, post club afternoon."
    show yuri turned neut cm e1b book at t11
    "I notice Yuri is reading her painting thing on the edge of the fountain."
    "Before I can call out to her, another guy does."
    "He seems familiar..."
    "What scene was he from again?"
    b "Hey, freak!"
    "Yuri shows no reaction, likely because she has been consumed by the contents of her book."
    b "I'm talking to you!"
    show yuri lsur -e1b oe at h11 
    "The guy, who I think was named Edward, grabs Yuri by her shoulder and gives her a shake."
    "{i}It would be impactful for you to see this, or for Edward to have a sprite, but we've got a budget.{/i}"
    y om "H-huh!?"
    show yuri cm 
    b "You think you're so cool? You and your… posture."
    y worr om "C-can I help you?"
    show yuri curi cm 
    b "Yeah sure, say hi to the fishies for me."
    y om "The fishie{nw}"
    show yuri vsur cm at falldown
    hide yuri 
    "WIthout warning, (other than the ominous line about 'fishies') Edward shoves Yuri into the fountain."
    mc "Yuri!"
    show layer master:
        truecenter subpixel True
        ease .7 zoom 1.4 xoffset -250
    "I run towards the fountain."
    "Peering in, Yuri is nowhere to be found."
    "Guess she teleported."
    "Putting Yuri's safety aside for a moment, I turn to Edward."
    "But he's nowhere to be found either."
    "Guess he teleported?"
    "Oh well. Problem for later."
    "What's really important is finding and checking in on Yuri."
    "I might know where to find her, but getting there will be an issue."
    scene bg residential_day with wipefast
    scene bg sayori_bedroom 
    show sayori turned casual neut cm oe at i11 
    with wipefast 
    mc "Hey Sayori!"
    show sayori happ om lup rdown at f11 
    s "Hey [player]. What can I do for y–{nw}"
    show sayori curi cm at t11
    mc "Hold on. I think I'm forgetting something."
    pause 1.5 
    "Right!"
    scene black with wipeleft  
    "I leave the room."
    "I gently open the door."
    play sound opend
    scene bg sayori_bedroom 
    show sayori turned casual anno cm oe at i11  
    with wipeleft_door
    mc "Sayori?"
    show sayori om at f11 
    s "Yes, [player]. I'm still here."
    s sedu "Now, were you interested in buying a self-defense noose? Perhaps a landmine even?"
    s mb "Or maybe even a cookie!{nw}"
    show sayori sad cm at t11 
    mc "No!"
    mc "Wait."
    show sayori neut 
    mc "The cookie. I'll take a cookie."
    show sayori happ om ce rup ldown at f11 
    s "Sure thing! One self-defense cookie, coming right up!"
    show sayori cm oe neut at t11 
    mc "What makes it 'self defense'?"
    s dist om "Well I figured it would be a lot more acceptable to have a 'self-defense' noose than it would to have a regular one…"
    show sayori happ om at f11 
    s "So I applied the concept to mercury-filled cookies."
    show sayori cm rdown 
    mc "That… makes sense?"
    mc "Hold on… mercury!?"
    show sayori lup rup om ce at f11 
    s "Yeah! Aren't they neat? They're super shiny on the inside!" 
    show sayori cm at t11 
    mc "So was I just your R&D when I ate one?"
    show sayori om neut oe ldown rdown at f11 
    s "Yeah, pretty much."
    s dist "Clearly the dosage was too low."
    s happ lup  "I can sell you one with the proper amount if you'd like~"
    show sayori cm at t11 
    mc "...I'm good."
    mc "But if you have any leftovers of the old ones, I'll could use some of those."
    s neut om "I have some left over." 
    s dist rup ldown "I was gonna  give them to the club, but you can take em."
    show sayori cm neut 
    mc "Yes please."
    show sayori at d11 
    "She hands me the cookies."
    "After shoving two of them in my pockets, I jam the cookie in my mouth."
    "{i}Disclaimer: please do not try this at home.{/i}"
    scene forest with fade 
    window hide 
    pause 1 
    mc "Worked like a charm!"
    "Man, Sayori sure is a lifesaver!"
    show bzoom onlayer bzm
    scene forest2 
    with dissolve 
    "I continue through the woods until I find Yuri."
    "She's lying on the ground, holding what looks to be an empty bottle in her hand."
    "Once I get close, she notices me and stands up."
    show yuri turned lup rup yand om oe at h11 
    y "Just on time!"
    show yuri cm 
    mc "Hey Yuri. You feeling okay?"
    y yand om "I feel incredible!"
    #yuri pulls off the knife
    show yuri yand om at f11 
    y "I'm a yandere now!"
    show yuri cm at t11
    #"Woah! That was a shift."
    "DId the fountain incident bring this on or the bottle?"
    mc "Where did you get the knife?"
    show yuri oe om happ at f11
    
    

    y "Good question, my sister brought it back for me on one of her business trips!" 
    y dist rup "Before she killed my parents..."
    y yand "Pretty neat, huh?"
    show yuri rdown cm at t11    
    mc "Uh..."
    "This may be where I die."
    "Im pretty sure my life is riding on how I go about calming her down."
    #menu between right and wrong
    menu:
        
        "Right":

            "Aw fuck it. I've got no better ideas."
            show layer master:
                truecenter 
                easein_quint .4 zoom 2.5 yoffset 400 
            show yuri lsur ldown rdown e3a
            "I grab a cookie out of my pocket and jam it into Yuri's mouth."
            window hide 
            pause .3
            show yuri ce 
            pause .1 
            show yuri neut oe 
            pause .1
            show yuri ce 
            pause .1 
            show yuri oe 
            pause 1.5
            show layer master:
                truecenter zoom 2.5 yoffset 400
                easein_quint .4 zoom 1 yoffset 0
            show yuri shy n3 om oe  
            y "uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu"
            show yuri turned flus om oe n3 at hf11  
            y "S-s-s-ss–s-s-sorry I wanted to stab you previously."
            show yuri cm at t11 
            "There we go, back to normal."
            mc "No worries."
            "I could never hold anything against Yuri."
            "Waifuism, fuck yeah!"
            mc "Are you… feeling okay?"
            show yuri -n3 neut om oe lup rdown 
            y "I'm doing quite fine."
            show yuri cm 
            mc "Well just know that I love you, and I think you're very poggers."
            y happ om "Thank you, [player]."
            show yuri cm 
            mc "So did you want to call it a day or…"
            y neut om "We could finish {i}Portrait of Markov{/i}."
            y pani "I-i-i-i-i-if you want to!"
            show yuri happ ce cm 
            mc "I'd love to."
            show yuri om 
            y "Lovely."
            show yuri cm 
            "We lay on a log and begin reading."
            "Hours pass."
            show layer master:
                truecenter subpixel True
                linear 50 zoom 0 alpha 0
            "Then those hours turn into days, and the days turn into weeks."
            "Months turn into years and so on."
            "I lost track of time long ago."
            "And yet, we have made no progress on reading the portrait of the markov."
            "It's length may very well be infinite."
            "No matter how coordinated our page turning is, it seems new pages are spawned into existence faster."
            "We grow old and frail, yet we continue on."
            "Our hearts no longer flutter as our souls fester."
            "Are even here anymore?"
            "Do we even exist?"
            "But where is 'here', anyways?"
            "No seriously, I have no clue where this island is located."
            "We could be on another planet for all I know."
            "Just the two of us, turning page after page for all of eternity."
            "A never ending cycle of words that have lost their color."
            "There is no escape from the grip of this monotunous tome of wisdom."
            "We're stuck here. Forever."
            show layer master at vpunch 
            show sayori turned casual happ ce om rup ldown at face

            show yuri vsur oe at h31 
            s "Hey you guys!"
            show yuri om at f31 
            show sayori curi oe ldown cm at t11
            y "AAAAH!"
            show yuri sad ce cm at t31 
            mc "Hey Sayori. How'd you find this place?"
            show sayori lsur om lup rup at f11 
            s "I dunno, I… walked?"
            show sayori cm rdown at t11 
            pause 3 
            show sayori vsur om oe at f11  
            s "{cps=15}...Is this heaven?"
            show sayori cm anno at t11 
            mc "Your dosage is still too low."
            show sayori ce om ldown rdown 
            s "{cps=18}...God Da-–{nw}"
            if persistent.y_complete == False:
                $ persistent.routes += 1
                $ persistent.y_complete = True 
            #cut to end
            scene black 
        "Wrong":
    
            
            mc "Damn, that's hot!"
            show yuri om at f11 
            y "I'm glad you think so!"
            show yuri at hf11 
            play sound "sfx/stab.ogg"
            show stab onlayer front:
                alpha 0 
                easein_quint .25 alpha 1 
                ease .5 alpha 0 
            pause .25 
            scene black 
            window hide 
            #stab effect
            pause 1.72
            show stab onlayer front:
                alpha 0 
                easein_quint .25 alpha 1 
                ease .5 alpha 0 
            pause 2.49 
            show stab onlayer front:
                alpha 0 
                easein_quint .25 alpha 1 
                ease .5 alpha 0 
            pause 1 
            "Yuri stabs me. {i}Seductively{/i}."
            "She keeps on slashing me until I'm filled with more holes than a sponge."
            mc "...You do have some kind of healing magic, right?"
            y "Nope!"
            #cut to black 
            #the end
            #Disclaimer: Please don't consume mercury or let a drunk girl stab you 
    return 


label counting:
    default count = 1 
    mc "[count]"
    $ count += 1 
    if count >= 30:
        jump send2 
    else: 
        jump counting 













label nextscene:
    pass
    # Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
label ccredits:
    pause 5 
    scene bg credits with dissolve_scene_full 
    pause 5
    scene bg notebook
    show bod:
        xoffset -300
    with dissolve
    pause 5
    return 