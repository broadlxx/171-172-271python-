import time

# Load file of words, one word per line
def read_word_file(filename):
    wordlist = []
    with open(filename, 'r') as f:
        while True:
           word = f.readline().strip()
           if word == '':  # END OF FILE
               break
           wordlist.append(word)

    print("%d Words read from %s" % (len(wordlist), filename))
    return wordlist

#=======================================================================
# A small wordlist so almost any algorithm will work

short_wordlist = [ 'not', 'on', 'you', 'this', 'but', 'his', 'from',
     'like', 'time', 'no', 'some', 'them', 'see', 'other', 'than',
     'then', 'now', 'look', 'its', 'over', 'also', 'after', 'use',
     'rat', 'raw', 'way', 'even', 'new', 'want', 'any', 'give', 'day',
     'most', 'us', 'tea', 'eat', 'sit', 'ate', 'stop', 'tops', 'post',
     'item', 'ton', 'sit', 'war']
#=======================================================================


def sort_dictionary(list):
    dictionary = {}
    for i in list:
        word = "".join(sorted(i))

        if word in dictionary:
           dictionary[word].append(i)
        else:
            dictionary[word] = [i]
    return dictionary

def printout(dictionary):
    dic = {}
    number = 0
    for i in dictionary:
        if len(dictionary[i]) > number:
            number = len(dictionary[i])
        if len(dictionary[i]) in dic:
            dic[len(dictionary[i])].append(dictionary[i])
        else:
            dic[len(dictionary[i])] = [dictionary[i]]
    for i in range(number):
        print("Anagrams classes of length %d"%(number-i) + "\n")
        for j in dic[number - i]:
               print(j)
        if (number - i ) == 1:
            break
        choice=input("Continue (y/n):" )
        if choice == "n":
            break

# When your program works with the short list, download 'words-v2.txt'
# from Stream and save it in the same directory as your .py file.  Then
# uncomment the 'read_word_file()' line below and try finding all the
# anagrams in 233,000 words.

#wordlist = short_wordlist
start_time = time.time()
wordlist = read_word_file('words.txt')
dictionary = sort_dictionary(wordlist)
#>>>>>>>>>>>> YOUR CODE GOES IN HERE
# print('Start of Wordlist: ', wordlist[:10])
#>>>>>>>>>>>> END OF YOUR CODE

end_time = time.time()
print("The program took %0.4f seconds" %
         ( end_time-start_time))
printout(dictionary)
# Now display the anagram classes

