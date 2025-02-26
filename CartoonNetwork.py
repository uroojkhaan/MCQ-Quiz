#Welcome Message For Cartoon Network Quiz :
print(" ===== WELCOME TO THE ULTIMATE CARTOON NETWORK QUIZ =====")
print(" Only A True Cartoon Network Fan Can Score 100 %. Are You Ready ? ")
print("------- LET'S BEGIN !!! -------")

# tuple of questions :
Questions = ( "What is the name of the bulldog who often protects Jerry ?:" ,
    "In Tom & Jerry , what is Jerry's favorite food ?:",
    "What is the main reason Tom always chases Jerry ?:",
    "What is the name of Horrid Henry's perfect little brother ?:",
    "Which phrase does Henry often say when he's frustrated ?:",
    " What is Henry's favorite activity ?:",
    "How many cockroaches lives in Oggy's house ?",
    "What is the name of Oggy's cousin who loves to fight ?:",
    "Which color best represents Oggy?",
    "Which Character is the leader of Baby Looney Tunes Group ?:",
    "What AnimaL IS Baby Tweety ?:",
    "Which character is known for being bossy ?:",
    "What special ability does Keymon Have ?",
    "Who is Keymon's best friend ?",
    "Which Object in the show is magical ?:",
    "Which Powerpuff girl wears green dress ?:",
    "Who created the Powerpuff girls ?:",
    "Who is the main villain in ' THE POWERPUFF GIRLS ' ?:",
    "What are the names of the two best friends in ' BARBIE & THE DIAMOND CASTLE ' ?:",
    "What magical object protects the Diamond Castle ?:",
    "What is the color of Rapunzel's Hair ?:",
    "What is the name of Rapunzel's pet chameleon ?:",
    "Which Bear is the oldest in 'WE BARE BEARS' ?",
    "What is Ice Bear's most famous catchphrase?:",
    "What is Mr. Bean's favorite stuffed animal called ?:" )

# Tuples For Options:
options = (("A. Max " ,"B. Spike ","C. Rex ","D. Bruno "),
           ("A. Cheese " ,"B. Bread ","C. Pizza ","D. Cookies"),
           ("A. They are best friends " ,"B. Jerry keeps stealing food ","C. Tom is bored ","D. Jerry wants to be caught "),
           ("A.Peter " ,"B. Paul ","C.Phillip ","D. Rude Raplh "),
           ("A.'Not Again!' " ,"B. 'That's so unfair !' ","C.'I give up !' ","D. 'Oops!' "),
           ("A. Studying " ,"B. Playing Soccer","C. Watching TV ","D. Annoying Other's"),
           ("A. Two " ,"B. Three","C. Four ","D. Five "),
           ("A. Joey " ,"B. Jack ","C. Bob ","D. Max"),
           ("A. Green " ,"B. Blue ","C. Red ","D. Yellow "),
           ("A. Baby Daffy " ,"B. Baby Tweety ","C. Baby Bugs ","D. Baby Lola "),
           ("A. Duck " ,"B. Rabbit ","C. Canary ","D. Cat "),
           ("A.Baby Sylvester " ,"B. Baby Daffy ","C. Baby Taz ","D. Baby Bugs"),
           ("A. Super Speed " ,"B. Talking to animals ","C. Magic Powers ","D. Invisibility "),
           ("A. Rahul" ,"B. Rohan ","C. Raj ","D. Ravi "),
           ("A. Pen " ,"B. Backpack ","C. Shoes ","D. Cap  "),
           ("A. Blossom " ,"B. Bubbles","C. ButterCup ","D. Bell "),
           ("A. Prof. Plutonium " ,"B. Prof. Proton","C. Prof. Utonium ","D. Prof. Neutron"),
           ("A. Mojo Jojo " ,"B. Fuzzy Lumpkins ","C. Him ","D. Sedusa"),
           ("A. Alexa & Liana " ,"B. Barbie & Teresa ","C. Chelsea & Skipper ","D. Melody & Harmony"),
           ("A. Crystal Crown " ,"B. Magic Mirror" ,"C. Golden Key ","D. Enchanted Necklace"),
           ("A. Black " ,"B. Blonde ","C. Brown  ","D. Red"),
           ("A. Maximus " ,"B. Pascal","C. Flynn ","D. Eugene"),
           ("A. Ice Bear " ,"B. Panda Bear ","C. Grizzly Bear ","D. Chloe "),
           ("A. 'Ice Bear Approves! ' " ,"B. 'Ice Bear Is Ready! ' ","C. 'Ice Bear Never Loses !'","D. 'Ice Bear Loves You!' "),
           ("A. Teddy " ,"B. Bunny ","C. Snuggles ","D. Bear ")
           )

#Tuples For Answers :
Answers = ("B","A","B","A","B","D","B","B","B","C","C","B","C","A","B","C","C","A","A","B","B","B","C","A","A")

# Score Counter :
Score = 0
# Question Number (Index no . = 0 +1) :
question_num = 0
guesses = []
# Index Ka Use Krtay Huay LOOP ka Use :
for question in Questions : # Yahan Per "question" jo hai ye aik temporary variable hai jo sirf loop ke andar work krega !
     print("-------------------------------")
     print("Questions No :",question_num +1 ) # It Will Show Question No.
     print(question)
     for option in options [question_num]: # Ye Loop Current Ques. Ke Saray Options One By One Show Krega!
         print(option)
# Guess User Ka Input Lekar Extra Spaces Hatata Hai Or Small Alphabet main covert krta hai !
     guess = input("Enter Your Answer (A,B,C,D) : ").strip().upper()
     question_num += 1
if guess == Answers :
    print(" Whoa ! Even Ben 10 Is Impressed ;) ")

else:
    print("Wrong ! You Slipped Harder Than Tom On A Banana Peel ;( ")
    Score += 1
    print(f"Your Final Score Is {Score} Out Of 25")

    print(f"Your Total Score Is {Score} Out Of 25")

