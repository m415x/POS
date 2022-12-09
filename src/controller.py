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
app.config['UPLOADS'] = os.path.join('uploads') # Guardamos la ruta de fotos como un valor en la app

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

    sql = "SELECT image, code, type, name, description, stock, cost, price FROM pos.products;"
    cursor.execute(sql)
    products = cursor.fetchall()
    
    conn.commit()

    return render_template('pos/pos.html', products=products)


# * ADD * -----------------------------------------------------------------------------------
@app.route('/add')
def add():

    return render_template('pos/add.html')



# * STORE * ---------------------------------------------------------------------------------
@app.route('/store', methods=['POST'])
def storage():
    
    _file = request.files['formFile']
    _type = request.form['formType']
    _code = f"{_type[0:2].upper()}-{request.form['formCode']}"
    _name = request.form['formName']
    _info = request.form['formInfo']
    _stock = request.form['formStock']
    _cost = request.form['formCost']
    _price = request.form['formPrice']

    picName = f"{_type[0:2].upper()}-{_code}.jpg"
    _file.save(f"uploads/{picName}")

    sql = f"INSERT INTO pos.products (image, code, type, name, description, stock ,cost, price) VALUES ('{picName}', '{_code}', '{_type}', '{_name}', '{_info}', {_stock}, {_cost}, {_price});"

    cursor.execute(sql)
    conn.commit()

    return render_template('pos/add.html')


# * INVENTORY * ------------------------------------------------------------------------------
@app.route('/inventory')
def inventory():

    sql = "SELECT image, code, type, name, description, stock, cost, price FROM pos.products;"
    cursor.execute(sql)
    products = cursor.fetchall()
    
    conn.commit()

    return render_template('pos/inventory.html', products=products)


'''
# * DELETE * ---------------------------------------------------------------------------------
@app.route('/delete/<int:id>')
def delete(id):

    sql = f"SELECT image FROM pos.products WHERE id={id};"
    cursor.execute(sql)

    pic = cursor.fetchone()[0]

    try:
        os.remove(os.path.join(UPLOADS, pic))
    except:
        pass

    sql = f"DELETE FROM pos.products WHERE id={id};"
    cursor.execute(sql)

    conn.commit()

    return redirect('/')


# * MODIFY * ---------------------------------------------------------------------------------Cambiar para que edite desde el mismo inventario, quizas no lo necesite
@app.route('/modify/<int:id>')
def modify(id):

    sql = f"SELECT * FROM pos.products WHERE id={id};"
    cursor.execute(sql)
    product = cursor.fetchone() # Trae un solo producto

    conn.commit()

    return render_template('pos/inventory.html', product=product)


# * UPDATE * ---------------------------------------------------------------------------------
@app.route('/update', methods=['POST'])
def update():

    _file = request.files['formFile']
    _type = request.form['formType']
    _code = f"{_type[0:2].upper()}-{request.form['formCode']}"
    _name = request.form['formName']
    _info = request.form['formInfo']
    _stock = request.form['formStock']
    _cost = request.form['formCost']
    _price = request.form['formPrice']

    if _file.filename != '':
        picName = f"{_type[0:2].upper()}-{_code}.jpg"
        _file.save(f"uploads/{picName}")

        sql = f"SELECT image FROM pos.products WHERE id={id};"
        cursor.execute(sql)
        conn.commit()

        pic = cursor.fetchone()[0]

        try:
            os.remove(os.path.join(UPLOADS, pic))
        except:
            pass

        sql = f"UPDATE pos.products SET image='{newName}' WHERE id={id};"
        cursor.execute(sql)
        conn.commit()

    sql = f"UPDATE pos.products SET code='{_code}', type='{_type}', name='{_prod}', description='{_info}', stock={_stock}, cost={_cost}, price={_price} WHERE id={id};"
    cursor.execute(sql)
    conn.commit()

    return render_template('pos/inventory.html')

'''
if __name__ == '__main__':
    app.run(debug=True)
