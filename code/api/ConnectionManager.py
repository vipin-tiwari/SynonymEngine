import redis

class ConnectionManager:
	def __init__(self):
		self.host = 'localhost'
		self.port = 6379
		self.db = 0
		self.POOL = None

	def connect():
		self.POOL = redis.ConnectionPool(host=self.host, port=self.port, db=self.db)

	def getVariable(self,variable_name):
		my_server = redis.Redis(connection_pool=self.POOL)
		response = my_server.get(variable_name)
		return response

	def setVariable(self,variable_name, variable_value):
		my_server = redis.Redis(connection_pool=self.POOL)
		my_server.set(variable_name, variable_value)