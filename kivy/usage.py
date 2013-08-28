#!/usr/bin/env python

import sys

'''
Kivy program

Usage:
    %s [-hdafkwrs] [-c section:key[:value]] [-p id:provider[,options]] [-m mod] [--size=geometry] [--dpi=depth] [--display=display]

Options:
    -h --help                Prints this help message.
    -d --debug               Shows debug log
    -a --auto-fullscreen     Force 'auto' fullscreen mode (no resolution change).
                             Uses your display's resolution. This is most likely what you want.
    -c --config configopt    Set a custom [section] key=value in the configuration object
                             where configopt is section:key[:value]
    -f --fullscreen          Force running in fullscreen mode.
    -k --fake-fullscreen     Force 'fake' fullscreen mode (no window border/decoration).
                             Uses the resolution specified by width and height in your config.
    -w --windowed            Force running in a window.
    -p --provider provopt    Add an input provider (eg: ccvtable1:tuio,192.168.0.1:3333).
                             Where provopt is id:provider[,options]
    -m mod --module mod      Activate a module (use "list" to get a list of available modules).
    -r --rotation            Rotate the window's contents (0, 90, 180, 270).
    -s --save                Save current Kivy configuration.
    --size geometry          Size of window geometry.
    --dpi depth              Manually overload the Window DPI (for testing only.)
    --display display        Sets the display

''' % basename(sys.argv[0])


