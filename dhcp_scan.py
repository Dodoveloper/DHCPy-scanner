# import sys, time
# from daemonize import Daemon
from scanner import Scanner
#
# class MyDaemon(Daemon):
#     def run(self):
#         s = Scanner()
#         while True:
#             s.run()
#             time.sleep(10)
#
# if __name__ == "__main__":
#     daemon = MyDaemon('/tmp/daemon-example.pid')
#     if len(sys.argv) == 2:
#         if 'start' == sys.argv[1]:
#             daemon.start()
#         elif 'stop' == sys.argv[1]:
#             daemon.stop()
#         elif 'restart' == sys.argv[1]:
#             daemon.restart()
#         else:
#             print("Unknown command")
#             sys.exit(2)
#         sys.exit(0)
#     else:
#         print("usage: %s start|stop|restart") % sys.argv[0]
#         sys.exit(2)
from daemon import DaemonContext, pidfile
import time

context = DaemonContext(
    working_directory="/tmp", # wip
    pidfile=pidfile.PIDLockFile('/tmp/dhcp_scanner.pid')
    )

s = Scanner()

with context:
    while True:
        s.run()
        time.sleep(30)
