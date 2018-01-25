make

# Download corpus. We chose a small corpus for the example, and larger corpora will yield better results.
#wget http://www.statmt.org/wmt14/training-monolingual-news-crawl/news.2010.en.shuffled.gz
#gzip -d news.2010.en.shuffled.gz
#CORPUS=news.2010.en.shuffled
#wget http://mattmahoney.net/dc/text8.zip
#unzip text8.zip
#CORPUS=text8
CORPUS=thoreau-walden.txt

pip install -r scripts/requirements.txt

# Clean the corpus from non alpha-numeric symbols
scripts/clean_corpus.sh $CORPUS > $CORPUS.clean
echo "cleaned corpus"

# A) Window size 2 with "clean" subsampling
mkdir w2.sub
python scripts/corpus2pairs.py --win 2 --sub 1e-5 --pos --thr 1 $CORPUS.clean > w2.sub/pairs
echo "Made pairs file"
bash scripts/pairs2counts.sh w2.sub/pairs > w2.sub/counts
echo "Made counts file"
python scripts/pairs2relations.py w2.sub/pairs > w2.sub/relations
echo "Made relations file"
python scripts/counts2vocab.py w2.sub/counts

./word2vec3 -train w2.sub/pairs -pow 1 -cvocab w2.sub/counts.contexts.vocab -wvocab w2.sub/counts.words.vocab -rvocab w2.sub/counts.relations.vocab -dumpcv w2.sub/context-matrix -dumprv w2.sub/relation-matrix -output w2.sub/vectors -negative 5 -size 300 -min-count 1 -tensor 1


