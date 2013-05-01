import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("stormCloudName")
args = parser.parse_args()

stormCloudConfigPath = os.path.join(os.path.expanduser("~"), ".storm", "storm-" + args.stormCloudName + ".yaml")
stormConfigPath = os.path.join(os.path.expanduser("~"), ".storm", "storm.yaml")

print stormConfigPath, stormCloudConfigPath

if(os.path.exists(stormConfigPath)):
	os.remove(stormConfigPath)

if(os.path.exists(stormCloudConfigPath)):
	os.symlink(stormCloudConfigPath, stormConfigPath)
else:
	print "One of your paths is bad"



#Check to see if there is a ~/.storm dir with a file called storm.yaml
#Check to see a corresponding file storm-name.yaml exists
#Symlink the two