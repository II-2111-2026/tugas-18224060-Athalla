# Probability & Statistics — GitHub Classroom (Practice Mode)

This starter repo is built for **Option 3**:
- Instructor updates quizzes/tests freely
- Student work is isolated in `submissions/` so it won't be overwritten

## Golden rule
Students edit **ONLY**:
- `submissions/wXX/answers.py`

Instructors edit/update freely:
- `weeks/wXX/quiz.qmd`
- `tests_bank/wXX/quiz_tests.py`
- `.github/**`, `tools/**`, `requirements.txt`, `ACTIVE_WEEK.txt`

## Week 01 (Practice Mode)
Week 01 is **complete** (quiz + tests), but `submissions/w01/answers.py` starts as **stubs**.
So the first run will fail until students implement the functions.

If you want a separate “demo-green” experience, use the other template that pre-fills a solution.

## How autograding chooses the week
- If a push changes exactly one folder `submissions/wXX/...`, that `wXX` is graded.
- Otherwise, autograding uses `ACTIVE_WEEK.txt` (instructor sets it weekly).

## GitHub Classroom setup (recommended)
Create **one** Classroom assignment for the whole semester from this template repo.

Protect these paths:
- `.github/**`
- `tools/**`
- `weeks/**`
- `tests_bank/**`
- `ACTIVE_WEEK.txt`
- `requirements.txt`

Do NOT protect:
- `submissions/**`
