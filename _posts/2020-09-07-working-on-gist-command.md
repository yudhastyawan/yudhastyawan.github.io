---
title: 'Working on Gist Command'
date: 2020-09-07
permalink: /posts/2020/09/working-on-gist-command/
tags:
  - tips
  - gist
---

In this post, I will show you how to deal with Gist on terminal/command line. Why do we should use it? Because we have to do efficiently saving the code and managing the code snippet. That's the idea! So that we should deal with the command line for the better work.

gist-paste
======
For the first understanding, see the description below based on the command `gist-paste --help`:

```bash
Usage: gist-paste [-o|-c|-e] [-p] [-s] [-R] [-d DESC] [-u URL]
                          [--skip-empty] [-P] [-f NAME|-t EXT]* FILE*
       gist-paste --login
       gist-paste [-l|-r]

        --login                      Authenticate gist on this computer.
    -f, --filename [NAME.EXTENSION]  Sets the filename and syntax type.
    -t, --type [EXTENSION]           Sets the file extension and syntax type.
    -p, --private                    Makes your gist private.
        --no-private
    -d, --description DESCRIPTION    Adds a description to your gist.
    -s, --shorten                    Shorten the gist URL using git.io.
    -u, --update [ URL | ID ]        Update an existing gist.
    -c, --copy                       Copy the resulting URL to the clipboard
    -e, --embed                      Copy the embed code for the gist to the clipboard
    -o, --open                       Open the resulting URL in a browser
        --no-open
        --skip-empty                 Skip gisting empty files
    -P, --paste                      Paste from the clipboard to gist
    -R, --raw                        Display raw URL of the new gist
    -l, --list [USER]                List all gists for user
    -r, --read ID [FILENAME]         Read a gist and print out the contents
        --delete [ URL | ID ]        Delete a gist
    -h, --help                       Show this message.
    -v, --version                    Print the version.
```

based the reference from [manpages.ubuntu.com](http://manpages.ubuntu.com/manpages/trusty/man1/gist-paste.1.html), we have to install firstly by using this command (if Ruby has been installed on your computer):

`gem install gist`

Then, login with your Github account by using this command:

`gist-paste --login`

until we can see and inputing the username and password on the command line:

```
Obtaining OAuth2 access_token from github.
GitHub username: 
GitHub password:
2-factor auth code:
Success! https://github.com/settings/applications
```

Viola! You have been already doing some stuffs in gist!!!

How to deal with *gist-paste*
------
copying and modifying some stuffs from the reference, this is the powerful command examples:

To upload the contents of `$filename` just:

`gist-paste $filename`

Upload multiple files:

```
gist-paste $filename1 $filename2 $filename3 
gist-paste *.$extension
```

By default it reads from STDIN, and you can set a filename with -f.

`gist-paste -f test.rb <$filename`

Alternatively, you can just paste from the clipboard (**but you need to make sure *xclip* has to be installed on your computer**):

`gist-paste -P`

but if you didn't install yet `xclip`, you can install using package manager on your OS distribution and then put this following `alias` to your `~/.bashrc`:
```
alias pbcopy='xclip -selection clipboard'
alias pbpaste='xclip -selection clipboard -o'
```
Use -p to make the gist private:

`gist-paste -p $filename`

Use -d to add a description:

`gist-paste -d "the brief description of your gist" $filename`

You can update existing gists with -u with ID of gist:

`gist-paste -u 42f2c239d2eb57299408 $filename`

If you´d like to copy the resulting URL to your clipboard, use -c.

`gist-paste -c <$filename`

If you´d like to copy the resulting embeddable URL to your clipboard, use -e.

`gist-paste -e <$filename`

And you can just ask gist-paste to open a browser window directly with -o.

`gist-paste -o <$filename`

Finally, if we want to see the list of our gists, we can use this command:

`gist-paste --list`