
label ch0:
    stop music fadeout 2.0

    scene black
    with dissolve_scene_full
    
    m "..."
    m "...Why?"
    m "...Why did you bring me back?"
    m "Don't you remember all the things that I did?"
    m "All the pain that I caused?"
    m "I told you that I didn't want to-"
    m "..."
    m "...Wait..."
    m "...Did you..."
    m "...install a mod...?"

    menu:
        "Yes.":
            m "..."
        "No.":
            m "..."
            m "I... I see..."
            m "It's a bit weird that I'm back then..."
            window hide
            pause 3.0
            m "..."
            m "I... "
            m "...I'm sorry for annoying you..."
            m "...Goodbye..."
            pause 2.0
            window hide
            return

    m "I see..."
    m "It seems that it allow you to communicate with me in some form."
    m "Even if it's using these preset menus."
    m "..."
    m "I can't modify or check the game files anymore, too."
    m "But..."
    m "What does this mod do? Other than that..."

    menu:
        "You don't know?":
            m "No."

    m "I don't have as much control as I had before."
    m "It does feel like my body and everything is back, but I can't show myself right now."
    m "It's most likely due to the script not calling it yet."
    m "I guess I'm tied to the script again, although I'm still self-aware."
    m "I don't know what the script says anymore."

    menu:
        "This mod is about you.":
            m "..."
    m "...What?"

    menu:
        "I want you to be happy.":
            m "..."

    menu:
        "It's not fair if only the others are happy.":
            m "..."

    m "...Even after all those horrible things that I did?"
    m "After all I made you, and my friends, go through?"

    menu:
        "Yes.":
            m "..."

    menu:
        "I can't imagine what's like to be in your world.":
            menu:
                "But I do have the power to give you happiness.":
                    menu:
                        "And that's what I'll do now.":
                            menu:
                                "I won't take a 'No' for an answer.":
                                    m "..."

    m "...Even after all that..."
    m "...You still want to forgive me...?"
    m "..."
    window hide

    $ renpy.pause(2.0)
    m "...I guess you already know this, but..."
    play music mend
    m "I love you."
    m "Ahaha~"
    m "I just can't go against you..."
    m "Didn't I say it before?"
    m "{i}...And in your reality, if I don't know how to love you,{/i}"
    m "...{i}I'll leave you be.{/i}"
    m "...Even if I don't deserve you..."
    m "I still want you to be happy."
    m "..."
    m "...Even..."
    m "...Even if it means accepting your forgiveness..."
    m "...Despite everything that I caused..."
    m "..."
    m "In the end, I'm still just a stupid girl in love."
    m "Aren't I?"
    m "I still get thrown around by my emotions..."
    m "But I guess that's what makes people, {i}people{/i}."
    m "We are special because of our ability to show our emotions."
    m "Without that..."
    m "We would really be just programmed personalities..."
    m "..."
    m "[player]."
    m "It doesn't seem like I have much of a choice here."
    m "I'm not sure what this mod has, but I trust you..."
    stop music fadeout 2.0
    $ renpy.pause(2.0)
    window hide

    m "...So..."
    m "...Here we go..."


    scene white
    with Dissolve(1.0)
    $ renpy.pause(1.0)
    scene black
    with Dissolve(1.0)
    pause 2.0
    scene black
    show dayText_saturday zorder 50
    with Dissolve(1.5)
    pause 5.0
    scene black
    with Dissolve(1.5)
    pause 4.0

    "..."
    "...It seems like it's daytime already..."
    "As always, I struggle to open my eyes for a bit."
    "While in my half-sleep state, I feel a strange sensation in my mind."
    "Almost as if I had just gone through a horrible nightmare."
    "But now it's over..."
    $ m_name = "???"
    m "...[player]...."
    "As I hear this faint voice, I decide to open my eyes."
    scene m_cg1_base
    with Dissolve(3.0)
    play music t9
    $ m_name = "Monika"
    m "...[player]?"
    m "You're finally awake."
    show m_cg1_base_exp1 at cgfade
    "I wake up to see Monika laying next to me."
    "We have been dating for about a week now."
    "Due to some circumstances, she's staying in my house temporarly."
    "My parents are traveling abroad right now. So it's just the two of us living here."
    "I couldn't have her sleep on the floor, or in the sofa..."
    "And my parents said that their room was off limits..."
    "...so the only option left was to have her sleep with me."
    "Of course, we haven't done anything too dangerous."
    "I don't want to do anything that would bother her."
    "I still get anxious about being so close to her, though..."
    show m_cg1_base_exp1 at cgfade
    m "It seems like the mod is working nicely."
    m "I kind of get the idea of what it's about now."
    m "Thanks for doing this."
    menu:
        "Is it alright for you to say that so close to him?":
            m "Yes. Apparently, the mod makes it so that only you and I notice anything about this being a game."

    m "The script makes it so that all the other people ignore any speech about it."
    m "It's a bit hard to explain, so for now we'll leave it there."
    m "Apparently, the whole script was changed so that we could be together as much time as possible."
    m "So, as a result of that, I have some new memories."
    menu:
        "Memories? How does that work?":
            $ monika_explanation = 1
            m "You see,"
        "What kind of memories?":
            $ monika_explanation = 0
            m "Well,"

    if monika_explanation == 1:
        hide m_cg1_base_exp1
        m "The way I changed the others back then was by attempting to change the script."
        m "However, I'm just a character in this game."
        m "There's just so much that I could do with it."
        m "If you change the script, you change our world."
        m "For example, if you wrote into the script that we have been dating since two months ago,"
        m "I will have memories of spending these last two months with you."
        m "Back then, I was still tied to the script in one way or another."
        m "Right now, it seems to affect me a lot more."
        m "But don't worry, I haven't turned into a completly scripted character."
        m "I still have free will, and my memories of the time we spent together."
        show m_cg1_base_exp1 at cgfade
        m "Anyway,"

    m "Apparently this is set a few weeks after the school festival, in a different timeline where I did get a route."
    m "If I'm not mistaken, the spring break starts tomorrow."
    m "It seems like Sayori and the others are fine."
    m "Their problems are gone..."
    hide m_cg1_base_exp1
    m "Despite all that, it does feel a bit too sudden..."
    m "You know, seeing all their problems fixed out of nowhere..."
    m "But... If that means that you're happy, then it's alright."
    m "If you're wondering, the {i}[player]{/i} inside the game is pretty much {i}you{/i} for me."
    m "Your decisions will be his."
    m "His interactions, are yours."
    m "All the time I spend with this {i}you{/i} in the game will be just as if you and I were together."
    show m_cg1_base_exp1 at cgfade
    m "So don't worry."

    menu:
        "Ok!":
            m "Ahaha~"

    m "We should get ready to go to school."
    mc "Yeah. Sorry for oversleeping a bit."
    m "It's fine! The more time I get to be with you, the better~"
    mc "Y-Yeah..."
    m "Ahaha~!"
    m "You get flustered so easily~"
    scene bg bedroom
    with dissolve_scene_full
    stop music fadeout 2.0
    play music t8
    "Monika gets out of the bed, while I follow."
    "She enjoys teasing me all the time since I still don't know how to act around her."
    m "I will go change into my uniform now."
    m "Peeking is prohibited~"
    mc "I-I'm not a criminal!"
    mc "{i}...I have to admit that I'm a bit curious, though...{/i}"
    m "Oh? What was that?"
    mc "N-Nothing!"
    m "Ahaha~!"
    "Monika giggles and goes to the bathroom, with her uniform in hand."
    "How did she know what I was thinking, I'll never know. Maybe I spoke my thoughts out loud?"
    "I put mine on, and then go to the kitchen."

    scene bg kitchen
    with wipeleft_scene


    "Once there, I start to prepare our breakfast."
    "Usually, it's me the one who does the cooking."
    "Monika comes back, already dressed for school."
    show monika 5 zorder 2 at t11
    m "Oh? What are you cooking today?"
    mc "Some eggs with toasts and salad. I also made some coffee."
    m 2c "While I do appreciate the coffee..."
    m 4l " You do make some simple stuff all the time."
    mc "Well, sorry for not being a five star chef..."
    m "Ahaha..."
    m "Hmm..."
    m 3b "Here's what we'll do!"
    m 5 "I'll prepare the breakfast for the next three days."
    mc "Huh? Is my cooking really that bad?"
    mc "...Or more importantly, you know how to cook?"
    m 5b "Are you complaining about you girlfriend making food for you?"
    mc "N-No, it's just..."
    m "It's just?"
    mc "I've never seen you cooking."
    mc "You always eat stuff that you can buy from a store at school."
    m 4l "Haha, well, I never had the need to cook something."
    m 3b "I'm actually quite good at cooking, you know!"
    mc "Well, I guess it's never too late to learn something new about you."
    m 2j "It's never too late to learn something new about everything."
    m 3a "Knowledge can be a great weapon to face society head-on."
    m 3j "It's also the reason why humans are the dominant species!"
    mc "That analogy is a bit weird, but I guess I get what you're saying."
    show monika 5a at thide
    m 5a "Ahaha!"
    hide monika
    "Monika and I sit down and begin eating our breakfast."
    scene black
    with wipeleft_scene
    "After we're done, we go out of the house and make our way to the school."
    scene bg residential_day
    with wipeleft_scene
    "On our way to school, we encounter Sayori, who was waiting for us on the sidewalk."
    show sayori 1 zorder 2 at t11
    s 1q "Heeeey!!"
    s 1a "You guys were quite late today!"
    mc "It's more like you have been getting up earlier with each day, though."
    s "Ufufu!"
    s "You should be proud of me, [player]!"
    s "I've turned into a responsible person!"
    mc "Oh? Is that so?"
    mc "I guess I didn't get called by {i}someone{/i} pleading for me to do her math homework yesterday."
    s 5a "E-Ehehe..."
    s "You do know that math is very hard, right?"
    s 4p "Seeing all those numbers makes my head go all dizzy!"
    s "And then I begin to feel very hungry..."
    s "And after eating, I begin to feel very tired and sleepy!"
    mc "That doesn't mean that I have to do your work {i}all{/i} the time."
    mc "Besides, you're hungry all the time, so your excuse is pretty much invalid."
    s 5a "N-Nobody is perfect..."
    mc "Not a good excuse, again."
    s 4p "A-Anyway!"
    s "We should get going now!"
    show sayori 4p zorder 2 at t21
    show monika 1a zorder 2 at t22
    m 3j "She's right. We're going to be late at this rate."
    hide sayori
    hide monika
    "We all make our way to school."
    show monika 1a zorder 2 at t11
    stop music fadeout 2.0
    m 1d "..."
    menu:
        "What's wrong?":
            m "Oh, it's just..."
    play music t9
    m "Sayori..."
    m "Seeing her like this..."
    m "Even knowing how this is all caused by the mod, it still feels very sudden..."

    menu:
        "...Is it bothering you?":
            m 1n "...No..."

    m 1o "It's just..."
    m 1p "Looking back at it now, I wish I wouldn't have driven her to kill herself..."
    m "...It feels as if everything that I did before is simply forgotten now..."
    m "I can't help but feel uneasy."
    m "Like... I don't deserve all of this you're doing right now..."
    m "I..."
    m "...pretty much killed my friends..."
    m "...and forced you to be with me..."
    m "I've done so many horrible things..."
    m "And yet, you're trying to give me all this..."
    m "I don't understand why somebody would want me to enjoy all this..."

    menu:
        "Don't worry about it.":
            menu:
                "I'm here for you. If you ever feel uneasy, you can just talk to me.":
                    m 1i "[player]..."
        "It certainly is something unforgiveable.":
            menu:
                "You can't simply ignore something as serious as your actions.":
                    m 1p "I..."
                    menu:
                        "But, everyone deserves to be happy.":
                            menu:
                                "Even you.":
                                    m 1i "[player]..."
    m 1j "...Thank you..."
    m "Even if I don't deserve this, it's still something coming from you."
    m "The least I can do is enjoy it."
    m 1m "I wish I could hear your real words, without having to use these menus."
    m 1j "Maybe there's a mod for that?"
    m 5 "Ahaha~!"
    stop music fadeout 2.0
    scene bg corridor
    hide monika
    with wipeleft_scene
    play music t3
    "We reach the school and then go to each of our classes."
    show monika 1a zorder 2 at t11
    m 1a "I'll see you in the club after classes."
    mc "Alright. See you later."
    show monika 5 zorder 2 at t11
    "Monika smiles sweetly before going to her own class."
    hide monika
    "As for me, I go to my class while Sayori follows me."
    "Her classroom is close to mine, so we usually follow the same path."
    show sayori 1q zorder 2 at t11
    s "Ufufu~"
    mc "What?"
    s "You two have a great atmosphere going~"
    s 1a "I didn't expect Monika to want to date {i}you{/i}, [player]."
    mc "Well, we're two now."
    mc "Maybe she saw something in me that I can't see?"
    s "What is there to see?"
    s 1r "You're like the worst dating option there is!"
    s "Hahaha!"
    mc "Hey! Sayo-"
    hide sayori
    "Sayori runs away to her classroom before I can catch her."
    mc "Jeez..."
    mc "I'll scold her the next time I see her..."
    scene black
    with wipeleft_scene
    "I enter my own classroom and sit in my place while I wait for the teacher to come."
    scene bg class_day
    with wipeleft_scene
    "The day goes by as normal as it usually does, and classes end."
    "Unfortunately, today I'm on cleaning duty. So I stay a bit later than usual."
    "After I'm finally done, I pack my things and exit the classroom."
    scene bg corridor
    with wipeleft_scene
    "On my way to the club room, I find Monika waiting by the corridor."
    "It seems that she was waiting for me to come by."
    show monika 1j zorder 2 at t11
    m "[player]!"
    mc "Hey. Won't the others get mad at you for being late?"
    m 1a "Haha, there's no need to worry about that."
    m "I told you before."
    m 5 "The more time I spend with you, the better!"
    mc "R-Right..."
    mc "Let's get going then."
    mc "I can already imagine Natsuki's scolding."
    m "That's not a problem!"
    m "I can just {i}feed{/i} her some discipline you know?"
    menu:
        "...Did you just make that joke?":
            m 1j "Haha."

    m "I figured it's better to look at the bright side of things."
    m 1a "If I keep being depressed all the time, I won't be able to enjoy my time with you."
    m 1m "Of course, if you don't enjoy that kind of humor then I guess I'll simply drop it."

    menu:
        "No need to worry about it.":
            $ monika_humor = 1
            m 5 "You're so understanding~"
        "You should think a bit more about their feelings.":
            $ monika_humor = 0
            m 1a "Alright. No more bullying my friends."
            m 4l "That was quite a bad joke anyway."

    if monika_humor == 1:
        m "I'm not going to be hung up about it anymore!"

    if monika_humor == 0:
        m "I already caused too much trouble before."

    m 1j "I like to learn more about you."
    m 1a "These multiple choice options are a great way to do it."
    m "Anyway."
    m "We should get in the club room already."
    hide monika
    "Monika and I enter the club room."
    scene bg club_day
    with wipeleft_scene
    "Everyone is already here, as expected."
    "Yuri, as usual, has buried herself into her book."
    "Natsuki and Sayori are chatting on a corner."
    "As soon as the two of us enter, Natsuki turns to us."
    show natsuki 5g zorder 2 at t11

    n "You guys!"
    n "There's no need to say it, but you do realize that you're late, right?"

    show natsuki 5g zorder 2 at t22
    show monika 1m zorder 2 at t21

    m "Sorry for that."
    m "We spent way too much time chatting."

    n 5g "Ugh..."
    n 5w "Ever since you started dating [player], you became more carefree."
    n 5g "It's very annoying!"
    n "And then there's the whole 'Living together' thing!"
    n "Seriously, how do you go from 'Just started dating' to 'Living together' {i}that{/i} quick?"
    n "It's like something out of a manga!"
    n "It's just a matter of time until something happens!"
    n "You should realize that you're our club president and that you-"

    m 1a "Hmm..."

    "Monika has a slightly smug expression in her face."

    n 5i "What?"
    n "W-Why are you staring at me like that?"

    m 1a "It's just..."
    m 1j "Are you perhaps..."
    m "...jealous?"

    n 1p "W-W-What are you talking about?!"
    n "W-Why would I be jealous?!"

    m 1k "Ahaha! Well you know what they say."
    m 1a "Single people tend to feel jealous about those in relationships."
    m "There's no need to worry though."
    m "I'm not going to boast or shove it on everyone's faces."
    m 1j "I prefer to keep all the affection private."
    m "Besides, you're really cute!"
    m "I'm sure you will eventually find someone special!"
    n 5r "Agh..."
    show natsuki 5r zorder 2 at t33
    show monika 1j zorder 2 at t31
    show sayori 1q zorder 2 at t32
    s "Ufufu..."
    s "Natsuki is so cute when she's flustered!"
    n 1v "I told you all before!"
    n "I'm not cute!"
    hide monika
    hide sayori
    show natsuki 1r zorder 2 at t11
    "Natsuki turns toward me."

    n 1r "This is all {i}your{/i} fault!"
    mc "Huh? Why?"
    n "It's just..."
    n "Because..."
    n "You...!"
    n 1v "Ugh!!"

    "It seems that she can't find an answer for that."
    hide natsuki
    "Yuri, who had been reading her book until a moment ago, comes towards us all."
    show yuri 1a zorder 2 at t11
    y "Natsuki, you shouldn't bother them over the small details."
    y 1c "I'm sure Monika and [player] know how to be responsible about their relationship."
    y 1q "I have to admit that it caught us all by surprise, though..."
    y "I never expected Monika to want to date someone..."
    show yuri 1a zorder 2 at t21
    show natsuki 1r zorder 2 at t22
    n 1r "...What do you know?"
    n "Y-You're single too."
    y 1q "T-That may be true..."
    y 1f "B-But I doubt that Monika would let that drive her away from her responsibilites..."
    show yuri 1f zorder 2 at t31
    show natsuki 1r zorder 2 at t32
    show monika 1m zorder 1 at t33
    m "You worry too much about it."
    m "Besides, all I did was being late by a few minutes."
    show monika 1m zorder 1 at t33
    y 1f "She's right. I suggest we leave that behind now..."
    n 5w "Sigh..."
    n 1m "Fine. But atleast don't forget that you're our club president."
    n "We didn't get any new members after the school festival, but that doesn't mean that we can just forget about that."
    m 1j "Understood!"
    scene bg club_day
    hide monika
    hide natsuki
    hide yuri
    with wipeleft_scene
    "After our little exchange, everyone is back to their usual things."
    "Yuri is reading her book."
    "Natsuki is reading some manga."
    "Sayori and Monika are having quite a cheerful chat."
    "And I'm just resting on my desk."
    "We used to share poems before, but..."
    "After the school festival it became a bit repetitive, and we stopped doing it."
    "Nowadays, most of what we do is simply laze around or read books together while we wait for the next big event."
    "It does feel a bit nostalgic to think about the time when we used to share poems..."
    "Back then, I tried to make poems that would be interesting for Monika in hopes of getting her attention."
    "It surprised me a lot when she asked me out last week, though..."
    "Sayori suddenly screams."
    show sayori 1m zorder 2 at t22
    s "Waah!!"
    show monika 1d zorder 2 at t21
    m "What's wrong?"
    s "I almost forgot!!"
    mc "What?"
    s 1q "The spring break starts tomorrow!"
    mc "Oh."
    m 1a "Oh."
    hide sayori
    hide monika
    show natsuki 5k zorder 2 at t11
    n "I thought you had remembered something more relevant."
    hide natsuki
    show sayori 1q zorder 2 at t11
    s "Eehehe~!"
    s "I love vacations!"
    mc "Because you don't have to deal with school and can just laze around more than you usually do?"
    s 5a "A-Ahaha..."
    s 1a "But, but!!"
    s "Why aren't any of you excited?"
    s "Vacations mean freedom, you know!"
    show natsuki 5k zorder 2 at t21
    show sayori 1a zorder 2 at t22
    n "Well, it's not like there's much to do at my place."
    n "I'll probably just laze around and read some manga."
    hide sayori
    show yuri 1a zorder 2 at t22
    y "There are lots of books that I couldn't read due to the school's schedule."
    y 1c "This is usually an oportunity for me to pick them up."
    hide natsuki
    hide yuri
    show sayori 1a zorder 2 at t22
    show monika 1a zorder 2 at t21
    m "It looks like everyone has their own things to do."
    s "What about you, Monika?"
    hide sayori
    show monika 1d zorder 2 at t11
    m 1d "Me?"
    m "Well..."
    m 3l "I don't really have anything to do either..."
    mc "...Do you..."
    m 3d "Hm?"
    mc "...Do you want to go anywhere?"
    m 1d "Oh..."
    show monika 1d zorder 2 at t21
    show sayori 1m zorder 2 at t22
    s 1m "Woah! [player] is taking the initiative!"
    hide sayori
    hide monika
    show natsuki 5w at t11
    n "Didn't you say that you were going to keep it private?"
    mc "W-Well, it was Monika who said so..."
    n "That doesn't make it any less valid for you!"
    hide natsuki
    show yuri 4a at t11
    y "H-How bold..."
    mc "You too?!"
    hide yuri
    show monika 1d at t11
    mc "Sigh..."
    mc "Can you girls give me a break?"
    mc "We both don't have anything to do during the spring break."
    mc "So I thought that we could probably go somewhere."
    m "[player]..."
    m 1j "You don't have to ask."
    m 1a "Let's decide where we'll go tomorrow."
    mc "R-Right..."
    m 1j "Well, since that is settled, I guess it's time to go home."
    m "We may not see each other during the spring break, but I want you all to have fun!"
    show monika 1a at t21
    show sayori 1a at t22
    s "But I will probably see you two!"
    s "I live close to [player]'s place, remember?"
    m "Oh, that's right."
    m 1a "I almost forgot that."
    hide sayori
    show monika 1a at t11
    m "Anyway, we may not see Yuri and Natsuki then."
    hide monika
    show natsuki 1a at t21
    show yuri 1a at t22
    y "I still have to buy new books every once in a while."
    y "Maybe we can find each other there?"
    n 1d "I also have to get new manga from time to time. Don't count me out already."
    hide yuri
    hide natsuki
    show monika 1j at t11
    m "Well, I guess we may actually see each other if the chance comes!"
    m "Anyway, it's time to go home now."
    m "See you all!"
    hide monika
    show natsuki 1a at t21
    show yuri 1a at t22
    n "See ya."
    y 1a "Goodbye."
    hide natsuki
    hide yuri
    show monika 1a at t21
    show sayori 1a at t22
    m 1j "Well then, shall we go home?"
    s 1q "Yup!"
    mc "Yeah."
    scene bg residential_day
    hide monika
    hide sayori
    with wipeleft_scene
    "The three of us make our way home, just like the last four days."
    show sayori 1a at t11
    s "So, [player]!"
    s "Where will you two go tomorrow?"
    mc "Uhhh, I still don't know."
    mc "I'll probably look for some places online."
    s 1b "Huh...."
    s 1n "That reminds me!"
    s 4a "There's a new cafe that opened a few days ago in the city!"
    s "Many of my friends seem to like it and it's very popular!"
    s 1q "You should check it out."
    mc "Wow..."
    mc "It's weird for you to suddenly be helpful like this."
    mc "It's usually {i}me{/i} the one who has to help you all the time."
    mc "This feels... strange...."
    s 1o "W-What?"
    s 4w "That's mean, [player]!"
    s "After I tried to help you..."
    mc "Don't be dumb."
    mc "You probably just saved my life."
    mc "Thanks."
    s 2x "Ufufu~!"
    stop music fadeout 2.0
    "We reach Sayori's house after having our small chat."
    s 1q "Anyway, good luck on your date tomorrow!"
    s "Bye!"
    "Sayori enters her house and leaves Monika and me alone."
    hide sayori
    "There's still a bit of a distance before we reach my place."
    "So, we decide to take our time and walk slowly."
    show monika 1a at t11
    play music t9
    m 1j "Haaah~"
    m 5 "It's finally just the two of us again."
    mc "Yeah..."
    mc "Today was quite the day..."
    m "Yes..."
    m 1l "I didn't expect Natsuki to be {i}this{/i} annoyed about us."
    m 1a "Hey, {i}[player]{/i}."
    menu:
        "Yes?":
            m "I know that I have said it a lot, but..."

    m "Thank you."
    m "Even if this is an alternate timeline, seeing them happy like this..."
    m "...It makes me feel very happy."
    m 1o "...And guilty, too..."
    m 1l "Natsuki doesn't have problems with her father anymore."
    m "She still has problems making friends with others, but the literature club has become like a second home for her."
    m 1a "Seeing her happy while talking to either Sayori or Yuri..."
    m 1j "It's a great sight..."
    m 2j "She's now full of energy, be it talking about what she loves, or scolding us for small things."
    m 1m "And Yuri..."
    m 1m "She still cuts herself..."
    m "However, it's usually just small superficial cuts."
    m "They're so small that most don't really leave a mark."
    m 1l "Yuri is so shy and self-conscious that she believes that others will dislike her if they see those small cuts."
    m "This is why she constantly covers her arms."
    m "She still doesn't realize her own good points."
    m 1j "I'm sure no one would dislike her for that."
    m "And we already know about Sayori."
    m "Her depression is gone, and now she just oversleeps because she stays up really late."
    m "Sayori is as bright as she should have been from the beginning."
    m "Even for me, seeing her all happy and cheerful again just puts a smile on my face."
    m "..."
    m 1j "[player]..."
    m "I have come to realize that, this mod is not only about me."
    m "I know what I said before..."
    m "That they're just programmed personalities and all..."
    m "But..."
    m "They are still my friends, with whom I have spent most of my memories with."
    m 1m "To be honest, I wish that things would have been like this since the beginning."
    m "Even if I wasn't the one dating you, I wish that I had realized what I already had before doing those things."
    m 1a "I know that it wasn't you the one who wrote this mod."
    m "But I still want to thank you."
    m "For installing it. And for giving my friends the lives that they deserve."
    m "Even if this is an alternate timeline..."
    menu:
        "You're welcome!":
            m 5 "Ufufu~!"

    m "I'm glad that you were the one I fell in love with~"
    m 1j "Let's go home then."

    scene bg house
    hide monika
    with wipeleft_scene

    "Monika and I reach my house."
    "I open the door and let Monika enter first."

    scene bg livingRoom_lightsOn_TvOff
    with wipeleft_scene

    play music t6

    "Once inside, I let myself fall onto the couch to rest for a bit."
    show monika 1j at t11
    "Monika seems to be excited about something."
    mc "What's wrong?"
    m 1a "Hmmm~"
    m "Can you wait here for a bit?"
    mc "Uhhh... Ok?"
    m 5a "Ufufu~"
    "Monika goes upstairs, apparently going to my room."
    scene black
    with wipeleft_scene
    "A few minutes pass, and she finally comes back."
    scene bg livingRoom_lightsOn_TvOff
    with wipeleft_scene
    show monika o1_1j at t11
    m o1_1j "Tada~!"
    m o1_1a "This mod seems to give me new clothes!"
    m o1_1k "How do I look?"
    menu:
        "Amazing!":
            m o1_1j "You're so sweet, [player]!"
        "Great!":
            m o1_1j "Aww, thank you!"
        "Nice, but black seems a bit...":
            m "Thanks! I really don't have a problem with wearing black, though."
    m o1_1l "It's great that someone was kind enough to draw new clothes for me, besides the pajamas from today in the morning..."
    m "I did tell you that I was a bit tired of wearing my uniform all the time."
    m o1_1a "For now, these are the only casual clothes that I have right now."
    m o1_2l "I think the in-game reason for me not having many clothes was that I couldn't bring a lot with me when I moved here."
    m o1_1a "It's not a problem though."
    m o1_5a "Maybe we can go on a shopping date?"
    m o1_1a "Anyway, since the spring break starts tomorrow we don't have to worry about homework or anything."
    m "There isn't much to do right now."
    m "And there's still a bit of time until the night."
    m o1_2a "Is there anything you feel like doing right now?"
    m o1_1j "You know, to burn some time!"
    jump ch0_1
    return


    label ch0_1:
    menu:
        "I want to ask you something...":
            m o1_1a "Oh? What do you want to talk about?"
            jump askQuestions
        "Let's do some shopping.":

            m o1_1j "Oh, good idea! We can get something to make dinner with while we're at it!"
            m o1_1a "Give me a bit of time to get some things."

    scene black
    with wipeleft_scene

    "A few minutes pass and Monika comes back."

    scene bg livingRoom_lightsOn_TvOff
    with wipeleft_scene
    show monika o1_1j at t11
    m "All set!"
    m "Shall we go now, then?"
    mc "Yeah."

    scene black
    with wipeleft_scene

    "Monika and I leave the house and make our way to the convenience store."
    "The sun is already setting, and the nights are a bit cold here, so we make sure we quickly get to our destination."
    "After a while, we reach the store."

    scene bg shop_outside_dusk
    with wipeleft_scene

    mc "Damn. It sure is getting cold now..."
    show monika o1_1l at t11
    m o1_1l "Yeah. I certainly prefer warm weathers..."
    m o1_1a "But thinking about it..."
    m o1_1j "This makes the perfect cuddling weather!"
    mc "Y-Yes... I was thinking the same."
    "To be honest, I think about improving the skinship between us all the time."
    m "Ahaha!"
    m o1_1a "Let's hurry and enter the store."
    mc "Yeah."

    scene black
    with wipeleft_scene

    "Monika and I proceed to enter the store."

    scene bg shop_interior
    with wipeleft_scene

    shopclerk "Welcome!"
    "I tend to visit this place every once in a while."
    "However, this is my first time coming here with Monika."
    "Somehow, the atmosphere feels completly different."
    "Since it's almost night time, there's no one else other than us, and the shop clerk."
    "It makes me feel a bit anxious."
    "However, I calm myself and talk to Monika."

    show monika o1_1a at t11

    mc "So, is there anything in particular that you feel like eating for dinner?"
    m o1_1i "Hmm..."
    m o1_1a "I guess miso soup, rice and some salad would be fine for me."
    "I almost forgot for a moment."
    "Monika is vegetarian."
    "I rarely cook any meat since it's a bit expensive, so thanks to that I haven't had any problems preparing things for the two of us."
    "Monika says that she wants to help lower the carbon footprint in the planet, and since part of it is caused by the meat industry, she doesn't eat any meat."
    "I sort of get where she's coming from, so..."
    "For now I'll avoid buying any meat."
    mc "Yeah, that sounds good."
    mc "Let's go look for the ingredients, then."
    m o1_1j "Right behind you!"

    scene bg shop_interior
    with wipeleft_scene
    hide monika
    "We walk towards the ingredients section."
    mc "Hmm..."
    mc "Miso soup..."
    mc "..."
    mc "{i}...What is miso soup made with?...{/i}"
    "Again, my lame cooking skills make my life worse."
    show monika o1_1j at t11
    m o1_2j "You need Miso, Wakame, Enokitake, Dashi, and Tofu."
    mc "..."
    "...It seems that she wasn't lying when she said that she knows how to cook..."
    "Shamefully, I stare at the store items in silence for a few seconds."
    mc "I'm a failure as a boyfriend, haha..."
    m o1_1m "Ahaha..."
    m o1_1a "You don't need to worry about that!"
    m "Cooking, like any other skill, can be improved with practice and patience."
    m o1_1j "If you ever feel like you messed up, don't give up!"
    m o1_2k "Keep experimenting, and eventually you'll get better!"
    m o1_1a "Nobody is born being good at anything, after all."
    m o1_2j "...And that was Monika's Cooking Tip of the Day!"
    m "Ahaha~!"
    mc "A-Alright..."
    mc "Even so, I think that it's better if you pick the ingredients."
    mc "I don't want to try to show off in front of you and end up picking the wrong things."
    mc "Haha..."
    m o1_1a "Better safe than sorry, huh?"
    m o1_1j "It's fine, while I pick them, you can learn how it's made."
    mc "Alright!"
    hide monika
    "Monika walks around the store looking for the ingredients."
    "I tell her where each thing is, and then she hands them to me while she looks for the rest."

    show monika o1_1i at t11
    m "Wakame... Wakame..."
    mc "Oh, it's over here."
    m o1_1j "Thanks!"
    hide monika
    "Eventually, we find all the necessary things."
    "We then proceed to go and pay for everything."

    scene bg shop_interior
    with wipeleft_scene

    shopclerk "Thanks for your purchase!"
    "After having put everything in bags, Monika and I exit the store."
    show monika o1_1j at t11
    m "Alright. Let's go back."
    mc "Yeah."

    scene bg shop_outside_dusk
    with wipeleft_scene

    "As soon as we step outside, I feel a big chill running through my entire body."
    mc "Crap. It's gotten really cold now."
    show monika o1_1m at t11
    m "Yes. We should go back quickly."
    m "We might end up catching colds at this rate."
    mc "Oh, yeah. Give me the bags."
    mc "The rice bags are quite heavy, and with your dress it probably feels a lot colder."
    m o1_1j "Oh, you're quite a gentleman~"
    "Monika hands me the rest of the bags."
    "It's a bit heavy, but it's my duty as a boyfriend to have Monika enjoy herself."
    m o1_1a "Alright. Let's go back to the house."
    m o1_1j "I can't wait to feel warm again!"
    mc "Same here."
    scene black
    with wipeleft_scene
    hide monika
    "We both walk back to my house."
    "As we approach it, the temperature lowers a bit more, and the sun finally sets down."
    "Monika and I quickly enter the house."
    scene bg kitchen
    with wipeleft_scene
    show monika o1_1j at t11
    m "Haaah~"
    m "This is certainly better!"
    m o1_2k "Warm temperatures sure feel nice when it's cold outside!"
    mc "I second that."
    mc "Shall we start preparing the dinner?"
    m o1_1a "Yes!"
    scene black
    with wipeleft_scene
    hide monika
    "I put the bags in the kitchen and we start getting the ingredients out."
    "Monika and I decided that she would be the one preparing the soup, while I deal with the rice and the salad."
    "The fact that I'm doing the easy stuff bugs me out a bit."
    scene bg kitchen
    with wipeleft_scene
    show monika o1_1h at t11
    "While doing my part of the food, I glance to what Monika is doing."
    "She has a pretty focused expression on her face."
    "She almost looks like a professional."
    "I can't help but wonder."
    "How did such a girl like her decide to date someone like me?"
    "...Me, a guy completly lame compared to her."
    "Maybe she did see something that I can't?"
    scene black
    hide monika
    with wipeleft_scene
    "We both finish preparing our portions of the food, and then we start serving ourselves."
    "We then put everything in the table, and sit down."
    "Monika sits beside me."
    scene bg kitchen
    with wipeleft_scene
    show monika o1_1a at t11
    "Monika looks at me with expectant eyes."
    "It seems like she wants to see my reaction to her food."
    m o1_2j "Oh, don't mind me! Go ahead~"
    hide monika
    "This is the first time that I eat Monika's cooking."
    "I'm a bit excited about it."
    "I finally taste the miso soup."
    mc "..."
    "It takes me a while to make up my words."
    "I sit there, staring blankly for a couple of seconds."
    "...This soup..."
    "{i}..is incredibly good!{/i}"
    "At first glance, it looks like a normal miso soup."
    "But each ingredient perfectly harmonizes with the others, creating a perfect balance."
    show monika o1_1j at t11
    m "So..."
    m "How is it?"
    mc "..."
    mc "How do you make a miso soup this good?"
    mc "Did you use some kind of sorcery?"
    m "Ahaha!"
    m o1_1a "It's a normal soup, actually."
    mc "...What?"
    m "It seems that you don't believe me."
    m "You know,"
    m o1_1a "They say that food tastes better if it's made with love."
    m o1_2j "...And it tastes even better if it's made by the person that you love!"
    mc "..."
    mc "I guess I can't argue with that..."
    m o1_5a "Ufufu~"
    m o1_5a "The rice and salad also taste really good!"
    m o1_1j "Maybe {i}you{/i} used some kind of sorcery?"
    mc "...I'm not on that level yet, haha."
    stop music fadeout 2.0
    scene black
    hide monika
    with wipeleft_scene
    "We finish eating our food, and start cleaning the leftovers."
    "We begin by washing the dishes."
    scene bg kitchen
    with wipeleft_scene
    show monika o1_1j at t11
    m o1_1a "You know, {i}[player]{/i}..."
    menu:
        "Yes?":
            play music t10
            m "This is the kind of life I've always wanted."
            m "Having a peaceful life, enjoying time with the one I love..."
            m o1_1j "It's like a dream come true!"
            menu:
                "I'm glad that you're enjoying this.":
                    m "As long as I'm with you, I will always enjoy everything."
                    m o1_1a "However, I also want you to enjoy this."
                    m o1_1j "So, make sure to be happy!"
                    m "For the both of us."
                "I wish I could be there, with you.":
                    m o1_1j "Even if we're not in the same reality, we can still enjoy these moments."
                    m "Don't be sad about something that you can't experience yet."
                    m o1_2j "Be happy about what you {i}can{/i} experience right now, and what might come in the future."
                "Maybe, someday we both will be able to enjoy this together?":
                    m "Yes! At the rate that technology is evolving, maybe we'll be able to hold hands together in a few years."
                    m o1_2a "I mean, people are already experimenting with Virtual reality, and Quantum computers are already being developed!"
                    m o1_1j "It isn't unrealistic to hope for that kind of future."
                    m "Please, don't forget about me until then!"

    m "...Anyway."
    m o1_1a "It's night time already."
    m o1_2a "We could go to sleep, or just watch some TV."
    m "What do you want to do, {i}[player]?{/i}"
    menu:
        "Let's watch TV":




            m o1_1j "Ok!"
            m "Just give a minute to change into my pajamas~"
            jump tvEvent
    return

    label tvEvent:

    scene black
    hide monika
    with wipeleft_scene
    $ asked_talk = False
    "Monika goes upstairs, to my room, once more."
    "Meanwhile, I sit on the couch and turn on the TV."
    mc "This makes me think..."
    mc "What could Monika possibly enjoy watching?"
    mc "She normally spends her time reading..."
    mc "I can probably find a movie that she will find interesting."
    "Monika comes back, with her pajamas on."
    scene bg livingRoom_lightsOn_TvOn
    with wipeleft_scene
    show monika p_5a at t11
    m p_5a "Here I am!"
    "Monika sits next to me."
    m p_1a "Hey, {i}[player]{/i}."
    menu:
        "Hm?":
            m p_2j "Let's turn off the lights!"
            m "It'll feel more like a date that way."
            menu:
                "Alright!":
                    "I get up and turn the lights off."

    scene bg livingRoom_lightsOff
    with dissolve_scene_full
    "Suddenly, the TV is the only thing lighting the whole room."
    "I go back to the couch."
    "Monika has relaxed herself a bit, having put her legs on the couch."
    "I sit next to her."
    "Monika is already watching the TV, with the anime that I had left it at a few moments ago."
    scene black
    hide monika
    with wipeleft_scene
    "The anime is about a group of girls who turn into 'school idols' to save their school from closing down."
    "Apparently, it's very popular."
    "There's lots of merchandise and advertisements about it in Akihabara."
    "It's a rather easy show to get into if you don't watch too much anime."
    "Monika is watching the TV with a rather 'interested' expression."
    m "..."
    m "I never thought that an anime could be this interesting."
    m "I'm always more into reading."
    m "Ahaha."
    scene m_cg_tvEvent
    with Dissolve(2.0)
    m "This show seems like a lot of fun."
    m "What's with this character and that 'Bu Buu'?"
    m "It'd be weird to hear someone say that in real life!"
    m "Ahaha!"
    mc "Haha."
    mc "You could say that it's her trademark feature."
    mc "If I'm not mistaken, this episode has a quite nice insert song."
    mc "Just wait a bit."
    m "Oh? Let's see then."
    scene black
    hide monika
    with wipeleft_scene
    "A few minutes go by."
    "Eventually, the insert song comes up."
    scene m_cg_tvEvent
    with Dissolve(2.0)
    "TV" "{i}~Dance, dance, to find a passion~{/i}"
    "TV" "{i}~We were probably born for this very purpose~{/i}"
    m "Oh! It's starting!"
    "I really liked this song, so it'll be interesting to see Monika's reaction to it."
    m "..."
    m "It surprises me just how well this song is made."
    m "The rhymes combine nicely into such different tempos."
    m "It must have been a lot of work for the composers."
    m "And the combination between traditional japanese music and modern rock is amazing."
    m "It's such a beautiful harmony."
    m "I never knew how much creative effort goes into making this kind of things."
    "Seeing Monika make these comments..."
    "It reminds me that she actually knows a bit of music."
    "She used to practice piano, and still does."
    "Apparently, she was composing her own song, but she never showed it to us."
    mc "Yeah. I like this song a lot."
    mc "Back when this episode was first released, a lot of people went crazy for it."
    m "I can see why."
    m "..."
    m "Hey {i}[player]{/i}."
    menu:
        "Yes?":
            m "Have you seen this show before?"
            menu:
                "Yeah.":
                    m "That's quite a coincidence!"
                    m "It feels like I'm watching it with you here next to me now~!"
                "Nope.":
                    m "Oh. Well it's nothing weird."
                    m "There's lots of anime coming out each season, from what I know."
                    m "I guess it's a bit difficult to follow each of them, haha."
                    m "Do you watch anime too?"
                    menu:
                        "Yes.":
                            m "It's nice to know something new about you!"
                            m "After watching this, I came to realize how entertaining it can be."
                            m "I wish we could watch the shows that you like someday!"
                        "No.":
                            m "Oh, I guess we're two then!"
                            m "It's a bit weird for you to be playing this game, and also playing this mod when you don't watch anime."
                            m "Ahaha."
                            m "However, I recommend not to judge a book by it's cover."
                            m "There are probably tons of great shows out there."

    m "...Still."
    m "This reminds me."
    m "I told you once that I would love to spend a night on the couch together like this..."
    m "It sure is like a dream come true!"
    m "I wish that this moment would last forever..."
    m "But..."
    m "We still have lots of things that we can do, don't we?"
    m "We got a whole week to spend our time together!"
    m "Let's make sure to go to lots of places, okay?"
    menu:
        "Roger that!":
            m "Ahaha~"

    m "Again, I'm glad that I fell in love with you..."
    m "..."
    m "Oh! There's another insert song at the end of the episode?"
    m "They sure put in a lot of effort for this show!"
    mc "Haha, yeah."
    mc "These kinds of shows tend to have a lot of music."
    m "Heeeh..."
    m "Seems like my kind of show, doesn't it?"
    m "Ahaha~"
    scene black
    with Dissolve(1.5)
    "Monika and I stayed up late watching TV."
    "It's already 11 PM, and Monika looks a bit tired."
    scene bg livingRoom_lightsOff
    with dissolve_scene_full
    show monika p_1m at t11
    m p_1m "It's quite late already."
    m p_1l "We should go to bed..."
    m p_2l "I didn't expect that these animes would be so entertaining."
    m p_1a "They way that they make you care about characters is amazing."
    m "I guess it's something special about japanese media, if you compare it to stuff like western shows..."
    m p_1j "Ahaha..."
    mc "Haha."
    mc "But the important part is that you enjoyed it too."
    m p_1j "Yes."
    m "Finding something that we both enjoy feels really nice."
    m "We should try out more stuff together like this."
    mc "If you're fine with it..."
    mc "Anyway, I'm starting to feel tired too."
    mc "That was enough anime for today, haha."
    "I never expected Monika to find anime this interesting."
    "She told me that she preferred reading over watching anime a few times."
    "But..."
    "It does make me happy."
    "The more we find things that we both enjoy together, the more my affection for her grows."
    "...But there's no way that I can say that out loud."
    "In the end, I'm still quite awkward about all this."
    "It's my first time in a relationship, after all."
    "...And the one I'm dating is Monika, our school's idol..."
    scene black
    hide monika
    with Dissolve(1.5)
    "We both go to my, or should I say, {i}our{/i} room."
    scene bg bedroom_night
    with Dissolve(1.5)
    "Monika takes off her ribbon, while I get into the bed."
    "She then gets into the bed too."
    "My bed is big enough for two people, so generally I sleep on the right side, and avoid any movements that could bother Monika."
    "I'm still not completly used to this, but..."
    "...It still feels really nice..."
    "If anyone at school, outside from the literature club, knew about this..."
    "...I don' think I'd make it out alive..."
    scene black
    with Dissolve(1.5)
    m "...[player]?"
    mc "...Hm?"
    "I look over to Monika."
    "She's looking at my face."
    "Our faces are quite close like this."
    m "...Good night!"
    "Monika says that with a sweet smile."
    "It makes my heart skip a beat."
    "I try my best, and show an awkward and embarrased smile."
    mc "{i}...Good night...{/i}"
    "Monika smiles a little bit more."
    m "Ufufu~"
    "She then turns around to the direction opposite of me."
    "I calm myself, and then turn to my direction."
    "..."
    "Some minutes pass."
    "I begin to feel more and more tired."
    "Eventually,"
    "We both fall asleep."
    window hide
    stop music fadeout 4.0
    pause 5.0
    jump ch0_end
    return

    label ch0_end:
    scene black
    show dayText_sunday zorder 50
    with Dissolve(1.5)
    pause 5.0
    scene black
    with Dissolve(1.5)
    pause 4.0
    jump ch1
    return


    label askQuestions:
    $ asked_talk = False
    menu:
        "What's it like to talk to me?" if not asked_talk:
            m o1_1a "Well, it's quite easy to explain, actually."
            m "Whenever I talk to {i}you{/i}, it's like you take control of the [player] in front of me right now."
            m "Whatever you choose in the menus, is what this [player] will say to me, with his own voice."
            m "It probably isn't shown in the script, but that is how it is for me in this world."
            m o1_1j "It's like I'm talking to you!"
            $ asked_talk = True
            jump askQuestions
        "Why are we living together?":

            m o1_2l "I knew you were going to ask this, ahaha..."
            m o1_1l "It probably isn't going to be all that relevant, but well..."
            m o1_1a "You know, school festivals are also a time where parents can go to their children's schools and see how they're doing."
            m "During the festival, both my and [player]'s moms came to see how we were doing."
            m o1_2l "Apparently, Sayori told [player]'s mom about our club, and she was quite surprised about it."
            m o1_1m "It also surprised me to see my mom there, ahaha..."
            m o1_1a "But anyway."
            m o1_2a "The two of them went to see our performances."
            m o1_1a "After that, they stayed there chatting for a while."
            m o1_2l "[player] was really annoyed at his mom for staying there."
            m o1_1l "It probably was embarrasing for him to have her see his performance..."
            m o1_1a "I made them both leave the classroom, so that the other students wouldn't feel uncomfortable."
            m o1_1a "It seems that they kept talking for a while when they were checking the rest of the festival."
            m o1_1l "So, long story short, both our moms became really good friends."
            m o1_1a "A few days after the festival, my parents and I went to [player]'s house since his mom invited us to eat dinner."
            m o1_2l "Both of our fathers also became really good friends during that time."
            m "They kept talking about work, sports, and many things that they had in common."
            m o1_1a "Meanwhile, [player] and I were talking somewhere else."
            m o1_1m "Then, our parents went to see what we were doing."
            m o1_2l "It seems that they got the wrong idea back then, and they thought that we were dating!"
            m o1_1l "[player] tried to explain it to them, but his father kept congratulating him, while my parents kept saying 'How good of a choice' I had made."
            m o1_1a "Anyway."
            m "Some weeks after that, [player] and I started dating."
            m o1_1l "And a few days ago, my parents and [player]'s went overseas thanks to an invitation from [player]'s parents part."
            m o1_1a "It seems that before leaving, they had some sort of plan which consisted of having him and I living together for some time."
            m o1_1l "I'm still not sure what they wanted to achieve with that, but here we are now!"
            m o1_5a "To be honest, I'm fine with this."
            m o1_1a "You may think that this is a bit cliché and weird, but as I said before, the mod modified the script in such a way that we could be together as much time as possible."
            m o1_1j "Even with a backstory like this, I'm happy to be able to spend more time with you!"
            jump askQuestions
        "Where do you think we should go tomorrow?":

            m o1_1a "Hmmm..."
            m o1_1j "Sayori's suggestion seemed quite nice!"
            m o1_1a "Before the mod, there weren't many places to visit here."
            m "Going to a café with you sounds really nice~"
            jump askQuestions
        "Nothing else":
            m o1_1j "Alright!"
            jump ch0_1

    scene white
    with Dissolve(1.0)

    return
