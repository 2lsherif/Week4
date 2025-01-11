from flask import Flask

app = Flask(__name__)

# Import routes only after initializing the app
import app.app_routes
