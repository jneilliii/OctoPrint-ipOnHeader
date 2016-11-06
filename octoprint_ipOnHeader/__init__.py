# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin
import socket

class ipOnHeaderPlugin(octoprint.plugin.StartupPlugin,octoprint.plugin.SettingsPlugin):
	def on_after_startup(self):
		self._logger.info("ipOnHeaderPlugin: " + [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1])
		self._settings.global_set(["appearance","name"],[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1])
		self._settings.save()
		self._printer.commands("M117 " + [(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1])

	##~~ Softwareupdate hook
	def get_update_information(self):
		return dict(
			ipOnHeader=dict(
				displayName="ipOnHeader Plugin",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="jneilliii",
				repo="OctoPrint-ipOnHeader",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/jneilliii/OctoPrint-ipOnHeader/archive/{target_version}.zip"
			)
		)

__plugin_name__ = "ipOnHeader Plugin"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = ipOnHeaderPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}

