from manos import mezclar, repartir, descartar

b = mezclar()

m1, m2, m3, m4, b = repartir(b)

def grande(m1, m2, m3, m4, envite):
    puntos = [0, 0, 0, 0]
    for m, i in zip([m1, m2, m3, m4], range(4)):
        for c in m:
            puntos[i] += 4**int(c)
    maximo = max(puntos)
    maximo_indices = [i for i, p in enumerate(puntos) if p == maximo]
    
    piedras = [0, 0, 0, 0]
    if len(maximo_indices) < 1:
        piedras[maximo_indices] += envite
    piedras[maximo_indices[0]] += envite
    return piedras

def pequeñas(m1, m2, m3, m4, envite):
    puntos = [0, 0, 0, 0]
    for m, i in zip([m1, m2, m3, m4], range(4)):
        for c in m:
            puntos[i] += 4**(10-int(c))
    maximo = max(puntos)
    maximo_indices = [i for i, p in enumerate(puntos) if p == maximo]
    
    piedras = [0, 0, 0, 0]
    if len(maximo_indices) < 1:
        piedras[maximo_indices] += envite
    piedras[maximo_indices[0]] += envite
    return piedras

def pares(m1, m2, m3, m4, envite):
    puntos = [0, 0, 0, 0]
    par = [0, 0, 0, 0]
    for i, m in enumerate([m1, m2, m3, m4]):
        for c in list(set(m)):
            if m.count(c) > 1:
                if m.count(c) == 4:
                    par[i] += 3
                    puntos[i] += (100+10*int(c))**3
                elif m.count(c) == 3:
                    par[i] += 2
                    puntos[i] += (100+10*int(c))**2
                elif m.count(c) == 2:
                    if len(list(set(m))) == 3:
                        par[i] += 1
                        puntos[i] += (100+10*int(c))
                    else:
                        par[i] += 3
                        other_card = list(set(m))[0] if list(set(m))[1] == c else list(set(m))[1]
                        if int(c) > int(other_card):
                            puntos[i] += (100 + 10 * int(c) - 10 + int(other_card)) ** 3
                        else:
                            puntos[i] += (100 + 10 * int(other_card) - 10 + int(c)) ** 3
                break
    maximo = max(puntos)
    maximo_indices = [i for i, p in enumerate(puntos) if p == maximo]

    piedras = [0, 0, 0, 0]
    if len(maximo_indices) > 1:
        if len(maximo_indices) == 4:
            return piedras
        piedras[maximo_indices[0]] += envite
    else:
        piedras[maximo_indices[0]] += envite
    
    for i in range(len(piedras)):
        if piedras[i] == envite:
            piedras[i] += par[i]
            piedras[(i + 2) % 4] += par[(i + 2) % 4]

    if piedras == [0, 0, 0, 0]:
        piedras[maximo_indices[0]] += par[maximo_indices[0]]
        piedras[(maximo_indices[0] + 2) % 4] += par[(maximo_indices[0] + 2) % 4]
        
    return piedras

def juego(m1, m2, m3, m4, envite):
    puntos = [0, 0, 0, 0]
    pts_juego = [0, 0, 0, 0]
    for i, m in enumerate([m1, m2, m3, m4]):
        pts = 0
        for c in m:
            if int(c) in [10, 9, 8]:
                pts += 10
            else:
                pts += int(c)
        if pts in [32, 31]:
            pts += 10
        puntos[i] = pts
        if pts > 30:
            pts_juego[i] += 2
        if pts == 41:
            pts_juego[i] += 1

    maximo = max(puntos)
    maximo_indices = [i for i, p in enumerate(puntos) if p == maximo]

    piedras = [0, 0, 0, 0]
    if len(maximo_indices) > 1:
        if len(maximo_indices) == 4:
            return piedras
        piedras[maximo_indices[0]] += envite
    else:
        piedras[maximo_indices[0]] += envite
    
    for i in range(len(piedras)):
        if piedras[i] == envite:
            piedras[i] += pts_juego[i]
            piedras[(i + 2) % 4] += pts_juego[(i + 2) % 4]
        
    return piedras

def suma_ronda(m1, m2, m3, m4, envites):
    grande_piedras = grande(m1, m2, m3, m4, envites[0])
    pequeñas_piedras = pequeñas(m1, m2, m3, m4, envites[1])
    pares_piedras = pares(m1, m2, m3, m4, envites[2])
    juego_piedras = juego(m1, m2, m3, m4, envites[3])
    piedras = [0, 0, 0, 0]
    for i in range(4):
        piedras[i] = grande_piedras[i] + pequeñas_piedras[i] + pares_piedras[i] + juego_piedras[i]

    return piedras

print(m1, m2, m3, m4)
print(suma_ronda(m1, m2, m3, m4, [[2,2,2,2], [2,2,2,2], [2,2,2,2], [2,2,2,2]]))
