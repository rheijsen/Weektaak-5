import matplotlib.pyplot as plt


def lees_inhoud(bestand):
    regels = bestand.readlines()
    data = []
    for regel in regels:
        record = regel.strip().split()
        data.append(record)
    del data[-1]
    counter = 0
    for _ in data:
        del data[counter][0]
        counter += 1
    return data


def sorteer_data(data):
    hiv1 = []
    hiv2 = []
    siv = []
    sivmnd2 = []
    counter = 0
    for i in data:
        if "HIV-1_" in i[0] or "hiv-1_orgineel" in i[0]:
            hiv1.append(data[counter])
            counter += 1
            del i[0]
        elif "HIV-2_" in i[0] or "hiv-2_orgineel" in i[0]:
            hiv2.append(data[counter])
            counter += 1
            del i[0]
        elif "SIV_" in i[0] or "siv_orgineel" in i[0]:
            siv.append(data[counter])
            counter += 1
            del i[0]
        elif "SIVmnd-2_" in i[0] or "sivmnd-2_orgineel" in i[0]:
            sivmnd2.append(data[counter])
            counter += 1
            del i[0]
    return hiv1, hiv2, siv, sivmnd2


def samenvoegen(hiv1, hiv2, siv, sivmnd2):
    hiv1_nieuw = []
    hiv2_nieuw = []
    siv_nieuw = []
    sivmnd2_nieuw = []
    for i in hiv1:
        for j in i:
            hiv1_nieuw.append(float(j))
    for i in hiv2:
        for j in i:
            hiv2_nieuw.append(float(j))
    for i in siv:
        for j in i:
            siv_nieuw.append(float(j))
    for i in sivmnd2:
        for j in i:
            sivmnd2_nieuw.append(float(j))
    return hiv1_nieuw, hiv2_nieuw, siv_nieuw, sivmnd2_nieuw


def maken_histogram(hiv1_nieuw, hiv2_nieuw, siv_nieuw, sivmnd2_nieuw):
    plt.hist(hiv1_nieuw, bins=50)
    plt.ylabel("Aantal")
    plt.xlabel("Percentage")
    plt.title("Aantal overeenkomsten per percentage HIV-1")
    plt.show()


if __name__ == "__main__":
    bestand = open("clustalO_resultaten", "r")
    data = lees_inhoud(bestand)
    hiv1, hiv2, siv, sivmnd2 = sorteer_data(data)
    hiv1_nieuw, hiv2_nieuw, siv_nieuw, sivmnd2_nieuw = samenvoegen(hiv1, hiv2, siv, sivmnd2)
    maken_histogram(hiv1_nieuw, hiv2_nieuw, siv_nieuw, sivmnd2_nieuw)