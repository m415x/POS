from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
from flaskext.mysql import MySQL
from datetime import datetime
import os


app = Flask(__name__)
app.secret_key = 'pointofsale'
mysql = MySQL()

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'pos'
# Guardamos la ruta de fotos como un valor en la app
app.config['UPLOADS'] = os.path.join('uploads')

UPLOADS = app.config['UPLOADS']

mysql.init_app(app)

conn = mysql.connect()
cursor = conn.cursor()


# * USERPIC * --------------------------------------------------------------------------------
@app.route('/userpic/<path:picName>')
def uploads(picName):

    return send_from_directory(UPLOADS, picName)


# * POS * ------------------------------------------------------------------------------------
@app.route('/pos')
def pos():

    sql = "SELECT code, type, name, info, stock, cost, price, img FROM pos.products;"
    cursor.execute(sql)
    products = cursor.fetchall()

    conn.commit()

    return render_template('pos/pos.html', products=products)


# * STORE * ---------------------------------------------------------------------------------
@app.route('/store', methods=['POST'])
def storage():

    _type = request.form['formType']
    _name = request.form['formName']
    _info = request.form['formInfo']
    _stock = request.form['formStock']
    _cost = request.form['formCost']
    _price = request.form['formPrice']
    _file = request.files['formFile']

    now = datetime.now().strftime('%Y%m%d%H%M%S')
    picName = f"{now}.jpg"
    _file.save(f"uploads/{picName}")

    sql = f"INSERT INTO pos.products (type, name, info, stock ,cost, price, img) VALUES ('{_type}', '{_name}', '{_info}', {_stock}, {_cost}, {_price}, '{picName}');"

    cursor.execute(sql)
    conn.commit()

    return redirect('/inventory')


# * INVENTORY * ------------------------------------------------------------------------------
@app.route('/inventory')
def inventory():

    sql = "SELECT code, type, name, info, stock, cost, price, img FROM pos.products;"
    cursor.execute(sql)
    products = cursor.fetchall()

    # payload = []
    # content = {}
    # for product in products:
    #     content = {'code': product[0], 'type': product[1], 'name': product[2], 'info': product[3], 'stock': product[4], 'cost': product[5], 'price': product[6], 'img': product[7]}
    #     payload.append(content)
    #     content = {}
    # jsonProds = jsonify(payload)
    # print(jsonProds)
    
    conn.commit()

    return render_template('pos/inventory.html', products=products) #return render_template('pos/inventory.html', products=products, jsonProds=jsonProds)


# * DELETE * ---------------------------------------------------------------------------------
@app.route('/delete/<int:id>')
def delete(id):

    sql = f"SELECT img FROM pos.products WHERE code={id};"
    cursor.execute(sql)

    pic = cursor.fetchone()[0]

    try:
        os.remove(os.path.join(UPLOADS, pic))
    except:
        pass

    sql = f"DELETE FROM pos.products WHERE code={id};"
    cursor.execute(sql)

    conn.commit()

    return redirect('/inventory')


# * UPDATE * ---------------------------------------------------------------------------------
@app.route('/update', methods=['POST'])
def update():

    # id = request.form.get('formCode')
    id = request.form['formCode']
    _type = request.form['formType']
    _name = request.form['formName']
    _info = request.form['formInfo']
    _stock = request.form['formStock']
    _cost = request.form['formCost']
    _price = request.form['formPrice']
    _file = request.files['formFile']
    print(id)

    if _file.filename != '':
        
        now = datetime.now().strftime('%Y%m%d%H%M%S')    
        picName = f"{now}.jpg"
        _file.save(f"uploads/{picName}")

        sql = f"SELECT img FROM pos.products WHERE code={id};"
        cursor.execute(sql)
        conn.commit()

        pic = cursor.fetchone()[0]

        try:
            os.remove(os.path.join(UPLOADS, pic))
        except:
            pass

        sql = f"UPDATE pos.products SET img='{picName}' WHERE code={id};"
        cursor.execute(sql)
        conn.commit()

    sql = f"UPDATE pos.products SET type='{_type}', name='{_name}', info='{_info}', stock={_stock}, cost={_cost}, price={_price} WHERE code={id};"
    cursor.execute(sql)
    conn.commit()

    return redirect('/inventory')


# * ADD * -----------------------------------------------------------------------------------
# @app.route('/add')
# def add():

#     return render_template('pos/inventory.html')


# * EDIT * -----------------------------------------------------------------------------------
# @app.route('/edit/<int:id>')
# def edit(id):

#     sql = "SELECT code, type, name, info, stock, cost, price, img FROM pos.products;"
#     cursor.execute(sql)
#     products = cursor.fetchall()
    
#     conn.commit()
    
#     sql = f"SELECT * FROM pos.products WHERE code={id};"
#     cursor.execute(sql)
#     product = cursor.fetchone() # Trae un solo producto

#     conn.commit()

#     return render_template('pos/edit.html', products=products, product=product)



# * RUN * ------------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
