import polling_monitor
import urllib2

app = polling_monitor.app

def poll():
  is_up = False
  try:
    is_up = urllib2.urlopen('http://not-a-real-site.com').getCode() == 200
  except:
    pass

  if not is_up:
    polling_monitor.alert('Uh-oh')

polling_monitor.callbacks.append(poll)
polling_monitor.start()
