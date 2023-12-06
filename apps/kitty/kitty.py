import os

from talon import Context, actions, ui

# TODO: fit this to terminal.py

ctx = Context()
ctx.matches = r"""
app: kitty
"""
directories_to_remap = {}
directories_to_exclude = {}


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

