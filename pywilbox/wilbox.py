import sys
import relayctl
from .selectorvalve_VICI import selectorvalve_VICI
from time import sleep

class Wilbox:
	def __init__(self, viciport, pumprelay=1, rollover=False):
		self.__vicivalve = self.__init_vici(viciport)
		self.__relayboard = self.__init_relays()
		self.__pumprelay = pumprelay
		self.pump_off()
		
		self.warning('Not yet implemented: log file with sampling events and stuff.')

	def __init_vici(self, viciport):
		self.warning('Not yet implemented: connect to VICI valve at ' + viciport)
		valve = selectorvalve_VICI(viciport)
		return valve

	def __init_relays(self):
		devices = relayctl.connect()

		if len(devices) == 0:
			self.error('No Sainsmart relay board found.')

		if len(devices) > 1:
			self.error('More than one Sainsmart relay board found.')

		return devices[0]  # Device object

	def pump_off(self):
		relayctl.switchoff(self.__relayboard, self.__pumprelay)

	def pump_on(self):
		relayctl.switchon(self.__relayboard, self.__pumprelay)
		
	def pump(self, seconds):
		try:
			self.pump_on()
			sleep(seconds)
		except:
			self.warning('Could not activate gas circulation pump for ' + str(seconds) + ' seconds.')
		self.pump_off()

	def warning(self, message):
		print(f"[WARN] {message}")

	def error(self, message):
		print(f"[ERROR] {message}")
		sys.exit(1)

