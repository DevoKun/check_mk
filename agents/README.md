
Check_MK Agents
===============



## MacOS X



### Install the Agent

#### Copy agent bash script in to place and create directories for local scripts
* Get **check_mk_agent.macosx** from the **check_mk source code** in the **agents** directory.

```bash
mkdir -p /usr/local/lib/check_mk_agent/local
mkdir -p /usr/local/etc/check_mk
cp check_mk_agent.macosx /usr/local/bin/check_mk_agent
chmod 0755 /usr/local/bin/check_mk_agent
```

#### Create LaunchAgent plist
* Get **de.mathias-kettner.check_mk_agent.plist** from the **check_mk source code** in the **agents/cfg_examples** directory.

```bash
cp de.mathias-kettner.check_mk_agent.plist /Library/LaunchAgents/de.mathias-kettner.check_mk_agent.plist
```

#### Load the LaunchAgent
```bash
launchctl load -wF "/Library/LaunchAgents/de.mathias-kettner.check_mk_agent.plist"
```

#### Check on the status of the LaunchAgent
```bash
launchctl list | grep check_mk_agent

launchctl list de.mathias-kettner.check_mk_agent
```



### Uninstall the Agent

#### Unload the LaunchAgent
```bash
launchctl unload de.mathias-kettner.check_mk_agent
```

#### Remove the agent bash script
```bash
rm  /usr/local/bin/check_mk_agent
```

#### Remove any local scripts
```shell
rm -rf /usr/local/lib/check_mk_agent
```




