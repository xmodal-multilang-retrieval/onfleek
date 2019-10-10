# onfleek

Scripts to help annotate Flickr30k in other languages.

## Tutorial

### Requirements

[Anaconda with Python 3.7](https://www.anaconda.com/distribution/)

### Guide

Create a directory for our project and change into it.

`mkdir xmodal-multilang-retrieval && cd xmodal-multilang-retrieval`

Clone this repo inside it and change dir into it.

`git clone git@github.com:xmodal-multilang-retrieval/onfleek.git && cd onfleek/`

Create and conda environment for our dependencies.

`conda create --name fleek python=3.7`

Activate the conda env.

`conda activate fleek`

Download and install our dependencies.

`pip install -r requirements.txt`

Run the script that downloads the dataset from a Google Drive folder I shared.

`python download_dataset.py`

Run Jupyter Notebook to begin annotating.

`jupyter notebook`

Run all cells and start translating!
