from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def blabla():
  return render_template("home.html")

#onderstaande is om flask te kunnen runnen via replit. Voor andere omgeving, moet je dit anders oplossen, zie ook: 
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)