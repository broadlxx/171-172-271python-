print("Name:XueXiang Lv  Student ID:175150  Massey ID:19023249")
        #Name:XueXiang Lv  Student ID:175150  Massey ID:19023249

import random

t = 0

def randomly(lines):
    movies=random.choice(lines)
    display.append(movies)
    return movies

def search():
    movie_name1=input("what is the key word:")
    movie_name2=input("what is the other word:")
    for i in movies_list:
        if movie_name2!="\n":
            if (movie_name1 in i.lower())and(movie_name2 in i.lower()):
                display.append(i)
                print(i)
        else:
            if (movie_name1 in i.lower()):
                display.append(i)
                print(i)
    return favouites

def starts():
    movie_name3=input("what is the movie`s name:")
    for i in range(len(movies_list)):
        if movie_name3 in movies_list[i]:
            display.append(movies_list[i])
            t=i
            print(t)
            break
        else:
            return
    for j in range(len(movies_list)):
        if t>j:
            continue
        else:
            print(movies_list[j])

def keep(display,favouites):
    for i in display:
        if i in favouites:
            continue
        else:
            favouites.append(i)
    return favouites

def display():
    print(favouites)

def clear(favouites):
    favouites=[]
    return favouites

display=[]
favouites=[]

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
    Choice=input("commend:?")
    if (Choice=="l")and(Choice!="q"):
       file = open("movies.txt", "r")
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
               starts()
           elif choice=="k":
               keep(display,favouites)
           elif choice=="f":
               favouites=display()
           elif choice=="c":
               clear(favouites)
           elif choice=="q":
               break
    else:
        print("your must input 'l' at frist")
        continue
    break

