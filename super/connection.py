class Connection: 
	__instance = None

	def __new__(cls, *args, **kwargs):
		if cls.__instance is None: 
			print("Connecting...")
			cls.__instance = super().__new__(cls)
			return cls.__instance