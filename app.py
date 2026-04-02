from flask import Flask

app = Flask (__name__)

@app.route('/')
def home():
    return "🎮Site de Jogos🖥️"

@app.route('/jogosDeFPS') #CamelCase redDeadRedenption, SnakeCase red_dead_redenption
def jogos():
    return "⚔️Melhores Jogos de fps🔫: CSGO, Valorant, Warzone, Fortinite"

@app.route('/jogos_historia')
def historia():
    return "🛕Os melhores jogos modo historia🗺️: Red Dead Redenption, God of War, The last of us"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)