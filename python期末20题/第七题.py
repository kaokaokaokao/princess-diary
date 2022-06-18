for i in 'ABCD':
    if (i != 'A') + (i == 'C') + (i == 'D') + (i != 'D') == 3:
        print(f"{i}做了好事!")