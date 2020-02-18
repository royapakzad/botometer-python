
# Botometer Python API

With this piece of python code, you can extract a user's follwoers and run botometer to figure out whether they show bot-like bahvior or not. From [IUNetSci/botometer-python](https://github.com/IUNetSci/botometer-python) with some additional feature to extract followers from Twitter and only showing the Universal score of that acccount. 

A Python API for [Botometer by OSoMe](https://osome.iuni.iu.edu).

## API Keys

### Mashape Market API key
Our API is served via [Mashape Market](//market.mashape.com). You must sign up
for a free account in order to obtain a Mashape secret key. 
    
### Twitter app
In order to access Twitter's API, one needs to have/create a [Twitter app](https://apps.twitter.com/).
Once you've created an app, the authentication info can be found in the "Keys and Access Tokens" tab of the app's properties

### Installation 
From your command shell install botometer, tweepy, csv, json, and pandas. 

```
$ pip install botometer
$ pip install tweepy
$ pip install pandas
$ pip install json 
```

### Python Code

in your shell run:

```
$ python follower_botometer.py
```

For more information on this response object, consule the [API Overview](https://market.mashape.com/OSoMe/botometer/overview#wiki-response-object) on Mashape.



