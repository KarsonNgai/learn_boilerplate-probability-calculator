import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **ball_in):
        self.ball_amount={}
        self.contents=[]
        for k,v in ball_in.items():
            self.ball_amount.setdefault(k,v)
        self.inside()
    def inside(self):
        self.contents=[]
        for i in self.ball_amount: #color of ball
            for j in range(self.ball_amount[i]): #number of particular color
                self.contents.append(i)
        return self.contents
    def draw(self, draw_number=0):
        self.inside() #run 一次,reset個self.contents
        draw_away_lst=[]
        if draw_number>=len(self.contents): #如果draw>現有既ball
            self.draw_away={}
            for i in self.contents:
                if i in self.draw_away: #key
                    self.draw_away[i]+=1 #value +=1
                else:
                    self.draw_away.setdefault(i,1)
            for i in self.contents:
                draw_away_lst.append(i)
            self.contents=[]
        else:
            for i in range(draw_number):
                drawing=random.randint(0,len(self.contents)-1) #number
                draw_away_lst.append(self.contents[drawing])
                del self.contents[drawing]
            self.draw_away={}
            for i in draw_away_lst:
                if i in self.draw_away: #key
                    self.draw_away[i]+=1 #value +=1
                else:
                    self.draw_away.setdefault(i,1)
        return draw_away_lst

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    fail=0
    for k in range(num_experiments):
        hat.draw(num_balls_drawn)
        for j in expected_balls:
            if j not in hat.draw_away or hat.draw_away[j]<expected_balls[j]:
                fail+=1
                break
    return((num_experiments-fail)/num_experiments)
