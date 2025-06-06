# © 2025 @Dypixx.
# Originally developed by @SHARATHITSISME and @ISMARTBOII_UJJWAL
# Modified with additional features and improvements by @Dypixx
# Huge respect to the original creators ❤️

from flask import Flask, Response
import requests
app = Flask(__name__)

@app.route('/')
def show_github_html():
    response = requests.get('https://raw.githubusercontent.com/Dypixx/live/main/index.html')
    return Response(response.text, mimetype='text/html') if response.status_code == 200 else ("Bot is LIVE", 500)

if __name__ == "__main__":
    app.run()