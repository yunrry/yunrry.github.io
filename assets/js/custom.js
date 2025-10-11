(function() {
    'use strict';
    
    if (window.categoryToggleInitialized) return;
    window.categoryToggleInitialized = true;
    
    function initCategoryToggle() {
      const sidebar = document.querySelector('.sidebar .nav__list .nav__items');
      if (!sidebar) return;
      
      const config = {
        '/categories/dev/': [
          '/categories/dev/frontend/',
          '/categories/dev/backend/',
          '/categories/dev/devops/'
        ],
        '/categories/language/': [
          '/categories/language/python/',
          '/categories/language/javascript/',
          '/categories/language/java/'
        ],
        '/categories/algorithm/': [
          '/categories/algorithm/basic/',
          '/categories/algorithm/sorting/',
          '/categories/algorithm/recursion/',
          '/categories/algorithm/graph/',
          '/categories/algorithm/dynamic/',
          '/categories/algorithm/greedy/',
          '/categories/algorithm/baekjoon/',
          '/categories/algorithm/programmers/',
          '/categories/algorithm/leetcode/'
        ],
        '/categories/cs/': [
          '/categories/cs/datastructure/',
          '/categories/cs/network/',
          '/categories/cs/os/',
          '/categories/cs/database/'
        ]
      };
      
      const allLinks = sidebar.querySelectorAll('a');
      const linkMap = new Map();
      
      // 한 번만 순회해서 맵 생성
      allLinks.forEach(link => {
        linkMap.set(link.getAttribute('href'), link);
      });
      
      Object.keys(config).forEach(parentUrl => {
        const parentLink = linkMap.get(parentUrl);
        if (!parentLink || parentLink.querySelector('.toggle-arrow')) return;
        
        // 화살표 추가
        const arrow = document.createElement('span');
        arrow.innerHTML = ' ▼';
        arrow.style.cssText = 'font-size:0.7em;margin-left:5px;display:inline-block;transition:transform 0.3s ease';
        arrow.className = 'toggle-arrow';
        parentLink.appendChild(arrow);
        
        // 하위 항목 찾기
        const childrenItems = config[parentUrl]
          .map(url => linkMap.get(url)?.closest('li'))
          .filter(Boolean);
        
        // 초기 상태: 닫힘
        childrenItems.forEach(child => child.style.display = 'none');
        
        // 클릭 이벤트
        let isOpen = false;
        parentLink.onclick = e => {
          e.preventDefault();
          isOpen = !isOpen;
          childrenItems.forEach(child => child.style.display = isOpen ? 'block' : 'none');
          arrow.style.transform = isOpen ? 'rotate(180deg)' : 'rotate(0deg)';
        };
      });
    }
    
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', initCategoryToggle);
    } else {
      initCategoryToggle();
    }
  })();