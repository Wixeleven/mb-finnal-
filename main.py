from flask import Flask, render_template, request
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

app = Flask(__name__)

client_id = "901dc1bd6ee24c2e97dcff8202d42387"
client_secret = "ea9eefdbe4094df68d9be5cc6ccc7e4b"

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def results():
    # Get the search query from the form data
    search_query = request.form["search_query"]

    # Search for tracks using the query
    results = sp.search(q=search_query, type="track", limit=10)

    # Extract track information from each search result and add to a list
    track_info = []
    for track in results["tracks"]["items"]:
        track_name = track["name"]
        track_artist = track["artists"][0]["name"]
        track_info.append((track_name, track_artist))

    return render_template("result.html", track_info=track_info)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
