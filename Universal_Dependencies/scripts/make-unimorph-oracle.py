#!/usr/bin/env python3

from collections import Counter
import csv
from itertools import groupby
import sys

'''
Make a QVEC oracle from a UniMorph table.

Usage: make-unimorph-oracle.py Unimorph_Table.csv > outfile
'''

def make_oracle(unimorph_table):
  with open(unimorph_table, encoding='utf-8') as fin:
    reader = csv.reader(fin, delimiter=',')

    headings = next(reader)
    # lemma_index = headings.index('page_url')
    infl_index = headings.index('cell_value')

    words = []
    for arr in reader:
      infl = arr[infl_index].strip()
      tags = [i for i in arr[:23]]
      words.append((infl, tags))

    words.sort(key=lambda x: x[0])

    for key, items in groupby(words, key=lambda x: x[0]):
      word_list = list(items)
      all_tags = []
      for i in range(23):
        one_tags = []
        for word, tags in word_list:
          if tags[i] != '':
            one_tags.append(tags[i])
        all_tags.append(one_tags)

      all_tags = [x for x in all_tags if len(x) > 0]
      sums = [len(x) for x in all_tags]
      all_tags = [Counter(x) for x in all_tags]

      d = {}
      for i in range(len(all_tags)):
        for tag in all_tags[i]:
          all_tags[i][tag] /= sums[i]

        d.update(all_tags[i])

      print(key + '\t' + str(d).replace('\'', '"'))


if __name__ == '__main__':
  make_oracle(sys.argv[1])
