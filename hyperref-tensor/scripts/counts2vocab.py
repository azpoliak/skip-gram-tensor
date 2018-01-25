from collections import Counter

from docopt import docopt

from representations.matrix_serializer import save_count_vocabulary


def main():
    args = docopt("""
    Usage:
        counts2pmi.py <counts>
    """)
    
    counts_path = args['<counts>']

    words = Counter()
    contexts = Counter()
    relations = Counter()
    with open(counts_path) as f:
        for line in f:
            split = line.strip().split()
            if len(split) == 4:
                count, word, context, relation  = split
            else:
                count, word, context = split
                relation = None
            count = int(count)
            words[word] += count
            contexts[context] += count
            relations[relation] += count

    words = sorted(words.items(), key=lambda (x, y): y, reverse=True)
    contexts = sorted(contexts.items(), key=lambda (x, y): y, reverse=True)
    relations = sorted(relations.items(), key=lambda (x, y): y, reverse=True)

    save_count_vocabulary(counts_path + '.words.vocab', words)
    save_count_vocabulary(counts_path + '.contexts.vocab', contexts)
    save_count_vocabulary(counts_path + '.relations.vocab', relations)


if __name__ == '__main__':
    main()
