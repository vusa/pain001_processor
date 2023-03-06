import pymqi

queue_manager = pymqi.connect('QM.1', 'SVRCONN.CHANNEL.1', '192.168.68.121(1434)')

q = pymqi.Queue(queue_manager, 'TESTQ.1')
msg = q.get()
print('Here is the message:', msg)