from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#

def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    # Create a new variable to store the maximum score seen so far (initially 0)
    best_score = 0
    # Create a new variable to store the best word seen so far (initially None)  
    best_word = None
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        is_a_valid_word = True
        temp_hand = hand.copy()
        for letter in word:
            if temp_hand.has_key(letter) == False or temp_hand.get(letter) <= 0:
                is_a_valid_word = False
            else:
                temp_hand[letter] = temp_hand.get(letter) - 1
        if is_a_valid_word is True:
# ALTERNATIVE        
#        if isValidWord(word, hand, wordList): 
            # Find out how much making that word is worth
            word_score = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if word_score > best_score:
                # Update your best score, and best word accordingly
                best_score = word_score
                best_word = word
    # return the best word you found.
    return best_word

#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # TO DO ... <-- Remove this comment when you code this function
    # Keep track of the total score
    total_score = 0
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0:
        # Display the hand
        print 'Current Hand: ',
        displayHand(hand)
        # Computer chooses a word
        com_word = compChooseWord(hand, wordList, n)
# I had to perform this test in case compChooseWord() doesn't find any valid word and return best_word = None !!!!!!!!!!!!!!!!
        if com_word == None:
            break
        # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
        total_score += getWordScore(com_word, n)
        print '"%s" earned %s points. Total: %s points'%(com_word, getWordScore(com_word, n), total_score)
        print ""
        # Update the hand 
        hand = updateHand(hand, com_word)
    print 'Total score: %s points'%(total_score)
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # TO DO... <-- Remove this comment when you code this function
    print "playGame not ywordet implemented." # <-- Remove this when you code this function
    n = HAND_SIZE
    hand = {}
    flag = ""
    while True:
        flag = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        print
        if flag == 'n':
            while True:
                user_or_pc = raw_input('Enter u to have yourself play, c to have the computer play: ')
                if user_or_pc == 'u':
                    hand =  dealHand(n)
                    playHand(hand, wordList, n)
                    break
                elif user_or_pc == 'c':
                    hand =  dealHand(n)
                    compPlayHand(hand, wordList, n)
                    break
                else:
                    print 'Invalid command.'
        elif flag == 'r' and hand == {}:
            print 'You have not played a hand yet. Please play a new hand first!'
            print
        elif flag == 'r' and hand != {}:
            user_or_pc = raw_input('Enter u to have yourself play, c to have the computer play: ')
            while True:
                if user_or_pc == 'u':
                    playHand(hand, wordList, n)
                    break
                elif user_or_pc == 'c':
                    compPlayHand(hand, wordList, n)
                    break
                else:
                    print 'Invalid command.'
        elif flag == 'e':
            break
        else:
            print 'Invalid command.'
            print
            

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


