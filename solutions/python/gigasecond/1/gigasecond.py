'''Determine the date and time one gigasecond after a certain date.'''
import datetime as dt
def add(moment:dt.datetime):
    return moment + dt.timedelta(seconds=1e9)