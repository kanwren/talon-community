app: kitty
and not win.title: /vim/
-
# makes the commands in terminal.talon available
tag(): terminal

# use readline keybindings for various editing commands
tag(): user.readline

# activates the implementation of the commands/functions in terminal.talon
tag(): user.generic_unix_shell

# makes commands for certain applications available
# you can deactivate them if you do not use the application
tag(): user.git
tag(): user.kubectl

tag(): user.tabs
