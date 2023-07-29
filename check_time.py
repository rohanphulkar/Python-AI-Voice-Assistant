import datetime
import locale

def check_time():
    # Set the desired locale to the system's default locale
    locale.setlocale(locale.LC_TIME, '')

    # Get the current date and time
    current_date_time = datetime.datetime.now()

    # Format the date and time in a human-readable format with AM/PM time
    formatted_date_time = current_date_time.strftime('%A, %d %B %Y %I:%M:%S %p')

    return formatted_date_time
