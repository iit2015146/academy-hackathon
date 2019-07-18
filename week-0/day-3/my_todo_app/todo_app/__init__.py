import os

from flask import Flask
from flask import request
from flask import render_template
todo_store =  {}
todo_store['shivam'] = ['coding','gym','movies']
todo_store['santosh'] = ['coding','cricket','movies']

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    def select_todos(name):
        global todo_store
        return todo_store[name]
    def GetTodos(name):
        try:
            return select_todos(name)
        except:
            return None    
    def insert_todo(name,todo):
        global todo_store
        current_todo = todo_store[name]
        current_todo.append(todo)
        todo_store[name] = current_todo
        return
    def add_todo_by_name(name,todo):
        insert_todo(name,todo)
        return    
    @app.route('/todos')
    #Below Function Is Our Controller
    def todos():
        name = request.args.get('name')
        # return todo_view(GetTodos(name))       
        get_todos = GetTodos(name)
        if get_todos == None:
            # return 404
            return render_template('404.html'),404
        else:
            return render_template('todo_view.html',todos = get_todos) 

    @app.route('/add_todos')
    def add_todos():
        name = request.args.get('name')
        todo = request.args.get('todo')
        add_todo_by_name(name,todo)
        return 'Success'
    return app

