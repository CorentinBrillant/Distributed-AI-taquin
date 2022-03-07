class Message(object):
	"""docstring for Message"""
	def __init__(self, sender, dest, content):
		super(Message, self).__init__()
		self.sender = sender
		self.dest = dest
		self.content = content


		