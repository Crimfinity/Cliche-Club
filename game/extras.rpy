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
    s "Oh hey [player], whats up?"
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
    s "Yay!{fast}{w=.15}Thanks [player]!"
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
    scene bg residential_day with wipeleft_scene
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
    y rdown ce "Your generosity is very effervescent."
    show yuri cm
    show sayori at thide
    hide sayori
    "I have no clue what that last word means."
    show yuri oe
    mc "N-no problem, Yuri."
    show yuri curi
    mc "So… Painting of Mark?"
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
    y "Good question, my father brought it back for me on one of his business trips!"
    y dist rup "Before he died..."
    y happ "Pretty neat, huh?"
    show yuri cm at t11
    "That sounds familiar…"
    show yuri neut
    mc "Sorry if this sounds a little intrusive, but…"
    show vignette with dissolve
    show yuri curi cm oe
    mc "How did your parents die?"
    show yuri dist om
    y "Good question."
    stop music fadeout .5
    show yuri cm at t11
    y "..."
    "I look at her expectantly, but she turns back to her book."
    hide vignette
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
    scene bg park 
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
    show yuri turned neut cm oe at t11 
    mc "Don't cut yourself lol."
    show yuri nerv om oe at f11 
    y "T-t-t-t-t-t-t-t-thank you [player]. I'm cured."
    show yuri at lhide 
    hide yuri 
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
    show monika oe neut at t11 
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
    show monika at thide 
    hide monika 
    if n_route == True:
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
    scene bg housen with wipeleft
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
  
label sroute1:
    Script:
label ss1:
     "I decide to go see what Sayori is up to."
     "It appears she's currently \'Uwaa~\'-ing in a loop."
     #monika pops up and fixes this
     s "Oh hey [player], whats up?"
     mc "Not much, just wanted to see what you were up to." 
     # mc "My homeslice."
     s "Oh I'm just… I forgot."
    "How did she-"
    "Right. Cliche mod."
mc "Well, how are you feeling?"
#weather report bg
#the news theme from undertale bc why not
"Where is this going?"
s "Well I'm glad you asked!"
s "I'm weatherette Sayori with channel 9 news."
mc "There is no way that's a real term."
#upset sayori
pause 0.5
mc "Okay, okay… fine."
#maybe have it fade into a greenscreen
s "Partly cloudy."
"huh."
s "Anyways, can you buy me a cookie?"
mc "Uh… Sure."
#s "Yes! Poggers!"
s "Yay! Thanks [player]!"
"Sayori jumps up and down as she wraps her arms around me in a bear hug."
mc "Alright, alright."
s "Ehehehehehehehehehhehehe sorry~"
"We step out of the clubroom and are greeted by a vending machine."
mc "Hold on, why is that there?" 
s "I dunno."
"Sayori shrugs." 
"Could it be…?"
#"N-Nani?!" 
m "Sorry, guys!" 
"I hear a distant shout from the clubroom."
pause .5
m "...And there!"
#vending machine disappears
s "Where'd it go?"
s "I wanted a cookie…"
"Suddenly, the vending machine reappears against the wall."
s "Huh?"
"Without questioning it, I slide an unnamed currency into the slot."
"Is it Yen? Is it Dollars? Maybe one of those 'Quids'?" 
#fokin ell geeza
"Guess we'll never know." 
#ye ma e
 #RULE BRITANNIA BRITANNIA RULE THE WAVES 
#riding round in a rover if i see opps in his over ill send man straigh to jehovah when i take shots like like em sharapova doing up tennis call man dennis im a menace doin up olives in venus big man ting im bigger than benis stop it otherwise unknown p might bash mans head straight down like a bopit so make like a freddo and hoppit your girl is 4 foot four and got bare hair on her toes like a hobbit when i see in the club im doing up aj
"Sayori's eyes widen as I conjure up a chocolate chip cookie." 
#the coupe is retarded
mc "'Tis magic, my dear."
s "It's beautiful…"
mc "Alright then." 
pause 1
mc "Alright, you ready to walk home?"
s "Sure."
scene bg residential_day with wipeleft_scene 
"Sayori and I walk home." 
"I get the urge to ask about her \'Uwaa-ing\' earlier, but I don't want to come off as intrusive." 
"Instead, I decide to ask about her day." 
mc "So.. How was your day?" 
s "61 degrees."
mc "Fahrenheit or celsius?"
s "Eh, I dunno."
mc "Alright then."
"We end up walking home in a calm silence."
"Eventually we say our goodbyes, and enter our respective houses." 
s "See ya, [player]!" 
mc "See you, Sayori." 
# scene bg bedroom
"Welp, nothing relevant to do at home yet. Guess it's time to go to sleep."
scene black 
pause 2 
scene bg bedroom 
"Ah, morning!"
"Time to go see what Sayori is up to!"
pause 1
"...What's that?{w=.5} What about the club?"
"That doesn't matter anymore, we only care about Sayori now!"
#check for other routes finished
"Maybe only because I already played another route, but who cares?"
"I get out of bed and tactically roll down my stairs."
scene bg kitchen 
show sayori at face 
s "HI [player!u]!!!"
mc "Gah! What are you doing in my house?"
s "I thought I would pay you a surprise visit! Just like when we were kids!"
mc "Ah, okay, makes sense."
mc "Hey, remember that one time we \[INSERT EVENT HERE\] when we were kids?"
s "Oh yeah! I totally do!"
mc "Fun times."
mc "So, want to get food or something?"
s "I love food!"
#sayori spins and flings offscreen
s "FOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO--"
 "Guess I should follow her."
