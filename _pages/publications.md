---
layout: archive
title: "Journal Publications"
permalink: /publications/
author_profile: true
---

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}

<hr style="border-top: 1px solid #ccc; margin: 2em 0;">

{% if site.author.googlescholar %}
  <div class="wordwrap">You can also find my articles on <a href="{{site.author.googlescholar}}">my Google Scholar</a>.</div>
{% endif %}