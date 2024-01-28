tag: terminal
-

katie previous: insert('prevd\n')
katie next: insert('nextd\n')

# wd command
wade: insert('wd ')
wade list: insert('wd list\n')
wade <user.text>: insert('wd "{text}"\n')

# h command
harry: insert('h ')
harry <user.text>: insert('h "{text}"\n')

# file system shortcuts
go to home: insert('cd ~\n')
go to talon: insert('cd ~/.talon/user\n')
go to downloads: insert('cd ~/Downloads\n')
go to desktop: insert('cd ~/Desktop\n')
