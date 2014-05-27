#!/usr/bin/env python

from bottle import get, post, request, route, run
from subprocess import call
import BaseHTTPServer

# HTML Resource Loaders

def redirect_html():
    return open('html/redirect-to-home.html', 'r')

@get('/')
def home():
    return open('html/index.html', 'r')
    
@post('/switch/on')
def switchOn():
    call(['wemo', 'switch', 'Living Room', 'on'])
    return redirect_html()
    
@post('/switch/off')
def switchOff():
    call(['wemo', 'switch', 'Living Room', 'off'])
    return redirect_html()

run(host='0.0.0.0', debug=True)
