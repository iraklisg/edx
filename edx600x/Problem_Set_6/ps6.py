# 6.00x Problem Set 6
# RSS Feed Filter

import feedparser
import string
import time
from project_util import translate_html
from Tkinter import *


#-----------------------------------------------------------------------
#
# Problem Set 6

#======================
# Code for retrieving and parsing RSS feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret
#======================

#======================
# Part 1
# Data structure design
#======================

# Problem 1

# TODO: NewsStory
class NewsStory(object):
    '''
    A general class
    
    '''
    def __init__(self, guid, title, subject, summary, link):
        assert type(guid) and type(title) and type(subject) and type(summary) and type(link) == str
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link
        
    def getGuid(self):
        return self.guid
    
    def getTitle(self):
        return self.title
        
    def getSubject(self):
        return self.subject
        
    def getSummary(self):
        return self.summary
        
    def getLink(self):
        return self.link
        

#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

# Whole Word Triggers
# Problems 2-5

# TODO: WordTrigger
class WordTrigger(Trigger):
    '''
    '''
    def __init__(self, word):
        assert type(word) == str
        self.word = word.lower()
        
    def isWordIn(self,text):
        '''takes in one string argument text.
        It returns True if the whole word word is present in text, False otherwise.
        This method should not be case-sensitive.
        
        ''' 
        text = text.lower()
        assert type(text) == str
        for punct in string.punctuation: # replace successively every punctuation in string.punctuation with a " "
            text = text.replace(punct, ' ')
        text_list = [e for e in text.split(' ') if len(e) > 0] # Get rid of elements with zero length (double spaces)
        return self.word in text_list # True/False

# TODO: TitleTrigger
class TitleTrigger(WordTrigger):
    '''fires when a news item's title contains a given word'''
    def evaluate(self, news_story_object):
        assert type(news_story_object) == NewsStory
        return self.isWordIn(news_story_object.getTitle())
    
# TODO: SubjectTrigger
class SubjectTrigger(WordTrigger):
    def evaluate(self, news_story_object):
        assert type(news_story_object) == NewsStory
        return self.isWordIn(news_story_object.getSubject())
    
# TODO: SummaryTrigger
class SummaryTrigger(WordTrigger):
    def evaluate(self, news_story_object):
        assert type(news_story_object) == NewsStory
        return self.isWordIn(news_story_object.getSummary())
    


# Composite Triggers
# Problems 6-8

# TODO: NotTrigger
class NotTrigger(Trigger):
    '''
    This trigger should produce its output by inverting the output of another trigger.
    The NOT trigger should take this other trigger as an argument to its constructor
    (why its constructor? Because we can't change what parameters evaluate takes in...that'd break our polymorphism).
    So, given a trigger T and a news item x,
    the output of the NOT trigger's evaluate method should be equivalent to not T.evaluate(x).
    
    '''
    def __init__(self,trigger):
#        assert isinstance(trigger, Trigger)
        self.trigger = trigger
    
    def evaluate(self, news_story_object):
        assert isinstance(news_story_object, NewsStory)
        return not self.trigger.evaluate(news_story_object)

# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self,trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2
        
    def evaluate(self, news_story_object):
        assert isinstance(news_story_object, NewsStory)
        return self.trigger1.evaluate(news_story_object) and self.trigger2.evaluate(news_story_object)
# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self,trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2
        
    def evaluate(self, news_story_object):
        assert isinstance(news_story_object, NewsStory)
        return self.trigger1.evaluate(news_story_object) or self.trigger2.evaluate(news_story_object)


# Phrase Trigger
# Question 9

# TODO: PhraseTrigger
class PhraseTrigger(Trigger):
    '''  fires when a given phrase is in any of the story's subject, title, or summary '''
    def __init__(self, phrase):
        assert type(phrase) == str
        self.phrase = phrase
    
    def evaluate(self, news_story_object):
        return self.phrase in news_story_object.getSubject() or self.phrase in news_story_object.getTitle() or self.phrase in news_story_object.getSummary()
        


