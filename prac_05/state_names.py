"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD":"Queensland", "NSW": "New South Wales", "NT" : "Northern Territory", "WA" : "Western Australia",
            "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
length_of_code = max(len(i) for i in CODE_TO_NAME)
for code in CODE_TO_NAME:
    print(f"{code:{length_of_code}} is {CODE_TO_NAME[code]}")

