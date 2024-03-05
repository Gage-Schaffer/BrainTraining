"""
This is a fun little program that spits the most popular baby names in 2011 from
New York City's birth registry, obtained from
data.gov

https://catalog.data.gov/dataset/popular-baby-names

"""
import csv


def summarize(input_csv):
    total_rows = 0
    total_males = 0
    total_females = 0

    male_names = dict()
    female_names = dict()

    with open(input_csv) as file:
        reader = csv.DictReader(file)

        total_rows = count_entries(reader, file)
        total_males, total_females = count_gender(reader, file)

        parse_names(reader, file, male_names, female_names)

    print("\nMost Popular Baby Names in New York City in 2011\n")
    print(f"Records Iterated: {total_rows}")
    print(f"Total Number of Males: {total_males}")
    print(f"Total Number of Females: {total_females}")
    print("")
    print("Most Popular Names:")
    print("Name   ", "|", "   Frequency   ")
    print("-------------------------------")
    print(max(male_names, key=male_names.get), "     ", max(male_names.values()))
    print(max(female_names, key=female_names.get), "   ", max(female_names.values()))


def count_entries(reader_dict, file):
    """
    Returns the number of entries in the iterated CSV. Returns the cursor back to the beginning of the file.
    :param reader_dict: The DictReader Object derived from the CSV.
    :param file: The opened file being operated on.
    :return: Count of all entries (int)
    """

    counter = 0
    for line in reader_dict:
        counter += 1
    file.seek(0)
    return counter


def count_gender(reader_dict, file) -> (int, int):
    """
    Iterates through the CSV DictReader object and returns the count of males and females
    from the CSV. Returns the cursor back to the beginning of the file.
    :param reader_dict: The DictReader Object derived from the CSV.
    :param file: The opened file being operated on.
    :return: A tuple containing the male and female counts (male, female)
    """
    counter_male = 0
    counter_female = 0
    for line in reader_dict:
        if line["Year of Birth"] == "2011":
            if line["Gender"] == "MALE":
                counter_male += int(line["Count"])
            if line["Gender"] == "FEMALE":
                counter_female += int(line["Count"])
    file.seek(0)
    return counter_male, counter_female


def parse_names(reader_dict, file, male_names, female_names) -> None:
    for line in reader_dict:
        if line["Year of Birth"] == "2011":
            if line["Gender"] == "MALE":
                if line["Child's First Name"] in male_names:
                    male_names[line["Child's First Name"]] += int(line["Count"])
                else:
                    male_names[line["Child's First Name"]] = int(line["Count"])
            if line["Gender"] == "FEMALE":
                if line["Child's First Name"] in female_names:
                    female_names[line["Child's First Name"]] += int(line["Count"])
                else:
                    female_names[line["Child's First Name"]] = int(line["Count"])
    file.seek(0)
    return


names_csv = "Popular_Baby_Names.csv"
summarize(names_csv)
