from flask import Flask, render_template, request
app = Flask(__name__, template_folder='templates')

from app import views