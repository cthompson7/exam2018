import string

def process_file_roster(filename):
    """
    Read roster.txt file in and only return the first name listed.
    :param filename: a string
    :return: a list of student first names [Angela, Alden, etc..]
    """
    hist = []
    fp = open(filename, encoding="utf8")

    strippable = string.punctuation + string.whitespace
    for line in fp:
        for word in line.split():
                word = word.strip(strippable)
                word = word.lower()

                hist.append(word)

    return hist[::2]


def process_file_positive_words(filename):
    '''
    Read positive-words.txt file in and return the words in the file in a list.
    :param filename: string
    :return: a list of positive words
    '''
    hist = []
    fp = open(filename, encoding="utf8")

    strippable = string.punctuation + string.whitespace
    for line in fp:
        for word in line.split():
                word = word.strip(strippable)
                word = word.lower()

                hist.append(word)

    return hist


def get_value(name):
    '''
    Get the sum value of all the letters in a name.
    :param name: string
    :return: sum value
    '''
    sum = 0
    for i in name:
        sum += ord(i) - 96
    return sum


def who_has_highest_value(name_list):
    """
    Determine who has the highest sum value for their first name in the roster.
    :param name_list: list
    :return: The highest value and name
    """
    highest_value = 0
    highest_name = ''
    for name in name_list:
        # print(name,get_value(name))
        if get_value(name) > highest_value:
            highest_value = get_value(name)
            highest_name = name

    return highest_value,highest_name


def get_words_with_same_value(given_name, word_list):
    '''
    Returns the words with the same sum value as the given name.
    :param given_name: string
    :param word_list: list
    :return:
    '''
    listOfSimilarWords = []
    for word in word_list:
        if get_value(given_name) == get_value(word):
            listOfSimilarWords.append(word)

    listOfSimilarWordsString = str(listOfSimilarWords)[1:-1]
    listOfSimilarWordsString = listOfSimilarWordsString.replace("'", "")

    if listOfSimilarWordsString == "":
        listOfSimilarWordsString = None

    return given_name, listOfSimilarWordsString


def main():
    r = process_file_roster('roster.txt')
    pw = process_file_positive_words('positive-words.txt')
    print(r)
    print(pw)
    print('')
    print('The sum value of Zirui is: ' + str(get_value('zirui')))
    print('')
    highest_value, highest_name = who_has_highest_value(r)
    print('The highest sum value is: {}. The highest name is: {}'.format(highest_value, highest_name))
    print('')
    given_name, listOfSimilarWordsString = get_words_with_same_value('christian', pw)
    print('Student Name: {}. \nWords Equal to Name: {}.'.format(given_name, listOfSimilarWordsString))
    # print("Student Name: {} \nWords Equal to Name: {}" + get_words_with_same_value('christian', r, pw))

if __name__ == '__main__':
    main()
