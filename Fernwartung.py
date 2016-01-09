#!/usr/bin/env python3

# Requirements:
# - zenity
# - lxqt-sudo, gksudo or similar (see config)
# - sshd and possibly port forwarding must be already configured

#
# CONFIG
#
config_graphical_sudo_bin = "lxqt-sudo"
config_zenity_bin = "zenity"
config_sshd_start = ["systemctl", "start", "sshd"]
config_sshd_stop  = ["systemctl", "stop", "sshd"]
config_lang = "de"
#
# CONFIG END
#

# Import required libraries
import sys
import translation
import subprocess
import os
sys.path.insert(0, "ipgetter")
import ipgetter

# Set the translation language
t = translation.t(config_lang)

# Helper Function: Display a message or error with zenity
def msg(text, is_error=False):
	arg_type = "--info"
	if is_error: arg_type = "--error"
	subprocess.call([config_zenity_bin, arg_type, "--title",
		"Fernwartung", "--text", text])

# Require root access
if not os.geteuid() == 0:
	try:
		subprocess.call([config_graphical_sudo_bin,__file__])
	except:
		msg(t.get("sudoerr")+"\n("+config_graphical_sudo_bin+")", True)
	sys.exit()

# Get the IP
msg(t.get("connect"))
ip = ipgetter.myip()
if ip == "":
	msg(t.get("ipfail"), True)
	sys.exit()

# Start SSHD
try:
	subprocess.call(config_sshd_start)
except:
	msg(t.get("sshstartfail"), True)
	exit()


# Keep running until the dialog closes
msg(t.get("running") + "IP: " +ip)


# Stop SSHD
try:
	subprocess.call(config_sshd_stop)
except:
	msg(t.get("sshstopfail"), True)
