# Instructions

`word2vec3` requires the following command line arguments:

1. `train` - a file containing training data
   1. each line contains the triples: *word context relation* (seperated by whitespace)
1. `cvocab` - a file containing the vocab and counts of the context words
   1. each line contains: *context count* (seperated by whitespace)
1. `rvocab` - a file containing the vocab and counts of the relations 
   1. seach line contains: *relation count* (seperated by whitespace)
1. `wvocab` -  a file containing the vocab and counts of the words in the text
   1. each line contains: *word count* (seperated by whitespace)

The following are optional command line arguments:
1. `negative` - the number of negative samples
1. `min-count` - the minimum number of times a word must appear for a vector to be generated for it
1. `size` - the dimensionality of the vectors
1. `tensor` - `1` indicates whether to use tensor factorization, `0` indicates to use matrix factorization
1. `pow`
 
# Example
We provide an example bash script `make-embeddings.sh` that will download text, clean and format the data appropriately, then run `word2vecf` to generate word vectors from the downloaded text.
