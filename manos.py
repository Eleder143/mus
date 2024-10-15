import random

def mezclar():
    b = [(n) for n in ['1', '1', '10', '4', '5', '6', '7', '8', '9', '10'] for p in ['O', 'C', 'E', 'B']]
    return random.sample(b, len(b))

def repartir(b):
    manos = [b[i:i+4] for i in range(0, 16, 4)]
    return manos[0], manos[1], manos[2], manos[3], b[16:]

def descartar(mano, descartes):
    m = [mano[i] for i in range(4) if i not in descartes]
    descarted = [mano[i] for i in range(4) if i in descartes]
    return m, descartes

