label splashscreen:
    scene black
    $ renpy.pause(1, hard=True)
    show text "Quokka Studio presents" with Dissolve(1)
    $ renpy.pause(2, hard=True)
    hide text with Dissolve(1)
    $ renpy.pause(.5, hard=True)
    return

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])

screen task1():
    imagemap:
        hotspot (120, 330, 100, 170) action Jump("calendar1") hover_child Solid("#66006666")
        hotspot (340, 250, 270, 180) action Jump("painting1") hover_child Solid("#66006666")
        hotspot (650, 210, 210, 130) action Jump("painting1") hover_child Solid("#66006666")
        hotspot (1050, 470, 420, 250) action Jump("drawer1") hover_child Solid("#66006666")
        hotspot (1480, 550, 400, 700) action Jump("table1") hover_child Solid("#66006666")
        if not taskdone[0]:
            ground "roome.png"
            idle "roome.png"
            hover "roome.png"
            hotspot (870, 310, 180, 630) action Jump("eden1") hover_child Solid("#66006666")
            hotspot (600, 530, 210, 300) action Jump("earlynoah") hover_child Solid("#66006666")
            hotspot (600,930,700,100) action Jump("task1") hover_child Solid("#66006666")
        else:
            ground "room.png"
            idle "room.png"
            hover "room.png"
            hotspot (600, 530, 210, 300) action Jump("flashback1") hover_child Solid("#66006666")

screen task2():
    imagemap:
        ground "proome.png"
        idle "proome.png"
        hover "proome.png"
        hotspot (120, 330, 100, 170) action Jump("calendar2") hover_child Solid("#66006666")
        hotspot (340, 250, 270, 180) action Jump("painting2") hover_child Solid("#66006666")
        hotspot (650, 210, 210, 130) action Jump("painting2") hover_child Solid("#66006666")
        hotspot (1050, 470, 420, 250) action Jump("drawer2") hover_child Solid("#66006666")
        hotspot (1480, 550, 400, 700) action Jump("table2") hover_child Solid("#66006666")
        hotspot (600, 530, 210, 300) action Jump("noah2") hover_child Solid("#66006666")
        hotspot (870, 310, 180, 630) action Jump("eden2") hover_child Solid("#66006666")
        if not havebanner:
            hotspot (1050, 20, 770, 450) action Jump("earlywall1") hover_child Solid("#66006666")
            hotspot (1630, 20, 300, 530) action Jump("earlywall2") hover_child Solid("#66006666")
        else:
            if not taskdone[1]:
                hotspot (1050, 20, 770, 450) action Jump("wall1") hover_child Solid("#66006666")
                hotspot (1630, 20, 300, 530) action Jump("earlywall2") hover_child Solid("#66006666")
            else:
                hotspot (1050, 20, 770, 450) action Jump("wall12") hover_child Solid("#66006666")
                hotspot (1630, 20, 300, 530) action Jump("flashback2") hover_child Solid("#66006666")

screen task3():
    imagemap:
        ground "proome.png"
        idle "proome.png"
        hover "proome.png"
        hotspot (120, 330, 100, 170) action Jump("calendar3") hover_child Solid("#66006666")
        hotspot (340, 250, 270, 180) action Jump("painting3") hover_child Solid("#66006666")
        hotspot (650, 210, 210, 130) action Jump("painting3") hover_child Solid("#66006666")
        hotspot (1050, 470, 420, 250) action Jump("drawer3") hover_child Solid("#66006666")
        hotspot (1480, 550, 400, 700) action Jump("table3") hover_child Solid("#66006666")
        hotspot (600, 530, 210, 300) action Jump("noah3") hover_child Solid("#66006666")
        hotspot (870, 310, 180, 630) action Jump("eden3") hover_child Solid("#66006666")
        hotspot (1050, 20, 770, 450) action Jump("wall13") hover_child Solid("#66006666")
        hotspot (1630, 20, 300, 530) action Jump("wall23") hover_child Solid("#66006666")

#############################################################################

label earlynoah:
    w "(...Isn't that...?)"
    w "(...N-No, it can't be him. {w}Can it?)"
    w "(Anyway... I should {u}clean up the glass shards first{/u}. Eden might get suspicious otherwise.)"
    call screen task1
label task1:
    "sweep sweep sweep"
    $ taskdone[0] = True
    scene room with dissolve
    show oec at mid with dissolve
    e "Good progress, Wilbur!"
    e "While you finish dusting off the furniture and whatnot, I'll go take a breather outside. OK?"
    e "In the meantime–"
    hide oec
    show oeh2 at mid
    eblack "{b}I'd prefer if you don't touch my things.{/b}"
    hide oeh2 with dissolve
    "{i}You thought this was another one of his gimmicks. To your surprise, he actually turns around and... leaves the house. {w}But not without first swiftly locking you inside."
    w "(There goes my escape plan. {w}...)"
    w "(Eden wouldn't enjoy this, but... maybe I should check on {i}him{/i}...)"
    w "(He looks just like–)"
    call screen task1

label earlywall1:
    show w2a at right with dissolve
    w "(I should get the {u}banner{/u} first...)"
    hide w2a with dissolve
    call screen task2
