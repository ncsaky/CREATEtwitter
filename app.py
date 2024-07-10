from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory data storage
tweets = []

class Tweet:
    def __init__(self, username, content):
        self.username = username
        self.content = content

@app.route('/')
def display_tweets():
    return render_template('display.html', tweets=tweets)

@app.route('/create', methods=['GET', 'POST'])
def create_tweet():
    if request.method == 'POST':
        username = request.form['username']
        content = request.form['content']
        new_tweet = Tweet(username, content)
        tweets.insert(0, new_tweet)  # Add the new tweet to the beginning of the list
        return redirect(url_for('display_tweets'))
    return render_template('create.html')
  
  
if __name__ == '__main__':
  app.run(debug=True)
