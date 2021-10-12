#import
from flask import Flask
from threading import Thread

#create server
app = Flask('')

@app.route('/')
def main():
  return "Easypass is live"

def run():
  app.run(host="0.0.0.0", port=8000)

def keep_alive():
  server = Thread(target=run)
  server.start()
