
# List of changes since forking

The code was produced during a hackathon on/of OmegaClaw. 
It is a series of small changes that get the system running on MacOS locally
against gemma4:e4b which is served via ollama.

gemma4:e4b requires about 8GB of memory.


# Changes

Install - built swiprolog from source so that it was compiles against the correct python version. : 
BUG: Code assumes linux and fails on MacOS. Add check which disables Landlock policy and warns. 



#

Result