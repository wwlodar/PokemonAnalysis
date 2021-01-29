from flask import Flask, render_template, request
import requests
from app import app

@app.route('/')
def index():
    return render_template('home.html')



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
