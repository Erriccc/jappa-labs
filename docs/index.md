---
title: Jappa Labs
---

Jappa Labs builds open-source tools and shares research for West Africans at home and abroad.

The digest follows open-source projects that serve Nigerians and West Africans. See [About](about.md) for how it works.

We also publish [send-to-nigeria](send-to-nigeria.md), a free plugin that compares ways to get goods from the US to Nigeria.

## Digest editions

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
