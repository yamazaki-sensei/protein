from bottle import route, request, abort
from src.client import pdb_client
from src.converter import converter
import json


@route('/pdb')
def pdb_code_from_input():
    input = request.query.input

    if not input:
        abort(400)
        return

    converted = converter.convert(input)
    pdbs = pdb_client.search_with_sequence(converted, 30)

    print('result = ' + str(pdbs))
    if len(pdbs) > 0 and len(pdbs[0]) > 0:
        res = {
            'input': input,
            'protein_sequence': converted,
            'pdb_code': pdbs[0]
        }

        return json.dumps(res)

    else:
        abort(404)
