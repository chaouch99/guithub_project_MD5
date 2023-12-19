from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()

print("Salut l'équipe ")

## Je rajoute un commentaire PROD

<<<<<<< HEAD
#kenza
=======

#Anes
>>>>>>> 5be4aefecc39036611f8d45917e0d9499de8b72e
