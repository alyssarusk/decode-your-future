# Password Cracker Activity
*Full Hour++ Lesson Plan can be found here for reference: [Password Cracker Lesson Plan](https://docs.google.com/document/d/1HAWjv2axYfAadN1Ue5201FzdvFxN5G3nJmjiY27EH5o/edit?tab=t.0#heading=h.qbyo3qi0b6m2).*

A digital copy of the activty handout can be found here: [Password Cracker Handout](https://github.com/alyssarusk/decode-your-future/Handouts/PasswordCrackerHandout.pdf).

1. Visual studio code should be open with the password cracker project
    - Ensure font size on VS Code is set to 14 pt font or something sufficiently easy to see 
    - Ensure code and terminal can be seen
2. *Time-permitting:* Briefly walk students through the code 
    - Get password from user
    - Start timer 
    - Define the characters to use (a-z)
        - We can change this later to include uppercase letters too
    - Iterate through every combination, increasing size of password guess until the correct password is reached
        - Each time check if the current guess matches the actual password
        - If all combinations for that length of password fail, increase the password guess size
    - End timer 
    - Output password and time it took
3. Show students how to run the program
    - `python password-cracker.py`
    - After that command is run it will ask for a password 
    - We keep using `python password-cracker.py` command each time we want to try a password
4. Have students experiment with passwords of length 1 all the way up to length 6 
    - Note the difference in time as the password increases 
    - Students may observe how the time increase is exponential 
    - Look at the difference even between 4 to 6 length passwords
        - Phone passwords tend to be 4 or 6 numbers in length 
    - Do not do a password above 6 characters in length 
        - Takes way too long!
5. **If students at any point give a very long password and are waiting too long they can use `ctrl + c` or `cmd + c` to stop the program from running**
6. Optional: Have students now try it with passwords that include upper or lower case letters 
    - Change characters to be: 
        - `characters = string.ascii_letters`
    - Does this make as much of a difference compared to length?
    - How does password complexity vs length compare 
7. Optional: Can discuss some questions afterwards 
    - What could we do to speed up our guessing?
        - Potential discussion points:
            - Make logical guesses
    - What are some methods we could use to help prevent someone from logging in as us?
        - Potential discussions points:
            - MFA
            - Limited login attempts
