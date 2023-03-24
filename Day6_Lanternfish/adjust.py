def adjust_lantenfish(lanternfish):
    i = 0
    for k in range(len(lanternfish)):
        if lanternfish[k] == 0:
            lanternfish[k] = 6
            i = i + 1
        else:
            lanternfish[k] = lanternfish[k] - 1
    for j in range(i):          #ovoliko novih lanternfisha se napravilo
        lanternfish.append(8)