label earlywall2:
    show w2a at right with dissolve
    if not havebanner:
        w "(I should get the {u}string lights{/u} first...)"
    else:
        w "(OK, let's do this.)"
        w "(... {w}But the middle wall looks so empty... Maybe I should hang up the {u}birthday banner{/u} first?)"
    hide w2a with dissolve
    call screen task2
label wall1:
    "Banner goes woop woop"
    $ taskdone[1] = True
    show w2s at right with dissolve
    w "(Now let's hang up the string lights...)"
    hide w2s with dissolve
    call screen task2

#############################################################################

label eden1:
    scene room with dissolve
    show oe at left with dissolve
    show ow at right with dissolve
    e "Need some help?"
    menu:
        "What's my task again?":
            hide oe
            show oef at left
            e "Oh my. I didn't realize this was your first day on the job."
            e "...I'm joking. Having trouble sweep up the {u}glass shards at the foot the table{/u}?"
            hide oef
            show oec at left
            e "Try {u}clicking them with your mouse{/u}. {w}You're smart enough. I believe in you."
            hide oec with dissolve
        "Who are you?":
            hide oe
            show oef2 at left
            e "..."
            e "I'm your hirer. I'm your client. I'm the one paying for this party. {w}And since you're in this house, I am your host."
            e "But if you keep pestering me instead of getting on with your {i}job{/i}..."
            hide oef2
            show oeh2 at left
            eblack "{b}{i}I won't keep being so hospitable.{/i}{/b}"
            hide oeh2 with dissolve
    hide ow with dissolve
    scene roome with dissolve
    call screen task1
label eden2:
    scene proom with dissolve
    show e at left with dissolve
    show w at right with dissolve
    e "Hmm?"
    menu:
        "What's my task again?":
            hide e
            show ef at left
            e "...How old are you? Twenty? And already there's the onset of memory loss..."
            if not havebanner:
                e "First, go get what you need from the {u}wooden drawer behind me{/u}, a little to the right. {w}Then come to me again, if you {i}still{/i} don't remember."
                hide ef
                show ec at left
                e "Alright? Good luck."
            else:
                e "Kindly hang up the {u}birthday banner on the middle wall{/u}, above the wooden drawer."
                e "Then, hang up the {u}string lights on the right wall{/u}, above the long table."
                e "Did you get all that? Or should I repeat myself?"
                hide ef
                show ec at left
                e "Just kidding. I'd rather not waste my breath."
            hide ec with dissolve
        "How'd you know Noah?":
            hide e
            show ef at left
            e "Noah? Is that his name?"
            e "You ask me how I know him. Maybe I {i}don't{/i}."
            hide ef
            show ec at left
            e "Or, maybe I'm just a nice acquaintance who's throwing a surprise party for our mutual friend!"
            hide ec
            show eh2 at left
            e "Or, better yet, maybe I'd prefer if you {b}get back to work.{/b}"
            hide eh2 with dissolve
    hide w with dissolve
    scene proome with dissolve
    call screen task2
label eden3:
    scene proom with dissolve
    show e at left with dissolve
    show w at right with dissolve
    e "Feeling hungry?"
    menu:
        "What's my task again?":
            hide e
            show ef at left
            e "Try not to eat everything. {w}...I'm joking."
            hide ef
            show ec at left
            e "Drag-and-drop the correct {u}food warmer– that's the metal containers{/u}– to the right place on the table."
            e "Once that's done, drag-and-drop the {u}each food to its corresponding container{/u}. Easy enough?"
            hide ec
            show e at left
            e "Go one by one. There's no rush."
            hide e with dissolve
        "Do you... have a therapist?":
            hide e
            show ef at left
            e "Oh? You think I could use one?"
            e "You seem like quite the competent advisor yourself. {w}No training, maybe, but you've got the {i}eyes{/i} of someone... well-acquainted with life's pitfalls."
            hide ef
            show ec at left
            e "Just kidding. I appreciate the concern, Wilbur, I really do. {w} But there's other stuff for you to be concerned about, no?"
            hide ec
            show eh at left
            e "{b}Like your head{/b} if you don't start getting busy."
            hide eh with dissolve
    hide w with dissolve
    scene proome with dissolve
    call screen task3
label eden4:
    "{i}A long table with food. For guests, supposedly.{/i}"
    call screen task4
label eden5:
    "{i}A long table with food. For guests, supposedly.{/i}"
    call screen task5

label calendar1:
    "{i}June (6), 7th.{/i}"
    call screen task1
label calendar2:
    "{i}June (6), 7th.{/i}"
    call screen task2
label calendar3:
    "{i}June (6), 7th.{/i}"
    call screen task3
label calendar4:
    "{i}June (6), 7th.{/i}"
    call screen task4
label calendar5:
    "{i}June (6), 7th.{/i}"
    call screen task5

label painting1:
    "{i}A strange painting.{/i}"
    call screen task1
label painting2:
    "{i}A strange painting.{/i}"
    call screen task2
label painting3:
    "{i}A strange painting.{/i}"
    call screen task3
label painting4:
    "{i}A strange painting.{/i}"
    call screen task4
label painting5:
    "{i}A strange painting.{/i}"
    call screen task5

label drawer1:
    "{i}The drawers are full of colorful banners and string lights.{/i}"
    call screen task1
