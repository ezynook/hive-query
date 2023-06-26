from flask import *
import pandas as pd
from pyhive import hive
import configparser
import sqlite3

app = Flask(__name__)
app.secret_key = 'MjkwOQ=='

def connect():
   try:
       hive_db = sqlite3.connect('backend/hive.db')
       db_config = hive_db.execute("select * from config").fetchone()
       conn = hive.Connection(host=str(db_config[1]), port=int(db_config[2]), username=str(db_config[3]), database=db_config[4])
       return [conn, db_config, hive_db]
   except Exception as e:
       return render_template("error.html", data=e)

@app.route('/')
def main():
    try:
        db = pd.read_sql("show tables", con=connect()[0])
        db_info = connect()[1]
        result = []
        for k,v in db.itertuples():
            result.append({"data": v})
                
        merge = [{},{},{},result, db_info]
        return render_template("main.html", data=merge)

    except Exception as e:
            return render_template("error.html", data=e)
   
        
@app.route("/data", methods=['POST'])
def query():
    sql = request.form['txtsql']
    try:
        db = pd.read_sql("show tables", con=connect()[0])
        result = []
        for k,v in db.itertuples():
            result.append({"data": v})
                
        data = pd.read_sql(sql, con=connect()[0])
        
        if len(data) > 0:
            mydict = data.to_dict('records')
            mycol = data.to_dict('records')[0]
            if len(mydict) < 1000:
                mydata = [mydict, mycol, {}, result, {}]
            else:
                mydata = [mydict[:1000], mycol, {}, result, {}]
            return render_template("main.html", data=mydata)
        else:
            return {"message":"query error"}
    except Exception as e:
        return render_template("error.html", data=e)

@app.route("/config", methods=['POST'])
def config():
    try:
        ipaddress = request.form['ipaddress']
        port = request.form['port']
        username = request.form['username']
        database = request.form['database']
        conn = connect()[2]
        conn.execute(f"UPDATE config SET ipaddress = '{ipaddress}', port = {port}, username = '{username}', database = '{database}'")
        conn.commit()
        return redirect(url_for('main'))
    except Exception as e:
        return render_template("error.html", data=e)



# if __name__ == '__main__':
#     app.run(host="0.0.0.0", port=3000, debug=True)