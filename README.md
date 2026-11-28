# Jappa Labs

Jappa Labs is a lab that builds brands and tools for west africans living abroad.

We are starting with idle land and empty houses back home. We aim to verify the owner's title, find tenants (farmers for land, renters for houses), collect rent and send it abroad. Owners keep the asset and could spend less of their own money supporting family.

## Open-source projects we build on (in progress)

We are curating active open-source projects to build on. The list is being collected in [issue #1](https://github.com/Erriccc/jappa-labs/issues/1) and will be added here.

## Plugin: send-to-nigeria

A Claude Code plugin for shoppers in Nigeria and senders in the US. It compares ways to get goods from the US to Nigeria (a relative's bag, Amazon, forwarders, traveller apps, couriers, buying locally), with each price sourced and dated, and re-checks live pages before quoting. It gives general information, not legal or customs advice.

Install it from inside Claude Code:

```
/plugin marketplace add Erriccc/jappa-labs
/plugin install send-to-nigeria@jappa-labs
```

Ask in plain words ("cheapest way to get an air fryer from Atlanta to Lagos?"), or run `/send-to-nigeria:ship-quote` for a step-by-step quote. The reviewed baseline covers Nigeria, with city guides for Chicago, DC/Baltimore, Houston/Texas and Atlanta; other cities and countries are researched live and labelled "not yet reviewed".

The source files are in [plugins/send-to-nigeria](plugins/send-to-nigeria). To share findings or ask for a provider listing, [open an issue](https://github.com/Erriccc/jappa-labs/issues).

## Research

See [docs/research-notes.md](docs/research-notes.md).

## Licence

MIT. See [LICENSE](LICENSE).
