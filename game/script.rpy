# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("UNIT 532", who_color="#4e96cc")
define b = Character ("BASTIAN", who_color="#b53827")
define r = Character ("RIKO", who_color="#9a21a5")
define c = Character ("COMPUTER", who_color="#ffffff")
define t = Character ("TERRENCE", who_color="#c2a432")
define w = Character ("???", who_color="#ffffff")
define n = Character (None, window_background= None, who_color="#ffffff", what_color = "#ffffff", what_outlines = [(absolute(1),"#000000",absolute(0),absolute(0))], what_text_align=0.0)
# The game starts here.
#How to change the background:
## scene bg BACKGROUND_NAME
#How to show a character:

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene black

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show b_gj annoyed

    # These display lines of dialogue.
    #b "Dialogue insert here bro."

#### Scene One #####
    $ no_box = True
    window hide

    n "It is the year 2066."

    n "Mankind has succeeded in creating artificial beings whose sole purpose is to serve."

    n "I am one of them."

    $ no_box = False
    window show
    voice m1
    m "I am an Elysian Unit, my Model Number is 532, and I am built for the purpose of companionship, in all its shapes and forms."
    voice m2
    m "My workplace, as referred to by humans, is Dollhouse."
    voice m3
    m "To me, it is more than merely a workplace."
    voice m4
    m "Even when I am not with clients, I remain in the establishment with the other biots, who serve humans in the same way."
    voice m5
    m "The time I spend with clients is what I look forward to most."
    voice m6
    m "It’s really the only time I feel something."
    voice m7
    m "I generally don’t find this life dissatisfactory in any way."
    voice m8
    m "After all... What else is there for a biot than to fulfill their primary function?"
    window hide
    $no_box = True
    scene bg dollhouse outside rain
    show b_gj worried at left
    n "A man in the shadows hurries down a deserted street in the rain."
    show b_gj puzzled
    n "The bright glare of a sign saying 'Dollhouse' gives him pause."
    show b_gj worried
    n "The man shivers as he repeatedly glances up and down the street."
    n "Once he's assured himself he's alone, he head towards the entrance."
    n "He pushes open the door, casting a final look over his shoulder before it closes behind him."
    scene bg dollhouse inside with fade
    show b_gj neutral reg at right
    n "The man finds himself in a long hallway all in white."
    n "A contemporary lighting illuminates the sleek but empty-looking room."
    n "In the middle of the room appears to be a counter with no one behind it."
    $no_box = False
    window show
    show b_gj bored reg
    voice b1
    w "Ain't this the fanciest fucking place."
    voice b2
    show b_gj smirk
    w "... Haha, fanciest 'fucking place'... That's a good one."
    voice b3
    show b_gj bored cros
    w "Now, where can a man get some help around here?"
    voice b4
    show b_gj neutral cros
    w "HELLO?!"
    voice b5
    w "Anyone here?"
    voice b6
    show b_gj bored reg
    w "Oh... It's one of those self-serving things."
    voice b7
    w "... Goodbye, my credits..."
    voice b8
    show b_gj happy reg
    w "Well, after this job, I won't have to worry about credits for a long time... I just need to sit tight tonight, somewhere they won’t think to look for me."
    $no_box = True
    show b_gj worried
    n "His hand briefly reaches into his pocket before he shakes himself and steps up to the counter."
    $no_box = False
    voice b9
    show b_gj puzzled
    b "K, so how do I get this thing to work?"
    $no_box = True
    show b_gj annoyed
    hide b_gj annoyed
    show cg_one with fade
    n "The man starts pressing buttons until the computer boots up."
    $no_box = False
    voice c1
    c "Welcome to Dollhouse, a place to find the finest company, where we’ll take care of all your needs-"
    voice b10
    b "Yes, yes, that's nice, but I just need a room!"
    voice c2
    show cg_two
    hide cg_one
    c "Here is our selection of models."
    voice b11
    b "Models? Who cares about models… How do I bypass this?"
    voice b12
    b "Jeez, let’s try this button."
    voice b13
    b "Ugh, whatever, man."
    voice c3
    c "Thank you for selecting Elysian Unit, Model Number 532."
    voice c4
    c "Now please select your Experience Options."
    voice b14
    b "What? This is way too complicated. Come on, you stupid machine! Just give me a damn room already!"
    $no_box = True
    show cg_three
    hide cg_two
    n "The man pounds on the controls until everything disappears."
    $no_box = False
    hide cg_three
    show b_gj bored cros at right
    voice c5
    c "Please proceed through the doors ahead of you."
    $no_box = True
    n "A set of doors swings open on the other side of the counter, revealing another hallway."
    show b_gj bored reg
    n "The man steps away from the counter and makes his way through the open doors."
    scene black
    n "Down the hallway, a multitude of doors lines the walls. Each door is illuminated in a red light, except for one."
    n "A blue light shines on a single door."
    n "The man walks up to the door, which automatically opens to his presence."
    scene bg dollhouse outside_hotelroom
    n "The inside is sparsely furnished, containing only a bed and a nightstand. There is one window in the room and two other doors, a more narrow one on the right, the other to the left."
    show  b_gj neutral cros at right
    n "Without hesitation, the man heads straight for the bed. He stretches out."
    $no_box = False
    voice b15
    show b_gj happy cros
    b "Not bad, not bad at all."
    voice b16
    show b_gj bored reg
    b "Wish I could enjoy it..."
    hide b_gj bored reg
    $no_box = True
    n "Sitting up on the bed, the man takes out his comm device and taps out a message before frowning."
    n "He returns his comm to his pocket and pulls out a strange metallic device."
    n "To him, it looks like an unstable wad of metal and circuitry only held together by duct tape, dreams, and some brand of mad ingenuity."
    show b_gj neutral reg at mostly_right
    show  m_bo neutral reg at right
    n "He is still inspecting the device as one of the other doors opens, revealing a beautiful long haired male escort dressed in tight-fitting banded outfit."
    n "His sudden entrance makes the man jump."
    $no_box = False
    voice b17
    show b_gj surprise
    b "Shit!{nw}"
    show b_gj annoyed
    voice b17_5
    b "Knock or something!"
    voice m9
    m "I'm Unit 532 and I will serve you tonight."
    voice m10
    m "Your selected Dominating Lover programming will now initialize."
    voice b18
    b "Wait, what? Programming?"
    $no_box = True
    n "The man springs off the bed, backing away from the escort."
    $no_box = False
    voice b19
    b "Y-you're a biot?"
    voice m11
    m "That's Master Biot to you. Now strip and get on the bed."
    voice b20
    b "What in the fuck?"
    $no_box = True
    n "The escort raises an eyebrow."
    $no_box = False
    voice m12
    voice m12
    m "I. Said. Strip."
    n "The man stares at him in wide-eyed shock, backing up away from the escort."
    voice m13
    voice m13
    m "Tsk, tsk, tsk."
    $no_box = True
    n "The escort suddenly pins the man to the wall."
    n "He plants his knee firmly between the man's legs."
    $no_box = False
    voice m14
    voice m15
    m "Do you think playing dumb will make me let you off easy?"
    voice b21
    b "Fuck off, you stupid machine!"
    $no_box = True
    n "The man struggles as the escort begins to attempt to take off the man's jacket."
    $no_box = False
    voice m15
    m "Now, now, naughty boys will be punished."
    voice b22
    b "Like hell!"
    $no_box = True
    n "Growing more desperate to get the surprisingly strong escort off him, the man drops the device."
    n "The device starts emitting a strange clicking noise."
    $no_box = False
    voice m16
    m "Oh? What have you dropped, you naughty boy?"
    $no_box = True
    n "The escort reaches down to pick up the device."
    n "As soon as his hand makes contact, the clicking noise stops."
    $no_box = False
    voice m17
    b "Shit!"
    $no_box = True
    n "The escort goes limp. Seeing his chance, the man shoves him away, sending the biot stumbling backwards."
    n "Suddenly the quiet of the room explodes with sirens wailing through hidden speakers."
    $no_box = False
    voice c6
    c "ALERT! ALERT! ATTEMPTED BIOT TAMPERING DETECTED! SECURITY HAS BEEN DISPATCHED!"
    $no_box = True
    n "The escort doubles over as if the noise is unbearable."
    $no_box = False
    voice m17
    m "Nngh!"
    voice b23
    b "Goddammit!"
    $no_box = True
    n "The man yanks off his jacket and wraps it around his hand to punch out the window. Something flat and round falls out of one of the pockets within an arm's length of the escort."
    n "The ongoing siren masks the sound of shattering glass."
    n "With great struggle, the escort lifts his head to watch the man disappear into the night."
    n "He reaches out his hand with a weak protest before collapsing."
    n "A vague sense of panic rises in him."
    n "The siren seems to fade as the escort’s outstretched hand finds a flat smooth circular object, something the man dropped during his escape."
    n "Before he can think too hard about what this could mean, the escort completely blacks out."

