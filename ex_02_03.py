counts = dict()

for line in open(r'q4_urls.txt', encoding="utf8"):
    cline = line.strip()
    counts[cline] = counts.get(cline, 0) + 1

counts = dict(sorted(counts.items(), key=lambda x:x[1], reverse=True))



out = open('new.txt', "w", encoding="utf8")

for line in counts:
    out.write(f"{line}; {counts[line]}\n")
