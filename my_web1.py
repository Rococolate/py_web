import sqlite3, os
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash
import cr_db as db
from time import sleep

app = Flask(__name__)
sys_path = os.getcwd()

print(sys_path)
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'contact.db'),
    DEBUG=True,
    SECRET_KEY='nickknackpaddywhack',
    USERNAME='admin',
    PASSWORD='thisisterrible'
))
app.config.from_envvar('LENDY_SETTINGS', silent=True)


@app.route('/')
@app.route('/adduser', methods=['GET', 'POST'])
def add_user():
    error = None
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        qq = request.form['qq']
        address = request.form['address']
        marriage = request.form['marriage']
        db.initDB()
        db.update_person(name=name, phone=phone, qq=qq, address=address, marriage=marriage)
        db.closeDB()
        print(name, phone, qq, address, marriage)
        return redirect(url_for('success'))
    return render_template('adduser.html', error=error)


@app.errorhandler(404)
def file_not_found(error):
    return render_template('404.html'), 404


@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/test')
def test():
    return render_template('mp4_player.html')


@app.route('/userlist')
def user_list():
    db.initDB()
    all_user_list = db.select_date()
    all_user_number = len(all_user_list)
    return render_template('userlist.html',
                           all_user_list=all_user_list,
                           all_user_number=all_user_number)

@app.route('/listtest')
def listtest():
    db.initDB()
    all_user_list = db.select_date()
    all_user_number = len(all_user_list)
    return render_template('listtest.html',
                           all_user_list=all_user_list,
                           all_user_number=all_user_number)

if __name__ == '__main__':
    # db.initDB()
    # print(db.select_date())
    app.run(host='127.0.0.1', port=4023)