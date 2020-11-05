import sublime
import sublime_plugin


class CaretPositionListener(sublime_plugin.EventListener):
	def on_selection_modified(self, view):
		sels = list(view.sel())
		begin, end = sels[0]
		text = "Position {}-{}".format(begin, end)
		if len(sels) > 1:
			text += "..."
		view.set_status('z_caret_position', text)
