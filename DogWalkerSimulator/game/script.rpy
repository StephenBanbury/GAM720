
init:

    $ config.screen_width = 1280
    $ config.screen_height = 720
    $ config.window_title = "Dog Walker Simulator"

    define c = Character("Crystal")
    define r = Character("Rusty")
    define t = Character("Trixie")
    define d = Character("Duck")
    define dw = Character("Dog Warden")

label start:

    $ rusty = True
    $ trixie = True

    $ rusty_first = True
    $ crystal_in_trouble = False
    $ energy = 100

    $ renpy.clear_game_runtime()

    $ renpy.music_start('/audio/movement.wav')

    scene bg park 1280

    show crystal happy 720 with dissolve
    show rusty 1 at left with dissolve
    show trixie 1 at right with dissolve

    "Crystal is a dog walker by profession."
    "Today, she is out on one of her excursions. She has two dogs - Rusty and Trixie - each on a leash."
    c "What a lovely day. Come on fellas.. it's time for walkies!"
    "Crystal and the very contented dogs happily make their way along the pathway next to the road and towards the park gate"
    "As they begin to turn off the pavement alongside a busy road, a passing fire engine suddenly and unexpectedly turns on its very loud and extremely piercing siren!!"

    hide crystal happy 720
    hide rusty 1
    hide trixie 1

    show fire engine with zoomin
    show crystal surprised 720  with dissolve
    show rusty 1 at left with dissolve
    show trixie 1 at right with dissolve

    "Startled, the dogs yank their leashes from Crystal's grasp and scatter into the park in all directions!"
    r "Woof woof woof!"
    t "Bark bark bark!"
    "Momentarily, Crystal is shocked and stands aghast, watching as the frightened dogs disappear from view."
    c "Oh My God! Which dog should I go after first?!!"

    menu:
        "Rusty":
            $ rusty_first = True
            jump find_rusty

        "Trixie":
            $ rusty_first = False
            jump find_trixie

label find_rusty:

    if rusty_first == True:
        c "Here I come Rusty - I'll save you!"

    scene bg park hedge 3

    show rusty 1 at left with dissolve

    "Rusty had got over the shock of the fire engine and was happily going about his doggy business"

    r "Hmm what's this? A nice thick hedge. I like hedges! And it's got a hole in it.. looks like fun to explore!"
    r "What's that? Did I hear Crystal calling me? Perhaps I should go back and find her"
    r "Then again.. this hole in a hedge looks very inviting! What should I do?"

    menu:
        "Hole in the hedge":
            jump hedge_hole

        "Go back to find Crystal":
            jump find_crystal

label hedge_hole:

    r "Hedge Hole... here I come!"
    "He squeezed through to the other side and took a good look around."

    scene bg dog warden with fade

    "Rusty hadn't realised that there was dog warden from the local dog pound on the other side of the hedge!"
    dw "Aha! Come here you varmint!"

    show cartoon dog warden

    "The dog warden's net scooped up Rusty and bundled him into a van"
    dw "It's the dog pound for you, pooch!"

    $ rusty = False

    if rusty_first == True:
        jump find_trixie
    else:
        if energy >= 80:
            c "C'mon Trixie - follow that van!"
            "They ran after the van and just about caught it before it got up to a decent speed."
            c "Hey.. that's my dog!"
            "After explaining what had happened, the dog warden let Rusty free."
            $ rusty = True
            $ energy-=25
        else:
            "After their ordeal at the river, Crystal and Trixie did not have enough energy to give chase."

        jump the_end

label find_crystal:

    r "Woof!"
    "With a wag of the tail, Rusty went tearing back to find Crystal"
    c "Rusty!! I'm so happy to have found you! You good dog!"

    if trixie == True and rusty_first == True:
        c "Let's go and find Trixie."
        jump find_trixie
    else:
        jump the_end

label find_trixie:

    if rusty != True:
        "Crystal saw the dog warden's van disappearing down the road and heard the sound of Rusty, barking for all he was worth."
        "She ran for nearly a minute trying to catch the van, but eventually gave up the chase."
        "Refusing to panic, she continued the search for Trixie. She'd go and get Rusty from the dog pound later.."
        $ energy-=25

    c "Hang in there Trixie.. I'm just behind you!"

    scene bg river still with fade

    show trixie 1 at right with dissolve

    "Trixie was still a little bewildered. But then, she noticed a duck bobbing around on a brook."
    d "Quack quack!"
    "Unable to resist the temptation, Trixie charged down the bank towards the edge of the river"
    c "Trixie, STOP!"
    "Trixie heard a very distant but familiar sound.. but it was not enough to stop her leaping from the bank into the river."
    "Crystal heard the splash and ran to the river's edge, only to see panicking Trixie disappearing under the water! What should she do?"

    menu:
        "Jump in after Trixie":
            jump jump_in

        "Grab a stick and hold it out for Trixie to hold onto":
            jump hold_out_stick

label jump_in:

    "Glug glug.. help.. glug glug.. oh dear. It's not going well here folks. Neither Crystal nor Trixie are strong swimmers!"

    $ crystal_in_trouble = True
    $ energy-=25

    if rusty_first == False:
        "Both Trixie and Crystal managed to get to the water's edge and scramble up the bank."
        "Exhausted, they took a few deep breaths.."
        c "Okay, Trixie, summon up your energy.. let's go and find Rusty before it's too late"

        jump find_rusty
    else:
        jump the_end

label hold_out_stick:

    "Trixie grabbed the stick with her strong jaws and held on for dear life!"
    t "Whimper whimper.."
    c "Hold on Trixie, I've got you"

    if rusty_first == False:
        "Good girl, Trixie! Great team-work!"
        c "Now let's go and find Rusty"

        jump find_rusty
    else:
        jump the_end

label the_end:

    if crystal_in_trouble == True and rusty_first == True:
        "Later that afternoon, two very bedraggled and dazed figures came back to consciousness on the banks of the river."
        "The local news was full of the story the next day"
        if rusty != True:
            show crystal sad 720 at left with zoomin
            hide rusty 1
            show trixie 1 at right with dissolve
            ".. although it was pretty awkward having to bail Rusty from the dog pound and explain it to his owners!"
        else:
            show crystal happy 720 with zoomin
            show rusty 1 at left with dissolve
            show trixie 1 at right with dissolve
            "Rusty, like his hero, Lassie, had gone and fetched help."
            "Crystal was hailed a hero, doubly so as she had managed to save two dogs in a single day!"
    elif rusty == True and trixie == True:
        if rusty_first == True:
            "Crystal pulls Trixie out of the water. She and the two dogs collapse in a happy heap at the side of the river"
            c "Thank God, both of you are safe... and best of all, no-one need know about it!"
            show rusty 1 at left with dissolve
            show trixie 1 at right with dissolve
            show crystal happy 720 with zoomin
        else:
            scene bg park hedge 3 with fade
            show crystal happy 720 with zoomin
            show rusty 1 at left with dissolve
            show trixie 1 at right with dissolve
            "Crystal and the two dogs jump around with joy!"
            "What a day! C'mon fellas, let's go and get an ice cream!"
    else:
        show crystal sad 720 at left with zoomin
        show trixie 1 at right with dissolve
        c "Right.. c'mon Trixie. To the dog pound to get Rusty."
        c "This is going to be awkward!"

    scene black with fade

# This ends the game.

    return
