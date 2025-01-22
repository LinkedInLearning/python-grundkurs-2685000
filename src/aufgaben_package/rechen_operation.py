def erhoehe_um_zwei(zahl):
    return zahl + 2

def multipliziere_mit_drei(zahl):
    return zahl * 3

def subtrahiere_zehn(zahl):
    return zahl - 10

def teile_durch_vier(zahl):
    if zahl % 4 != 0:
        raise ValueError("Zahl muss durch 4 teilbar sein")
    return zahl / 4