label drawer2:
    if not havebanner:
        "{i}The drawers are full of colorful banners and string lights.{/i}"
        menu:
            "Take banners and string lights":
                $ havebanner = True
            "Don't take them":
                pass
    else:
        "{i}Empty.{/i}"
    call screen task2
label drawer3:
    "{i}Empty.{/i}"
    call screen task3
label drawer4:
    "{i}Empty.{/i}"
    call screen task4
label drawer5:
    "{i}Empty.{/i}"
    call screen task5

label table1:
    "{i}A long table. The tablecloth appears stained.{/i}"
    call screen task1
label table2:
    "{i}A long table. The tablecloth appears stained.{/i}"
    call screen task2
label table3:
    "{i}A long table. The tablecloth appears stained.{/i}"
    menu:
        "Set up food for catering":
            "food!! yippee"
            jump flashback3
        "Not yet":
            call screen task3
    call screen task3
label table4:
    "{i}A long table with food. For guests, supposedly.{/i}"
    call screen task4
label table5:
    "{i}A long table with food. For guests, supposedly.{/i}"
    call screen task5

label noah2:
    "{i}Noah Chalan.{/i}"
    call screen task2
label noah3:
    "{i}Noah Chalan.{/i}"
    call screen task3
label noah4:
    "{i}Noah Chalan.{/i}"
    call screen task4
label noah5:
    "{i}The birthday star.{/i}"
    call screen task5

label wall12:
    "{i}A birthday banner.{/i}"
    call screen task2
label wall13:
    "{i}A birthday banner.{/i}"
    call screen task3
label wall14:
    "{i}A birthday banner.{/i}"
    call screen task4
label wall15:
    "{i}A birthday banner.{/i}"
    call screen task5

label wall23:
    "{i}String lights.{/i}"
    call screen task3
label wall24:
    "{i}String lights.{/i}"
    call screen task4
label wall25:
    "{i}String lights.{/i}"
    call screen task5

#############################################################################

init python:
    def charvoice(event, interact = True, voicefile = "edenvoice.mp3", **kwargs):
        if not interact:
            return
        if event == "show_done":
            renpy.sound.play(voicefile)
        elif event == "slow_done":
            renpy.sound.stop()

define whitetext = Character("", what_color = "#ffffff", window_background=im.MatrixColor("gui/textbox.png", im.matrix.tint(0.0, 0.0, 0.0)), what_outlines=[ (0, "#fff") ])
define anon = Character("???", callback = charvoice)
define e = Character("Eden", what_color = "#660066", callback = charvoice)
define eblack = Character("Eden", what_color = "#000000", callback = charvoice, what_outlines=[ (0, "#fff") ])
define w = Character("Wilbur", what_color = "660066", callback = charvoice)
define n = Character("Noah", what_color = "#1F3B4D", callback = charvoice)

image white = Solid("#fff", xsize=1920, ysize=1200)
image blackslow:
    im.MatrixColor("flashback11.png", im.matrix.tint(0,0,0))
    alpha 0
    linear 5 alpha 1
image ow = Transform("w.png", ypos = 0.04)
image owa = Transform("wa.png", ypos = 0.04)
image ows = Transform("ws.png", ypos = 0.04)
image owh = Transform("wh.png", ypos = 0.04)
image ow2s = Transform("w2s.png", ypos = 0.06)
image ow2a = Transform("w2a.png", ypos = 0.06)
image oe = Transform("e.png", ypos = 0.015)
image oec = Transform("ec.png", ypos = 0.015)
image oef = Transform("ef.png", ypos = 0.015)
image oef2 = Transform("ef2.png", ypos = 0.015)
image oeh = Transform("eh.png", ypos = 0.015)
image oeh2 = Transform("eh2.png", ypos = 0.015)
image w = Transform(im.MatrixColor("w.png", im.matrix.tint(.9, .75, 1)), ypos = 0.04)
image wa = Transform(im.MatrixColor("wa.png", im.matrix.tint(.9, .75, 1)), ypos = 0.04)
image ws = Transform(im.MatrixColor("ws.png", im.matrix.tint(.9, .75, 1)), ypos = 0.04)
image wh = Transform(im.MatrixColor("wh.png", im.matrix.tint(.9, .75, 1)), ypos = 0.04)
image w2s = Transform(im.MatrixColor("w2s.png", im.matrix.tint(.9, .75, 1)), ypos = 0.06)
image w2a = Transform(im.MatrixColor("w2a.png", im.matrix.tint(.9, .75, 1)), ypos = 0.06)
image e = Transform(im.MatrixColor("e.png", im.matrix.tint(.9, .8, 1)), ypos = 0.015)
image ec = Transform(im.MatrixColor("ec.png", im.matrix.tint(.9, .8, 1)), ypos = 0.015)
image ef = Transform(im.MatrixColor("ef.png", im.matrix.tint(.9, .8, 1)), ypos = 0.015)
image ef2 = Transform(im.MatrixColor("ef2.png", im.matrix.tint(.9, .8, 1)), ypos = 0.015)
image eh = Transform(im.MatrixColor("eh.png", im.matrix.tint(.9, .8, 1)), ypos = 0.015)
image eh2 = Transform(im.MatrixColor("eh2.png", im.matrix.tint(.9, .8, 1)), ypos = 0.015)

