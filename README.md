# twitter-sentiment-timeseries-forecast
An application that uses deep learning to forecast financial time series based on historical timeseries data and sentiment analysis of tweets

# stocknet-dataset

stocknet-dataset is a comprehensive dataset for stock movement prediction from tweets and historical stock prices. I cloned the dataset from https://github.com/yumoxu/stocknet-dataset. The dataset is based on the following paper 

Xu, Y., & Cohen, S. B. (2018). Stock movement prediction from tweets and historical prices. In Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) (Vol. 1, pp. 1970-1979).


# select a particular stock

To extarct price and tweet data for a particular stock, use the following script

`python extract_stock_data.py --stock AAPL --target apple-stock`

This will create a new directory `apple-stock` with two files `AAPL.csv` and `AAPL.json`. The former is Apple stock prices data and the latter is a all the relevant tweets

