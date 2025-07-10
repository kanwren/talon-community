tag: terminal
and tag: user.nix
-
nix {user.nix_command} [<user.nix_arguments>]:
    args = nix_arguments or ""
    "nix {nix_command}{args} "
