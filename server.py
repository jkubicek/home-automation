#!/usr/bin/env python

from bottle import route, run, template
from subprocess import call
call(["ls", "-l"])
import BaseHTTPServer

@route('/')
def home():
    return '<h1>Welcome</h1><p>Welcome to the Raspberry Pi</p>'
    
@route('/switch/on')
def switchOn():
    call(['wemo', 'switch', 'Living Room', 'on'])
    return '<h1>On</h1>'
    
@route('/switch/off')
def switchOn():
    call(['wemo', 'switch', 'Living Room', 'off'])
    return '<h1>Off</h1>'

run(host='0.0.0.0', debug=True)
