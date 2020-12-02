# Password Philosophy

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc

Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?

## Pseudocode

    // List of Tuples -> Number
    // Given a Set of Password Rule Definitions and Possible Passwords, total the number of Passwords which pass their respective definitions
    For each tuple:
        Evaluate password using Regex constructed from Rule Definition
        If Regex found, add 1 to count
        If not, move to next tuple

No matter what, we are going to have to go through the entire list at least once. This solution does that, and keeps track of the results pretty efficiently with a simple counter. There may be some optimizations possible (such as first checking if the given letter exists at all before checking if it matches the required count), but these are unlikely to be significant in their impact (and could possibly add time by requiring evaluating each item twice for limited benefit).

Actually, the trickier piece of this problem seems to be how to get the input into a form that's readable by the code. Let's define the structure of our Tuple:

    Passwords Tuple is:
        - lower bound
        - upper bound
        - character
        - string // proposed password

So our evaluation is asking: Does the proposed string contain the character with a count between the lower bound and the upper bound.

To translate the input, we're going to need to do some separating:

    For each line in input:
       - The first numbers before a "-" = lower bound
       - The numbers between the "-" and a space = upper bound
       - The char between the first space and a ":" = the character
       - the remaining string after the final space = the proposed password

We'll need to construct a list of these tuples from each line of the input.