scene bg restaurant with wipeleft_scene
mc "So Sayori, how are you feeling today?"
#yandere eyes
s "I am entirely motivated by food."
s "So I'm great!"
mc "I'm glad to hear it."
"A pause comes over us as neither of us can think of what to say."
"But it isn't awkward really, the two of us are just enjoying each other's presence and munching on fries."
"It's quite nice, just the two of us sitting across from each other, me and my cute food vacuum waifu."
"{i}Bet that's a phrase you never expected to hear.{/i}"
mc "Hey Sayori, this reminds me of all the times we went to this restaurant as kids."
s "Oh yeah!"
mc "I still don't understand how you managed to burn down a restaurant you didn't work at."
mc "Hell, it only reopened last week!"
s "Eh? Don't remind me, meanie!"
mc "Alright, alright. I'm sorry."
s "No worries, [player]."
"Sayori killed twelve people that day."
"I can still remember the screams reverberating throughout the smoldering Jack in the Box™."
#Time skip
mc "Man I'm stuffed, what about you Sayori?"
s "My stomach is an abyss with infinite capacity for nutrients/"
mc "Do you want me to like... buy you more fries?"
s "It's fine. I'll be a-okay!"
mc "If you say so."
"It seems our lunch 'date' is coming to a close."
"But there's still plenty of light out, so maybe we can find something else to do."
mc "Hey Say, did you want to take a stop at the park on the way back?"
s "That sounds like fun!"
"With Sayori's approval, the two of us depart to go to the park."
#park time
#sayori is swinging on a swing super fucking fast
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
#sky bg 
"Just gotta line this up..."
#slide whistle
#fade to white
#bg of the park burning down with child sayori sprite
s "EVERYTHING WILL BURN."
s "NOTHING IS FREE FROM THE HELL THAT I CAST UPON IT."
s "YOU WILL ALL PERISH BENEATH ME."
#fade to present time
"I'm starting to think this may be a problem of hers."
s "Thanks for catching me ehehehehehe~"
mc "I guess you could say you've... fallen for me."
s "I guess?"
mc "What do you say we call it a day? I can only take one near death experience per park trip."
s "Oh, like that time we met that weird football guy?"
"I... don't know exactly what she's talking about, nor do I want to know."
mc "Yeah, exactly like that."
#residential night
mc "So uh... see you tomorrow?"
s "Yeah, I had a great time! It's been a while since we last hung out like this."
s "When's the last time we spent time together outside of school anyways?"
mc "Probably when you burned down that movie theatre."
s "Oh I remember now!"
mc "I remember all too well."
s "hey, don't judge me! They undercooked my popcorn."
mc "Ah, you and your food."
s "Yeah, yeah, laugh it up."
"A brief pause overcomes us as we take in the silence of our surroundings."
s "Hey, [player], there's something you should know..."
mc "Yeah, what is it?"
#pause and zoom for 60 seconds
#zoom out
s "I love you."
mc "Wait, what?"
"I thought this was gonna be another pitch for her self defence noose or whatever."
s "You heard me, meanie."
mc "Uh, yeah, I did. You just caught me off guard."
s "Are you really that surprised? I mean we've basically known each other our whole lives."
mc "I guess it makes sense."
mc "I uh... love you too?"
s "R-really?"
mc "Didn't you just say it wasn't surprising you had feelings for me? What makes it different the other way around?"
s "Well, yeah, but, it's {i}me{/i} we're talking about, I haven't even seen another guy in my life, and there's {s}three{/s} two cute girls you can go for in the club, wouldn't you rather be with either of them?"
mc "I love {i}you{/i}, Sayori. and I wouldn't have it any other way."
#if they played another route
"I also already went through another route, but who am I to rain on her parade."
scene black
"We then kiss or something."
"It's pretty cool."
#residential night
s "So, now that you're my boyfriend..."
s "You have to come help me make an ad for my self defence noose!"
"I've been played."
s "Chop chop, [player], I've got the video camera set up in my living room!"
#fade to residential day