#======================
# Part 3
# Filtering
#======================

def filterStories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder (we're just returning all the stories, with no filtering)
    triggered_stories = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story) == True:
                triggered_stories.append(story)
                break
        
    stories = triggered_stories
    return stories

#======================
# Part 4
# User-Specified Triggers
#======================

def makeTrigger(triggerMap, triggerType, params, name):
    """
    Takes in a map of names to trigger instance, the type of trigger to make,
    and the list of parameters to the constructor, and adds a new trigger
    to the trigger map dictionary.

    triggerMap: dictionary with names as keys (strings) and triggers as values
    triggerType: string indicating the type of trigger to make (ex: "TITLE")
    params: list of strings with the inputs to the trigger constructor (ex: ["world"])
    name: a string representing the name of the new trigger (ex: "t1")

    Modifies triggerMap, adding a new key-value pair for this trigger.

    Returns a new instance of a trigger (ex: TitleTrigger, AndTrigger).
    """
    # TODO: Problem 11
    if triggerType == 'TITLE':
        triggerMap[name] = TitleTrigger("".join(params))
    elif triggerType == 'SUBJECT':
        triggerMap[name] = SubjectTrigger("".join(params))
    elif triggerType == 'SUMMARY':
        triggerMap[name] = SummaryTrigger("".join(params))
    elif triggerType == 'NOT':
        triggerMap[name] = NotTrigger(triggerMap["".join(params)])
    elif triggerType == 'AND':
        triggerMap[name] = AndTrigger(triggerMap["".join(params[0])], triggerMap["".join(params[1])])
    elif triggerType == 'OR':
        triggerMap[name] = OrTrigger(triggerMap["".join(params[0])], triggerMap["".join(params[1])])
    elif triggerType == 'PHRASE':
        triggerMap[name] = PhraseTrigger(" ".join(params))
#    else: raise ValueError('not correct type of trigger')
    
    return triggerMap[name]

def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """

    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    triggers = []
    triggerMap = {}

    # Be sure you understand this code - we've written it for you,
    # but it's code you should be able to write yourself
    for line in lines:

        linesplit = line.split(" ")

        # Making a new trigger
        if linesplit[0] != "ADD":
            trigger = makeTrigger(triggerMap, linesplit[1], #(triggerMap, triggerType, params, name)
                                  linesplit[2:], linesplit[0])

        # Add the triggers to the list
        else:
            for name in linesplit[1:]:
                triggers.append(triggerMap[name])

    return triggers
    
import thread

SLEEPTIME = 60 #seconds -- how often we poll


def main_thread(master):
    # A sample trigger list - you'll replace
    # this with something more configurable in Problem 11
    try:
        # These will probably generate a few hits...
        t1 = TitleTrigger("Obama")
        t2 = SubjectTrigger("Romney")
        t3 = PhraseTrigger("Election")
        t4 = OrTrigger(t2, t3)
        triggerlist = [t1, t4]
        
        # TODO: Problem 11
        # After implementing makeTrigger, uncomment the line below:
        triggerlist = readTriggerConfig("triggers.txt")

        # **** from here down is about drawing ****
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)
        
        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)

        # Gather stories
        guidShown = []
        def get_cont(newstory):
            if newstory.getGuid() not in guidShown:
                cont.insert(END, newstory.getTitle()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.getSummary())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.getGuid())

        while True:

            print "Polling . . .",
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

            # Process the stories
            stories = filterStories(stories, triggerlist)

            map(get_cont, stories)
            scrollbar.config(command=cont.yview)


            print "Sleeping..."
            time.sleep(SLEEPTIME)

    except Exception as e:
        print e


if __name__ == '__main__':

    root = Tk()
    root.title("Some RSS parser")
    thread.start_new_thread(main_thread, (root,))
    root.mainloop()

