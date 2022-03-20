from flask import Flask
import posts

app = Flask('app')

@app.route('/')
def lonely():
  return posts.list()

app.run(host='0.0.0.0', port=8080)
