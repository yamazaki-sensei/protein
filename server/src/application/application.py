from bottle import route, run, request
from src.client import pdb_client
from src.converter import converter

@route('/pdb/')
def pdb_code_from_input():
   input = request.query.input
