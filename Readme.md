README
------

### Python packages used by the script

* nltk
* gensim (Word2vec model)

Look at the following websites to install it.

http://www.nltk.org/install.html
https://radimrehurek.com/gensim/install.html

- First, download this repository and extract the zip file.
- Then, download the word2vec model from:

https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit

- Rename the file to bin.gz and put it in the same directory as the downloaded repo (don not unzip it)
- Run the script using:

`python script.py`

- Let the code run for a while since it has to load the word2vec model (consumes about 4 Gbs of RAM, make sure you have enough).

- The script will ask you for a word. After entering the word, it will show the 5 highest sections with the scores.


