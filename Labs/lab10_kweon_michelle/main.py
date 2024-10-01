# Michelle Kweon, mkweon@usc.edu
# ITP 115, Fall 2021
# Section: Boba
# Lab 10

# function: read_file
# parameter: file_name with a default value of story.txt
# return value: dictionary where keys are words (strings) and
# values are lists with line numbers (integers)
def read_file(file_name="story.txt"):
    # create a dictionary
    words_dict = {}

    # open the file
    file_in = open(file_name, "r")

    # create a variable for the line number
    line_num = 1

    # read the file obj and loop through each line
    for line in file_in:
        line = line.strip()
        line_list = line.split()  # whitespace
        # line_list is a list of words

        # loop through each word in the line
        for word in line_list:
            word = word.lower()
            # get rid of punctuation around word
            # .,::?'
            word = word.strip(".,;:?'")

            # add to or update in dictionary
            if word in words_dict:
                # update the value by appending the line number
                # value is a list
                words_dict[word].append(line_num)
            else:  # not in the dictionary
                # add the word to the dictionary
                # dict[key] = value
                # value is a list of line numbers
                words_dict[word] = [line_num]
        # after the 'for word' loop
        # update line number
        line_num += 1

    # close the file
    file_in.close()

    # return the dictionary
    return words_dict

# function: sort_keys
# parameter: dictionary
# return value: a list of sorted keys from dictionary
def sort_keys(dictionary):
    keys = dictionary.keys()
    keys_list = list(keys)
    keys_list.sort()
    return keys_list

def main():
    story_dict = read_file()
    story_keys = sort_keys(story_dict)
    print("Here is the concordance for the file 'story.txt':")
    # use the list of sorted keys for printing
    for key in story_keys:
        print(key + ":", story_dict[key])

main()