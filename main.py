print('This is Project Orange')
print('This is a game that is strictly text based')
v = input('What is your name?')
print(f'Your name is {v}?')
print(f'Nice to meet you, {v}!')
print('Your jouney is about to start.')
print('You wake up in a strange place, it looks like a hospital room.')
print('You look around and find yourself straped to a bed')
print('You strugle to loosen the bindings, but it didnt work.')
print('You hear a sound on the other side of the door.\n The doorknob starts to turn, then a person that looks like a doctor walks in.\n He has dark hair, fair skin, tall, dark blue eyes, and a big smile.')
print(f'Strange Doctor: Good morning {v}, How are you feeling today?')
y = input("fine, where am I, Who are you and How did I get here(choose one)")

if y.upper() == "FINE":
  print("That is good to hear. Oh where are my manners, my name is Dr.Snow")
elif y.upper() == "WHERE AM I":
  print("I can't tell you that. Oh where are my manners, my name is Dr.Snow")
elif y.upper() == "WHO ARE YOU":
  print("My name is Dr.Snow.")
elif y.upper() == "HOW DID I GET HERE":
  print("You were picked up by some of our operatives. Oh where are my manners, my name is Dr.Snow")
print("Dr.Snow: You are probably wondering why you are here.")
print("Dr.Snow: You were selected for this project...")
print("You(thinking): Project? What is this place, better keep listening.")
print("Dr.Snow: ... because of your blood and the way your brain works.")
print("You: My blood? My brain? This isn't making any sense, whats so special about me?")
print(f"Dr.Snow: I am glad you asked {v}, the reason you are so special is because you have ancient secerets locked away inside your genome, but I wont tell you what the are just yet.")
print("You(thinking): My genome, what are they going to do to me?\n Dr.Snow: Well I have to get ready for surgery, you have to get ready as well, it is your surgery after all.\n Dr.Snow starts to leave, but before he does he says one more thing.\n Dr.Snow: See you on the other side! Or not, we will see how it goes.\n Before you could say anything, he shut the door, an eerie silence flows into the room.\n You: 'Or not' What did he mean by that? I got to get out of here.")
print("you look around, and see a scalple on the table beside you.\n You take a look at your restraints, it seems that the are just zip ties.\n You try grab the scalple with your mouth, your close, but not close enough.\n You notice some of the bar you are strapped to is jagged, so you start to saw one of the zip ties off.\n Once you managed to get it off you grab the scalple and cut the rest off of you.\n You run to the door, check if anyone is outside, and exit.")
print("There are two ways to continue, which way will you go?")
y = input("Right or Left")
if y.upper() == "RIGHT":
  print("You decided to go right.")
elif y.upper() == "LEFT":
  print("You decided to go left.")
print("As you go down the hall you start to notice a sound,it was quiet at first, hardly noticable, but it steadilly got louder.\n You try to identify the sound, it is coming from the other side of a wall, you look around and find a window to your right.\n You peer through the window, and you find a firing squad practicing for something, probably killing failed 'experiments'.")
print("You try to sneak under the window, but step on something and, as a natural response, say something that might have gotten you killed by your mother.\n You start to hear the men in the room walk to the door, you start to run, just missing the door opening, the soldiers yell and sound the alarm.")
print("there is a cross section in the path, which way do you go?")
x = input("Right, Left, or Straight")
if x.upper() == "RIGHT":
  print("You go down the right path, but there were guards down that path, you were shot and killed.")
  print("GAME OVER")
elif x.upper() == "LEFT":
  print("You down the left path, but it was a dead end, you were cornered, shot, and bleed to death.")
  print("GAME OVER")
