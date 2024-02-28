from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.dojo import Dojos
from flask_app.models.ninja import Ninja

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def display_dojos():
    dojos = Dojos.get_all()
    return render_template('dojo.html', dojos = dojos)

@app.route('/dojos/add',  methods=['POST'])
def new_dojo():
    Dojos.save(request.form)
    return redirect ('/dojos')

@app.route('/dojos/<int:dojo_id>')
def chosen_dojo(dojo_id):
    dojo = Dojos.get_dojos_and_ninjas(dojo_id)
    return render_template('show_dojo.html', dojo = dojo)

@app.route('/dojos/ninja')
def new_ninja():
    dojos = Dojos.get_all()
    return render_template('ninja.html', dojos = dojos)

@app.route('/dojos/ninja/add', methods=['POST'])
def add_new_ninja():
    Ninja.save(request.form)
    return redirect ('/')

@app.route('/dojos/edit/<int:ninja_id>')
def edit_ninja(ninja_id):
    ninjas = Ninja.get_one_ninja(ninja_id)
    return render_template('edit_ninja.html', ninjas = ninjas)

@app.route('/dojos/edit/update', methods=['POST'])
def updated_ninja():
    dojo_id = request.form['dojo_id']
    Ninja.update(request.form)
    return redirect (f'/dojos/{dojo_id}')

@app.route('/dojos/delete/<int:ninja_id>/<int:dojo_id>')
def delete_ninja(ninja_id, dojo_id):
    print('running')
    Ninja.delete(ninja_id)
    return redirect(f'/dojos/{dojo_id}')