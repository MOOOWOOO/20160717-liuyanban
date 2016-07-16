# coding: utf-8

from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect

from model import Message

__author__ = 'Jux.Liu'

app = Flask(__name__)


@app.route('/')
def index_view():
    message_list = Message.query.all()
    return render_template("index.html", message_list=message_list)


@app.route('/message/add', methods=['POST'])
def add_message():
    message = Message(request.form)
    message.save()
    return redirect(url_for('index_view'))


if __name__ == '__main__':
    app.run()
