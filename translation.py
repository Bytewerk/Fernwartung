class t:
	def __init__(self, lang):
		self.lang = lang
	
	def get(self, code):
		
		############################################
		# English
		############################################
		
		if self.lang == "en":
			if code == "sudoerr":
				return "Couldn't get required root access!\n"\
					"Is the graphical sudo-program installed?"
			if code == "connect":
				return "Please make sure, that you are connected to"\
					" the Internet.\nClick on 'OK' and wait a few"\
					" seconds, so your IP address can be looked up."
			if code == "ipfail":
				return "Failed to fetch the IP address.\n"\
					"Please try again."
			if code == "sshstartfail":
				return "Failed to start the SSH program!"
			if code == "running":
				return "Remote maintenance is active.\n\n"\
					"It will be inactive as soon as you close this"\
					" window.\n\n"
			if code == "sshstopfail":
				return "Failed to stop the SSH program!"
			
			return "(Missing Translation for "+code+")"
		
		
		############################################
		# German
		############################################
		
		if self.lang == "de":
			if code == "sudoerr":
				return "Konnte benötigte root-Rechte nicht erhalten!\n"\
					"Ist das grafische sudo-Programm installiert?"
			if code == "connect":
				return "Bitte stelle sicher, dass du mit dem Internet"\
					" verbunden bist.\nKlicke auf 'OK' und warte ein"\
					" paar Sekunden, während die IP Adresse abgefragt"\
					" wird."
			if code == "ipfail":
				return "IP Adresse konnte nicht abgefragt werden.\n"\
					"Bitte erneut versuchen."
			if code == "sshstartfail":
				return "Starten des SSH-Programms fehlgeschlagen!"
			if code == "running":
				return "Fernwartung ist aktiv.\n\n"\
					"Sobald dieses Fenster geschlossen wird, wird sie"\
					" beendet!\n\n"
			if code == "sshstopfail":
				return "Stoppen des SSH-Programms fehlgeschlagen!"
			
			return "(Fehlende Übersetzung für "+code+")"
