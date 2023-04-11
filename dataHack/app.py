from flask import Flask, request, render_template, jsonify
import pandas as pd
import re
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pickle
from io import BytesIO
import base64


app = Flask(__name__)


users = {
    'krishi':'lodu',
    'shivam':'sivam',
    'jasleen':'yazz',
    'kashish':'reactparkarenge',
    'aarya':'bhosu'
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and password == users[username]:
            return render_template('index.html', username=username) 
        else:
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')

        

@app.route('/test', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        category = int(request.form['category'])
        print(category)
        df1 = pd.read_csv("my_dataframe.csv")
        # filter the dataframe for the given category
        category_df = df1[df1['category_id'] == category]
        
        # calculate likes to view ratio for each tag
        category_df['likes_to_views_ratio'] = category_df['likes'] / category_df['view_count']
        
        # define a function to extract words from each tag
        def extract_words(tag):
            # remove special characters and digits
            tag = re.sub('[^a-zA-Z]+', ' ', tag)
            # convert to lowercase and split into words
            words = tag.lower().split()
            return words

        # apply the extract_words function to the 'tags' column and concatenate the resulting lists
        tags = category_df['tags'].apply(extract_words).sum()
        
        # group the tags by their average ratio
        tag_ratio = category_df.groupby('tags')['likes_to_views_ratio'].mean().reset_index()

        # sort the tags based on their ratio in descending order
        sorted_tags = tag_ratio.sort_values(by='likes_to_views_ratio', ascending=False)

        # take top 50 tags based on their ratio
        top_tags = sorted_tags.head(50)
        print (top_tags)
        # generate word cloud
        with open('stats1.pkl', 'rb') as f:
            wordcloud = pickle.load(f)
        #print(wordcloud)
        wordcloud = WordCloud(width=1200, height=800, stopwords=set(STOPWORDS)).generate(''.join(top_tags['tags']))
        wordcloudImage=wordcloud.to_image()
        img=BytesIO()
        wordcloudImage.save(img, format='PNG')
        imgword='data:image/png;base64,{}'.format(base64.b64encode(img.getvalue()).decode())
        print(imgword)
        # save the wordcloud to a file
        with open('wordcloud.pkl', 'wb') as f:
            pickle.dump(wordcloud, f)

        return render_template('index.html', category=category,cloud=imgword)
    else:
        return render_template('index.html')

@app.route('/wordcloud',methods=['GET','POST'])
def wordcloud():
    # load the wordcloud from the file
    if(request.method=='POST'):
        with open('wordcloud.pkl', 'rb') as f:
            wordcloud = pickle.load(f)
            
        wordcloudImage=wordcloud.to_image()
        img=BytesIO()
        wordcloudImage.save(img, format='PNG')
        imgword='data:image/png;base64,}'.format(base64.b64encode(img.getvalue()).decode())
        return render_template('wordcloud.html', wordcloud = imgword)
        # display the wordcloud
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.tight_layout()
        plt.show()
        
        return jsonify(success=True)
if __name__ == '__main__':
    app.run(debug=True)
