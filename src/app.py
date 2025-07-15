from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'thisissecret'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
    app.config['MAIL_PORT'] = 2525
    app.config['MAIL_USERNAME'] = 'user'
    app.config['MAIL_PASSWORD'] = 'password'
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    from src.models import user, product, sale, commission
    from src.controllers import sales, auth, data_import, reporting, simulation

    app.register_blueprint(sales.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(data_import.bp)
    app.register_blueprint(reporting.bp)
    app.register_blueprint(simulation.bp)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app