elif x.upper() == "STRAIGHT":
  print("You go forward, at the end of the hall you find two doors.")
  print("You have to choose quickly or you will die.")
  b = input("Door#1 or Door#2")
  if b.upper() == "DOOR#2":
    print("You go through door#2, on the other side is Dr.Snow, he has a revolver pointed at your head.\n Dr.Snow: I really wanted you to live, but I don't need you alive for the surgery.\n He pulled the trigger and everything goes black.")
    print("GAME OVER")
  elif b.upper() == "DOOR#1":
    print("You go through door#1, on the other side is a dog like creature in a cage, lips raised, it has crimson liquid dripping from its mouth.")
    print("You look at the floor of the cage and see a body torn to shreads.\n You feel a sudden wave of nausea rush over you, soon after you throw up in a near by container.\n You(thinking): What is that thing? Is this the the ancient secret that they are trying to figure out?\n You look back at the beast, it had it's eyes locked on you the entire time, but it was sitting and was no longer bearing it fangs.\n It almost looked like a German Sheperd, if a German Sheperd had scales, snake eyes, and two tails.")
    print("You: I wonder if your not as agressive as you look.\n The creature layed down and made a werid chirp sound.")
    a = input("Approach the beast or Wait")
    if a.upper() == "WAIT":
      print("You decided to wait.\n 20 minutes later, the door burst open, soldiers shot the beast in surprise, like they did know it was there, but it bounced right off of it, but it made the beast mad, it almost ripped the bars off.\n They looked around and finally noticed you, without a word someone pulled the trigger of their gun, and killed you without a thought.")
      print("GAME OVER")
    elif a.upper() == "APPROACH THE BEAST":
      print("As you approach the beast, it's ears perk up.\n You put your had just close enouph to the cage to were it could smell it.\n It sniffed your hand, then licked it, it felt kinda hot to the touch.\n It started to wag it's tails, and yet again it chirped.")
      k = input("You see that it is a girl,you decided to name her, what do you want to name her?")
      print(f"You named her {k}")
      print("You try to find the lock to her cage and find a heavy duty lock that need a key.\n You look around and find a box on the wall with a big key inside.\n You try to open it and to your surprise it opened, a safety pin fell to the floor.\n You: I guess someone wanted to help her.")
      print(f"You go back to {k}'s cage.\n You put the key in the lock, it fits, you turn the key and the lock falls to the ground.\n {k} nudges the door open, walks out, and looks at you.\n You: Please dont kill me right after I just freed you.\n {k} looks you up and down, then, she starts to walk towards you.\n You feel inclined to back up, but don't.\n She sniffs you, and sits with a sigh.\n You also sigh, but out of relief.")
      print(f"You look around for another way out of the room.\n There is a door on the west side of the room marked 'CONTAINMENT UNIT'.\n You look at {k} for any sign of an answer, she give you a look that says 'Don't look at me, I have been stuck in a cage for the past decade'.\n You approach the door and try to listen for anything that might tell you not to go in there.\n But you hear nothing, nothing at all.")
      print("You crack open the door and peak outside, the alarm stopped but it seems that there are armed guards patrolling the halls.\n You close the door and think over your choises, hide or take your chances and try to look for an exit down the hall.")
      u = input("What should you do? Hide or go down the hall")
      if u.upper() == "HIDE":
        print("You hide and wait, you hide, you run, you hide again, you wait, you run, hide, wait, run, over and over again, until you stop and hide for the very last time.")
        print("GAME OVER")
      elif u.upper() == "GO DOWN THE HALL":
        y = input("As you exit the room, you look around to see if there were any guards around.\n The coast was clear, so you go into the hall, you have two options, left or right?")
        if y.upper() == "LEFT":
          print("As you go down the left path, you hear gunshots again, but this time, they are accompanied by screams.\n you slow down and start to be more cautious around doors and windows, as you approach a window, flashes of light emited from the window as the shots were fired.")
          r = input("Do you want to see what is happening in the room? Yes or no")
          if r.upper() == "YES":
            print("As you peek through the window, you see guards fireing at something humanoid in apperance trapped in a cage.\n But its not human, it was paper white with long limbs, a gaping mouth, and eyes white as its skin.\n They had it chained faceing the back wall.\n You(thinking):It looks like some thing I've heard of, what was it called? SP3? No, thats not it. ACP? No, thats not it either. SCP's! Thats it, wait does that mean they are real. And that I am in one of their facilities? This is getting out of hand.")
          elif r.upper() == "NO":
            print("You decide you don't want to know and continue forward.")
          print(f"As you move forward, you hear Dr.Snow talking to someone in a room.\n Dr.Snow: We are working on finding {v} as we speak.\n Stranger: I want the subject found now, not as we speak.\n Dr.Snow: We are scouring the facility the best we can, Director..\n Director: I want better, now!\n Dr.Snow:...Yes sir.\n You hear someone aproaching the door, there is no where to hide so you get ready to run, but instead of spoting you, Dr.Snow went the other way and didn't notice you.\n You stay quiet until you don't hear the footsteps, then you push forward.")
          w = input(f"As you continue on the path, you find yourself at another split, but this time both doors are marked as exit.\n {k} seems to want to sniff around.\n What do you want to do?\n Go through exit#1, exit#2, or let her sniff around?")
          if w.upper() == "EXIT#1":
            print(f"As you open the the door, the alarm blares and you are surounded instantly by guards, they put {k} in a cage so she wouldn't interfere.\n You put your hands up but they fired anyway, when the first bullet ripped through you, you knew it was over, you were so close and yet so far.")
            print("GAME OVER")
          elif w.upper() == "EXIT#2":
            print("As you open the door and walk in, the floor falls from under your feet, and you start to plummet to your death.\n No one hears your screams for help, and a few seconds later you splat on the cold cement and everything goes black.")
            print("GAME OVER")
          elif w.upper() == "LET HER SNIFF AROUND":
            print(f"You wait for {k} to be done with her sniffing, but she stops abruptly and paws at the wall as she chirped.\n You: Whats up {k}?\n You get up and investigate the wall, there seems to be tiny seems in the wall, almost like there was a door there.\n You push against the wall and it clicks in, as you realese part of the wall pops out and slides open.\n In the opening there was a long dimly lit hall.\n You look at {k} and she walked in, so you followed her.")
            print(f"As you go down the hall you see the light get brighter and brighter as you go on.\n When you get to the brightest point you enter a room and the lights dim again, and you see Dr.Snow infront of a bunch of monitors, flipping franticaly through security feeds, looking for something, you most likely.\n You stay quiet and listen to what he is saying.\n Dr.Snow: Come on {v}, where are you? I am trying to help you here while I can still think straight.\n You: What do you mean 'while you can think straight'?\n Dr.Snow turned around in his chair with his eyes wide open.\n Dr.Snow: Oh thank god they didn't find you, the Director put mind control chips in us this week and I wondered why, now I know.\n You: Mind control chips? You let them do that to you?\n Dr.Snow: It was either that or die, what choice did I have, I put a dampener on so it is harder for them to control me.\n You: that was a lot to absorb.\n Dr.Snow: Yeah I know, here I wanted to give you this before they took control again.\n He hand you a hand gun, looks like a Desert Eagle.\n You: You trust me not to kill you?\n Dr.Snow: Yes, yes I do.")
            t = input("You debate on whether or not to kill him what do you do? Kill or Spare")
            if t.upper() == "KILL":
              print(f"You lift the gun and point it at his head.\n Dr.Snow: I understand, just when you get out, give this to my wife and kids.\n He hands you a piece of paper, you nod, grab it, and put it in your pocket.\n You pull the trigger and a flash of red spurts on the monitors.\n You look at the moniters for an exit of some kind.\n It seem the only way outside is to go through the front door, then to actually escape you need to go through a guarded gate.\n It is guarded by 5 guards and two turrets.\n It seems you can deactivate the turrets from the computer, but there is still the guards to worry about the guards.\n On the table is two papers one about {k}, which is called scp-8579309, and the other paper was about the white humaniod called scp-096 or The Shy Guy.\n The odd thing was it said that {k} was extremely hostile and would try to kill or maime anyone who got close to the cage.\n while contemplateing what you just read, you notice a paper in Dr.Snow's jacket pocket, you grab it as respectfuly as possible and unfolded it.\n It was decribing you in perfect detail and marked you as scp-0 or the founder.\n It said that you had the ability to comunicate with the scp's and make them peaceful towards you and others.\n Aperantly they were going to try to make a mutigen out of your blood to try to make the other scp's docile.")
              q = input("You:That means I can use Shy Guy to my advantage, or I can go straight to the gate.\n What should I do?")
              if q.upper() == "USE SHY GUY TO MY ADVANTAGE":
                print("Before you leave to free Shy Guy, you turn off the turrets and make sure that is the only way out, and it is.")
                print(f"You head back to the room you saw shy guy in, the 3 guards were taking a break from shooting it.\n As you open the door you draw the pistol and aim it at one of the guards, {k} tenses up sencing that there was going to be a fight.\n As you pull the trigger, {k} runs at the second one, before the third one could react he had a barbed tail stabed through his sternum.\n Shy Guy heard this and turned around ready for mass murder, but when he locked eyes with you he chilled out.\n You aproach the gate and unlock the cage, as Shy Guy steps out of the cage he nods at you in appreciation.\n You step outside of the room with {k} and Shy Guy, and proceed toward the exit. \n When you find the exit door, you peer through the window next to it, just like before there are five guards and two turrets, still disabled.\n You prepare yourself for some trouble, and burst through the door killing two of the guards, {k} took out another, and Shy Guy took out the others in one swing.\n You walk up to the gate, just one barrier to freedom, you open the gate, step out of the hell hole.\n But you don't make it five feet before you hear a voice.\n Director: So close and yet so far, what a waste of good potential.\n You turn around and see the turrets are turned back on and pointed at you, you see {k} and Shy Guy in bindings, before you are abliterated by the turrets.")
                print("GAME COMPLETED\n Thats the end of the game, did you enjoy it?\n Probably not thanks to that ending, could you have survived or died earlier, the only way to find out is to play again, see you later!")
              elif q.upper() == "GO STRAIGHT TO THE GATE":
                  print(f"Before you head toward the gate, you turn off the turrets and make sure that is the only way out, and it is.\n You run to the exit trying not to think about what you just did, when you reach the door you look out of a window next to it.\n As expected, there are five guards and two deactivated turrets.\n You prepare yourself for the battle ahead and burst through the door guns blazing, you kill two and {k} takes out another, the other two fired of a shot each.\n One of them missed but the other went straight through your knee, before you raise your gun to fight back, a gun is pressed on your head.\n Your heart sinks as you look up to see a woman holding the gun, when she speaks, you reconize her voice.\n Director: You only had to stay in your bed, you would have lived for a long time.\n In that moment, you feel like she might be right, what if you stayed in the bed?")
                  print("GAME COMPLETED\n Thats the end of the game, did you enjoy it?\n Probably not thanks to that ending, could you have survived or died earlier, the only way to find out is to play again, see you later!")
            elif t.upper() == "SPARE":
                print("You put the gun away and continue listening to what he has to say.")
                print(f"Dr.Snow: There is only one exit to this building and it is guarded by five guards and two turrets, but I can deactivate them before you leave.\n You: Thank you, but why are you doing this?\n Dr.Snow: Because no one should live a life of pain and suffering this company will put you through.\n Dr.Snow: There is something that can give you an edge in the fight to come, SCP-096, aka Shy Guy.\n You: I think I saw him in the hall awhile ago.\n Dr.Snow: And you didn't get caught? Impressive, you surprise me more and more every second.\n You: How long have you been watching me?\n Dr.Snow: On and off through out the day, no one has been able to tame SCP-8579309, or {k} as you know her.\n Dr.Snow: I probably should tell you something that will help you understand why you were brought here, you are classified as SCP-0 or The Founder.\n Dr.Snow: You have the ability to calm any SCP and make them do what you want them to do, that is why you are here, obviously you were the child or grandchild of the original Founder, other wise you would know about your ability.\n You ponder on what this might do to your family if you tell them about this, would this change the way they treat you?\n You: Either way, I am left with two options.")
                q = input("You:I can use Shy Guy to my advantage, or I can go straight to the gate.\n What should I do?")
                if q.upper() == "USE SHY GUY TO MY ADVANTAGE":
                  print("Dr.Snow: Good luck\n You: Thanks")
                  print(f"You head back to the room you saw shy guy in, the 3 guards were taking a break from shooting it.\n As you open the door you draw the pistol and aim it at one of the guards, {k} tenses up sencing that there was going to be a fight.\n As you pull the trigger, {k} runs at the second one, before the third one could react he had a barbed tail stabed through his sternum.\n Shy Guy heard this and turned around ready for mass murder, but when he locked eyes with you he chilled out.\n You aproach the gate and unlock the cage, as Shy Guy steps out of the cage he nods at you in appreciation.\n You step outside of the room with {k} and Shy Guy, and proceed toward the exit. \n When you find the exit door, you peer through the window next to it, just like before there are five guards and two turrets, still disabled.\n You prepare yourself for some trouble, and burst through the door killing two of the guards, {k} took out another, and Shy Guy took out the others in one swing.\n You walk up to the gate, just one barrier to freedom, you open the gate, step out of the hell hole.\n But you don't make it five feet before you hear a voice.\n Director: So close and yet so far, what a waste of good potential.\n You turn around and see the turrets are turned back on and pointed at you, you see {k} and Shy Guy in bindings, just then the turrets powered down and the bindings on {k} and Shy Guy unlock.\n The Director is in total shock, then the intercom came on.\n Dr.Snow: Bye bye Director, have a nice afterlife.\n {k} stabs the Director with her tails, one in the abdomen and the other in the neck.\n The Director lie there slowly bleeding to death.\n Dr.Snow: Get out of here {v} while you still have the chance!\n You run out of the gate, {k} follows close behind, while Shy Guy runs off into the woods.\n Once you were at least five miles away, you slowed down to a walk and take in that you are actually free from that hell hole\n You: I wonder how Mom is doing?")
                  print("GAME COMPLETED\n Hooray, you got one of the good endings, if you aren't saticfied with the outcome, play again at your own risk.")
                elif q.upper() == "GO STRAIGHT TO THE GATE":
                  print("Dr.Snow: Good luck\n You: Thanks")
                  print(f"You run to the exit, wondering if you should have brought Dr.Snow with you, when you reach the door you look out of a window next to it.\n As expected, there are five guards and two deactivated turrets.\n You prepare yourself for the battle ahead and burst through the door guns blazing, you kill two and {k} takes out another, the other two fired of a shot each.\n One of them missed but the other went straight through your knee, before you raise your gun to fight back, a gun is pressed on your head.\n Your heart sinks as you look up to see a woman holding the gun, when she speaks, you reconize her voice.\n Director: You only had to stay in your bed, you would have lived for a long time.\n In that moment, you feel like she might be right, what if you stayed in the bed?\n Just before she pulls the trigger, you hear gun fire, the Director looked around to see what the commotion was about, you take this chance to shoot her in the knee.\n She falls to the ground and you get up, pointing the gun at her.\n You:Any last words?\n The Director: We will find you eventually, no matter where you hide, you can't out run the Foundation.\n You: But I can kill the Foundation everytime they aproach me, {k}, or anyone with me.\n You pull the trigger, the Director spasmed, then went limp.\n You look around and see Dr.Snow in a car, bleeding from the back of his neck.\n You run over and ask him if he is ok.\n Dr.Snow: Had the chip removed, but otherwise I'm fine.\n You: Thats good.\n Dr.Snow: What are you waiting for, get in!\n You call {k} and she jumps in the back, you look around for Shy Guy, but he is gone.\n Dr.Snow: Don't worry about him, he ran off into the woods when his bindings were taken off.\n You get into the car, and you drove away from that mad house.")
                  print(f"MONTHS LATER....\n You are living in a remote area with {k}, Dr.Snow, his family, Shy Guy, and on occation other SCP's.\n You finally found peace, you haven't seen the Foundation in all that time, either you are really good at hiding, or they gave up.\n But that dosen't matter, even if they tried they would be dead the moment the stepped within a 500 mile raidius of this place.")
                  print("GAME COMPLETED\n That was such an amazing ending, don't you think?\n But there are many other endings and deaths in this game, maybe you ran into them, maybe you didn't, the only way to know what could have happened is to play again\n Hope to see you soon.")
        elif y.upper() == "RIGHT":
          print("As you go down the right path,")
