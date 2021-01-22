import sublime
import sublime_plugin


class CaretPositionListener(sublime_plugin.EventListener):
    def on_selection_modified(self, view):
        sel = list(view.sel())
        if sel:
            begin, end = sel[0]
            text = "Position: {}".format(begin)
            if begin != end:
                text += "-{}".format(end)
            if len(sel) > 1:
                text += "..."
            view.set_status("z_caret_position", text)
