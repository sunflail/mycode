#!/usr/bin/env python3

import shutil
import os
#os.chdir sets the starting directory
os.chdir("/home/student/mycode/")
#copies a single file, including renaming
shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
#copies an entire folder, source to destination
shutil.copytree("5g_research/", "5g_research_backup/")
