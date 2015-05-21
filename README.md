# Simple Search Engine Written by Python

## Description

- Base on [MASASHI Shibata's project](https://github.com/c-bata/SearchEngine)
- Web Crawler
- Use [pyltp](https://github.com/HIT-SCIR/pyltp) to segment Chinese word
- MongoDB as storage
- Flask as web framework

## Requirements

- Python 2.7
- pip

## Setup

1. Clone repository

    ```
    $ git clone git@github.com:scorpio147wbh/information-retrieval-experiment.git
    ```

1. Download LTP Chinese word segment model from [here](http://pan.baidu.com/share/link?shareid=1988562907&uk=2738088569#path=%252Fltp-models%252F3.2.0%252Fsubmodels)

1. Install python packages

    ```
    $ cd information-retrieval-experiment
    $ pip install -r requirements.txt
    ```

1. MongoDB settings

    Please rewrite MONGO_URL in config.py

1. LTP settings

    Please rewrite CWS_MODEL_PATH in config.py
    
1. Run

    ```
    $ python run-crawler.py http://nlp.stanford.edu/courses/NAACL2013/ # build a index
    $ python run-webapp.py # access to http://127.0.0.1:5000
    ```

