import pymqi

queue_manager = pymqi.connect('QM1', 'SVRCONN.CHANNEL.1', '192.168.68.121(1414)')

q = pymqi.Queue(queue_manager, 'TESTQ.1')
q.put('Hello from Python!')