default forgive = 0
default taskdone = [False, False, False, False]
default havebanner = False

transform left:
    xpos -0.25
transform coverup:
    xpos -0.15
transform tocoverup:
    xpos -0.25
    linear .5 xpos -0.15
transform right:
    xpos 0.25
transform mid:
    xpos 0
transform jumpsprite:
    subpixel True
    crop (400, 0, 1050, 600) size (1920, 1080)
    pause .7
    linear .3 crop (0,0,1920,1080) size (1920,1080)
transform jumpnoah:
    subpixel True
    crop (300,0,1400,800) size (1920, 1080)
    pause 3
    linear 2 crop(0,0,1920,1080) size (1920,1080)

#############################################################################

label start:
    stop music fadeout 3.0
    scene white
    with Dissolve(.5)
    scene white
    $ renpy.pause(2, hard=True)

    scene intro1
    with Dissolve(.5)
    "{i}Trees. Winding mountain road. Big isolated house uphill.{/i}"
    "{i}Cold currents come howling past as I drive up the road. Or was that wolves? {w}Expensive as the land lots are up here, it's sure like a horror movie at night.{/i}"
    scene intro2
    "{i}Oh yeah. {w}That's me, by the way.{/i}"
    "{i}I don't live there. Obviously. No way in hell I can ever afford a mountain view mansion.{/i}"
    "{i}...But as long as whoever hired me {/i}can{i}, that's all that matters.{/i}"
    "{i}I work at parties. Kids' birthdays, mostly. Preparing, catering, entertaining, cleaning up after guests' messes...{/i}"
    "{i}This one's a birthday, as you can probably tell from the miserable cake strapped to my passenger seat.{/i}"
    "{i}It's an in-between-jobs kinda industry. My colleagues move onto bigger, better jobs in a few months, sometimes weeks.{/i}"
    "{i}I've been stuck here for two years.{/i}"
    scene intro3
    with Dissolve(.5)
    "(That must be the house...)"
    "(Let's go? I guess?)"
    "{i}I park my beat-up car somewhere close but discreet, so the guests coming up in their Porsches don't have to see it.{/i}"
    scene porch with pixellate
    "{i}Upon closer inspection...{/i}"
    show owa at right with dissolve
    anon "..."
    "{i}...The house doesn't seem all that luxurious.{/i}"
    hide owa with dissolve
    menu:
        "Knock on the door":
            jump knockdoor
        "Look through the peephole":
            jump peephole

label knockdoor:
    "{i}You knock on the door.{/i}"
    $ renpy.pause(3, hard=True)
    "{i}Footsteps. Then...{/i}"
    show oe at mid with dissolve
    $ renpy.pause(1)
    "(Wow. Someone missed the dress code. {w}...Is this the right house?)"
    anon "Oh, you must be Wilbur."
    jump introcont

label peephole:
    "{i}You tiptoe to the door, and squint through the peephole.{/i}"
    "{i}Nope. It's all blurry. You can't see anything insid{/i}{nw}"
    show oef at jumpsprite
    $ renpy.pause(1.5, hard=True)
    "?!!"
    hide oef
    show oeh2 at mid
    anon "It's impolite to spy on people, you know?"
    "W-Where did you{nw}"
    hide oeh2
    show oe at mid
    anon "Anyway. You must be Wilbur?"
    jump introcont

label introcont:
    w "Y-Yeah!! And you're Mr... {w}uhh... {w}Edgar...?"
    hide oe
    show oec at mid
    "{i}He chuckles a frightening, knife-sharp chuckle that sends shivers down my spine. Is he supposed to be amused??{/i}"
    hide oec
    show oef2 at mid
    e "It's Eden."
    w "Oh shit. {w}I mean damn. No I mean– {w}I blame my manager. He speaks too fast. I didn't quite catch it... when he told me..."
    "{i}There goes my tips.{/i}"
    hide oef2
    show oe at mid
    e "Come in."
    hide oe with dissolve
    "{i}Eden disappears behind the door.{/i}"
    "{i}Somehow I have a bad feeling about this. Like a sour knot twisting in my guts. Maybe it's the moldy wall.{/i}"

    $_dismiss_pause = False
    scene black with CropMove(2, "wipeleft")
    "{i}Anyhow, I follow him in.{/i}"
    scene room with CropMove(7, "wipeleft", hard=True)
    $_dismiss_pause = True
    $ renpy.pause(2, hard=True)
    show owh at right with dissolve
    "..."
    w "What the...?"
    show oe at left with dissolve
    e "Hmm? Something wrong?"
    w "That– that guy–"
    hide oe
    show oef at left
    e "Oh, yes? That's our birthday star."
    hide oef
    show oec at left
    e "Ha ha, did I spoil the surprise? Sorry."
    hide owh
    show owa at right
    w "N–No. I mean, is he OK?? He looks like he's–{w=.3}{nw}"
    show black onlayer foreground
    whitetext "He looks like he's dead.{w=.5}{nw}"
    hide black onlayer foreground
    w "Like he's... passed out..."
    hide oec
    show oeh2 at left
    e "... {w}..."
    hide oeh2
    show oec at tocoverup
    e "Aw, seems like he's taking a nap. How nice of you to be concerned about someone under {i}my{/i} care."
    e "Frankly, Wilbur..."
    hide oec
    show oeh at coverup
    hide owa
    show owh at right
    eblack "{b}It's none of your goddamn business.{/b}"
    eblack "{b}It's not your place to question me.{/b}"
    e "Understood?"
    menu:
        "No. I want to leave.":
            jump leave
        "Yes":
            jump preleave

