from flask import Flask, render_template
from advDiceGame.game import Game  # Змінено на абсолютний імпорт

app = Flask(__name__)
game = Game()

@app.route("/")
def index():
    return render_template("index.html", game=game)

@app.route("/attack/<int:i>")
def attack(i):
    game.attack(i)
    return index()

if __name__ == "__main__":
    app.run(debug=True)
