
# Import the modules
import sys
import random

ans = true

while ans=true:
    question = raw_input("Ask if your wish will be granted: (press enter to quit) ")
    
    answers = random.randint(1,8)
    
    if question == "":
        sys.exit()
    
    elif answers == 1:
        print ("Congratulations! The odds are in your favour and your wish will surely be granted! What did you wish for anyway? I'm so curious!!")
    
    elif answers == 2:
        print ("There is a high chance your wish will come true, but you need to put in the effort. Remember, you reap what you sow, so remember to work hard! The journey may be hard, but you will definitely make it someday!")
    
    elif answers == 3:
        print ("Your wish will not come true easily, so do work hard to achieve your dreams! Remember the most beautiful views come at the top of the hardest climb...I will support you throughout!")
    
    elif answers == 4:
        print ("If you really want this wish to come true, you must work really hard or it won't come true. But I believe that hard work pays off! I will support you throughout your journey!")
    
    elif answers == 5:
        print ("I'm sorry, but the chances of this wish coming tre are really slim. However, don't feel down, I'm sure another wish will come true! Why not press enter again to get another result?")
    
    elif answers == 6:
        print ("I'm really sorry but this wish doesn't seem to have a chance of coming true. It's okay, I believe that you can still be happy. Be positive! I will support you too!")
    
    elif answers == 7:
        print( "Hmm, the chances of your wish coming true are really 50/50. Press enter again to get another result!")
    elif answers==8:
        print("Hard work and effor are the key to sucess!However luck plays its part too...You have some chance for your wish to suceed...")
        
        print "Thank you for making your wish! Whether your result be positive or not, I wish you all the best! And that wish shall come true! :D Come back again!!")
    res=input("enter 1 to try again")
    
    if res==1:
        ans=true
    else:
        ans=false
  
    

