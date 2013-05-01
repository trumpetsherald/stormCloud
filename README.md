stormCloud
==========

A quick and dirty python script to allow fast switching between storm configs.

This script is currently a 5 minute POC but it works with caveats, here's how:

It assumes your storm config is in ~/.storm and is named storm.yaml. Rename
this file to something like storm-dev.yaml or storm-prod.yaml.

Create an alias in your .profile or .bashrc like this:
alias stormCloud = "python ~/foo/stormCloud/stormCloud.py"

Now you can create multiple configs for Storm and name them storm-X.yaml
and this script will just symlink storm.yaml to storm-X.yaml by typing
stormCloud X
