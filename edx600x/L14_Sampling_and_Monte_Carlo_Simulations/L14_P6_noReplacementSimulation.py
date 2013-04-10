import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    res = 0
    for i in range(numTrials):
        res = res + pick_three_balls()
    
    return res/float(numTrials)
        

# this is my helper function
def pick_three_balls():
    '''
    given a number on num_pics, calculates the
    probability of of drawing 3 balls of the same color
    out of a bucket containing 3 red and 3 green balls
    
    '''
    bucket_of_balls = ['R','R', 'R', 'G', 'G', 'G']
    selected_balls = []
    for i in range(3):
        ball = random.choice(bucket_of_balls)
        selected_balls.append(ball)
        bucket_of_balls.remove(ball)
        
    if selected_balls[0] == selected_balls[1] and selected_balls[1] == selected_balls[2]:
        return True
    else: return False
        
        
print 'calculated probability',noReplacementSimulation(100000)
print 'expected probability:',1/10.0