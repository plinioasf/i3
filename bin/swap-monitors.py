#!/usr/bin/python3

import i3

def main():
    outputs = i3.get_outputs()
    workspaces = i3.get_workspaces()

    active_workspaces = [o['current_workspace'] for o in outputs if o['active'] is True]

    if len(active_workspaces) != 2:
        return

    focused_workspace = [w['num'] for w in workspaces if w['focused'] is True]
    active_workspaces.remove(str(focused_workspace[0]))
    i3.command('workspace', active_workspaces[0])

if __name__ == '__main__':
    main()
