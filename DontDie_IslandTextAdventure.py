while True:
    answer = input("Would you like to play? (yes/no) ")

    if answer.lower().strip() == "yes":

        print("You awaken high upon a mountain top after your private flight crashed." 
        + "Most of the crew and passengers seem to have either parachuted before the crash or are otherwise not around the crash site."
        + "You are currently trying to make your way down the mountain to look for a way off the island or a way to get help. ")
        answer = input("You reach a crossroads, would you like to go left or right? (left / right)").lower().strip()
        if answer == "left":
            answer = input("You encounter a goblin, would you like to run or attack? (run / attack)").lower().strip()
            if answer == "run" or answer == "flee" or answer == "escape":
                print("You make a rush around the goblin down the left hand path. "
                + "The goblin gives chase calling you a coward to your back. He quickly gives up as the distance widens. ")

                answer = input("You see a boat moored by a river leading towards a tumultous series of rapids. "
                + "Further down the path is a donkey tied to a post. "
                + "How do you intend to travel? (boat / donkey / walk)").lower().strip()

                if answer == "boat" or answer == "river" or answer == "water":
                    print("You paddle your way into the middle of the river, gently navigating the rapids, falls and rocks before the current takes your boat and smashes it on the rocks at the bottom of a tall waterfall. "
                    + "You briefly glimpse a hut by the water before darkness takes you. "
                    + "You died! ")

                elif answer == "donkey" or answer == "mount" or answer == "mount donkey":
                    print("You approach the donkey from behind to jump on it's back. It's ears quiver once before it bucks and kicks you in the neck. You land with a thud beside a bag of carrots.")

                elif answer == "walk" or answer == "foot" or answer == "on foot":
                    answer = input("You walk further down the path, sloping downhill at a leisurely pace and arriving at late day by a hut near dense forest and a steep cliff drop. "
                    + "Outside the hut you can see an axe, a rope, and a soda. Inside the hut you can see a radio."
                    + "What would you like to investigate? (axe / radio / rope / soda)").lower().strip()

                    if answer == "axe":
                        print ("You pick up the axe but before you can do anything else the owner of the hut returns, shooting two shotgun shells through your chest to take out the threat at his abode. "
                        + "You died!")

                    elif answer == "radio":
                        print ("You enter the house and change around on the frequencies until you hear a voice. "
                        + "You've just about managed to get a clear signal and call for help before a shotgun blast slams you to the wall."
                        + "You hear a voice call you a thief and a home invader before you drift into darkness.."
                        + "You died!")

                    elif answer == "rope":
                        answer = input("Upon picking up the rope you hear a voice shout 'something I can help you with?'"
                        + " as a man in hunting gear holding a shotgun approaches you. "
                        + " What do you want to do? (attack / climb / forest / radio )").lower().strip()

                        if answer == "attack":
                            print("As soon as you begin running towards the hunter he levels his gun and blows two shotgun cartridges into your chest." 
                            + "You died!")

                        elif answer == "axe":
                            print("Ignoring the hunter, you pick up the axe, take his soda and march straight into the woods."
                            + "As a bear rushes you, you take one swing of the axe downwards, crushing its skull. "
                            + "You make a cloak out of the bear and make yourself content to live out your days hunting and gathering on the island."
                            + "You survive!")
                            break

                        elif answer == "climb":
                            print("You tell the hunter you intend to climb down the cliff."
                            + "He ties some knots and loops in the rope for you and helps you set up a secure line down the cliff."
                            + "After an hour or so, you reach the bottom and easily traverse your way out to the beach."
                            + "As the sun gets close to dipping over the horizon, you catch sight of a small fishing boat passing the island and manage to wave down the captain. "
                            + "The captain feeds you medicinal brandy and salmon on the journey back to the mainland."
                            + "You escaped the island, you win!")

                        elif answer == "forest":
                            print("You tell the hunter you intend to pass through the forest to get to the coast."
                            + "He seems to little unsure but tells you to be careful."
                            + "Shortly after entering the woods, a bear rushes you and defenseless you get mauled before being dragged back to its den and eaten."
                            + "You died!")

                        elif answer == "radio":
                            print("You explain how you got here and ask to radio for help."
                            + "The hunter radioes in to a nearby captain and requests he take you as a passenger."
                            + "After arriving on the beach, you meet the captain and the hunter sees you off."
                            + "You get safely back to mainland and manage to escape the island."
                            + "You win! ^_^ ")
                            break

                        else: 
                            print("Whaaat? You died!")

                    elif answer == "soda":
                        print("You crack open the soda and take a seat - enjoying the crisp sweet and sourness in the evening sun."
                        + "A man approaches you in hunting gear, sees you enjoying yourself and cracks open a soda in kind."
                        + "He listens to your story and radioes in for a nearby boat to come within the week."
                        + "Although your ears are burnt off from listening to stories from the islands hermit, you escape the island essentially unharmed."
                        "You win! ^_^ ")
                        break


                elif answer == "feed donkey" or answer == "give carrot" or answer == "give a carrot" or answer == "pet donkey" or answer == "pet the donkey":
                    print("You find a bag of carrots and feed some to the donkey, petting it on the head. " 
                    + "It's demeanor softens and it's ears stop flicking. " 
                    + "You untie the donkey from the tree and mount it before continuing down the path."
                    + "With the sun still high in the sky, you arrive at a hut. "
                    + "Outside sits a man making stew. He looks perplexed and exclaims 'I thought I put her in the shade, whoopsy!' as you approach"
                    + "He gives you some stew and a straw hat before guiding you down to the beach. " 
                    + "A cruise liner takes you on a paid expenses tour around the island chain before dropping you back on the mainland."
                    + "You win!!  ^_^  ")
                    break

                else:
                    print("A poor decision presumably, I don't know what you were trying to do.. You die!")

            elif answer == "attack" or answer == "punch":
                print("You leave out a roar before punching the goblin in the face. " 
                + "It grunts once before stabbing you in the leg with a poison dagger and walking away. "
                + "You die!")

            elif answer == "talk" or answer == "negotiate" or answer == "haggle":
                print ("The goblin talks at length about how their kind have been misjudged and they're a decent sort. He then proceeds to betray you at the first opportunity, garroting you as you sleep. You died!")

            else:
                print("Why would you do that? Your choice, or lack of caused you to die!")

        elif answer == "right":
            print("You walk aimlessly to the the right and fall on a patch of ice. " 
            + "You injure your leg and cannot continue. Game over!")

        else: 
            print("Invalid choice, you lose! ")

    else:
        print("Oh well! That's a pity..  >:D ")
        break
