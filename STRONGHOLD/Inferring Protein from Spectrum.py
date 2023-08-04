path = 'rosalind_spec-2.txt'

pre_mass_table = {71.03711: 'A',
        103.00919: 'C',
        115.02694: 'D',
        129.04259: 'E',
        147.06841: 'F',
        57.02146: 'G',
        137.05891: 'H',
        113.08406: 'I',
        128.09496: 'K',
        131.04049: 'M',
        114.04293: 'N',
        97.05276: 'P',
        128.05858: 'Q',
        156.10111: 'R',
        87.03203: 'S',
        101.04768: 'T',
        99.06841: 'V',
        186.07931: 'W',
        163.06333: 'Y'}

with open(path, 'r') as r:
    mass = []
    for line in r:
        mass.append(float(line.replace('\n', '')))


mass_table = {}
for key in pre_mass_table:
    mass_table[round(key, 4)] = pre_mass_table[key]


ans = ''
for i in range(1, len(mass)):
    m = round(mass[i] - mass[i - 1], 4)
    print(mass[i] - mass[i - 1], m)
    ans += mass_table[m]

print(ans)

