import csv

dict_champions = {}
info = []


def main():
    """call and pass data to functions"""
    filename = "wimbledon.csv"
    wimbledon_winners = get_file(filename)
    dict_count_champions, win_countries = count_champions(wimbledon_winners)
    display_countries(win_countries, dict_count_champions)

