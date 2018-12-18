from scanner import Scanner
from daemon import DaemonContext, pidfile
import time

context = DaemonContext(
    working_directory="/tmp", # wip
    pidfile=pidfile.PIDLockFile('/tmp/dhcp_scanner.pid')
    )

s = Scanner()

with context:
    s.run()
    # time.sleep(5)
