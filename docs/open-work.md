---
title: Open work
---

What we are working on, and where help is welcome. Each item is an open issue on GitHub, refreshed every time the site is built.

{% assign issues = site.data.issues %}
{% if issues and issues.size > 0 %}
<ul class="open-work">
{% for issue in issues %}
  <li>
    <h3>{{ issue.title | escape }}</h3>
    <p class="open-work-meta">
      Opened {{ issue.created_at | date: "%-d %B %Y" | escape }}
      {%- for label in issue.labels %} &middot; <span class="open-work-label">{{ label | escape }}</span>{% endfor %}
    </p>
    <p>{{ issue.body | default: "" | strip_html | truncate: 200 | escape }}</p>
    <p class="open-work-link"><a href="{{ issue.url | escape }}">Discuss on GitHub</a></p>
  </li>
{% endfor %}
</ul>
{% else %}
No open work right now.
{% endif %}
