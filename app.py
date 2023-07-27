from flask import Flask, render_template, request, redirect, url_for, flash, session
import pyrebase

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a secure random key


if __name__ == '__main__':
    app.run(debug=True)
