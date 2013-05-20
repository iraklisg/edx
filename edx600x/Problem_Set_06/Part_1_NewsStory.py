from ps6 import *
import string

test = NewsStory('foo', 'myTitle', 'mySubject', 'some long summary', 'www.example.com')
print test.getGuid()

stringi = 'ramoons.mp3'
print stringi.endswith('ms.mp3')

# PROBLEM 2
word = 'soft'
text = 'Downey makes my clothes the softest they can be!'
word = word.lower()
text = text.lower()
for punct in string.punctuation: # replace successively every punctuation in string.punctuation with a " "
    text = text.replace(punct, ' ')
    
text_list = [e for e in text.split(' ') if len(e) > 0] # Get rid of elements with zero length (double spaces)

print 'returning...', word in text_list # True/False