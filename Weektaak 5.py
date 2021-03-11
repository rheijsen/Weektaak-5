import random
from textwrap import wrap


def lees_inhoud(bestand):
    with open(bestand) as fasta:
        seq = "".join(line.rstrip() for line in fasta)
    return seq


def split_seq(seq):
    seq_split = wrap(seq, 1)
    return seq_split


def random_seq(seq_split):
    c = 1
    seq_list = []
    while c < 101:
        seq = ""
        random.shuffle(seq_split)
        for i in seq_split:
            seq += i
        seq_list.append(seq)
        c += 1
    print(seq_list[10])
    return seq_list


if __name__ == "__main__":
    bestand = "oppervlakte hiv-1"
    seq = lees_inhoud(bestand)
    seq_split = split_seq(seq)
    seq_list = random_seq(seq_split)