s "HEEEEY!"
mc "Oh hey Sayori, you're up early!"
s "You noticed~"
s "It sure is a sunny day!"
"I look up."
mc "Yeah, it sure is."
s "I meant more metaphorically, but yeah."
mc "Oh."
mc "So, did you want to walk to school together?"
s "Sure!"
#fade to club I guess 
#show sayori 
s "Hey everyone, I have an announcement to make!"
#show everyone else
"All of the club members turn to address Sayori."
s "I am depression!"
#pause
y "...Do you mean {i}have{/i} depression?"
#zoom plus vignette focusing on sayori and Yuri
s "DON"T RUIN THIS FOR ME, YURI."
y "imsorry."#small text
#effect ends abruptly
m "{i}Ahem.{/i}{w} We're very proud of you for telling us and support you indefinitely."
#s "Even if I burn things to cope with my sadness?"
m "Yeah, sure, knock yourself out."
mc "Don't encourage her Monika."
s "The reckoning is nigh, [player]."
s "The flames of cleansing will reach everyone indiscriminately."
s "I will turn everything to ash."
mc "Writers, a little help here?"
scene black
"Whew, thank god that scene's over."
pause 2 
#fade into picnic scene (already written in Nat route)

#fade to res night
mc "Boy, what a day that was."
s "Say, it's late, and our parents are not only not home, but basically nonexistent."
mc "Yeah?"
s "Did you maybe wanna..."
s "Buy a self defenc--{nw}"
mc "Not interested."
s "Meanie."
s "In that case, I'm going to sleep."

#fade into save the dokis scene (also from natsuki's scene but I'll have to write a few lines for Natsuki

#residential day
 "Ah, the weekend~"
"It's a nice day out, couldn't have asked for any better."
"Say, I wonder what Sayori is up to on this fine afternoon."
scene black with wipeleft_scene
pause 1.5
"Uhh...{w=.5} Why is her house so dark?"
"it made sense when it was nighttime, but it's the middle of the afternoon."
"Does she just not have windows?"
"Or maybe this is just some kind of time or budget constrai--"
#screen glitches
"Lets go see what Sayori is up to."
"I gently open the door, not because I really care about being sensitive, but because it feels right."
#sayori in suicide clothes with noose
mc "Hey Sayori."
"Her eyes light up when she sees me."
s "Oh! Hiya [player]! It's great to see you."
mc "Performing some R&D on your self-defence noose."
s "You know it! Wanna help me test it?"
mc "I'll pass, thank you very much."
s "Welp, looks like it's up to me."
#sayori slides over a little
"Sayori begins fastening the rope to her ceiling."
"She then grabs a chair and slides it underneath."
"Hey, wait a minute..."
"Sayori, you aren't going to try killing yourself, are you?"
s "hehe, no silly~"
s "It's not a matter of trying, I will succeed."
"My heart rate accelerates."
"Fuckfuckfuckfuck."
"Sayori's life in danger right now."
"What should I do?"
choice between right and wrong

right:

s "Hey, could you step out for a second?"
mc "When you're about to off yourself?"
s "Well yeah, you don't want to see it happen, do you?"
mc "I don't want it to happen in the first place!"
s "Relax, once I'm gone, there's three other people you can talk to."
s "Actually there's only two worth talking to, but that's being nitpicky."
mc "But we all care about you, and I don't want to talk to any of them."
mc "Hell, they're practically entirely ignored on this route."
s "I guess you have a point."
s "But I would've wasted so much time!"
s "I made this whole business solely as a guise to hold onto a ton of nooses."
"Wow, she's a lot more clever than I have her credit for."
"Even if that's way darker than this mod should be."
s "It would be such a drag to {i}not{/i} kill myself at this point."
mc "Okay, first, wouldn't you be wasting more time by just not living?"
mc "Second, we don't have to waste the nooses, we could build a massive corporate empire."
mc "I'll help you sell all your nooses so you don't have to throw them out."
"I sure hope people end up buying them because they're cheaper than rope and not because they come pre-tied."
s "Alright, you've got a deal."
s "Pleasure doing business with you."
"Sayori steps down from her chair and embraces me."
#scene black
mc "So, are you feeling a little better now?"
s "One hundred degrees."
mc "Wait, were the degrees just percentages the whole time?"
#roll credits

wrong:

s "Hey, could you step out for a second?"
mc "Huh? Uh, yeah, sure."
s "Great! Thanks."
#close door
s "Alright, now count to 30 and come back in."
mc "Is this a game of hide and seek."
s "Sure is."
"I chuckle."
"She really is childish. I mean, when was the last time we played hide and seek."
"Better get to counting."
#I'm literally just going to code a loop that counts to thirty.
mc "Ready or not, here I come!"
"I excitedly gently open the door."
# s kill, shocker.
#monika is behind the window, disappointed 
"Oh wow, she killed herself."
"I for one, am shocked."
#to be continued in I gently open the door 2
m "Seriously? You're using an ending to plug another one of your shitty projects?"
#the splash text changes to respond
"Fuck off, Monika."
"Just let me have this."
"My wife is leaving me, and she's taking the kids, is this too much to ask for?"
m "Riiight, we both know you don't have a wife."
"JUST LET ME HAVE THIS."
m "...Fine."
















label nextscene:
    pass
    # Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
label ccredits:
    pause 5 
    scene bg credits with dissolve_scene_full 
    pause 5
    scene bg notebook with dissolve
    show bod:
        xoffset -300
    pause 5
    return 