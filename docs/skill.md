---
title: The skill
---

The Send to Nigeria guide also works as a skill for AI assistants. It answers from the same sourced, dated research as the [guides](guides.md), and re-checks live pages before it gives a quote.

## For senders

Ask it in plain words, for example "cheapest way to get an air fryer from Atlanta to Lagos?". It can tell you:

- which size class your item falls in, and how that size is billed;
- the cheapest safe way to send it from your city;
- what you must not send or carry;
- whether Nigerian duty applies.

Today it runs inside an AI assistant such as Claude, so you need one set up to use it. A ready-to-use chat assistant is coming soon, in [issue #26](https://github.com/Erriccc/jappa-labs/issues/26). Until then, the [guides](guides.md) have the same answers.

## For builders and creators

The skill is a plugin for Claude Code. From inside Claude Code:

```
/plugin marketplace add Erriccc/jappa-labs
/plugin install send-to-nigeria@jappa-labs
```

Then ask in plain words, or run `/send-to-nigeria:ship-quote` for a step-by-step quote.

Coming soon:

- Skill-only, tool-only (MCP) and full-plugin installs, in [issue #22](https://github.com/Erriccc/jappa-labs/issues/22).
- A branded version creators can run with their own referral code, in [issue #24](https://github.com/Erriccc/jappa-labs/issues/24).

The source is in [plugins/send-to-nigeria](https://github.com/Erriccc/jappa-labs/tree/main/plugins/send-to-nigeria) on GitHub.
