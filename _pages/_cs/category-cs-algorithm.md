---
title: "Algorithm"
layout: category-split
permalink: /categories/cs/algorithm/
taxonomy: cs/algorithm/
author_profile: true
sidebar:
  nav: "categories"
---

#### <a href="#" data-content="/assets/contents/cs/algorithm/time-complexity.md"><span style="color: #9bd6bd;">♡</span> 시간복잡도 Big O</a>

#### <a href="#" data-content="/assets/contents/cs/algorithm/algorithm-sorting.md"><span style="color: #9bd6bd;">♡</span> 정렬 Sorting</a>

#### <a href="#" data-content="/assets/contents/cs/algorithm/binary-search.md"><span style="color: #9bd6bd;">♡</span> 이진탐색 Binary Search</a>

#### <a href="#" data-content="/assets/contents/cs/algorithm/algorithm-exam.md"><span style="color: #9bd6bd;">♡</span> Algorithm 실기 기출 유형 </a>


## CheckList

- [ ] 각 알고리즘을 종이에 그려가며 이해하기  
- [ ] 직접 손으로 코드를 작성해보기  
- [ ] 시간복잡도를 항상 함께 생각하기  
- [ ] 기출문제를 반복해서 풀어보기  
- [ ] 정렬 전후 배열 상태를 비교하기  

---
<br><br>

<div id="normal-content">
  <div class="category-tabs">
    {% assign categories = "algorithm" | split: "," %}
    {% for cat in categories %}

    {% endfor %}
  </div>

  {% for cat in categories %}
    {% assign cat_files = site.data.contents | where: "category2", cat | sort: "created" | reverse %}
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
