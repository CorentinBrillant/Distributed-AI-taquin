class Message(object):
	"""docstring for Message"""
	def __init__(self, sender, dest, content, priority):
		super(Message, self).__init__()
		self.sender = sender
		self.dest = dest
		self.content = content
		self.priority = priority

	def toString(self):
		return "mail from "+str(self.sender)+" to "+str(self.dest)+" : leave "+str(self.content)+" with priority "+str(self.priority)


		