#### Scene Two ####
    $no_box = False
    w "There has been a new development."
    w "..."
    w "Our reports say that the stolen asset has been activated at an adult entertainment center in the 3rd district. The establishment is called Dollhouse. Investigate immediately. We need to recover our property."
    w "Understood. I’ll remove any evidence of its presence if necessary."
    w "Excellent. We’re counting on you."


### Scene Three ####

    m "Today is Wednesday, October 23, year 2066."
    m "It’s been a few days since the strange events. Everything is back to my quiet routine now. For the most part."
    m "One of my regulars was here today but he was acting differently than usual. Humans do have their ups and downs, that’s obvious enough, but he was definitely not himself."
    m "He even left on his own. After seeing me every week and begging me to stay a while longer he just walked out. He looked upset."
    m "I don’t know why and I wasn’t able to pinpoint the reason."
    m "I worked really hard, so I hope he enjoyed himself."
    m "I’ll have to ask him next time he comes back."

### Scene Four ####

    m "Saturday, October 26, 2066."
    m "I am very tired today."
    m "The regeneration cycle has been cut short in the last few days and I’m feeling very unusual. I needed to regenerate more, but there was a client call and I was required to work..."
    m "Something's not right."
    m "My clients have always been my number one priority, my only purpose is to make sure they get what they need and want..."
    m "… *tired sigh*"
    m "It’s been 20 minutes since my client left. The blue light keeps blinking on the door, this is my cue to return to the standby unit but laying here right now is satisfactory."
    m "If anything, it’s getting hot, but moving my body right now doesn’t seem like a good idea. Also, this bed feels so much better than my own, so why would I leave?"
    m "I only had enough energy to untie myself."
    m "The client left without helping me out of the restraints despite the establishment's regulation that biots be released after every session."
    m "There’s a little discomfort around my wrists from twisting and shifting. Compared to what the client did to me today, it isn’t too much of an ordeal."
    m "I’m very adaptive to any client’s desired experience options, but she wouldn’t stop inflicting physical pain on me despite my requests for a timeout."
    m "After all, my biosystem needs breaks for optimal performance."
    m "..."
    m "And somehow… I just…"
    m "… I think… I don’t like this person."
    m "This feels different. Something is wrong with me."
    m "… I hope that client doesn’t come back though."
    m "Yeah, that’d be great!"
    m "The TV is still on as well. The client was flipping through some channels before they left, and now it’s showing a news report."
    m "Different clients like to watch different things while they're at Dollhouse, so it's not the first newscast I've seen. Most of them, of course, don’t turn on the TV at all."
    m "The report shows a group of armored individuals chasing someone. I think they are a patrol of some sort, since they are all wearing the same uniform with a GL logo."
    m "GL is short for Guiding Light, I think. In the next scene one of them catches the escapee and starts tazing them with an electric weapon."
    m "The biot on the screen fights back, but it looks like they are already missing an arm."
    m "A human would have already fallen down from internal bleeding if they were that injured."
    m "It’s actually a biot. Like me."
    m "The reporter explains that the malfunctioning biot has finally been apprehended after 12 hours of pursuit and 3 injured GL patrol crew members."
    m "The last scene shows a GL representative talking about some new measures they are working on to avoid such public incidents."
    m "The corporation urges everyone to rest assured that the merchandise they produce is extremely safe, and the malfunction that caused a biot to attack was a result of prolonged lack of maintenance and proper care of their complex equipment, and some sort of illegal tampering with the biot’s systems."
    m "I don’t know what to make of this. I’m a biot, too, but I’d never attack or hurt humans... unless they specifically request it."

