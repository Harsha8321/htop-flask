from flask import Flask
import os
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def htop():
    name = "Harshan N"
    
    try:
        user = os.getlogin()
    except:
        user = "codespace"

    ist = pytz.timezone('Asia/Kolkata')
    time_ist = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S %Z')

    return f"""
    Name: {name}<br>
    User: {user}<br>
    Server Time (IST): {time_ist}<br><br>
    TOP output:<br>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)