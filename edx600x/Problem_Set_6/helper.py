import string

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
        
        return (self.word in text_list) # True/False
        
    def dummy(self):
        return self.word in self.word

# TODO: TitleTrigger
class TitleTrigger(WordTrigger):
    '''fires when a news item's title contains a given word'''
    def evaluate(self, news_story_object):
#        assert type(news_story_object) == NewsStory
        return self.isWordIn(news_story_object.getTitle())
    
# TODO: SubjectTrigger
class SubjectTrigger(WordTrigger):
    def evaluate(self, news_story_object):
#        assert type(news_story_object) == NewsStory
        return self.isWordIn(news_story_object.getSubject())
    
# TODO: SummaryTrigger
class SummaryTrigger(WordTrigger):
    def evaluate(self, news_story_object):
#        assert type(news_story_object) == NewsStory
        return self.isWordIn(news_story_object.getSummary())

a = TitleTrigger('myTitle')
print a.word
b = NewsStory('foo', 'myTitle', 'mySubject', 'some long summary', 'www.example.com')
print a.evaluate(b)
k = WordTrigger('soft')
print 'and returns....',k.isWordIn('Downey makes my clothes the softest they can be!')
print 'and returns....',k.dummy()
t = Trigger()
print t.evaluate(b)
