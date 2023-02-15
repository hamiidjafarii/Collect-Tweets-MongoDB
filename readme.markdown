<h1 text-align="center"><h1>Collect tweets on MongoDB</h1>

<p text-align="center"><project-description>
Through the code, you can store user and tweet objects (which contain information about a user and a tweet) in Tweepy on MongoDB. The code and its result will help data journalists and researchers evaluate trends on Twitter. I have used the official Twitter API and three Python libraries, including Configparser, Tweepy, and MongoClient from PyMongo, for getting related data. After authenticating Twitter API keys, I created a database on MongoDB to save associated tweets. In the next step, I defined a query for getting tweets from Tweepy. In this part of the code, you can consider a specific hashtag and use "search tweet." Based on the code, you can receive tweet JSON data, and based on the data, you can store tweets. I used the if statement to update and insert new tweets. For this part, if you want to have an update, you will probably face the message "The tweet is skipped because it already existed." This is because some tweets are duplicates, and the code doesn’t save them again in your database and only saves new tweets.
</p>

## Built With

- Python


## Author

**Hamid Jafari**

- [Github](https://github.com/hamiidjafarii "github.com/hamiidjafarii")