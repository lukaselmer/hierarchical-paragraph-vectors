# HPV Code

## Setup

* Install [pyenv](https://github.com/yyuu/pyenv) and [pyenv-virtualenv](https://github.com/yyuu/pyenv-virtualenv)

```sh
pyenv install
```

* Install virtualenvwrapper

Make sure that this has been added to your environment (e.g. .zshrc):

```sh
eval "$(pyenv init - zsh)"
eval "$(pyenv virtualenv-init -)"
```

* Clone the project, setup virtualenv and install dependencies:

```sh
git clone git@github.com:lukaselmer/hierarchical-paragraph-vectors.git
cd code
pyenv virtualenv 3.4.3 master-thesis-kaggle-3.4.3
# this should happen automatically if not, check your pyenv and pyenv-virtualenv description
# pyenv activate master-thesis-kaggle-3.4.3
pip install -r requirements.txt
```

* Unzip the data to reproduce the results: unzip the file in code/model_data/cache/data-export-new.hdfConverted3.csv.hdf.zip to code/model_data/cache/data-export-new.hdfConverted3.csv.hdf

The data is from:

* http://ai.stanford.edu/~amaas/data/sentiment/
* https://www.kaggle.com/c/word2vec-nlp-tutorial/data

## Usage

### Deploy the Simple Job Runner

See https://github.com/lukaselmer/simple-job-runner#deployment

### Schedule new runs

* Adjust code/schedule.py
* run ```API_HOST=<API_HOST> API_KEY=<API_KEY> python schedule.py```
  * e.g. ```APP_HOST=rocky-lowlands-2159.herokuapp.com API_KEY=zyMvxTzylN1ZKLd5TSaWQD9UsESsU00CGH3P python schedule.py```

You should see the scheduled runs on https://\<API_HOST\>/runs

### Execute the runs

The simplest way to execute the runs is to execute the following command (zsh):

```sh
while (true) ; do ; API_HOST=<API_HOST> API_KEY=<API_KEY> python slave.py ; sleep 1 ; done
```

## Install New Requirements

```sh
pip install <whatever>
pip freeze > requirements.txt
```

## Inspired by (and some code copied from)

* https://github.com:wendykan/DeepLearningMovies
* https://github.com/piskvorky/gensim/blob/develop/docs/notebooks/doc2vec-IMDB.ipynb

