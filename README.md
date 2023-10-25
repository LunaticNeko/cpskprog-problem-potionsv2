# Problem: Potion Shop v2

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

In this version, you are expected to implement the potions program using
a more robust method, defining properties as well.

NOTE: The doctest is CORRECT but NOT NECESSARILY COMPLETE. Always check the
docstring to see what else must be implemented!

## Grading Standard

  No. | Score | Criteria
 ---- | ----- | ---------
   1  |   30  | doctest (straightforward) (-1 per failed test, min 0)
   2  |   10  | pytest 1 (basic implementation) (10 tests, 1 points/ea.)
   3  |   10  | pytest 2 (efficiency) (5 tests, 2 points/ea.)
   4  |   20  | pytest 3 (basic implementation V2) (10 tests, 2 points/ea.)
   5  |   10  | pytest 4 (efficiency V2) ("2" tests, 5 points/ea.)
   6  |   10  | PEP 8 (automated linter)
   7  |   10  | Repository Correctness (real name, at least 2 commits)

* Pytest files 1 and 2 are (almost) the same as previous version.
* Each test shows up as all-or-nothing on GitHub. Granular scoring will be
  done by TA or instructor. The final score is then given on Google Classroom.
* Most of the problem will revolve around doing this correctly. Efficiency
  is checked in pytest 2 but is not a major part of your score.
* TA's will check for plagiarism.
* PEP 8 check may still get deducted if we find other faults not detected by
  the linter. Instructor + TA decision is final.
* For PEP 8 check, your score is calculated as follows:
    score = lambda x: math.ceil((x-5) * 2)
  This means you must score at least 5 on pylint to receive score in this
  criteria!

## Notes

* Inspecting pytest files is permitted but not encouraged. Following the
  directions in the assignment file should be enough.
* Intentional modification of pytest files to circumvent proper grading process
  is considered academic dishonesty and will be punished accordingly.
  If you want to create tests of your own, implement them as additional files.
  (File and function names should begin with test_ to allow pytest to detect
  them properly.)

## Problem Author

(C) 2023 Chawanat Nakasan, Department of Computer Engineering,
Faculty of Engineering, Kasetsart University

If you found this as a forked repository, any further work is not done by the
original problem author.

Starter and tester code originally released under MIT License.

