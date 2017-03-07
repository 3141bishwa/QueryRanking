README
------

### Python packages used by the script

   * nltk
   * gensim (Word2vec model)

Look at the following websites to install it.

   * http://www.nltk.org/install.html
   * https://radimrehurek.com/gensim/install.html


### Steps

- First, download this repository and extract the zip file.

- Then, download the word2vec model from:

https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit

- Rename the file to data.bin.gz and put it inside the repository that you just downloaded. (do not unzip it)
- Run the script using:

`python solution.py`

- Let the code run for a while since it has to load the word2vec model (consumes about 4 Gbs of RAM, make sure you have enough).

- The script will ask you for a word. After entering the word, it will show the 5 highest sections with the scores.

#### Example Results

## Example - I

Choose a word: Adidas

Clothing, footwear, personal accessories, and related products 1.05587802322

Materials and supplies for production and related products, except processed food and beverage inputs for human food manufacturing and food services 0.625179410053

Home entertainment, recreation and culture products, including household pets and related products 0.348155523003

Leisure and long-distance travel, tourism, and accommodation products 0.323897407827

Food, beverage, and tobacco products, except raw farm products 0.316514945691

## Example - II

Choose a word: car

Automobiles, light-duty trucks, local passenger transportation services, and related products 1.32620191537

Materials and supplies for production and related products, except processed food and beverage inputs for human food manufacturing and food services 0.927495097188

Home entertainment, recreation and culture products, including household pets and related products 0.711177651617

Clothing, footwear, personal accessories, and related products 0.527105139476

Leisure and long-distance travel, tourism, and accommodation products 0.495456686573
