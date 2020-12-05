# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 12:41:46 2020

@author: Louis
"""

from flask import Flask, render_template, jsonify, request
from cape.client import CapeClient
from settings import USERNAME, PASSWORD

app = Flask(__name__)

_CAPE_CLIENT = CapeClient()
_CAPE_CLIENT.login(USERNAME, PASSWORD)

_LAST_DOC_ID = None
_ANSWER_TOKEN = _CAPE_CLIENT.get_user_token()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add_document', methods=['POST'])
def add_document():
    global _LAST_DOC_ID
    doc_text = request.form.get('doc', "")
    _LAST_DOC_ID = _CAPE_CLIENT.upload_document(title='ctrl_f_doc', text=doc_text, replace=True)
    print(f'uploaded doc with id: {_LAST_DOC_ID}')
    return jsonify({'success': True})


@app.route('/ctrl_f', methods=['GET'])
def ctrl_f():
    if _LAST_DOC_ID is None:
        return jsonify({'success': False, 'answers': []})
    query_text = request.args['query']
    answers = _CAPE_CLIENT.answer(query_text,
                                  _ANSWER_TOKEN,
                                  document_ids=[_LAST_DOC_ID],
                                  number_of_items=5)
    print(f'answers: {answers}')
    return jsonify({'success': True,'answers': answers})


if __name__ == '__main__':
    app.run(port='5050')