---
title: "AI"
layout: category-split
permalink: /categories/tools/ai/
taxonomy: tools/ai
author_profile: true
sidebar:
  nav: "categories"
---

<div id="normal-content">
  <div class="category-tabs">
    {% assign categories = "ai" | split: "," %}
    {% for cat in categories %}

    {% endfor %}
  </div>

  {% for cat in categories %}
    {% assign cat_files = site.data.contents | where: "category", "tools" | where: "category2", cat | sort: "created" | reverse %}
    <div class="category-section {% if forloop.first %}active{% endif %}" data-category="{{ cat }}">
      <ul class="posts-list" style="list-style:none; padding:0;">
        {% for doc in cat_files %}
          <li style="margin-bottom:20px; padding-bottom:10px; border-bottom:1px solid #dfe6e4;">
            <div style="display:flex; justify-content:space-between; align-items:baseline;">
              <span style="color:#999; font-size:0.85em;">
                {% if doc.created %}📅 {{ doc.created }}{% endif %}
                {% if doc.updated %} (updated: {{ doc.updated }}){% endif %}
              </span>
              <span style="color:#9bd6bd; font-size:0.75em; text-transform:uppercase;">{{ doc.category }}</span>
            </div>
            <h3 style="margin:1px 0;">
              <a href="#" data-content="{{ doc.path | relative_url }}">{{ doc.title }}</a>
            </h3>
            {% if doc.excerpt %}
              <p style="color:#666; font-size:0.9em;">{{ doc.excerpt | strip_html | truncatewords:30 }}</p>
            {% endif %}
          </li>
        {% endfor %}
      </ul>
    </div>
  {% endfor %}
</div>