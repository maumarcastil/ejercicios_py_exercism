def distance(strand_a, strand_b):
    if (len(strand_a) != len(strand_b)):
        raise ValueError("Lengths Aren't the Same")
    return sum([strand_a[x] != strand_b[x] for x in range(len(strand_a))])
