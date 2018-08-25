# ZSH history sorter

ZSH has a great feature of preserving command history
from multiple shells. But sometimes it's also useful to combine
shell histories from multiple hosts.  One can just 'cat' all the
history files together, and this work.  There is just one slight
problem with this.  The history file must be sorted by timestamp
of the command.

This little tool does exactly that.  It reads concatenation of
multiple history files and outputs them as sorted by the
timestamp field.