label preleave:
    w "I–I understand{nw}"
    show black onlayer foreground
    whitetext "He looks like he's dead.{w=.5}{nw}"
    hide black onlayer foreground
    jump leave

label leave:
    hide owh
    show owa at right
    w "W-Wait, no!"
    w "I don't know {i}what{/i} the hell you're plotting, but–{w} but I definitely don't wanna get swept up in it."
    hide owa
    show ow at right
    w "Terribly sorry. I'm leaving."
    hide oeh
    show oeh2 at coverup
    e "Hmm, you sure? That's gonna warrant a poor review."
    hide ow
    show owa at right
    w "Of course I'm sure.{w} You've got an {i}unconscious{/i} person at your two-man party, and I'm just supposed to stay??"
    w "It's not like I'm the ultra-obligated protagonist of some free horror game. I don't have to go along with this sick plot."
    w "Let me go, or I'm calling the police."
    hide oeh2
    show oe at coverup
    e "I'd like to see you try."
    scene black with dissolve
    "{i}I run towards the door, half-stumbling, pulling out my phone to dial 911.{/i}"
    "{i}Shaking, I reach for the door handle –{/i}"
    whitetext "\"Your call cannot be completed as you are outside our zone of service. Sorry for the inconvenience.\""
    e "The door's locked, by the way."
    "{i}– it doesn't budge. {w}I shake the handle with the whole weight of my body – not a jolt. Not even a rattle. {w}I try again. {w}And again. {w}And again.{/i}"
    "{i}Red imprints take shape on the inside of my fingers.{/i}"
    scene black with dissolve
    pause 1
    "{i}I did give up eventually.{/i}"
    $_dismiss_pause = False
    scene room with Dissolve(3)
    $_dismiss_pause = True
    "..."
    show oe at mid with dissolve
    e "Ready to begin your first task?"
    w "..."
    hide oe
    show oec at mid
    e "Great! Let's start by tidying up the room a little. The table could use a wiping-down... {w}oh, and won't you kindly {u}sweep those glass shards off the floor{/u}?"
    e "Many thanks~ I'll be here if you need me."
    hide oec with dissolve
    scene roome with dissolve
    call screen task1

label flashback1:
    w "..."
    "{i}You glance behind you, making sure Eden hasn't come back. {w}Then, you approach the table discreetly.{/i}"
    w "(Why do I even bother?? It can't really be him. {w}Can it?)"
    show black onlayer foreground
    whitetext "Wouldn't that be nice? {w}Dead at last."
    whitetext "Like you've always wished for.{nw}"
    hide black onlayer foreground
    w "..."
    "{i}You carefully turn him over to look at his face.{/i}"
    $ time = .7
    $ timer_jump = "skipmenu"
    show screen countdown
    menu:
        "Look":
            hide screen countdown
            jump skipmenu

