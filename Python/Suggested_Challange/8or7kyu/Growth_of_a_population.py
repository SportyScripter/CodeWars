def nb_year(p0, percent, aug, p):
    years = 0
    while p0 < p:
        p0 = p0 + p0 * percent/100 + aug
        years += 1
    return years +1

print(nb_year(1500, 5, -5, 5000))
print(nb_year(1500000, 2.5, 10000, 2000000))
print(nb_year(1500000, 0.25, 1000, 2000000))




