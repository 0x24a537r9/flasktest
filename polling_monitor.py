from flask import Flask
import threading

app = Flask(__name__)
callbacks = []
timer = None

def start():
  global timer
  timer = threading.Timer(1, poll)
  timer.start()

def poll():
  global timer
  for callback in callbacks:
    callback()
  timer = threading.Timer(3, poll)
  timer.start()

def alert(msg):
  print 'Alert: %s' % msg

@app.route('/silence')
def silence():
  if timer:
    timer.cancel()
  return 'Silenced'