 #A neat & clean title for MCQ quiz
print("------------- MULTIPLE CHOICE QUESTIONS ---------------\n")

# fixed questions , options , answers (isliye teeno tuple hain )
questions = (" Who is the highest run-scorer for Pakistan Cricket Team ? :",
             " Which Pakistani bowler has taken the most wicket in One Day International ? :",
             "In which year did Pakistan win their first ICC WorldCup ? :",
             " Who hold the record for the highest individual score in an ODI for Pakistan ? :",
             " Against which team did Pakistan win their first-ever test match ? :",
             " Who was the captain of Pakistan during their 2009 ICC WorldCup Twenty20 victory ? : ",
             " Which Pakistani cricketer is known for scoring a century on his test debut in 2016 ? : ",
             " How many wickets did Shahid Afridi take in his his best ODI bowling performance ? : ",
             " Which Pakistani batsman has the most centuries in ODIs ? : ",
             " Who is the youngest cricketer to score a test century ? : ",
             " Which Pakistani bowler has the best bowling figures in a test innings ? :",
             " In which city did Pakistan win the 2017 ICC champions trophy final ? :",
             " Who was the Pakistan's first test captain ? :",
             " Which Pakistani player has the individual score in a test match ? :",
             " Who is the leading wicket-taker for Pakistan in test cricket ? : ",
             " Which Pakistani cricketer has the highest batting average in test cricket ? :",
             " Who was the first Pakistani bowler to take a hat-trick in test cricket ? :",
             " Which Pakistani batsman scored a triple century against india ? :",
             " Who is the fastest Pakistani bowler to reach 100 wickets in ODIs ?: ",
             " Which Pakistani cricketer has the most catches in test cricket ? :",
             " Who was the first Pakistani to score a double century in ODIs ?:",
             " Which Pakistani bowler has the best economy rate in T20 internationals ?:",
             " Who is the only Pakistani cricketer to score century in all three formats ? :",
             " Which cricketer holds the record for the highest individuals score in a test match ? :",
             " Who has taken the most wickets in Test Cricket History ? :",
             " Which team had won the inaugural ICC T20 WorldCup in 2007 ?:",
             " Who is the fastest batsman to reach 10,000 runs in ODI cricket ? :",
             " Which bowler has the best bowling figures in a single ODI match ? : ",
             " Who scored the fastest century in ODI cricket ? :",
             " Which country has won the most ICC WorldCup titles ?:",
             " Who is the only player to score 100 100 international centuries ? :",
             " Which wicket keeper has the most dismissals in test cricket ? :",
             " Who was the first batsman to score a double century in ODI cricket ? :",
             " Which team holds the record for the highest team total in a test match ? :",
             " Who is the youngest player to score a century in international cricket ? :",
             " Which bowler has the most five-wicket hauls in test cricket ?:",
             " Who is the highest run-scorer in Women's ODI cricket ?:",
             " Which cricketer has the highest batting average in test cricket (minimum 20 innings) ?:",
             " Who holds the record for the fastest fifty in T20 international cricket ? :",
             " Which team achieved the highest successful run chase in a test match ?:",
             " Who has the most catches in test cricket as a non wicketkeeper ? : ",
             " Which bowler has the best economy rate in T20 international ?:",
             " Who is the only cricketer to have taken two ODI hat-tricks ?: ",
             " Which player has the most appearance in international cricket ? : ",
             " Who is the first bowler to take 500 wickets in Test cricket ?:",
             " Which batsman holds the record for the most sixes in ODI cricket ?:",
             " Who is the only player to have scored centuries in both innings of a test match three times ?:",
             " Who is the only cricketer to score a triple century in test cricket twice ?:",
             " Which bowler holds the record for the fastest 100 wickets in ODI cricket ? :",)

