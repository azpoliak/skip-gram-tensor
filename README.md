# Explaining and Generalizing Skip-Gram through Exponential Family Principal Component Analysis

The popular skip-gram model induces word
embeddings by exploiting the signal from
word-context coocurrence. We offer a new
interpretation of skip-gram based on exponential
family PCA—a form of matrix
factorization. This makes it clear that we
can extend the skip-gram method to tensor
factorization, in order to train embeddings
through richer higher-order coocurrences,
e.g., triples that include positional information
(to incorporate syntax) or morphological
information (to share parameters across
related words). We experiment on 40 languages
and show that our model improves
upon skip-gram.

## Paper
The original EACL 2017 paper can be found [here](http://aclweb.org/anthology/E17-2028)

## Instructions
To run the tensor-factoization word embeddings code, run `bash make-embeddings.sh` from the `hyperref-tensor` directory
<br>Right now, that example uses an early paragraph from Thoreau's *Walden* extracted from this [website](https://textfiles.com/etext/NONFICTION/thoreau-walden-186.txt)



## Repo Structure: 
1. ```hyperref-tensor```: C code to generate word embeddings. The directory includes the original word2vecf code which we use as a baseline.

1. ```Universal_Dependencies```: Data and code corresponding to UD experiments in the paper 

## Citation
If you make use of this code, please you the following citation: 
```
@InProceedings{E17-2028,
  author = 	"Cotterell, Ryan
		and Poliak, Adam
		and Van Durme, Benjamin
		and Eisner, Jason",
  title = 	"Explaining and Generalizing Skip-Gram through Exponential Family Principal Component Analysis",
  booktitle = 	"Proceedings of the 15th Conference of the European Chapter of the Association for Computational Linguistics: Volume 2, Short Papers",
  year = 	"2017",
  publisher = 	"Association for Computational Linguistics",
  pages = 	"175--181",
  location = 	"Valencia, Spain",
  url = 	"http://aclweb.org/anthology/E17-2028"
}
```
