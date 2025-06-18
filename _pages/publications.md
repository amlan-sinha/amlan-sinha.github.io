---
layout: archive
title: "Selected Journal Publications"
permalink: /publications/
author_profile: true
---

{% include base_path %}

{% assign publications_by_year = site.publications | group_by_exp: "post", "post.date | date: '%Y'" %}
{% assign sorted_years = publications_by_year | sort: "name" | reverse %}

<div class="publication-timeline">
  {% for year_group in sorted_years %}
    <div class="year-block">
      <div class="timeline-column">
        <div class="timeline-year">{{ year_group.name }}</div>
        <div class="timeline-line-dynamic"></div>
      </div>
      <div class="timeline-entries">
        {% assign sorted_posts = year_group.items | sort: 'date' | reverse %}
        {% for post in sorted_posts %}
          <div class="timeline-entry">
            <div class="timeline-content">
              {% include archive-single.html %}
            </div>
          </div>
        {% endfor %}
      </div>
    </div>
  {% endfor %}
</div>

<hr style="border-top: 1px solid #ccc; margin: 2em 0;">

{% if site.author.googlescholar %}
  <div class="wordwrap">You can also find my articles on <a href="{{ site.author.googlescholar }}">my Google Scholar</a>.</div>
{% endif %}