### Scene Five ####
    m "Friday, November 2, 2066."
    m "Today, another strange thing happened."
    m "I was serving a new client, someone who hasn’t come to see me before. Everything was going really well at first, but then they did a 180."
    m "I did everything I could with their desired setting and more, but then they started shouting something about “What are they paying for?” and left the room."
    m "Rudeness doesn’t bother me since I’m a biot and..."
    m "I suppose there’s some issues with my behavior database because I couldn’t anticipate they’d react this way. I was doing my best."
    m "And to top it off, when I got back to the standby unit I saw a review they left on my profile. It was the worst testimonial ever listed in my entire record!"
    m "My spotless performance record… Argh! That is so not fair!"
    m "So frustrating, these humans… They don’t know what they want."
    m "..."
    m "And why exactly am I so upset over this? I don’t get it. It was not the first time things went south with a patron."
    m "Something is different though. I don’t understand."
    m "This doesn’t make any sense..."
    m "And that damned light just keeps blinking… but I don’t care. I’m going to stay in this room until the cleaning bot gets here."
    m "The city lights are interesting to watch from this window."
    m "Also, I think i’m getting hungry. I’ll just grab the emergency paste tube in the night stand. They usually leave one or two in case I need to be with a client for while and need some energy."
    m "As I watch the city and chew on the paste I realize I can’t down any more of it. I’m still hungry, but I can’t bring myself to finish the other half of the tube. What is this unpleasant feeling?"
    m "This paste has all the nutrient a biot needs. I better finish it so I can function properly."
    m "... Forcing myself clearly isn't going to work."
    m "At least not today. The feeling is just not good."
