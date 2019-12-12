word = "ssdf sdfaa"
words = word.split()
print(words)
dictionary = {"a":" ","e":" ","i":" ","o":" ","u":" "}
list = []
for i in word:
    list.append(dictionary.get(i,i))
sent = "".join(list)
print(sent)
