# Michelle Kweon, mkweon@usc.edu
# ITP 115, Fall 2021
# Section: Boba
# Lab 9

# function: read_file
# parameter 1: user_genre
# parameter 2: file_name is a string with a default value of "shows.csv"
# return value: a list of shows where the user's genre is inside of the show's genre
def read_file(user_genre, file_name="shows.csv"):
    show_list = []
    open_file = open(file_name)
    for line in open_file:
        line = line.strip()
        info_list = line.split(",")
        show_genre = info_list[1]
        if user_genre in show_genre:
            show_list.append(info_list[0])
    open_file.close()
    show_list.sort()
    return show_list

# function: write_file
# parameter 1: genre is a string
# parameter 2: show_list is a list of shows (variable name doesn't have to be repeated)
# return value: None
# write the list to a file
# the name of the file is the genre + ".txt"
def write_file(genre, show_list):
    name_file = genre + ".txt"
    out_file = open(name_file, "w")
    for show in show_list:
        print(show, file=out_file)
    out_file.close()

def main():
   print("TV shows")
   genre_str = "action & adventure, animation, comedy, documentary, drama, mystery & suspense, science fiction & fantasy"
   print("The possible genres are", genre_str)
   user_genre = input("Enter a genre: ")
   while user_genre not in genre_str:
       user_genre = input("Enter a genre: ")

   shows = read_file(user_genre)
   write_file(user_genre, shows)
   print("The file '" + user_genre +".txt' has the following shows:")
   print(shows)

main()