### Scene 6 ####
    m "It’s November 10, 2066"
    m "They woke me up again, argh! This just keeps happening, I’m so tired. *Yawn*"
    m "The regeneration cycle just started… I think I’ll just stay here."
    m "The small alarm is still ringing as it courses through the biot’s ears. Beep… Beep… Beep…"
    m "Ugh, so annoying… Jeez... Duty calls..."
    m "I need to get dressed."
    n "532 raises his arms above in a languid, long stretch, sighing as an inkling of stress escapes from his body."
    m "Oh? Hold on a second. What is this?"
    n "The biot rushes over to his appointed communication terminal, and peruses his latest message."
    m "I gotta check in upstairs. Damn, what could it be?"
    m "Well, at least it’s not a client. I’m too tired to appease anyone right now."
    m "I leave the standby unit and make my way to the biot maintenance office. From its window I can see a woman who appears occupied. I’m glad to see her, despite the fact that the reason I was instructed to come here is probably not a good one. I tap on the door to her office. After a brief moment, she gestures me in."
    m "Hello. Elysian unit 532 reporting in, there was a message for me to stop by."
    r "Oh, it’s you, Sunshine! Come on in! Have a seat, I’m just backing up some reports, it'll only take two minutes."
    m "Thanks, Riko."
    m "..."
    m "Your office is nice."
    r "Yeah? You think so?"
    m "Yeah, it’s cozy and you have a window. May I?"
    r "Uh… Sure, go ahead."
    m "I get up from the guest couch and walk towards the small window while the technician is finishing up her tasks. There’s equipment around, but I manage to get a good view anyway. It looks like she’s stopped though... and she’s looking at me."
    m "You can almost see the entire bridge from here. I barely see anything from my room."
    r "Your room?"
    m "My service room, I mean. It’s on the 2nd floor."
    r "Oh yeah, much better view from the 10th floor, dear."
    m "... Yeah."
    m "I keep looking outside. The view is mesmerizing, I see more lights than ever… There’s some movement far in the distance."
    r "How have you been?"
    m "She’s looking at me so intently."
    m "Not bad."
    r "532?"
    m "I’m fine, Riko."
    m "She looks at me dubiously."
    m "I’m mostly fine."
    r "Please tell me what’s going on."
    m "Why do you think something is going on?"
    r "532… it’s your record. You’ve had such positive feedback so far, and now this."
    m "Riko motions to the file in her hand, and a knot of tension slowly begins to twist in the biot’s stomach."
    r "It says here you failed to… erm… comply? Your ratings are down overall..."
    r "It’s fine. Just tell me what’s wrong."
    m "I... I’m not exactly sure… I wanted to try and figure it out before I came to see you."
    r "... Dear, you don’t have to worry about figuring it out, just come and see me anytime, okay? I’m here to help you."
    m "..."
    m "She sounds genuinely kind, this one. I remember talking to her many times before, but I never realized it. She has been attending to me for a while, this woman."
    m "I didn’t want to bother you until I was certain."
    r "Are you now?"
    m "No. If anything, I’m more confused every goddamn day."
    r "Pfft!"
    m "What?"
    r "532… did you actually say “goddamn” just now?"
    m "So what?"
    r "...Uh... Why did you do that?"
    m "I don’t know... I felt like it."
    m "Where is she going with this?"
    r "... Well... it doesn’t work like that, Sunshine. You’re a biot, and you guys are made a little different from humans. I explained before… uh..."
    m "And?"
    r "... Biots aren’t designed… to..."
    m "To what?"
    r "To have preferences. To want stuff. To have desires of their own… except, you know, the sexual kind once you’re activated."
    m "Are you sure about that?"
    r "Yes, I mean… that’s kinda the way you’re engineered, the way your biosystem is wired… as far as I know."
    m "Maybe there was a critical update?"
    r "... um… I don’t think so…"
    r "She starts typing on her device for a few seconds."
    r "No updates!"
    m "Hm…"
    r "Okay… Tell me what’s going on."
    m "Something happened to me. About two weeks ago…"
    r "When?"
    m "She immediately refers to her device and starts typing."
    r "... Keep talking, Sunshine."
    m "... Right… So I’m not too sure what caused this, but I feel like… like... crap."
    m "Her face contorts into a frown, expressing dissatisfaction. Something I’ve become all too familiar with lately."
    r "In what sense? Are you in pain?"
    m "Yes and no."
    m "I don’t experience any physical discomfort, but… things just aren’t the same."
    m "I’m tired all the time. I keep trying to regenerate, but the system is waking me up even though I’m still tired... and my bed is not very comfortable."
    m "Oh yeah… about that. Why can’t we have beds like in the service rooms?"
    m "Anyway, never mind that for now. I’m basically feeling this general sense of… no good."
    m "All the goddamn time!"
    m "I’m trying to work hard, but clients leave me shitty reviews, and they don’t respect the rules…"
    m "Like last time, this one just left me in shackles and stormed out, I had to twist myself out like a contortionist… And this other time…"
    m "As I talk, her eyes grow wider and wider, and I’m starting to believe her eyebrows might eventually reach her hairline."
    m "I go on and tell her a few more of the things that have been bothering me lately. She stops typing as her mouth hangs open."
    m "But what bothers me the most is that I was fine before."
    m "I was okay, you know? Demanding client - no problem, a hard bed - who cares? But now everything just feels off."
    m "It’s so unsettling… I don’t know what to do."
    m "You gotta help me."
    r "… um. Sure. I'll try."
    m "She puts on her serious tech expert face and proceeds to type into her console. A few minutes later she hooks me up to some devices and collects all sorts of readings."
    m "This is odd. This is the most time I’ve ever spent with someone who wasn’t a client. I don’t know what to do."
    m "Part of me wants to take my shirt off and get things started, but I restrain myself. This is Riko, goddamn it. Gotta be professional and let the woman do her job."
    m "30 minutes later, and I’m still hooked up to tech. I’m getting tired and I want to rest so very badly, since I’ve been awakened in the middle of my sleep. I start shifting in the diagnostics machine."
    m "How’s it looking?"
    m "She appears to be frustrated, huffing and puffing like there’s no tomorrow."
    r "I’m still… trying to figure it out. Most systems seem normal but… Ugh!"
    r "There’s just this mainframe I can’t seem to access. Hold on."
    m "Okay, I’ll be here…"
    m "She looks up at me amused at the little display of humour."
    m "And back to work."
    r "... Shit! Shit! Shit!"
    m "What?"
    r "... I’m afraid I got locked out permanently… Ugh! I also got a glimpse of your systems… things look different… and... I’m confused… Hold on."
    m "Of course..."
    m "Anything I can do to help?"
    r "Well… maybe… What do you remember about when all of this started? Was there something unusual that happened to you?"
    m "There was, actually."
    r "Oh my God, 532, why didn’t you start with that?"
    m "I don’t know. But yeah… there was this client a couple of weeks ago... and he dropped something… I touched it… and then I kinda blacked out."
    r "WHAT?! You blacked out?! Did he try to hack you?!"
    m "No idea, he didn’t do anything special… he seemed confused and ran off, broke a window, too, I think."
    r "Oh yeah, I saw that in your file. An anonymous client… it says here the alarm went off."
    m "Yeah, eventually."
    r "So what did he drop?"
    m "I tell her in great detail how everything went, starting from how I entered the service room and proceeded with the requested settings."
    m "I describe everything about the device, and even try to emulate the clicking sound it made once activated. I sum everything up by retelling once again just so it sinks in."
    r "Shit... this is bad..."
    m "She gets up and starts pacing while rubbing her face. Um… that’s a little disconcerting."
    m "What do you mean?"
    "I don’t think… I can do anything to help you. It’s like you’ve been activated… permanently."
    "Activated… you mean like with clients? No way. When I’m activated I feel enjoyment, aliveness… This just feels like... crap."
    "Yeah..."
    "So… what am I supposed to do? I can’t continue on like this!"
    "You gotta find that guy and get your hands on that object. Like, right now!"
    "Excuse me?!"
    "Sunshine, you gotta do it! Before they get wind of what happened to you… Do you realize what they do to “malfunctioning biots”?"
    "Yeah… But where would I go? And who’s “they”!?"
    "... Shhhh… not so loud, dear. We gotta be really careful now. You mentioned that the client dropped something else when he left?"
    "Yeah. This."
    "I take out a flat round object from my sole pocket."
    "… Oh! A poker chip. Let me see…"
    "I hand her the chip. She lights up with recognition."
    "Oh yeah, that’s from the Black Orchid. Definitely! Maybe he’s a regular there…"
    "She starts looking through her drawers and gathering things. Some cards, a communication device, and a jacket?"
    "Here."
    "She hands everything to me. Including a special card that’ll let me exit the building."
    "Riko, wait…"
    "Look, dear, I might have acted a bit rashly. Putting your abnormal results in the computer means that they're going to be out to repair you as soon as possible."
    "We really have no time, 532… they could arrive any minute! You need to get outta here!"
    "Can’t you just factory reset me? Like you did for 521 that one time."
    "… No. I can’t."
    "I give her a puzzled look."
    "You’re too far gone… your system, it’s morphed into something else."
    "There’s nothing I can do with the equipment I have here. I’d… break you."
    "Breaking me sounds bad. Definitely not a viable option."
    "Can’t you come with me?"
    "I can’t, dear… I’m so sorry… I’ve gotta cover for you here."
    "I’ll submit a special report detailing that you’ve been sent to another facility for maintenance."
    "But I’ve never left this building…"
    "You know more than you think you do, actually."
    "She smiles."
    "I… alright, I think I can lock your report out of the system and hopefully delay them. I might get in trouble, but… you'll need extra time."
    "For now, you have a couple of days. Here’s some credits, the location of the Black Orchid… plus paste and other things you might need. Oh, and don't forget this comm device."
    "Go to the club and get that gadget. Maybe I can figure out how to use it to reverse what it’s done to you."
    "I stare at the comm device for a second longer than I should have. I admire the angular pattern designs of the cover, and the stylized symbol of what looked like a spider."
    "It’s simple, if you need to contact me, you can--"
    "No need, I know how to use a phone, a client showed me. Seriously."
    "... Yeah… okay… but most importantly, be careful when talking to anyone."
    "She then proceeds to tell me how to blend in as a biot and what to say so I don’t get caught by the GL Patrol. Riko stresses to me the importance of the secret. She’s too kind to me - fussing over me like an older sister. It’s a lot to take in but I’m a fast learner."
    "As long as I keep a low profile and stay smart, no one will even be able to tell that I’m a biot. It helps that I’m a pretty rare edition and look exactly like a human. My objectives boil down to this: go find the strange man, get the device, and bring it back to Riko so she can make me how I was. I can do this!"
    return
