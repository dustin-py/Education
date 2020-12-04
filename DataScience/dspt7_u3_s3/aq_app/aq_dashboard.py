"""Application Dashboard to display data"""
from flask import Flask, render_template, request
from .aq_db import DB, Record
from .aq_api import add_aq_data


def create_app():
    """Create and cnfigure an instance of the Flask app"""
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    DB.init_app(app)

   
    @app.route('/')
    def root():
        """Home Dashboard"""
        return render_template('base.html',
                                title='AQI Dashboard',
                           	    record=Record.query.filter(Record.value >= 10).all())
    
    @app.route('/refresh')
    def refresh():
        """Pull fresh data from Open AQ and replace existing data."""
        DB.drop_all()
        DB.create_all()
        add_aq_data()
        DB.session.commit()
        return "Database succesfully refreshed!"
    
    return app
