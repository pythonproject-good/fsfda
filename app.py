from flask import Flask
from extensions import db, login_manager
from routes import routes  # Import the blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auction.db'

# Initialize extensions
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'routes.login'

# Register the blueprint
app.register_blueprint(routes)

if __name__ == '__main__':
    app.run(debug=True)
