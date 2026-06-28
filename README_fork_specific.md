
# List of changes since forking

The code was produced during a hackathon on/of OmegaClaw. 
It is a series of small changes that get the system running on MacOS locally
against gemma4:e4b which is served via ollama.

gemma4:e4b requires about 8GB of memory.


# Changes

 - Install - built swi-prolog from source so that it was compiles against the correct python version.   
`
 brew reinstall --build-from-source swi-prolog
`
 - BUG: Code assumes linux and fails on MacOS. Add check which disables Landlock policy and warns. 
 - New provider that loads a custom system prompt



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

# Results

System could process the prompt at around 384.59 tokens per second, and could answer at about 26.46 tokens per second.
Running locally allowed 
 - faster prompt tuning,
 - faster iteration time on code changes
 - deeper understanding of the code
 - no concern over token usage
 - ability to reduce or remove 'sleeps' between messages to LLM, i.e. no dead time.


