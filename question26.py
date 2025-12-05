import itertools
import math

hcf_values = []

items = list(range(1, 11))
seen = set()
splits = []

for combo in itertools.combinations(items, 5):
    g1 = tuple(sorted(combo))
    g2 = tuple(sorted(x for x in items if x not in g1))

    pair = tuple(sorted([g1, g2]))
    if pair not in seen:
        seen.add(pair)
        splits.append(pair)

for split in splits:
    hcf = math.gcd(math.prod(split[0]), math.prod(split[1]))
    print(hcf)
    hcf_values.append(hcf)

print(sum(set(hcf_values)))