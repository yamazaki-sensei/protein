import requests
from urllib.parse import quote

__url = 'http://www.rcsb.org/pdb/rest/search'

def search_with_sequence(sequence, identity=70):
    print('Try to fetch with sequence: {}'.format(sequence))
    query = '<orgPdbQuery> \
               <queryType>org.pdb.query.simple.SequenceQuery</queryType>\
               <sequence>{0}</sequence>\
               <searchTool>blast</searchTool>\
               <sequenceIdentityCutoff>{1}</sequenceIdentityCutoff>\
            </orgPdbQuery>'.format(sequence, identity)

    encoded = quote(query, safe='')
    headers = {
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }

    res = requests.post(__url, data=encoded, headers=headers)
    print('res = {}'.format(res.text))
    return res
