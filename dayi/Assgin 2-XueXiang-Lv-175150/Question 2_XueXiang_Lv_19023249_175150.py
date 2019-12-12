print("Name:XueXiang Lv  Student ID:175150  Massey ID:19023249")
        #Name:XueXiang Lv  Student ID:175150  Massey ID:19023249

import random
t = 0

def randomly(lines):          #This function user can randomly choose a movie
    movies=random.choice(lines)
    display.append(movies)   #display and ready for keeping
    return movies

def search():               #This function user can search one movie using one or two words
    movie_name1=input("what is the key word:")
    movie_name2=input("what is the other word:")
    for i in movies_list:
        if movie_name2!="":
            if (movie_name1 in i.lower())and(movie_name2 in i.lower()):     #User input two words
                display.append(i)
                print(i)
                break
        else:
            if (movie_name1 in i.lower()):         #User input one words
                display.append(i)
                print(i)
                break
    return display

def starts():       #This function can search a movie and start with the movie
    for i in range(len(movies_list)):      #Find a movie`s NO.
        if (movie_name3 in movies_list[i])or(movie_name3 == movies_list[i]):
            display.append(movies_list[i])
            t=i
            break
        else:
           print("do not have this movie")
    for j in range(len(movies_list)):   #Output all the movies after the movie
        if t>j:
            continue
        else:
            print(movies_list[j])

def keep(display,favouites):     #This function can make a copy
    for i in display:
        if i in favouites:    # Check if there is any repetition
            continue
        else:
            favouites.append(i)
    return favouites

def Display():       #This function can display all the favouites movie
    for i in favouites:
        print(i)

def clear():     #This function can empty the favouites
    favouites=[]
    return favouites

print("*** Movie Title Explorer ***")
print("  l - load file of movie titles")
print("  r - random movie")
print("  s - search")
print("  sw - starts with")
print("  k - keep - save the last displayed movie title to your favourites")
print("  f - favourites display")
print("  c - clear favouites")
print("  q - quit")
display=[]    # other list
favouites=[]   #define a list about favouites
while True:
    Choice=input("commend:?")
    if Choice=="l":
       file = open("movies.txt", "r")     #open the file
       movies_list = file.readlines()
       file.close()
       while True:
           print("*** Movie Title Explorer ***")
           print("  l - load file of movie titles")
           print("  r - random movie")
           print("  s - search")
           print("  sw - starts with")
           print("  k - keep - save the last displayed movie title to your favourites")
           print("  f - favourites display")
           print("  c - clear favouites")
           print("  q - quit")
           choice=input("commend:?")
           if choice=="r":
              print(randomly(movies_list))
           elif choice=="s":
               search()
           elif choice=="sw":
               movie_name3=input("what is the movie`s name:")
               starts()
           elif choice=="k":
               favouites=keep(display,favouites)
               display=[]
           elif choice=="f":
               Display()
           elif choice=="c":
               favouites=clear()
           elif choice=="q":  #Quit the Internal circulation
               break
           else:
               print("An error instruction ")
               continue
    else:
        print("your must input 'l' at frist")    #unit you inpur "l" ,implement the Internal circulation
        continue
    break      #Quit the loops


