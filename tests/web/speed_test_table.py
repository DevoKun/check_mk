import subprocess
from subprocess import Popen, PIPE
import re
import numpy as np
import shlex


do_5k = False
do_break = False
n_runs = 2

rt = {}
rt[1] = []
rt[2] = []
rt[3] = []
rt[4] = []

if not do_5k:
    print ' ----------------------- testing on 1000 rows -------------------------------'
else:
    print ' ----------------------- testing on 5000 rows -------------------------------'

for j in range(n_runs):
    for i in range(1,5):
        try:
            if not do_5k:
                session = subprocess.Popen(shlex.split('curl --next "http://localhost/heute/check_mk/view.py?view_name=allservices_test_%d&_username=automation&_secret=66d8d259-6d70-40dc-860b-d1a28839ebc6"'%i), stdout=PIPE, stderr=PIPE)
            else:
                session = subprocess.Popen(shlex.split('curl --next "http://localhost/heute/check_mk/view.py?check_command=&host_regex=&is_host_in_notification_period=-1&is_in_downtime=-1&is_service_acknowledged=-1&is_service_active_checks_enabled=-1&is_service_in_notification_period=-1&is_service_in_service_period=-1&is_service_is_flapping=-1&is_service_notifications_enabled=-1&is_service_scheduled_downtime_depth=-1&limit=hard&neg_host_regex=&neg_opthost_group=&neg_optservice_group=&neg_service_output=&neg_service_regex=&opthost_group=&optservice_group=&selection=1c0643ed-ec85-43ff-8c38-833b1cd8d763&service_output=&service_regex=&site=&st0=on&st1=on&st2=on&st3=on&stp=on&view_name=allservices_test_%d&_username=automation&_secret=66d8d259-6d70-40dc-860b-d1a28839ebc6"'%i), stdout=PIPE, stderr=PIPE)
            stdout, stderr = session.communicate()
            stdout = re.findall(r'<div>\s*Time to render.*</div>', stdout)[0]
            stdout = re.findall(r'\d+.\d+', stdout)[0]
            rt[i].append(float(stdout))
        except:
            print 'error!'
            do_break = True
            break
    if do_break:
        break
for i in range(1,5):
    print "Test %d" %i
    runtimes = rt[i]
    print "Mean out of %d runs: %3.2f\nStd deviation: %1.4f" %(n_runs, np.mean(runtimes),np.std(runtimes))


