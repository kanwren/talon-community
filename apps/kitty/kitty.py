import os

from talon import Context, Module, actions, ui

# TODO: fit this to terminal.py

ctx = Context()
mod = Module()

ctx.matches = r"""
app: kitty
"""
directories_to_remap = {}
directories_to_exclude = {}

ctx.lists["self.pane_navigation"] = {
    "down": "down",
    "left": "left",
    "right": "right",
    "up": "up",
    "next": "next",
    "previous": "previous",
}
mod.list("pane_navigation", desc="Pane navigation commands")

@mod.capture(rule="{user.pane_navigation}")
def pane_navigation(m) -> str:
    "One pane navigation command"
    return m.pane_navigation

@mod.capture(rule="<user.pane_navigation>+")
def pane_navigations(m) -> str:
    "One or more pane navigation commands"
    return str(m)


@mod.action_class
class Actions:
    def pane_navigate(s: str):
        "Follows one or more pane navigation commands"
        for d in s.split():
            if d == "left":
                actions.key("ctrl-shift-h")
            elif d == "right":
                actions.key("ctrl-shift-l")
            elif d == "up":
                actions.key("ctrl-shift-k")
            elif d == "down":
                actions.key("ctrl-shift-j")
            elif d == "next":
                actions.key("ctrl-shift-e")
                actions.key("n")
            elif d == "previous":
                actions.key("ctrl-shift-e")
                actions.key("p")
            else:
                raise RuntimeError(f"Invalid pane navigation command: {d}")


@ctx.action_class("edit")
class EditActions:
    def delete_line():
        actions.key("ctrl-u")


@ctx.action_class("user")
class UserActions:
    def tab_jump(number: int):
        actions.key(f"ctrl-shift-{0 if number == 10 else number}")

    def file_manager_current_path():
        title = ui.active_window().title

        # take the first split for the zsh-based terminal
        if " - " in title:
            title = title.split(" - ")[0]

        if "~" in title:
            title = os.path.expanduser(title)

        if title in directories_to_remap:
            title = directories_to_remap[title]

        if title in directories_to_exclude:
            title = None

        return title

    def file_manager_show_properties():
        return

    def file_manager_open_directory(path: str):
        actions.insert("cd ")
        path = f'"{path}"'
        actions.insert(path)
        actions.key("enter")
        actions.user.file_manager_refresh_title()

    def file_manager_open_parent():
        actions.insert("cd ..")
        actions.key("enter")

    def file_manager_select_directory(path: str):
        actions.insert(path)

    def file_manager_new_folder(name: str):
        name = f'"{name}"'
        actions.insert("mkdir " + name)

    def file_manager_open_file(path: str):
        actions.insert(path)
        actions.key("enter")

    def file_manager_select_file(path: str):
        actions.insert(path)

    def file_manager_refresh_title():
        return


@ctx.action_class("app")
class AppActions:
    def tab_open():
        actions.key("ctrl-shift-t")

    def tab_close():
        actions.key("ctrl-shift-z")

    def tab_previous():
        actions.key("ctrl-shift-p")

    def tab_next():
        actions.key("ctrl-shift-n")

