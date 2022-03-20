from flask import Flask
import crawl

app = Flask('app')

@app.route('/')
def lonely():
  return crawl.run()

app.run(host='0.0.0.0', port=8080)
