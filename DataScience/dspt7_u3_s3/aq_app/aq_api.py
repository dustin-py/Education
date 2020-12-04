"""Module to fetch openaq data"""
import openaq
from .aq_db import DB, Record

api = openaq.OpenAQ()

def add_aq_data():
    """Add data to dashboard"""
    data = api.measurements(
        city='Los Angeles',
        parameter='pm25')[1]
    

    for i in range(100):
        db_data = Record(
            id=i,
            datetime=dict(data['results'][i])['date']['utc'],
            value=int(dict(data['results'][i])['value'])
        )
    
        DB.session.add(db_data)