label skipmenu:
    scene flashback11 at jumpnoah
    $ renpy.pause(7, hard=True)
    w "..."
    w "(It's him alright.)"
    w "(Why the hell is he here? And– his mouth–)"
    w "(... {w}Fuck. Is he...)"
    "{i}Is he dead?{/i}"
    "{i}Shivering, I reach out to check his breath. {w}I hesitate. My arms feel numb– every nerve's screaming to pull away. But I clench my teeth and do it.{/i}"
    "{i}A fly buzzes quietly on his face.{/i}"
    w "(... {w}... {w}...No way. {w}There's no way.)"
    "{i}Unconvinced, I put my hand against his neck, looking for a pulse.{/i}"
    scene flashback11
    $ renpy.pause(2, hard=True)
    "{i}Nothing.{/i}"
    $_dismiss_pause = False
    scene flashback14 with ImageDissolve(im.MatrixColor("flashback11.png", im.matrix.tint(1,0,1)), 3, reverse=True)
    $_dismiss_pause = True
    "He's not alive."
    "..."
    "{i}Is this some kind of sick joke?{/i}"
    "{i}I can smell the blood that's congealed on the table, dark and iron-foul and sticky. {w}All the light and cunning and arrogance have gone from his eyes. All the ugliness.{/i}"
    "{i}Who knew{/i} this {i}is how we meet again, Noah?{/i}"
    "{i}And still you won't talk to me. {w}Too proud to talk to me.{/i}"
    "{i}Noah?{/i}"
    show black onlayer foreground with dissolve
    whitetext "{i}Noah?{/i}"
    whitetext "{i}Noah?{/i}"
    whitetext "\"Wilbur!!\""
    scene flashback12
    hide black onlayer foreground with Dissolve(3)
    n "There you are, Wilbur!"
    n "Ha ha, you sure take your time~ I've been looking for you since the play finished."
    w "... But it just finished a minute ago!!"
    w "Besides, {i}I{/i} was waiting for you at the–"
    n "Sooo! How was it?"
    w "Huh?"
    n "Did you like the play?"
    "{i}I grumble. He got to play the King again this year. {w}In fact– he's toying with his gold-glittery paper crown right now! What a show-off...{/i}"
    w "I-It was good..."
    n "Hehe, of course. Did you like my acting?"
    w "Yeah. But you said–"
    n "Hah, I knew it! And Maxine kept saying {i}my{/i} acting was bad. I'll tell her Wilbur loved it – and we all know you have the {i}best{/i} taste, because you're my friend! Hehe."
    w "...?? What's that supposed to... {w}A-Anyway, you promised you wouldn't audition for the play this year! You said we'd hang out at the Carnival!"
    n "Oh? {w}I did?"
    w "Yeah– I waited three hours for you at the ferris wheel– you told me you'd show up–"
    n "Aw, I'm sorry, Wilbur. It must've slipped my mind. {w}I've just had so much to do."
    w "T-They saw me alone again and– I told them I {i}really{/i} was– waiting for someone this time–"
    n "We'll hang out next time, OK?"
    scene black with ImageDissolve("flashback12.png", 1, reverse=True)
    "Next time, OK?"
    whitetext "Next time, OK?"
    show blackslow onlayer toplay
    whitetext "Next time, OK?"
    whitetext "Next time, OK?"
    whitetext "Next time, OK?"
    whitetext "Next time, OK?"
    whitetext "Next time, OK?"
    show black onlayer overlay
    scene flashback13
    hide black onlayer overlay
    hide blackslow onlayer toplay
    $ renpy.pause(1, hard=True)
    w "..."
    scene flashback14 with pixellate
    $ renpy.pause(2, hard=True)
    "{i}Do you forgive him?{/i}"
    menu:
        "Yes.":
            $ forgive += 1
        "No.":
            pass
    scene black with Dissolve(4)
    $ renpy.pause(2, hard=True)
    scene proom
    show ec at mid
    e "That's your {u}first task completed{/u}! Good job, Wilbur."
    hide ec
    show ef at mid
    e "I won't lie, I began questioning your ability a little when you started trying to run away and whatnot."
    e "But it seems I've underestimated you..."
    w "W-Wait."
    hide ef with dissolve
    show e at left with dissolve
    show w2a at right with dissolve
    e "Hmm?"
    w "...I know that guy."
    hide e
    show ef2 at left
    e "Well, what a nice surprise!"
    e "To celebrate a friend's birthday... Although, shame you couldn't have come more respectably. {w}You know. {w}As a guest."
    hide w2a
    show wa at right
    w "...Why were there glass shards on the floor?"
    hide ef2
    show ec at left
    e "Why were there stars in the sky? Why were there fish in the sea?"
    hide ec
    show ef at left
    e "More importantly, why were there omissions in your role description? {w}I didn't realize your job included hassling over my every little mistake."
    e "I broke a glass. What's it to you?"
    w "..."
    w "You killed him."
    e "And you're killing the cozy atmosphere. You'd better hurry back to work. {w}Oh, by the way,{w=.5}{nw}"
    hide ef
    hide wa
    show eh at left
    show wh at right
    eblack "{b}Keep your hands to yourself.{/b}"
    eblack "{b}Keep your nose out of my business.{/b}"
    hide eh
    show ec at left
    e "Just basic manners, isn't it?"
    hide ec
    show ef at left
    e "Anyway, you've seen what's become of your friend. He's not leaving this place any time soon."
    e "{i}You{/i}, on the other hand..."
    hide wh
    show wa at right
    w "...? Me?"
    hide ef
    show e at left
    e "You've still got a head on those shoulders. Be smart, don't throw it away."
    e "If you play nice, maybe I'll even let you out of here."
    w "P-Play nice?? In your dreams! {w}It's not like I need to be scared of– a psycho like you– I've got–"
    hide wa
    show ws at right
    w "... {w}..."
    hide e
    show ef2 at left
    e "No no, please, continue."
    hide ws
    show w2a at right
    w "... {w}... Do I have no other options? {w}...That can't be..."
    w "(...I can{i}not{/i} be stuck here with a dead body and a crazy murderer. {w}Does my company not have safety measures for stuff like this? {w}Are they so desperate they'd just take any client??)"
    hide w2a
    show w2s at right
    w "(Aha. I know. {w}I'll play along and discreetly look for an exit–){w=.3}{nw}"
    hide ef2
    show ec at left
    e "There's no back door, by the way. {w}The windows are barred. And I can only unlock the door if I'm alive, so for your own good, don't try anything funny."
    hide w2s
    show w2a at right
    w "(...{w} ...Guess I'll... {w}just play along then...)"
    hide ec with dissolve
    hide w2a with dissolve
    show e at mid with dissolve
    e "Now, task two. These walls look a little bare without any decorations, don't they? {w}That's unacceptable for a birthday party. Especially not your {i}friend's{/i}."
    e "So – won't you {u}put up some banners and string lights{/u}? They're in the wooden drawer there, behind me."
    e "After you get them, put them up on the middle and right walls, respectively."
    hide e
    show eh2 at mid
    e "Don't accidentally hang yourself on them. {b}I'll be watching.{/b}"
    hide eh2 with dissolve
    scene proome with dissolve
    call screen task2

