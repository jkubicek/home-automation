#!/usr/bin/env python

from bottle import get, post, request, route, run, template
from subprocess import call
call(["ls", "-l"])
import BaseHTTPServer

@get('/')
def home():
    return '<h1>Welcome</h1><p>Welcome to the Raspberry Pi</p>'
    
@post('/switch/on')
def switchOn():
    call(['wemo', 'switch', 'Living Room', 'on'])
    
@post('/switch/off')
def switchOn():
    call(['wemo', 'switch', 'Living Room', 'off'])

run(host='0.0.0.0', debug=True)
