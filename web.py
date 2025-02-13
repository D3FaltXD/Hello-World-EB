from flask import Flask, render_template_string
import random

app = Flask(__name__)

# List of League of Legends character images
character_images = [
    "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Ahri_0.jpg",
    "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Ashe_0.jpg",
    "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Garen_0.jpg",
    "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Lux_0.jpg",
    "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Yasuo_0.jpg"
    "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Teemo_0.jpg"
    "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Vex_0.jpg"
    "https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Viego_0.jpg"
    
]

@app.route('/')
def index():
    image_url = random.choice(character_images)
    return render_template_string('''
        <html>
            <head><title>Random League of Legends Character</title></head>
            <body>
                <h1>Random League of Legends Character</h1>
                <img src="{{ image_url }}" alt="League of Legends Character">
            </body>
        </html>
    ''', image_url=image_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3000,debug=True)