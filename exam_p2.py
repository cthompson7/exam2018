def process_file(file_name):
    """
    Given a file name, returns a list of lists [name, gender, births]
    HINT: https://stackoverflow.com/a/35340988/941742

    :param file_name: a string
    :return: a list of lists, [[name1, gender1, births1], [name2, gender2, births2]...]

    Example:
    process_file('yob1880.txt')
        will return
    [["Mary","F",7065], ["Anna","F",2604],...]

    """
    import csv

    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        your_list = list(reader)

    return your_list


def total_births(year):
    """
    Returns the total number of births in a year.
    :param year: an integer, between 1880 and 2010
    :return: an integer, the total births of all the babies in that year
    """
    file_to_process = 'babynames/yob'+str(year)+'.txt'
    birth_info = process_file(file_to_process)

    sum_of_births = 0
    for birth in birth_info:
        sum_of_births += int(birth[2])
    return sum_of_births


def proportion(name, gender, year):
    """
    :param name: a string, first name
    :param gender: a string, "F" or "M"
    :param year: an integer, between 1880 and 2010
    :return: a floating number, the proportion of babies with the given name to total births in given year
    """
    file_to_process = 'babynames/yob'+str(year)+'.txt'
    birth_info = process_file(file_to_process)

    for birth in birth_info:
        if birth[0] == name and birth[1] == gender:
            return int(birth[2]) / total_births(year)


def highest_year(name, gender):
    """
    :param name: a string
    :param gender: a string, "F" or "M"
    :return: an integer, the year when the given name has the highest proportion over the years (among all the proportions of the same name in different years)
    """
    highest_proportion = 0
    highest_year = 0
    for year in range(1880,2010):
        if not name_in_year(name, year):
            continue
        if proportion(name, gender, year) > highest_proportion:
            highest_proportion = proportion(name, gender, year)
            highest_year = year
    return highest_year


def name_in_year(name, year):
    """
    If name doesn't exist, the highest_year function fails. Needed to have a way to keep checking proportions.
    :param name: a string, first name
    :param year: a string, an integer, between 1880 and 2010
    :return: return True or False if name is in the year
    """
    file_to_process = 'babynames/yob'+str(year)+'.txt'
    birth_info = process_file(file_to_process)

    for birth in birth_info:
        if name == birth[0]:
            return True
    return False


def main():
    year1981 = process_file('babynames/yob1981.txt')
    print(year1981)
    print('The total number of births in 1981 is: {}.'.format(total_births(1981)))
    print('The proportion of births for Christian, Male, in 1981 is: {:.4F}%'.format(100*proportion('Christian', 'M', 1981)))
    print('The highest proportion of births for the name Christian, Male, across all years is: {}.'.format(highest_year('Christian', "M")))


if __name__ == '__main__':
    main()
