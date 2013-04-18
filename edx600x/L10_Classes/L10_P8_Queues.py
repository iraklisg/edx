class Queue(object):
    """
    This is a FIFO queue
    """
    def __init__(self):
        """
        Create an empty list to store the queues
        """
        self.queue = []
        
    def insert(self, e):
        self.queue.append(e)
    
    def remove(self):
        try:
            return self.queue.pop(0)
        except:
            raise ValueError()
 
queue = Queue()
print queue.insert(5)
print queue.insert(6)
print queue.remove()
print queue.insert(7)
print queue.remove()
print queue.remove()
print queue.remove()