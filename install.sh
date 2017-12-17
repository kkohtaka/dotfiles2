#!/usr/bin/env bash

export DOTFILES_DIRS=$HOME/dotfiles

rcup \
  -t atom \
  -t bash \
  -t git \
  -t mozc \
  -t rcm \
  -t syp
