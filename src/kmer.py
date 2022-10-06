"""Computing kmers of a string."""


def kmer(x: str, k: int) -> list[str]:
    """
    Computer all k-mers of x.

    >>> kmer('agtagtcg', 3)
    ['agt', 'gta', 'tag', 'agt', 'gtc', 'tcg']

    >>> kmer('AGTAGTCG', 3)
    ['agt', 'gta', 'tag', 'agt', 'gtc', 'tcg']
    """
    kmers = []
    for i in range(k, len(x)+1):
        kmers.append(x[i-k:i].lower())
    return kmers

def unique_kmers(x: str, k: int) -> list[str]:
    """
    Compute all unique k-mers of x.

    >>> unique_kmers('agtagtcg', 3)
    ['agt', 'gta', 'tag', 'gtc', 'tcg']

    >>> unique_kmers('AGTAGTCG', 3)
    ['agt', 'gta', 'tag', 'gtc', 'tcg']
    """
    # Hvordan bruge dictionary?

    # Version where the order of the unique kmers is preserved. 
    kmers = kmer(x, k)
    unique = []
    for mer in kmers:
        if mer not in unique:
            unique.append(mer)
    return unique

    # Version where set() is used to extract all unique kmers of x. The
    # unique kmers of x are given in a random order in unique_kmers.
 
    # kmers = kmer(x, k)
    # unique = list(set(kmers))
    # return unique

def count_kmers(x: str, k: int) -> dict[str, int]:
    """
    Computer all k-mers of x and count how often they appear.

    >>> count_kmers('agtagtcg', 3)
    {'agt': 2, 'gta': 1, 'tag': 1, 'gtc': 1, 'tcg': 1}

    >>> count_kmers('AGTAGTCG', 3)
    {'agt': 2, 'gta': 1, 'tag': 1, 'gtc': 1, 'tcg': 1}

    """
    kmers = kmer(x, k)
    d = {}
    for mer in kmers:
        if mer not in d:
            d[mer] = 1
        else:
            d[mer] += 1 
    return d
