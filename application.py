import requests
from flask import Flask, render_template, request
from pipeline.prediction_pipeline import hybrid_recommendation

app = Flask(__name__)

def get_poster_url(anime_title):
    url = f"https://kitsu.io/api/edge/anime?filter[text]={anime_title}&page[limit]=1"
    headers = {
        'Accept': 'application/vnd.api+json',
        'Content-Type': 'application/vnd.api+json'
    }
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        data = resp.json()
        if data['data']:
            attr = data['data'][0]['attributes']
            return attr['posterImage']['medium']
    except Exception as e:
        print(f"Error fetching poster for '{anime_title}':", e)
    return "https://via.placeholder.com/120x160?text=No+Image"

@app.route('/', methods=['GET', 'POST'])
def home():
    recommendations = []
    if request.method == 'POST':
        try:
            user_id = int(request.form['userID'])
            titles = hybrid_recommendation(user_id)  # Should return a list of anime titles
            for title in titles:
                poster = get_poster_url(title)
                recommendations.append({"title": title, "poster": poster})
        except Exception as e:
            print("Error occurred:", e)
            recommendations = []
    return render_template('index.html', recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
