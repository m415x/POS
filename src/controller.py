from flask import Flask, render_template, request, redirect, url_for, send_from_directory, flash
from flaskext.mysql import MySQL
from datetime import datetime
import os


app = Flask(__name__)
app.secret_key = ''
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
@app.route('/userpic/<path:nombreFoto>')
def uploads(nombreFoto):

    return send_from_directory(UPLOADS, nombreFoto)


# * POS * ------------------------------------------------------------------------------------
@app.route('/')
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
    _code = request.form['formCode']
    _type = request.form['formType']
    _prod = request.form['formProd']
    _info = request.form['formInfo']
    _stock = request.form['formStock']
    _cost = request.form['formCost']
    _price = request.form['formPrice']
    
    # if _nombre == '' or _correo == '' or _foto.filename == '':
    #     flash('¡Recuerde llenar todos los campos!')
    #     return redirect(url_for('create'))

    now = datetime.now().strftime('%Y%m%d-%H%M%S')

    if _file.filename != '':
        _file.save(f"uploads/{now}_{_file.filename}")
        # nuevoNombreFoto = f"{now}_{_file.filename}"
        # _file.save('uploads/' + nuevoNombreFoto)

    sql = f"INSERT INTO pos.products (code, type, name, description, stock ,cost, price) VALUES ('{_code}', '{_type}', '{_prod}', '{_info}', {_stock}, {_cost}, {_price});"

    cursor.execute(sql)
    conn.commit()

    return redirect('/')


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

    _id = request.form['formId']
    _file = request.files['formFile']
    _code = request.form['formCode']
    _type = request.form['formType']
    _prod = request.form['formProd']
    _info = request.form['formInfo']
    _stock = request.form['formStock']
    _cost = request.form['formCost']
    _price = request.form['formPrice']

    if _file.filename != '':
        now = datetime.now().strftime('%Y%m%d-%H%M%S')
        newName = f"{now}_{_file.filename}"
        _file.save('uploads/' + newName)

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


if __name__ == '__main__':
    app.run(debug=True)
