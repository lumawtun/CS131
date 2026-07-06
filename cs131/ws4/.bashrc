#!/bin/bash
# ~/.bashrc  —  Lucas, CS131

# ---- if-statement: only run the rest for interactive shells ----
case $- in
    *i*) ;;        # interactive -> keep going
      *) return;;  # non-interactive (scp, cron) -> stop here
esac

# ---- alias: jump straight into the CS131 repo ----
alias cs131='cd ~/cs131'

# ---- alias: readable long listing with human sizes + colors ----
alias ll='ls -alFh --color=auto'

# ---- if-statement: only enable colored grep if dircolors exists ----
if [ -x /usr/bin/dircolors ]; then
    alias grep='grep --color=auto'
fi

# ---- shell function: stage, commit, and push in one step ----
gacp() {
    if [ -z "$1" ]; then
        echo "usage: gacp \"commit message\""
        return 1
    fi
    git add -A && git commit -m "$1" && git push
}
