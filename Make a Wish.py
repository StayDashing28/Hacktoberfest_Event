
# Import the modules
import sys
import random

ans = True

while ans:
    question = raw_input("Ask if your wish will be granted: (press enter to quit) ")
    
    answers = random.randint(1,7)
    
    if question == "":
        sys.exit()
    
    elif answers == 1:
        print "Congratulations! The odds are in your favour and your wish will surely be granted!"
    
    elif answers == 2:
        print "There is a high chance your wish will come true,but you need to put in the effort."
    
    elif answers == 3:
        print "Your wish will not come true easily, so do work hard to achieve your dreams!"
    
    elif answers == 4:
        print "If you really want this wish to come true,you must work really hard or it won't come true. But I believe that hard work pays off! "
    
    elif answers == 5:
        print "I'm sorry,but the chances of this wish coming tre are really slim."
    
    elif answers == 6:
        print "I'm really sorry but this wish doesn't seem to have a chance of coming true. It's okay, I believe that you can still be happy.Be positive!"
    
    elif answers == 7:
        print "Hmm, the chances of your wish coming true are really 50/50. Press enter again to get another result!"
        
        print "Thank you for making your wish! Whether your result be positive or not, I wish you all the best! And that wish shall come true! :D"
    