label flashback2:
    "String lights go woop woop"
    scene black with Dissolve(1.5)
    $ renpy.pause(1, hard=True)
    scene flashback21 with Dissolve(2)
    $ renpy.pause(1, hard=True)
    w "(...)"
    w "{i}From the corner of my eye, I catch a glimpse of the banner I'd just put up. Happy Birthday, it says. {w}Ironic. {w}For once{/i} he{i}'s the butt of a joke.{/i}"
    w "(Banners. They're meant to be celebratory, I guess. {w}I should know. Carnival play... {w}prom... {w}graduation...)"
    scene flashback23 with Dissolve(1.5)
    "..."
    "{i}None of it ended up worth celebrating.{/i}"
    scene black with Dissolve(1.5)
    $ renpy.pause(1, hard=True)
    "\"And at first place, we have...\""
    show flashback22 onlayer foreground
    "\"Noah Chalan!\""
    scene flashback22
    hide flashback22 onlayer foreground
    "{i}\"Noooaaah!!\"{/i}"
    "{i}Noah's friends cheer from the audience. He's got a lot of them, now.{/i}"
    "{i}It's a little silly, to be honest. Just a school science fair project. {w}What was the fair about, even? Forests? Astrophysics? I can't remember.{/i}"
    "{i}But I remember how he kept calling me, when I just wanted to focus on my project. {w}How he dragged me out to play. {w}How he told {/i}me{i} to put it off, because {/i}he{i} put it off."
    "{i}How he didn't have anything ready, the night before the fair.{/i}"
    "{i}How he told me he'll just give up his place.{/i}"
    scene black
    show black onlayer toplay
    whitetext "{nw}"
    hide black onlayer toplay
    whitetext "I guess he wasn't asking for my help. {w}Regardless, that's what I gave him. Stupid me."
    whitetext "I scrambled for cardboard and colored paper and glue, while he sat humming, telling me that I really needn't worry about him. {w}That I can finally win this year."
    whitetext "I laughed. Of course I'd win. {w}There's no way this crammed overnight project– which {i}I{/i} was making for {i}him{/i} out of sheer pity– would be better than mine. {w}I spent weeks on mine."
    whitetext "..."
    whitetext "Seems like he gave it a little renovation the morning of the fair. A little margin here and there. A pretty title."
    whitetext "But that doesn't answer it. {i}How could he win?{/i}"
    whitetext "{i}How could he win?{/i}{w=.4}{nw}"
    whitetext "{i}How could he win?{/i}{w=.2}{nw}"
    whitetext "{i}How could he win?{/i}{w=.1}{nw}"
    whitetext "{i}How could he win?{/i}{w=.1}{nw}"
    whitetext "{i}How could he win?{/i}{nw}"
    show flashback23 onlayer toplay
    scene flashback23
    hide flashback23 onlayer toplay
    w "!!..."
    w "(N-No, I–){w=.3}{nw}"
    scene flashback22 with ImageDissolve("flashback23.png", 2, reverse=True)
    "{i}–{w}The applause scorches like molten iron in my ears. I look at the audience, tracing their gaze. They're all looking at him.{/i}"
    "{i}To my surprise, he turns towards me. I meet his eyes with foolish expectancy.{/i}"
    "{i}He grins brightly, and whispers,{/i}"
    scene black with ImageDissolve("flashback22.png", .5, reverse=True)
    $ renpy.pause(1, hard=True)
    anon "{b}\"Thanks, Wilbur~\"{/b}"
    show flashback21 onlayer toplay
    scene flashback21
    hide flashback21 onlayer toplay
    $ renpy.pause(4, hard=True)
    "{i}Do you forgive him?{/i}"
    menu:
        "Yes.":
            $ forgive += 1
        "No.":
            pass
    scene black with Dissolve(4)
    $ renpy.pause(2, hard=True)
    scene proom
    show ef2 at left
    e "..."
    show wa at right with dissolve
    w "What?"
    e "You've got a sour expression. Like you're holding a grudge over some silly little thing from middle school."
    hide wa
    show ws at right
    w "...I don't know what you're talking about..."
    hide ws
    show w2s at right
    w "Besides, you don't know my middle school. Maybe it {i}was{/i} bad."
    hide ef2
    show ef at left
    e "..."
    e "I admire your ability to say that with a straight face."
    hide ef
    show e at left
    e "Anyway. How'd you know him?"
    hide w2s
    show w at right
    w "...?"
    e "How'd you know Noah?"
    hide w
    show ws at right
    w "...Well he's– just an acquaintance really– we aren't {i}that{/i} close–"
    e "Through school, I reckon? Or were you childhood friends?"
    hide ws
    show wa at right
    w "Hey! How did you know?? Are you a stalker or something??"
    hide e
    show ef at left
    e "... Even if I were, {i}you{/i}'d probably be safe."
    hide ef
    show ef2 at left
    e "But if you want my thought process– you probably knew Noah through work or school. {w}And given your job, he... doesn't seem like a colleague."
    e "Or you could live in the same neighborhood. Which... {w}... again, isn't too likely."
    hide ef2
    show ec at left
    e "So? You were saying something about middle school being bad?"
    w "... Forget it... {w}When are you letting me go, anyway?"
    hide ec
    show eh2 at left
    e "... {w}Glad you asked. {w}Not before the party is finished. {w}Don't be impatient."
    hide wa
    show ws at right
    w "Pfft. D-Doesn't look like much of a party to me. A couple {i}real{/i} guests might've helped."
    eblack "Do not get clever with me, Wilbur. It reflects poorly on your service."
    hide ws
    show w2a at right
    w "Hey! I–I get it, OK?? No need to be scary..."
    e "... {w}{b}I wonder how your head would look hanging from the chandelier.{/b}{w=.3}{nw}"
    hide w2a
    show wh at right
    w "What the hell was that?"
    hide eh2
    show ec at left
    e "Hmm? Just a little appreciation for your natural assets. {w}Anyway, you're gonna like this {u}next task{/u}! We're setting up some snacks and drinks for catering."
    "{i}He retrieves a range of buffet food warmers from... god-knows-where. {w}The storage room? The kitchen? Look like stainless steel.{/i}"
    hide wh
    show w2a at right
    "{i}Then, he shoves a few boxes of dessert delivery in my hands, and a carton of fruit punch.{/i}"
    hide ec
    show e at left
    e "Cupcakes... they may look tempting, but try not to steal a bite. {w}I don't have the budget to order more, in case our guests run out."
    hide w2a
    show w2s at right
    w "(Hah, he's still on about some... \"guests\"...? Besides–)"
    "{i}I weigh the oil-stained delivery boxes in my hands. The cardboard feels damp on my fingers.{/i}"
    hide w2s
    show w2a at right
    w "(–Eugh. The desserts must've long gone cold and greasy...)"
    hide e
    show ef at left
    e "Unless... you'd offer to bake some more?"
    hide w2a
    show wa at right
    w "... {w}Just now– did you– {w}say something about the chandelier??"
    hide ef
    show ec at left
    e "What? No, not at all."
    hide ec
    show eh at left
    hide wa
    show wh at right
    e "But I might if you don't {b}stop lazing around.{/b}"
    hide eh
    show eh2 at left
    e "... Kindly {u}set these up on the long table{/u} to the right, with the white tablecloth. {w}{b}Don't{/b} disappoint me now."
    hide eh2 with dissolve
    hide wh with dissolve
    scene proome with dissolve
    call screen task3

