# Caesar-Crack
Caesar-cipher bruteforce program

A Caesar cipher is an insecure method of encryption involving "shifting" letters forwards or backwards based on a "shift key" in order to hide information.
Each letter is assigned a number 1-26, and has the number of the shift key(e.g. 3) added to it.
This is then changed backed into letters resulting in a scrambled message.
For example: "hello" -> "khoor", with a key of 3

This is extremely insecure, as if you simply guess every key, you will crack the cipher.

I have created this program to demonstrate that even a sub-par programmer like myself can very easily write a program that breaks low level encryption such as this.

NOTE: This program is not meant to be used! It is a proof of concept as to how easy breaking Caesar ciphers is and as such is: not user friendly, not optimized,
and not thoroughly bug-checked! Like, at all!

For those of you dead-set on using this code-breaking disaster, it is relatively straightforward:
1. Input encoded string when prompted by ">>"
2. Watch in wonder as the console spits out a just-barely comprehensible list of EVERY POSSIBLE CIPHER!(not quite, but it sure is quite a few of them).

HOW IT WORKS:
This program takes the following steps:
1. Accept string
2. Break string into characters
3. Shift characters up by key
4. Reassemble characters
5. Print
6. Shift characters down by the same key(from the same starting point as the shift up)
7. Print
8. Increase key by 1
9. Repeat until key=26
10. Loop from a->z or z->a if necessary

NOTE 2: For parsing reasons, all characters will be changed to lowercase.
