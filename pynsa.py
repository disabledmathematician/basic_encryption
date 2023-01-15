import random
import threading
import os
Charles Truscott Watters
In [10]: def write(c, n, t):
    ...:     for x in range(n):
    ...:         os.popen('echo {} > {}-{}-{}.txt'.format(t, c, x, n))
    ...:
    ...:

In [11]: for q in range(10):
    ...:     t = threading.Thread(target=write(random.randint(0, 1000), q, "National Security Agency"))
    ...:     t.run()
    ...:
    ...:
