# CS 115 - Introduction to Programming in Python Lab Guide 05
Lab Objectives: Tuples, Lists, Dictionaries
1. Write a program that is used to store and retrieve year and title information about movies. Your program should
have the following functions:
load_movies(): takes a file pointer (reference to an opened file) as a parameter. Each line of the file contains the movie year, and the movie name, separated by commas. The function should return a dictionary where the keys are the integer years, and the values are a list of movies produced in that year.
get_movies_by_year(): takes a dictionary of movies and an integer year as parameters. Return a list of the names of movies produced in the given year. If no movies exist, return an empty list.
get_movies_by_keyword(): takes a dictionary of movies and a string keyword. Return a list of tuples where each tuple contains the movie name and movie year for all movies whose name contains the given keyword.
print_list(): takes a list as a parameter and prints each element in the list on a separate line. Use this function to print all lists in question 2 below.
2. Write a script that uses the functions defined above to do the following:
a. Creates a dictionary using the load_movies() function using the file file ‘movie_data.csv’ (a
text file containing comma-separated values) .
b. Inputs a year from the user and displays the names of all movies from the given year.
c. Inputs a keyword from the user and displays the name and year of all movies whose title contains the
keyword given.
Sample Runs:
Enter year to search: 2005
Movies made in 2005:
Elfen Lied
Up and Down
Voyage to the Planets and Beyond
WWE: Royal Rumble 2005
Enter keyword to search: and
(2004, 'Pitcher and the Pin-Up')
(2004, 'The Rise and Fall of ECW')
(1997, 'Zeus and Roxanne')
(1996, "You're Invited to Mary-Kate and Ashley's Vacation Parties")
(1996, 'Young and Dangerous 2')
(2005, 'Up and Down')
(2005, 'Voyage to the Planets and Beyond')
(2002, 'Lilo and Stitch')
(1978, 'Get Out Your Handkerchiefs')
(1992, 'Husbands and Wives')
(1952, 'The Bad and the Beautiful')
(1968, 'Quatermass and the Pit')
Enter year to search: 2018
No movies from 2018 found
Enter keyword to search: turkey
No movies with the keyword "turkey" found
  
