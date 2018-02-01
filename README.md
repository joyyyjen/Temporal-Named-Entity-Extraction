# date_matching
Homework 1 for LING 406
Temporal Named Entity Extraction:
- This program reads from standard input and outputs the American format of date. 

It's a python program. (Idealy python3)
- using library re and stdin

1. How to run?
- If you are using Mac, open Terminal, run ./datereg.py

2. Double check the python path in your environment
- mine is in /usr/local/bin/python3
- After executed, if you received this error: "No such file or directory"
- try changing the first line #!/usr/local/bin/python3 to #!/usr/bin/python3 

3. How does it work?
- The program read from standard input
- The default testfile for this progam is "testpp.txt"
- run "cat testpp.txt | ./datereg.py"
- or you can use your own txt file, using cat "your-file-name" | ./datereg.py on Terminal

- the testpp.txt output a testline in format of ****[0-9]**** indicating there should be how many solutions for each paragraph



