import sublime
import sublime_plugin


class CaretPositionListener(sublime_plugin.EventListener):
	def on_selection_modified(self, view):
		text = "Position"
		for begin, end in view.sel():
			text += " " + str(begin)
			if end != begin:
				text += "-" + str(end)
		view.set_status('z_caret_position', text)