label flashback3:
    scene black with Dissolve(2)
    scene flashback31 with Dissolve(2)
    w "(Finally. All set up. {w}Even if there are no guests to cater...)"
    w "(...It'd be a shame to let these go to waste, though. Maybe I {i}should{/i} take one?)"
    w "(Ugh, but it'd be so noticeable! Eden'd see it right away. {w}Should I? Should I not? {w}Should I? Should I not? {w}...)"
    scene black with dissolve
    w "Ahh, I can't decide..."
    n "Oh come {i}on{/i}, you should just tell her!"
    w "B-But what if. You know. Maxine doesn't like me back? Will she think I'm a creep?? Does she even know I exist???"
    n "Well, she {i}would{/i} know if you toughen up and introduce yourself. And who knows? You might just get lucky."
    w "...That's easy for you to say... {w}you could probably win anyone's heart you want..."
    n "Hey, not {i}everyone{/i} likes me."
    w "–Only your exes don't!! I haven't even had one girlfriend– {w}...But I guess you're right... maybe I'll ask her to... be my date for..."
    n "Hmm? What was that?"
    w "N-Nothing!!–"
    scene flashback32 with pixellate
    $ renpy.pause(2, hard=True)
    "..."
    "{i}I mean, at this point, I should've probably expected it.{/i}"
    "{i}I was no competition for Noah. Who {/i}wouldn't{i} want to be Noah's prom date? In fact, people {/i}speculated{i} about it. Which lucky girl?{/i}"
    "{i}On the other hand – who would ever want to be mine?{/i}"
    "{i}But it's just mean. He knew I liked her. {w}Or did he forget again? Like he always did?{/i}"
    "{i}Does it even matter?{/i}"
    "{i}There I was, early evening, waiting for him to show up so I'd have someone to talk to. Just where {/i}was{i} he? I kept thinking, as if that made me less of a loner.{/i}"
    "{i}And– admittedly– I was looking all over the venue for a glimpse of Maxine. {w}How heavenly would she look in a prom dress? What color did she pick? What cut? {w}Did she wear her hair up or down?{/i}"
    "{i}Guess I found out the answers for both. {w}And it just had to be across the food table. {w}When I'd given up waiting and gone back for seconds.{/i}"
    scene black with ImageDissolve("flashback32.png", 2, reverse=True)
    $ renpy.pause(2, hard=True)
    scene flashback33 with pixellate
    $ renpy.pause(2, hard=True)
    w "(Funnily enough, I don't have much of an appetite anymore.)"
    show flashback33 onlayer toplay with dissolve
    $ renpy.pause(2, hard=True)
    hide flashback33 onlayer toplay with dissolve
    "{i}Do you forgive him?{/i}"
    menu:
        "Yes.":
            $ forgive += 1
        "No.":
            pass
    scene black with Dissolve(4)
    $ renpy.pause(2, hard=True)
    scene proom
    show e at left
    e "Is your brain rotted?"
    e "EEENNND OF GAAAME BACKPEDAL RIGHT NOW"
    return