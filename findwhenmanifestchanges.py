#!/bin/python
import subprocess
import os
import glob

found = False
while not found:
 os.chdir('/home/Tim.Zwart/some_repo/')
 subprocess.call(['rm', '-r', 'unzipped_jarfile.dir/'])
 #checkout the parent commit, we take the first parent because why not
 subprocess.call(['git', 'checkout', 'HEAD^1'])
 #first we clean and rebuild, check whether manifest has the string we need
 subprocess.call(['mvn', 'clean', 'package'])
 #unzip the relevant buildfile
 #find the buildfile
 os.chdir('/home/Tim.Zwart/INGEX_Core/core/target')
 jarfiles = glob.glob('*.jar')
 if jarfiles:
  jarfile = jarfiles[0]
 else:
  raise SystemExit('no jarfile built for some reason. exiting')
 subprocess.call(['unzip', jarfile, '-d', '../../unzipped_jarfile.dir'])
 #open the manifest, search for the relevant string. if we do not find it, set found to true
 os.chdir('/home/Tim.Zwart/some_repo/unzipped_jarfile.dir/META-INF/')
 print(os.getcwd())
 with open('MANIFEST.MF') as manifestfile:
  manifest = manifestfile.read()
 if manifest.find('the_string') == -1:
  found = True
print("found the commit where manifest does no longer have string. the repo now points at this commit")
