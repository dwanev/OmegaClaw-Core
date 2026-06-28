
# AIM

1) Get OmegaClaw running and start to understand it
2) Get it working against a local LLM.
3) Understand custom skills.


# List of changes since forking

The code was produced during a hackathon on/of OmegaClaw. 
It is a series of small changes that get the system running on MacOS locally
against gemma4:e4b which is served via ollama.

gemma4:e4b requires about 8GB of memory and could process 384.59 tokens per second for the prompt and could 
answer at about 26.46 tokens per second on a Macbook M3 with 96GB of memory.


# Changes

 - Install - built swi-prolog from source so that it was compiles against the python version installed in the system.   
`
 brew reinstall --build-from-source swi-prolog
`
 - BUG: Code assumes linux and fails on MacOS. Add check which disables Landlock policy and warns. 
 - New provider that connects to ollama, and strips certain strings from the prompts.
 - New system prompt


# New System Prompt Used  
`
System Break down the user task into a plan that is expressed as a list of skill calls. So a user task of 'remember that the morning standup is at 10am', would output a plan of one step, (remember "that the morning standup is at 10am")  
SKILLS: [  
 '- Remember a particular string such as skills and memories: remember string',   
 '- Query long-term embedding memory for skills and memories with short phrases only: query string',   
 '- Episodes searches history for episodes around a time stamp, time format is same as in TIME: episodes time_string', 
 '- Pin a certain string as short-term working memory item to keep track of task state: pin string', 
 '- Execute shell command without apostrophe in string, it returns the command output to you: shell string', 
 '- Read file to string: read-file filename', 
 '- Write string to file: write-file filename string', 
 '- Append line to file: append-file filename string',  
 '- Send message to user: send string', 
 '- Search the web: search string', '- Search the web using the Tavily Search Agent: tavily-search string', 
 '- Get technical analysis for a stock ticker using the Technical Analysis Agent: technical-analysis ticker', 
 '- Send dwane a message with the skill dv-skill1 : (dv-skill1 "msg to send dwane")'
 '- Execute MeTTa expression: metta sexpression', 'Example to invoke Non-Axiomatic Logic via MeTTa: ', 
 'metta (|- ((--> (× sam garfield) friend) (stv 1.0 0.9))', 
 '          ((--> garfield animal) (stv 1.0 0.9)))', 
 'metta (|- ((==> (--> (× $1 elephant) eat) (--> $1 ([] dangerous))) (stv 1.0 0.9))', 
 '          ((--> (× tiger elephant) eat) (stv 1.0 0.9)))', 
 'Also: note the $1 for independent variables, and for negated knowledge use (stv 0.0 0.9)', 
 'Additionally |- also works for revision, to merge evidence even when the term of both premises is the same.', 
 'You can also use PLN:', 'metta (|~ ((Implication (Inheritance $1 (IntSet Feathered))', 
 '           (Inheritance $1 Bird)) (stv 1.0 0.9))', 
 '          ((Inheritance Pingu (IntSet Feathered)) (stv 1.0 0.9)))'] 
Task 
`

# User instruction entered to the system via IRC

`
Send dwane the message "that the bananas are green" and then write the same message to the file "./dwane.txt"
`
 - triggered a syntax error in the result as the LLM returned the " symbols, and metta(?) could not parse it.

`
Send dwane the message 'that the bananas are green' and then write the same message to the file ./dwane.txt
`
 - this version is processed correctly

# Limitations

 - The 'prompt.txt' file needed to be overwritten with the prompt above. Swapping in a clean way is still in progress.
 - _quote_ _newline_ and others are stripped from the prompts sent to gemma. this seems to be necessary, but where it has been implemented probably violates the design of the rest of the system.
 - LLM settings like temperature have not been looked at. Reducing temperature may make the example more reproducible.

# Results

OmegaClaw **CAN** be run natively on a Macbook. (**beware** it is not yet sandboxed)

The query was process correctly. The following was returned from the LLM:
(RESPONSE: ((dv-skill1 "that the bananas are green") (write-file "./dwane.txt" "that the bananas are green")))

Which was parsed correctly and both actions were triggered correctly. 

System could process the prompt at around 384.59 tokens per second, and could answer at about 26.46 tokens per second.
Running locally allowed 
 - faster prompt tuning
 - faster iteration time on code changes
 - deeper understanding of the code
 - no concern over token usage
 - ability to reduce or remove 'sleeps' between messages to LLM, i.e. no dead time.




