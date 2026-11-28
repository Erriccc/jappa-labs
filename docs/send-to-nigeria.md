---
title: Send to Nigeria
---

send-to-nigeria is a free, open-source plugin for Claude Code. It helps shoppers in Nigeria and senders in the US pick a cheap, safe way to get goods from the US to Nigeria.

It compares the usual routes: a relative's bag, Amazon, Nigerian and global forwarders, traveller apps, express couriers, and buying locally. Every price it uses has a source and a date, and it re-checks live pages before giving a quote. It also covers Nigerian duty, prohibited items, and ways to pay from Nigeria.

This is general information, not legal, customs or tax advice. Prices and rules change, so confirm with the carrier or forwarder before you ship.

## Install

From inside Claude Code:

```
/plugin marketplace add Erriccc/jappa-labs
/plugin install send-to-nigeria@jappa-labs
```

Then ask in plain words, for example "cheapest way to get an air fryer from Atlanta to Lagos?", or run `/send-to-nigeria:ship-quote` for a step-by-step quote.

## Scenarios: US city by size class

The plugin has a guide for each US city it has reviewed: [Chicago](https://github.com/Erriccc/jappa-labs/blob/main/plugins/send-to-nigeria/skills/send-to-nigeria/references/scenarios/chicago.md), [DC and Baltimore](https://github.com/Erriccc/jappa-labs/blob/main/plugins/send-to-nigeria/skills/send-to-nigeria/references/scenarios/dc-baltimore.md), [Houston and Texas](https://github.com/Erriccc/jappa-labs/blob/main/plugins/send-to-nigeria/skills/send-to-nigeria/references/scenarios/houston-texas.md) and [Atlanta](https://github.com/Erriccc/jappa-labs/blob/main/plugins/send-to-nigeria/skills/send-to-nigeria/references/scenarios/atlanta.md). Each guide has one section per size class, from an envelope to a garage load, and each section ends with the expected best route and why. The links open the plugin's own files, so you always see the current figures.

The size classes, and how each one is billed, are explained in [size-classes.md](https://github.com/Erriccc/jappa-labs/blob/main/plugins/send-to-nigeria/skills/send-to-nigeria/references/size-classes.md). For a city that is not listed, the plugin researches it live, following its [research method](https://github.com/Erriccc/jappa-labs/blob/main/plugins/send-to-nigeria/skills/send-to-nigeria/references/research-method.md), and labels the results "not yet reviewed".

Other files in the plugin:

- [Options ladder](https://github.com/Erriccc/jappa-labs/blob/main/plugins/send-to-nigeria/skills/send-to-nigeria/references/options-ladder.md): the routes and when each one wins.
- [Price baseline](https://github.com/Erriccc/jappa-labs/blob/main/plugins/send-to-nigeria/skills/send-to-nigeria/references/price-baseline.md): prices per provider, with sources and dates.
- [Nigerian duty](https://github.com/Erriccc/jappa-labs/blob/main/plugins/send-to-nigeria/skills/send-to-nigeria/references/nigeria-duty.md) and [prohibited items](https://github.com/Erriccc/jappa-labs/blob/main/plugins/send-to-nigeria/skills/send-to-nigeria/references/prohibited-and-carry-warnings.md).
- [Paying from Nigeria](https://github.com/Erriccc/jappa-labs/blob/main/plugins/send-to-nigeria/skills/send-to-nigeria/references/paying-from-nigeria.md).

The full source is in [plugins/send-to-nigeria](https://github.com/Erriccc/jappa-labs/tree/main/plugins/send-to-nigeria).

## Sources

The research behind the plugin is in public issues [#12](https://github.com/Erriccc/jappa-labs/issues/12), [#16](https://github.com/Erriccc/jappa-labs/issues/16) and [#17](https://github.com/Erriccc/jappa-labs/issues/17). The plugin's [resources file](https://github.com/Erriccc/jappa-labs/blob/main/plugins/send-to-nigeria/skills/send-to-nigeria/references/resources.md) says what each one covers and where the original sources are.

Found a better price, a new city, or a mistake? [Open an issue](https://github.com/Erriccc/jappa-labs/issues/new).
