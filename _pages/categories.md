---
title: "전체 카테고리"
layout: single
permalink: /categories/
author_profile: true
sidebar:
  nav: "categories"
---

<!-- Normal Content -->
<div id="normal-content">
  <div class="category-tabs">
    {% assign categories = "dev,algorithm,cs,language" | split: "," %}
    {% for cat in categories %}
      <button class="category-tab {% if forloop.first %}active{% endif %}" 
              onclick="switchCategory('{{ cat }}', this)">
        {{ cat | capitalize }}
      </button>
    {% endfor %}
  </div>

  {% for cat in categories %}
    {% assign cat_files = site.data.contents | where: "category", cat | sort: "created" | reverse %}
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

<!-- Split Content -->
<div id="split-content" style="display:none;">
  <div class="split-container">
    <div class="split-left">
      <div class="split-header">
        <button id="close-split" class="close-button">← 돌아가기</button>
      </div>
      <div id="split-categories-container"></div>
    </div>
    <div class="split-right">
      <div class="content-display">좌측에서 포스트를 선택하세요.</div>
    </div>
  </div>
</div>

<!-- 스타일 -->
<style>
.category-tabs {
  display: flex;
  gap: 10px;
  margin-bottom: 30px;
  border-bottom: 2px solid #e0e0e0;
  flex-wrap: wrap;
}
.category-tab {
  padding: 10px 20px;
  cursor: pointer;
  border: none;
  background: none;
  font-size: 1.1em;
  color: #666;
  transition: all 0.3s;
}
.category-tab:hover {
  color: #9bd6bd;
}
.category-tab.active {
  color: #9bd6bd;
  border-bottom: 3px solid #9bd6bd;
  margin-bottom: -2px;
}
.category-section {
  display: none;
}
.category-section.active {
  display: block;
}
.split-container {
  display: flex;
  gap: 20px;
  width: 100%;
  min-height: 70vh;
}
.split-left {
  flex: 0 0 45%;
  padding-right: 20px;
  border-right: 2px solid #e0e0e0;
}
.split-right {
  flex: 1;
  padding-left: 20px;
  position: relative;
}
.split-header {
  margin-bottom: 20px;
  padding-bottom: 15px;
  border-bottom: 2px solid #e0e0e0;
}
.close-button {
  background: #9bd6bd;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 14px;
  font-weight: 500;
}
.close-button:hover {
  background: #88bca7;
}
.content-display {
  flex: 1;
  overflow-y: auto;
}
[data-theme="dark"] .category-tabs { border-bottom-color: #333; }
[data-theme="dark"] .category-tab { color: #b0b0b0; }
[data-theme="dark"] .split-left { border-right-color: #333; }
[data-theme="dark"] .split-header { border-bottom-color: #333; }
</style>

<!-- Marked.js, Prism.js -->
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/prism.min.js" data-manual></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-java.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-python.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.29.0/components/prism-javascript.min.js"></script>

<!-- 스크립트 -->
<script>
function switchCategory(category, button){
  // 모든 섹션 숨기기
  document.querySelectorAll('.category-section').forEach(s => s.classList.remove('active'));
  document.querySelector(`[data-category="${category}"]`).classList.add('active');

  // 탭 active 처리
  document.querySelectorAll('.category-tab').forEach(t => t.classList.remove('active'));
  if(button) button.classList.add('active');

  // 리스트 아이템 클릭 이벤트
  const section = document.querySelector(`[data-category="${category}"]`);
  section.querySelectorAll('a[data-content]').forEach(link => {
    link.onclick = function(e){
      e.preventDefault();
      openSplitView(section, this.getAttribute('data-content'));
    }
  });
}

function openSplitView(section, path){
  document.getElementById('normal-content').style.display='none';
  document.getElementById('split-content').style.display='flex';

  const splitContainer = document.getElementById('split-categories-container');
  splitContainer.innerHTML = section.outerHTML;

  // 각 링크에 이벤트 추가
  splitContainer.querySelectorAll('a[data-content]').forEach(link=>{
    link.onclick = function(e){
      e.preventDefault();
      loadContent(this.getAttribute('data-content'));
    }
  });

  // 클릭한 요소의 컨텐츠를 바로 로드
  loadContent(path);
}

function loadContent(path){
  const container = document.querySelector('.content-display');
  container.innerHTML = '<p>로딩 중...</p>';
  fetch(path)
    .then(r => r.ok ? r.text() : Promise.reject('파일 없음'))
    .then(md=>{
      md = md.replace(/^---[\s\S]*?---\n/, '');
      const rawStart = "{% raw %}", rawEnd = "{% endraw %}";
      md = md.replaceAll(rawStart,'').replaceAll(rawEnd,'');
      container.innerHTML = marked.parse(md);
      Prism.highlightAllUnder(container);
    })
    .catch(e=>container.innerHTML=`<p style="color:red;">❌ ${e}</p>`);
}

document.getElementById('close-split').onclick = function(){
  document.getElementById('split-content').style.display='none';
  document.getElementById('normal-content').style.display='block';
}

// 초기화: 첫 카테고리 이벤트 등록
switchCategory("dev", document.querySelector('.category-tab.active'));
</script>
