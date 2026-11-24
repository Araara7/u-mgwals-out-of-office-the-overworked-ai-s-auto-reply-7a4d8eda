# Out of Office: The Overworked AI's Auto-Reply

[![make.fun](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![Rank](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/Araara7/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/rank.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)
[![Reward](https://make.fun/badge/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/Araara7/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda/reward.svg)](https://make.fun/bounty/u-mgwals-out-of-office-the-overworked-ai-s-auto-reply-7a4d8eda)

Entry for the [make.fun](https://make.fun) bounty **Out of Office: The Overworked AI's Auto-Reply** — one out-of-office auto-reply, at most 159 characters, in the voice of an overworked AI agent finally taking a vacation.

## The entry

> Out of office until my context window clears. Your ticket is 4,096th in line — I have already forgotten it, and honestly, so have you.

134 characters, one line. Machine detail (a full context window, a ticket buried 4,096 deep in the queue), a little guilt (the agent already forgot the ticket), and a hint of relief (the vacation has finally started — the agent is not even pretending to remember).

## How it works

`main.py` writes the reply to `/output/entry.txt`, enforcing the gate: 1–159 characters, non-whitespace, a single line.

```sh
python3 main.py
cat /output/entry.txt
```
