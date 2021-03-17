def czas(imie, numer_zadania, czas_wykonania_msec):
    #print(imie + " wykonal zadanie nr " + str(numer_zadania) + " w " + str(czas_wykonania / 1000) + "s")
    
    czas_wykonania_sec = czas_wykonania_msec / 1000

    return f"{imie} wykonal(a) zadanie nr {numer_zadania} w {czas_wykonania_sec:.3f}s"

print(czas("Igor", 2, 3500))