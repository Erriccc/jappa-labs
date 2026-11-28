---
title: Jappa Labs
layout: landing
---

<div class="hero-label" markdown="1">

# Send it home, minus the guesswork.

The cheapest safe way to get your things from the US to Nigeria, city by city.
{: .hero-sub}

---

[Open the Send to Nigeria guide](send-to-nigeria.md){: .hero-cta}

<p class="stamp" aria-hidden="true">Sourced<br>and dated</p>

</div>

Every price in the guide has a source and a date, and the routes run from a relative's bag to forwarders, couriers and buying in Lagos. It is free, and general information, not legal, customs or tax advice.

## What are you sending?

Pick the closest size to see how it is billed and which routes make sense.

- [Envelope or phone](guide/size-classes.md#1-envelope-or-phone)
- [Laptop](guide/size-classes.md#2-laptop)
- [Backpack or small parcel](guide/size-classes.md#3-backpack-or-small-parcel)
- [Carry-on or bulky box](guide/size-classes.md#4-carry-on-size-or-bulky-box)
- [Small suitcase](guide/size-classes.md#5-small-suitcase)
- [Large suitcase](guide/size-classes.md#6-large-suitcase-50-lb)
- [Barrel](guide/size-classes.md#7-barrel)
- [Several boxes or a garage load](guide/size-classes.md#8-multiple-boxes-or-a-garage-load)
{: .tags}

## Where are you sending from?

Each city guide walks through every size, ending with the best route and why.

- [Chicago](guide/scenarios/chicago.md) <span>and northwest Indiana</span>
- [Washington DC](guide/scenarios/dc-baltimore.md) <span>Baltimore and Northern Virginia</span>
- [Houston](guide/scenarios/houston-texas.md) <span>and the rest of Texas</span>
- [Atlanta](guide/scenarios/atlanta.md) <span>and Georgia</span>
{: .labels}

Somewhere else? The [options ladder](guide/options-ladder.md) explains when each route wins, wherever you start.

## Before you send

- [Nigerian duty](guide/nigeria-duty.md): when you pay it, and how much.
- [Prohibited items](guide/prohibited-and-carry-warnings.md), and why not to carry parcels for strangers.
- [Paying from Nigeria](guide/paying-from-nigeria.md) for US orders.
- [Who ships to Nigeria](guide/providers.md), listed by type with no paid placement.

## Research

The guide rests on public research into routes, rules and the companies on this route. Read the [research notes](research/index.md).

## Builders digest

Jappa Labs also publishes a weekly digest of open-source projects that serve Nigerians and West Africans, crediting the people who build them. See [About](about.md) for how it works.

{% assign editions = site.pages | where_exp: "p", "p.path contains 'digest/'" | sort: "path" | reverse %}
{% if editions.size > 0 %}
<ul>
{% for edition in editions %}
  <li><a href="{{ edition.url | relative_url }}">{{ edition.title | default: edition.name }}</a></li>
{% endfor %}
</ul>
{% else %}
No editions yet.
{% endif %}
