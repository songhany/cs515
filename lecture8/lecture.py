preference = {
    "Emily": ["Evanescence", "Him", "Cem Adrian", "Maneskin", "Emily Sande"],
    "Mary": ["Dua Lipa", "Billie Eilish", "Bruno Mars"],
    "Joe": ["Metallica", "ACDC", "Bon Jovi", "Nirvana"]
}

def read_preference(filename):
    dic = {}
    with open(filename, "r") as f:
        for line in f:
            [username, singers] = line.strip().split(':')
            singersList = singers.split(",")
            dic[username] = singersList
    return dic


