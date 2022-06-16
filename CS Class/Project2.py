#Zakariyah. M. J. Khan
#ICS2O_2122_S2
#31/05/2022
#Hello, how are you doing
#Project 2 Encryption

import random
#Prints welcome statement
print("___________.__             ________   _____  _____.__                   ___  ____ ___      _________ ___    \n\__    ___/|  |__   ____   \_____  \_/ ____\/ ____\__| ____  ____      /  / |    |   \    /   _____/ \  \   \n  |    |   |  |  \_/ __ \   /   |   \   __\\   __\|  |/ ___\/ __ \    /  /  |    |   /    \_____  \   \  \  \n  |    |   |   Y  \  ___/  /    |    \  |   |  |  |  \  \__\  ___/   (  (   |    |  /     /        \   )  ) \n  |____|   |___|  /\___  > \_______  /__|   |__|  |__|\___  >___  >   \  \  |______/ /\  /_______  /  /  /  \n                \/     \/          \/                     \/    \/     \__\          \/          \/  /__/   ")
print("  ________    _____      _____  ___________\n /  _____/   /  _  \    /     \ \_   _____/\n/   \  ___  /  /_\  \  /  \ /  \ |    __)_ \n\    \_\  \/    |    \/    Y    \|        \n \______  /\____|__  /\____|__  /_______  /\n        \/         \/         \/        \/ ")

#Confirming whether user want to play
play = input("Would you like to play? y/n: ")
while play != "y" and play != "n":
    play = input("Would you like to play? y/n: ")
if play == "n":
    print("Thank you for opening the Office (U. S) game\nHave a good day")
