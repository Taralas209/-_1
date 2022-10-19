with open('regions.csv', encoding='utf-8') as region_f:
    regions = set()
    for line in region_f:
        line = line.strip()
        rline = (line.replace('"', ''))
        regions.add(rline)