deck_x_axe = []
for x1 in range(0, 750, 50):
    for x2 in range(50, 800, 50):
        deck_x_axe.append((x1, x2))


[(x1, x2) for x1 in range(0, 751, 50), x2 in range(49, 800, 50)]
print(deck_x_axe)
