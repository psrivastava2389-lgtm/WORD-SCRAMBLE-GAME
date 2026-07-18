import mysql.connector 
import random 
import time 
   #mysql database connection 
hi=mysql.connector.connect(user="root",host='localhost',passwd='123456') 
cursor=hi.cursor() 
cursor.execute("use word_scramble") 
  
def line(): 
     print("------------------------------------------------------------------------------------------------------------------") 
  
#func on to scramble a word 
def scramble_word(word): 
    word_list = list(word) 
    random.shuffle(word_list) 
    return ''.join(word_list) 
  
#func on to insert user detail into databse 
def start_game(name,user_id,passwd,score=0): 
    try: 
        cursor.execute(("insert INTO user_detail VALUES (%s,%s,%s)"),(name,user_id,passwd)) 
        cursor.execute(('insert into scores values(%s,%s)'),(score,name)) 
        hi.commit() 
        print("{Data added successfully}") 
    except: 
        print("username already exists, TRY AGAIN") 
    else: 
        play_game(name) 
  
 #accessing users from database 
cursor.execute("select username from scores") 
users=[] 
k=cursor.fetchall() 
for i in k: 
    for j in i: 
        users.append(j) 
  
  

 
 #func on to check whether its an old user or new 
def creation(): 
    ch=input('''* New user or old?? 
             * Press *N* for new 
             * Press *O* for old:''') 
    line() 
    if ch in'nN': 
        adduser() 
    elif ch in 'oO': 
        name=input('enter username:') 
        line() 
        for i in users: 
            if i.lower()==name.lower(): 
                    score=old_user(name) 
                    play_game(name,int(score)) 
                    break 
        else: 
            print('username not found') 
            creation() 
    else: 
        print("OOPS! invalid literal. TRY AGAIN") 
        creation() 
  
 #func on to add a new user 
def adduser(): 
    name=input('* enter username:') 
    user_id=input('* enter  user id:') 
    passwd=input('* enter password:') 
    line() 
    start_game(name,user_id,passwd,score=0) 
  
 #func on for an old user to play the game 
def old_user(name): 
    cursor.execute(("select score from scores where username=(%s)"),(name,)) 
    score_input=cursor.fetchone() 
    score=score_input[0] 
    return score 
  
 #func on to play the game 
def play_game(name,score=0): 
    choice='y' 
    while choice=='y': 
            try: 
                lev=input('''enter the level you wish to play in 
                           enter: 
                          1)E=Easy 
                          2)M=Medium 
                          3)H=hard===>''') 
                line() 
                if lev.lower()=='e': 
                        cursor.execute('select words from e order by rand() limit 1') 
                elif  lev.lower()=='m': 
                        cursor.execute('select words from m order by rand() limit 1') 
                elif lev.lower()=='h': 
                        cursor.execute('select words from h order by rand() limit 1') 
                random_word=cursor.fetchone() 
                correct_word=random_word[0] 
                scramble=scramble_word(correct_word)  
            except: 
                print('invalid level,kindly enter the values given above') 
            else: 
                cursor.execute(f'select meaning from {lev.lower()} where words=%s',(correct_word,)) 
                hint_tuple=cursor.fetchone() 
                hint=[] 
                for c in hint_tuple: 
                        hint.append(c) 
            attempts=0 
            time_limit=60 
            start_time=time. time() 
            while start_time<time_limit or attempts<5 and scramble!=correct_word: 
                print("Unscramble the word:",scramble ) 
                print("hint is:",hint) 
                ans=input("enter your answer:") 
                if ans.lower()==correct_word.lower(): 
                    attempts+=1 
                    score+=1 
                    cursor.execute(('update scores set score=(%s) where username=(%s)'),(str(score),name)) 
                    hi.commit() 
                    print("yippeee u got it!!") 
                    break 
                elif attempts<5: 
                    attempts+=1 
                    print("oops u got it wrong, try again") 
            else: 
                if start_time==time_limit: 
                        print("time up!! you lost it") 
                elif attempts==5: 
                        print('correct word is',correct_word) 
            line() 
  
  
 
            choice=input('''* Wanna play more? 
                         Insert: 
                         1)'n' for no. 
                         2)'y' for yes. 
                       T H A N K  Y O U .===>''') 
  
            line() 
  
            if choice.lower()=='n': 
                    print("*", 'T H A N K S  F O R  P L A Y I N G '," *",name,"*", ' W E  W I S H  Y O U  H A V E  A  G R E A T  D A Y ') 
                    print("*", 'Y O U R  S C O R E  I S  :  ',score) 
                    line() 
                    cursor.execute("select * from scores") 
                    print("*","HERE IS YOUR LEADERBOARD") 
                    line() 
                    k=cursor.fetchall() 
                    l=[('SCORE','NAME')] 
                    user_score=[] 
                    for i in k: 
                            user_score.append(i) 
                    user_score.sort(reverse=True) 
                    print(l[0][0]," | ",l[0][1]) 
                    for j in user_score: 
                            print(j[0],' | ',j[1]) 
                    cursor.execute(" select username ,score from scores where score=(select max(score) from scores)") 
                    max_score=cursor.fetchall() 
                    line() 
                    print("* THE WINNER IS :","*", max_score[0][0],"*") 
                    line() 
                    print("* YOU ARE ON ",user_score.index((score,name))+1,"POSITION .") 
            elif choice not in 'ny': 
                 print('invalid literal ') 
creation()