elif play == "y":
    #Displays the player's character and runs through the dialogue between the characters
    print("                       .+sso+/:oydyo/:-:+shdys/    `-:.     `-/+o+/`\n                 `/sdh+/::/::ss:`ymdhyso//hmMNyhNNms+ososys+/-:/shms/`\n                .+hNNy++oo+/.`.--/osyhdmNNMMMMMMMMMNdsssssoso+hhhhsoo+ymdo.\n              -smNy/+ymmmmmNNNNMNMMMMMNNNmmNMMMMMMMMMho:///:--shydNMMNdo-sNs`\n            -hNd+-sNMNdmNMMMNNNMNNNMMMddNMMNNmNMMMMMMNmy+///::/:-:/++ymNNdmMN\n          `sNMs`+NMNNNMMMMNNNMMMMMMNmhyso///+ohMmoNMmoo+/::/-:oymNNmsosshdhmMM/\n         +NMMy`hMMMhyNMNMMNNNMds:-.`-:syddmNMMmyo`+yMMho:..-+//++omMNNNNNNNmdNMs\n       :mMMMh`yMNdodNNNMNMMMs.+sdmmmmmdhNMMMNhy/..`-syhNmdyssso+/.`:yNMMMMNMNMMMy\n      :NMNh:-+MMh+mdNNNNNMd.+NNMMMMMMMMmho:-......:--::ohNMMMMMMNmNy/.oNMNmNMNMMMs\n     :NMm+/dmmMNydyhNdhMMN.yMMNmhysso+:-``        ```.--:/+sdMMMMMNNNm:-mMNNNNMMMMy\n    :NMy/hNMMMMmNddsh/NmMy-Mms:..`.--.`                ``..-.:yNMMMMNMNs:NMMMNNNNMMy\n   :NNy/mMMMMMMmNMMshsNdMo/d-...``                       ```...-yMMMNNMd`NMMNMdmoNMM-\n  /mMm+NMNNMMNMNNNNNNNNMMmom/                              ```..`+NMMMMh`NMMMMNNdhNMh\n +NMMmmMNyNMNMMMMMNmmmNMdNNyh+.                             ``````/NMMM::MMMMNMNNmNMN\n+MNNMMMNymMNNMMMNNNNNMh+:+dNmddhyoo+`                        ````.`sMMN`sMNNMNNMNNNNN\ndNNNMNNddMNNNNNNmymMN+---::/shdhyyy:                         `````..hMo.NMNMNMMMNmMMd\ndNNNMMNmNNNmmNMNdNMM+.-..----.-:::.                          ````...:mh/NMMMNMMMNNMMh\nsMNNMMNMNNmyNMNdmNMo--.....                                  ``...---:dNMNMMNMMNNNMMN.\n:NNNMMMNNNsmMNmMNMy...`.-.`                                    `.-----:odNmmNMMMMMNMMo\n.NMMMmMMMNmMNNNNMm:-.```..                                       ``-----:/o//dMMMNMMMm\n.NMMMNMMNMMNMNNNNs--.``...                                         `....---..dMNMMMMM`\n.NNMMNNNNNMMMNNNN:-...`...                                          ```.....`+MMMMMMM.\n.MNNNNNNNMMMMMNNy.......-.`                                         ``..---.`.NMMMMMM`\n`NMNMMNNNMMNMMMm-...`.-----.`                                        ``.-----.`yMMMMMd\n dMMMNNNNMMNNMMo`-....----..`          ``                      `.`` ```.------`:MMMMM-\n /MMNMNNNMMNMMN-`.`..-.--.` `--..-:-.-.``..``               ```.-......--.----..NMMMd\n `mMNMNNMMMNNMN.``...-.-../hddyysyhysyyso+--/::-..--...----:::+syyyyhhdddy+:-.-.hMMM:\n  :NNNNNNMMMMMN.`....--.:dy/:-.-/+++ososss+/:+shyo/::/:+os+:+syosyoso+/://ss//.`+MMm\n   +MdmNNMNMMMN+.--....:+-.-:+ooymdddmdhyo++ss+/yMo.`..oNsyhdhmdmmmmNmdo:-.--:+-:MM/\n  `y/..-+dNNMMMo-shhyo++--+sso-`dsymoso.smyso+//.od+/:/ho+yyhd/ymsNhyy./yy/``.-hhmm`\n  .s+md+- oMMMm``.-/sy//-.+/s.  odys+s-  /shyso+.sm+:::yd/hh+:`.hyyhy- `/y/.` `hs/s`\n  -oyMNyhs:NMMo     `.-`         .---` ``.`/::+s/ms````-mo+:`````.--` ````     `sNm`\n  `hsMh`.hymMM:       `-         `          .:+:hy`     od:-`                  .+sM-``\n   o+o/``-/mMM-        .-                ``.```hy`       s.`.`                 -/+M+``\n   .s `./NMMMM-         --            ````  `:ho`        .s`  ```             ./.+My`\n    /: `+MMdMM/          -.  `       `   ..+++-           :d/.             ``:o-`oMy\n     o. .sdNMMm`            `--:://+//.`-///:.           `.ohooo:-.`` `.-:+//:..`hMy\n     `s```.yMMMs                  ```     .y+  `::.:----.-``o:-::/:::--:::-----..mMo\n      :s` `oMNMN-                         :N+  -NNhy/:/sds./:..----------------`/MN\n        +o``-NMNMd`                      `-syyoo++/.++:so/+yN+..--....-..-....--`dM+\n        +:.`oMNNN`                     .:-` `.::.` `--..---/+/---.```........-.:d:\n         ./++Ny::`                   `--`          .--..-----::-..```......---.s.\n           `:os.--`                  .`            `.. ``.------.`.```..-----.:o\n             `h-..`                 ``        .:syy/-/ydho-.--...`````.------.+.\n              +o`.`                        ./ymNNNNNNNmmNNNh:....``.```.-----:s\n              `h-`.                    -/+oyo/:----:---.--:+sso:........--::-+:\n               /d...                 `.++:  -:--/+:/oo+o++-.``--.....-----:-:y\n               `Md:.`                ``     `-:/+ooooo+/-........-----------yo\n                mNNs-`                     `..-/oo+://:/oo:......----------os\n                h:+md:.                  ...``.`         `------.---------++\n               `h..-+ddo.`                            ``.----------------s:\n                h` .--/ydy:`                   `...--------------------+y.\n                h`   ..--+yds+.`               `....----------------:+dN`\n               `y      `.-.-:sdhs:.`    `...````..----------------:smsdm\n               `h         .--..-+ymdy+/:----:----------------.-/shs+.`os\n               `h           `..--..:sdmmhyo/::----------::/+syhy/....`+-\n               -y              `..--..--/oosyyyhhhyyyssoooo/:.`...`.` /-\n               `.                  `..--.......................````   +`\n                                      `...------..-.........``\n                                          ``..-.--........``\n                                               ```..```")
    print("\nYour character: Dwight Schrute")
    print("(When prompted with \":\" hit enter)")
    input(": ")
    print("\nWelcome to the game of the Office. Full of metaphor and inside jokes from the Office (U. S)")
    input(": ")
    print("You are playing the character of Dwight and today in the Office Jim is smiling a little bit too much.")
    input(": ")
    print("You are wondering what jim is upto.")
    input(": ")
    print("Here the adventure starts")
    input(": ")
    print("Jim: Dwight, Where are your keys?")
    input(": ")
    option = input("[1]Dismiss him\n[2]Check your assigned house key pocket\n: ")
    if option == "1":
        print("\nDwight: Nice try Jim, stop wasting company time by talking to me!")
        input(": ")
        print("Jim: Ok *smiles*")
        input(": ")
        print("Out of curiosity you still check you pocket trying not to let Jim see\n")
    input(": ")
    print("You are in shock, your house keys are gone")
    print("Dwight: *shouts* JIM WHAT DID YOU DO WITH MY KEYS \n")

    option = input("[1]Call Michael\n[2]Ask jim calmly where your keys are\n: ")
    if option == "1":
        print("\nDwight: *shouts* MICHAEL")
        input(": ")
        print("Michael: What is it Dwight")
        input(": ")
        print("Dwight: Jim took my keys, fire him")
        input(": ")
        print("Michael: Dwight, you know i cannot fire him , he's one of our best sales men\nGo deal with it your self\n")

    if option == "2":
        print("\nDwight: Jim, where are my keys. Don't worry jim, ill count to 5 before i get my katana")
        input(": ")

        print("5     4       3         2\n")
    input(": ")
    print("Jim: Don't worry Dwight, I'll tell you where your keys are")
    input(": ")
    print("Jim: I hid encrypted messages around the office.")
    input(": ")
    print("Jim: Each clue leading to the next. You'll need to decipher these messages")
    input(": ")
    print("Jim: You'll eventually find an envelope, in here you'll find the location of your house keys\n")
    input(": ")

    #Determines how many rounds there will be and display the game instructions
    game_count = random.randint(4, 7)
    first_run = game_count
    print("How to play: You will be presented with an encrypted message, a list of locations and the option for a hint.")
    print("             You can try and decipher the messages and can use the hints every so often to assist.")
    print("             After decrypting previous messages it should get easier and easier")
    print("             You start off the game with", game_count*4, "points, for each wrong guess and hint, you lose 1 point")
    input(": ")
    #Generates all neccessary lists and varibales needed for later in the game such as the
    #alphabet, list of locations and phrases
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    new_alphabet = []

    count = 0
    while count != 26:
        num = random.randint(0, 25)

        while num in new_alphabet:
            num = random.randint(0, 25)
        new_alphabet.append(num)

        count += 1

    clues = ["the clue is in michaels office", "the clue is in the annex", "the clue is at reception",
             "the clue is at your desk", "the clue is in the washroom", "the clue is in the lobby",
             "the clue is in the security desk", "the clue is in the conference room", "the clue is in the parking lot"
    ]
    clue_hint = ["michael", "toby", "pam",
                 "flat plane of work", "the place of relief", "corridor central",
                 "hank", "place of meeting", "car storage"
    ]
    locations = ["Michael's Office", "Your Desk", "Security Desk",
                 "Annex", "Washroom", "Conference Room",
                 "Reception", "Lobby", "Parking Lot"]

    completion_phrases = ["Congratulations you got to last location by deciphering the last cipher, you found an envelope with the location of your keys.",
                          "Congratulations, you actually deciphered Jim's code. You now have the envolope with the location of your keys in your hand",
                          "Hooray, you have located the envelope with the location of your house keys",
                          "Good job, you succeeded, you are holding the envelope with the location of your keys."]
    jim_attacks = ["hit jim in the face with a snow ball", "tell Michael about Jim's horrible workplace behaviour", "scream Michael",
                   "scramble all of Jim's files", "end Jim's phone call", "expose Jim's lies to Charles Miner",]

    jim_attacks_execution = ["You go outside, make snow balls and put it in a bucket.\nYou walk upto Jim's desk while laughing and throwing snowballs at Jim's face.",
                             "You are walking to Michael's office\nMichael: *sighs* What is it that you want Dwight\nDwight: Jim hid my keys, but i found it, but fire him because of misbehaviour in the workplace\nMichael: Wait, you found you keys\nDwight: Yes\nMichael: GO HOME then",
                             "You are walking to Michael's office\nMichael: *sighs* What is it that you want Dwight\nDwight: Jim hid my keys, but i found it, but fire him because of misbehaviour in the workplace\nMichael: Wait, you found you keys\nDwight: Yes\nMichael: GO HOME then",
                             "You walk to Jim's files while he is not looking and with a sinister laugh, then you proceed to mix up all his files",
                             "You walk up to Jim's desk and unplug his phone with a smile on your face",
                             "You walk upto Charles Miner\nDwight: Did you know that Jim actually doesn't know how to play soccer and has been sucking up to you this whole time\nCharles: Oh really, Thats good to know\nCharles: I'll keep that in mind for his next performance review\nYou smille",
                             ]
    nums = []
    cnt = 0
    while cnt != 9:
        cnt += 1
        nums.append(str(cnt))
    bonus_word = ""
    completed_locations = []
    last_message = ""
    redo = ""
    points = 0
    finish = False
    #This is the core part of the game with the logic and different rounds
    while not finish:
        #This loop runs the game as many times as the predetermined variable
        while game_count != 0:

            #This ensures that the same location isn't chosen twice within one game run
            clue_choice = random.randint(0, len(clues)-1)
            while clue_choice in completed_locations:
                clue_choice = random.randint(0, len(clues) - 1)
            text1 = clues[clue_choice]
            completed_locations.append(clue_choice)
            new_text = ""
            count1 = 0

            #This while loop encrypts the message
            while count1 != len(text1):
                if text1[count1] != " ":
                    new_text += alphabet[new_alphabet[alphabet.index(text1[count1])]]

                if text1[count1] == " ":
                    new_text += " "
                count1 += 1
            count1 = 0

            added_points = 4

            #This reitierates some instructions if it is the first round
            if game_count == first_run:
                print("\nThis is the first message you'll need to decipher:\n" + new_text.upper())
                input(": ")
                print("\nDo not worry though, you'll always gets the option for hints!\nDo note that you will lose 1 potential point if used.")
                hint = input("Would you like a hint? y/n: ")
                while hint != "y" and hint != "n":
                    hint = input("Would you like a hint? y/n: ")
                if hint == "y":
                    print("Your hint is", clue_hint[clue_choice])
                    added_points -= 1

            #This asks the user if they would like a hint and subtracts points accordingly
            elif game_count != first_run:
                print("\nYour message is:\n" + new_text.upper())
                hint = input("Would you like a hint? y/n: ")
                while hint != "y" and hint != "n":
                    hint = input("Would you like a hint? y/n: ")
                if hint == "y":
                    print("Your hint is", clue_hint[clue_choice])
                    added_points -= 1

            #This displays the encrypted message and the list of locations to choose from
            message = "Enter the location you would like to go"
            print(new_text.upper())
            print("\n" + message.upper() +"\n")
            print("                            OPTIONS")
            print("--------------------------------------------------------------------")
            print("| [1]Michael's Office      [4]Your Desk       [7]Security Desk     |")
            print("| [2]Annex                 [5]Washroom        [8]Conference Room   |")
            print("| [3]Reception             [6]Lobby           [9]Parking Lot       |")
            print("--------------------------------------------------------------------")

            # print(clue_choice, clue_choice, count1) used for debugging
            #Takes user input for location and handles invalid inputs
            location = input("Input: ")
            while location not in nums:
                location = (input("Input: "))
            if location in nums:
                location = int(location)

            #Removes a point if the location was guessed wrong and asks the user to try again
            while location != clue_choice+1:
                if added_points != 0:
                    added_points -= 1
                print("You got it wrong, you lost 1 potential point\nTry again")
                location = input("Input: ")
                while location not in nums:
                    location = (input("Input: "))
                if location in nums:
                    location = int(location)

            #Displays the current score
            points += added_points
            print("\nYour current score is:", points)

            #Displays if the user got the answer correct
            if location == clue_choice+1:
                print("You got it right")
                input(": ")

                #If structure of different texts that will be displayed depending on the location the user is going to
                print("You will now be making your way to:", locations[clue_choice])
                if game_count != 1:
                    if clue_choice == 0:
                        print("You are about to enter a place where work is not often done, but when work is done it is simply genius")
                    elif clue_choice == 1:
                        print("This is the place where boredom reaches new heights, simply because of one being")
                    elif clue_choice == 2:
                        print("This is is where beauty lays, the name of the beauty is pamalamadingdong")
                    elif clue_choice == 3:
                        print("This is the place where the psycho devises his plan")
                    elif clue_choice == 4:
                        print("This is the place where to best of smells come out from")
                    elif clue_choice == 5:
                        print("This is the place where all the great people of the building can meet each other")
                    elif clue_choice == 6:
                        print("This is the place where the most useful and protecting man sleeps")
                    elif clue_choice == 7:
                        print("This is the place where a great amount of insight comes from and some of the best ideas, second to Michael's office")
                    elif clue_choice == 8:
                        print("This is the place where all the the Lincolns and the Pontiacs meet")
                    input("Open the next clue: ")
                #If the user has completed the game it prompts them to to move on and
                #includes aspect of storyline which is different each time
                if game_count == 1:
                    print(" ____  ____  _      _____ ____  ____  _____  _     _     ____  _____  _  ____  _      ____  _  _  _ \n/   _\/  _ \/ \  /|/  __//  __\/  _ \/__ __\/ \ /\/ \   /  _ \/__ __\/ \/  _ \/ \  /|/ ___\/ \/ \/ \n|  /  | / \|| |\ ||| |  _|  \/|| / \|  / \  | | ||| |   | / \|  / \  | || / \|| |\ |||    \| || || |\n|  \__| \_/|| | \||| |_//|    /| |-||  | |  | \_/|| |_/\| |-||  | |  | || \_/|| | \||\___ |\_/\_/\_/\n\____/\____/\_/  \|\____\\_/\_\\_/ \|  \_/  \____/\____/\_/ \|  \_/  \_/\____/\_/  \|\____/  (_)(_)(_)                                                                                                    ")
                    print("\n" + completion_phrases[random.randint(0, 3)])
                    open_env_phrase_choice = random.randint(0, 5)
                    open_env = input("[1]Would you like to open the envelope or [2]" + jim_attacks[open_env_phrase_choice] + ": ")

                    #Handles invalid inputs, continues storyline and siplays envelope animation
                    while open_env != "1" and open_env != "2":
                        open_env = input("1 or 2: ")
                    if open_env == "2":
                        print(jim_attacks_execution[open_env_phrase_choice])
                    print("____________________\n|\                /|\n| \              / | \n| /\____________/\ | \n|/                \| \n|__________________|")
                    input(": ")
                    print("     ____________\n    /     _.'\   \ \n   /   _.'    \   \ \n  /_.-'        \___\ \n |\_\ ``   .-   \ _/|\n |  _\___________.  | \n | /              \ | \n |/                \| \n |__________________| ")
                    print("You open the envelope and when you read the letter, you are in shock. The keys were simply put underneath his own welcome mat at his house")
                    input(": ")
                    print("Dwight: *scream*")
            game_count -= 1
        #Prints final score
        input("Reveal final score: ")
        print("Your final score is:", points)

        #Asks user if they would like to play again. Handles invalid inputs.
        #If yes is selected, all neccessary variables are reset
        redo = input("\nWould you like to play again? y/n" )
        while redo != "y" and redo != "n":
            redo = input("Would you like to play again? y/n")
        if redo == "y":
            game_count = random.randint(4, 7)
            completed_locations = []
        elif redo == "n":
            finish = True
    #When user doesn't not want to play the storyline finishes
    #At this point the user can choose if they'd like to use the SUPERENCYPTER
    #,it encrypts any word entered and terminates when "stop" is entered
    print("Dwight: *smiles*")
    print("Dwight: *thinking to yourself* Now that I have all of these deciphered messages from Jim\nI have the secret to his encryption!!!")
    print("As a result of playing the game, you have access to the SUPERENCRYPTER. This Machine can encrypt any message.")
    encryption = input("Would you like to use the encrypter? y/n: ")
    while encryption != "y" and hint != "n":
        encryption = input("Would you like to use the encrypter? y/n: ")
    if encryption == "y":
        print("Enter \"stop\" to end the encryption machine")
    while encryption == "y":
        text1 = input("Enter your word: ")
        if text1 == "stop":
            encryption = "stop"
        if encryption != "stop":
            new_text = ""
            count1 = 0

            while count1 != len(text1):
                if text1[count1] != " ":
                    new_text += alphabet[new_alphabet[alphabet.index(text1[count1])]]

                if text1[count1] == " ":
                    new_text += " "
                count1 += 1
            count1 = 0

            print(new_text)
#Prints farewell message
print("   _____                 _ _                \n  / ____|               | | |               \n | |  __  ___   ___   __| | |__  _   _  ___ \n | | |_ |/ _ \ / _ \ / _` | '_ \| | | |/ _  \n | |__| | (_) | (_) | (_| | |_) | |_| |  __/\n  \_____|\___/ \___/ \__,_|_.__/ \__, |\___|\n                                  __/ |     \n                                 |___/      ")