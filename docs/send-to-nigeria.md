---
title: Send to Nigeria
---

send-to-nigeria is a free, open-source guide to getting goods from the US to Nigeria cheaply and safely. It is for shoppers in Nigeria and senders in the US.

It compares the usual routes: a relative's bag, Amazon, Nigerian and global forwarders, traveller apps, express couriers, and buying locally. Every price it uses has a source and a date. It also covers Nigerian duty, prohibited items, and ways to pay from Nigeria.

This is general information, not legal, customs or tax advice. Prices and rules change, so confirm with the carrier or forwarder before you ship.

## Scenarios: US city by size class

There is a guide for each US city we have reviewed: [Chicago](guide/scenarios/chicago.md), [DC and Baltimore](guide/scenarios/dc-baltimore.md), [Houston and Texas](guide/scenarios/houston-texas.md) and [Atlanta](guide/scenarios/atlanta.md). Each guide has one section per size class, from an envelope to a garage load, and each section ends with the expected best route and why. These pages are built from the plugin's files, so you always see the current figures.

The size classes, and how each one is billed, are explained in [size classes](guide/size-classes.md). For a city that is not listed, the plugin researches it live and labels the results "not yet reviewed".

More from the guide:

- [Options ladder](guide/options-ladder.md): the routes and when each one wins.
- [Price baseline](guide/price-baseline.md): prices per provider, with sources and dates.
- [Provider directory](guide/providers.md): shippers and forwarders by type, with no paid placement.
- [Nigerian duty](guide/nigeria-duty.md) and [prohibited items](guide/prohibited-and-carry-warnings.md).
- [Paying from Nigeria](guide/paying-from-nigeria.md).

## Sources

The [research notes](research/index.md) summarise the research behind the guide. The full sourced notes are in public issues [#12](https://github.com/Erriccc/jappa-labs/issues/12), [#16](https://github.com/Erriccc/jappa-labs/issues/16) and [#17](https://github.com/Erriccc/jappa-labs/issues/17). The [resources page](guide/resources.md) says what each one covers and where the original sources are.

Found a better price, a new city, or a mistake? [Open an issue](https://github.com/Erriccc/jappa-labs/issues/new).

## For builders

The guide is also a plugin for Claude Code. From inside Claude Code:

```
/plugin marketplace add Erriccc/jappa-labs
/plugin install send-to-nigeria@jappa-labs
```

Then ask in plain words, for example "cheapest way to get an air fryer from Atlanta to Lagos?", or run `/send-to-nigeria:ship-quote` for a step-by-step quote. The plugin re-checks live pages before giving a quote.

The full source is in [plugins/send-to-nigeria](https://github.com/Erriccc/jappa-labs/tree/main/plugins/send-to-nigeria).
