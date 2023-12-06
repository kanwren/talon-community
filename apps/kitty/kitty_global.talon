app: kitty
-
tag(): user.readline
tag(): user.tabs

suspend: key(ctrl-z)
resume:
    insert("fg")
    key(enter)

shell copy: key("ctrl-shift-c")
shell paste: key("ctrl-shift-v")

pane layout tall:
    key("ctrl-shift-g")
    key("t")
pane layout wide:
    key("ctrl-shift-g")
    key("f")
pane layout stack:
    key("ctrl-shift-g")
    key("shift-s")
pane layout grid:
    key("ctrl-shift-g")
    key("g")
pane layout binary:
    key("ctrl-shift-g")
    key("x")
pane layout main:
    key("ctrl-shift-g")
    key("x")
pane layout row:
    key("ctrl-shift-g")
    key("s")
pane layout column:
    key("ctrl-shift-g")
    key("v")
pane layout decrease:
    key("ctrl-shift-[")
pane layout increase:
    key("ctrl-shift-]")
pane rotate:
    key("ctrl-shift-r")
# like the stack layout, but togglable
pane only:
    key("ctrl-shift-o")

vertical split: key("ctrl-shift-w")
split: key(ctrl-shift-s)

pane detach: key("ctrl-shift-d")
pane close: key("ctrl-shift-q")
pane left: key("ctrl-shift-h")
pane right: key("ctrl-shift-l")
pane down: key("ctrl-shift-j")
pane up: key("ctrl-shift-k")
pane move left:
    key("ctrl-shift-m")
    key("h")
pane move right:
    key("ctrl-shift-m")
    key("l")
pane move down:
    key("ctrl-shift-m")
    key("j")
pane move up:
    key("ctrl-shift-m")
    key("k")

tab move backward: key("ctrl-shift-,")
tab move forward: key("ctrl-shift-.")

hint url:
    key("ctrl-shift-y")
    key("u")
hint path:
    key("ctrl-shift-y")
    key("p")
hint hash:
    key("ctrl-shift-y")
    key("h")
hint line:
    key("ctrl-shift-y")
    key("l")
hint ip:
    key("ctrl-shift-y")
    key("i")

hint multi url:
    key("ctrl-shift-y")
    key("m")
    key("u")
hint multi path:
    key("ctrl-shift-y")
    key("m")
    key("p")
hint multi hash:
    key("ctrl-shift-y")
    key("m")
    key("h")
hint multi line:
    key("ctrl-shift-y")
    key("m")
    key("l")
hint multi ip:
    key("ctrl-shift-y")
    key("m")
    key("i")

