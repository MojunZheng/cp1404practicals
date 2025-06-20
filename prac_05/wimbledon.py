import csv

dict_champions = {}
info = []


def main():
    """call and pass data to functions"""
    filename = "wimbledon.csv"
    wimbledon_winners = get_file(filename)
    dict_count_champions, win_countries = count_champions(wimbledon_winners)
    display_countries(win_countries, dict_count_champions)

def get_file(filename):
    """read the file"""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        record = csv.reader(in_file)
        next(record)
        for i in record:
            info.append(i)
    return info