options = (("A.Javed Miandad ","B.Inzimam-ul-Haq ","C.Younis Khan ","D.Mohammad Yousuf " ),
           ("A.Waqar Younus ", "B.Wasim Akram ","C.Shoaib Akhtar ","D.Saqlain Mushtaq "),
           ("A.1987 ", "B.1992 ","C.1996 ","D.1999 "),
           ("A.Saeed Anwar ", "B.Fakhar Zaman ","C.Babar Azam ","D.Shahid Afridi "),
           ("A.England ", "B.Australia ","C.India ","D.West Indies "),
           ("A.Shoaib Malik  ", "B.Younis Khan ","C.Misbah-ul-Haq ","D.Shahid Afridi "),
           ("A.Babar Azam ", "B.Fawwad Alam ","C.Mohammad Rizwan ","D.Asad Shafique "),
           ("A.5 ", "B.6 ","C.7 ","D.8 "),
           ("A.Saeed Anwar ", "B.Inzamam-ul-Haq ","C.Mohammad Yousuf ","D.Babar Azam "),
           ("A.Javed Miandad ", "B.Shahid Afridi ","C.Imran Nazir ","D.Hasan Raza "),
           ("A.Imran Khan ", "B.Abdul Qadir ","C.Yasir Shah ","D.Sarfaraz Nawaz  "),
           ("A.London ", "B.Birmingham ","C.Cardiff ","D.Manchester "),
           ("A.Abdul Hafeez Kardar ", "B.Imtiaz Ahmed ","C.Hanif Mohammad ","D.Fazal Mehmood "),
           ("A.Hanif Mohammad ", "B.Inzimam-ul-Haq ","C.Younis Khan ","D.Javed Miandad "),
           ("A.Wasim Akram ", "B.Waqar Younis ","C.Imran Khan  ","D.Yasir Shah "),
           ("A.Mohammad Yousuf ", "B.Younis Khan ","C.Javed Miandad ","D.Inzamam-ul-Haq "),
           ("A.Wasim Akram ", "B.Jalal-ul-Din ","C.Saqlain Mushtaq ","D.Mohammad Sami "),
           ("A.Inzamam-ul-Haq ", "B.Younis Khan ","C.Mohammad Yousuf ","D.hanif Khan "),
           ("A.Waqar Younis  ", "B.Saqlain Mushtaq ","C.Shoaib Akhtar ","D.Hasan Ali "),
           ("A.Younis Khan ", "B.Inzamam -ul-Haq ","C.Mohammad Yousuf ","D.Misbah-ul-Haq "),
           ("A.Saeed Anwar ", "B.Fakhar Zaman ","C.Babar Azam  ","D.Imran Nazir "),
           ("A.Mohammad Amir ", "B.Saeed Ajmal ","C.Umar Gul ","D.Shahid Afridi "),
           ("A.Babar Azam ", "B.Mohammad Hafeez ","C.Ahmed Shahzad ","D.Shoaib Malik "),
           ("A.Brain Lara ", "B.Don Bradman ","C.Sachin Tendulkar ","D.Virendar Sehwag "),
           ("A.Shane Warne ", "B.Muttiah Muralitharan ","C.Anil Kumble ","D.James Andreson "),
           ("A.Australia ", "B.India ","C.South Africa ","D.West Indies "),
           ("A.Sachin Tendulkar ", "B.Ricky Ponting ","C.Virat Kohli ","D.Jacques Kallis "),
           ("A.Glenn McGrath ", "B.Muttiah Muralitharan ","C.Chamanda Vaas ","D.Anil Kumble "),
           ("A.AB de Villiers ", "B.Shahid Afridi ","C.Corey Andreson ","D.Sanath Jayasuriya "),
           ("A.West Indies  ", "B.India  ","C.Australia ","D.England "),
           ("A.Ricky Ponting ", "B.Kumar Sangakara ","C.Sachin Tendulkar ","D.Jacques Kallis "),
           ("A.Adam Gilchrist ", "B.Mark Boucher ","C.Ms Dhoni ","D.Kumar Sangakara "),
           ("A.Sachin Tendulkar ", "B.Virendar Sehwag ","C. Chris Gayle ","D.Martin Guptill "),
           ("A.Australia ", "B.India ","C.SriLanka ","D.England "),
           ("A.Shahid Afridi ", "B.Sachin Tendulkar ","C.Mohammad Ashraful ","D.Hamilton Masakadza "),
           ("A.Richard Hadlee ", "B. Shane Warne ","C.Muttiah Muralitharan ","D.Anil Kumble "),
           ("A.Charlotte Edwards ", "B.Mithali Raj ","C.Belinda Clark ","D.Stafine Taylor "),
           ("A.Steve Smith ", "B.Don Bradman ","C.Graeme POllock ","D.Herbert Sutcliffe "),
           ("A.Yuvraj Singh ", "B.Chris Gayle ","C. k ieron Pollard  ","D. David Miller   "),
           ("A.West Indies  ", "B.Australia ","C.South Africa ","D.India "),
           ("A.Rahul David ", "B.Mahela Jayawardene ","C.Jacques Kallis ","D.Ricky Ponting "),
           ("A.Sunil Narine ", "B.Rashid Khan ","C.Daniel Vettori ","D.Mujeeb Ur Rehman "),
           ("A.Wasim Akram ", "B.Chaminda Vaas ","C.Trent Boult ","D. lasith Malinga "),
           ("A.Mahela Jayawardene ", "B.Sachin Tendulkar ","C.Kumar Sangakara ","D.Ricky Ponting "),
           ("A.Courtney Walsh  ", "B.Shane Warne ","C.Muttiah Muralitharan ","D.Glenn McGrath "),
           ("A.Chris Gayle ", "B.Shahid Afridi ","C.Sanath Jayasuriya ","D.MS Dhoni "),
           ("A.Sunil Gavaskar ", "B.Ricky Ponting ","C.David Warner ","D.Rahul Dravid "),
           ("A.Brain Lara ", "B.Virendar Sehwag ","C.Dob Bradman ","D.Chris Gayle "),
           ("A.Brett Lee ", "B.Saqlain Mushtaq ","C.Rashid Khan ","D.Mitchell Starc "))
answers = ("C","B","B","B","C","B","A","C","A","A","B","A","A","A","A","C","B","B","B","A","B","B","A","A","B","B","C","C","A","C","C","B","A","C","A","C","B","B","A","A","A","B","D","B","A","A","A","C","D")

# Initialize Variables ( Score Or Question no. Ka Track rakhne keliye )
score = 0
i = 0

#loop for each question (Har question ko show krega )
for question in questions :
    print(f"Q{i+1}: {question}")#f-string for formatting , "Q" is added to show Question Number before each question

    # har Question ke option show krne keliye
    for option in options[i] :
        print(option)
#User se input lena , aur upper case main covert krna
    guess = input(" Your Answer (A/B/C/D):").strip().upper()
#Check if the answer is correct or wrong
    if guess == answers[i] :
        print("CORRECT ANSWER")
        score +=1 #If the answer is correct then add +1 in score
    else:
        print(f"WRONG ANSWER !!!")
        i +=1 # Next question ki taraf barhne keliye question no. main 1+ krna
# Final Score Quiz Ke End Main Dikhana
print("--------------- QUIZ COMPLETED ---------------")
print(f"YOUR FINAL SCORE :{score} OUT OF 49" )
print(" Match Winning Performance ! You Are A True Cricket Legend ;) ")
