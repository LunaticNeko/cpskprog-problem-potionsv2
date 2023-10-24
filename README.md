# Problem: Potion Shop

There are two sets of instructions on separate matters. You must do them both.

## Git Repository Instructions

You must do the following:

* You must continue developing the code, creating at least two more commits on
  top of the template code given.
* The commit pointed by the HEAD tag must contain both files listed below.
* The file to be graded MUST be called "potions.py".
* Any files provided by the lecturer can be left in, but they will be ignored.

To configure your username and email in the Git environment, from your command
line tool, use the following commands:

```
git config user.name "Kasetsart STUDENT"
git config user.email kasetsart.st@gmail.com
```

This changes your Git username and email just for this repository.

You can use `git config --global ...` instead to make the commands affect
every single repo onwards.

## Programming Problem Instructions

You're an apprentice at a potion shop. The proprietor (owner) is an old man
who often forgets his potion specs, and we're here to help him out.

In the file called `potions.py`, you must implement a class that represents
a potion, of course.

You will be guided precisely in the program file. Implement everything based
on the docstring and doctest. You can do it!

NOTE: The doctest is CORRECT but NOT NECESSARILY COMPLETE. Always check the
docstring to see what else must be implemented!

## Type Hints

To guide you to using correct data types and letting you know what can be
assumed, type hints are given in the code. See the code how it works.

See also: [[https://docs.python.org/3/library/typing.html]]

## Grading Standard

  No. | Score | Criteria
 ---- | ----- | ---------
   1  |   30  | doctest (straightforward) (-1 per failed test, min 0)
   2  |   30  | pytest 1 (basic implementation) (10 tests, 3 points/ea.)
   3  |   20  | pytest 2 (efficiency) (4 tests, 5 points/ea.)
   4  |   10  | PEP 8 (automated linter)
   5  |   10  | Repository Correctness (real name, at least 2 commits)

* Most of the problem will revolve around doing this correctly. Efficiency
  is checked in pytest 2 but is not a major part of your score.
* TA's will check for plagiarism.
* Criteria 4 may still get deducted if we find other faults not detected by
  the linter. Instructor + TA decision is final.
* For Criteria 4, your score is calculated as follows:
    score = lambda x: math.ceil((x-5) * 2)
  This means you must score at least 5 on pylint to receive score in this
  criteria!

## Notes

Inspecting pytest files is permitted but not encouraged.

Following the directions in the assignment file should be enough.

## Problem Author

(C) 2023 Chawanat Nakasan, Department of Computer Engineering,
Faculty of Engineering, Kasetsart University

If you found this as a forked repository, any further work is not done by the
original problem author.

Starter and tester code originally released under MIT License.

