FILENAME = "subject_data.txt"


def main():
    datas = load_data()
    display_data(datas)


def load_data():

    datas = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)
        print(repr(line))
        line = line.strip()
        parts = line.split(',')
        print(parts)
        parts[2] = int(parts[2])
        print(parts)
        datas.append(parts)
        print("----------")
    input_file.close()
    return datas

def display_data(datas):
    for i in datas:
        course, name, number = i
        print(f"{course:<6} is taught by {name:<12} and has {number:<3} students")



main()