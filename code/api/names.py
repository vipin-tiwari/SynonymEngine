import json
import bottle
from bottle import route, run, request, abort
from ConnectionManager import ConnectionManager


redis_pool = ConnectionManager();

@route('/:term/:synonym', method='POST')
def put_document(term,synonym):
	try:
		redis_pool.setVariable(term, synonym)
	except ValidationError as ve:
		abort(500, str(ve))
     
@route('/:term', method='GET')
def get_document(term):
	try:
		entity = redis_pool.getVariable(term)
		
	except Exception, e:
		abort(500, str(e))
	if not entity:
		abort(404, 'No synonym for term %s' % term)
	return str(entity)

run(host='0.0.0.0', port=8080)