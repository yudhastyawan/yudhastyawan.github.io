---
title: 'How Cool i3 Window Manager!'
date: 2020-09-08
permalink: /posts/2020/09/powerful_i3wm/
tags:
  - review
  - cheat sheet
---

As a Linux lover, have you ever try window manager like i3wm? If you didn't try it yet, let me inform you how powerful it is.

i3wm
------
i3 is a dynamic tilling window manager inspired by wmii that is primarily targeted at developers and advanced users <sup>[1](https://wiki.archlinux.org/index.php/I3)</sup>. The goal is to control the appearance and placement of windows in a windowing system. It can be used as a part of Desktop Environment like GNOME or KDE, but also it can be used as standalone applications <sup>[2](https://opensource.com/article/18/8/i3-tiling-window-manager)</sup>. Currently I have used this window manager as a kind of standalone applications. If you want to do efficiently in your computer without worrying about the good viewer of desktop environment looks like, try it and let you enjoy to all these features!

![Overview of i3 Window Manager](/images/i3wm.png "Overview of i3 Window Manager")

<center>Overview of i3 Window Manager</center>


Why should we use i3? <sup>[2](https://opensource.com/article/18/8/i3-tiling-window-manager)</sup>
------
1. Minimalism, you can enjoy your computer what only you want.
1. Screen real estate, minimising a program is useless!
1. Keyboard-driven workflow, mouse can be rarely used!
1. Flexibility to set up by your own configuration
1. Easy to control workspaces


Controling i3wm using Keyboard Shortcuts
------
That's the point! As a user who deep in the Linux environment, terminal is everything. All of the stuffs can be done efficiently by using command lines. Okay, these are some configurations to do in i3wm. In this session, I used [cheatography.com](https://cheatography.com/davechild/cheat-sheets/i3-window-manager/) as a reference to see the default of i3 window manager keyboard shortcuts.

**Controlling i3**

Keyboard key | Description
--- | ---
$mod+Shift+r | Reload i3
$mod+Shift+e | Exit i3

*Note:* Reload i3 is important if you want to reset or update the configuration file on i3 so that you can use it directly without restarting the computer.

**Manage Windows**

Keyboard key | Description
--- | ---
$mod+Shift+q | Kill current window
$mod+Shift+num | Move current window to workspace number num
$mod+Shift+f | Set window to floating mode
$mod+j | Focus on window to the left
$mod+k | Focus on window above
$mod+l | Focus on window below
$mod+; | Focus on window to the right
$mod+Shift+j | Move window left
$mod+Shift+k | Move window up
$mod+Shift+l | Move window down
$mod+Shift+; | Move window right

*Note:* I am not familiar with the default kill current window, so I change the key with `Ctrl+F4` in i3 config file. You can check the file in the directory `~/.config/i3/config`. In addition, focusing on certain window can be done by using `$mod+{arrow}`. Great!

**Workspaces**

Keyboard key | Description
--- | ---
$mod+num | Switch to workspace num
$mod+Shift+num | Move current window to workspace number num

**Containers**

Keyboard key | Description
--- | ---
$mod+e | Default container
$mod+h | Horizontal split container
$mod+v | Vertical split container
$mod+w | Tabbed container
$mod+f | Toggle fullscreen mode
$mod+s | Toggle stacking mode
$mod+S­hif­t+Space | Toggle floating mode

*Note:* These are powerful keyboard shortcuts for managing the container.

**Applications**

Keyboard key | Description
--- | ---
$mod+enter | Open new terminal window
$mod+d | Open dmenu