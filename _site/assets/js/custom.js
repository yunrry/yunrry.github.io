(function() {
  'use strict';
  
  // ============================================
  // 1. 카테고리 토글 기능
  // ============================================
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
  
  // ============================================
  // 2. 다크모드 토글 기능 (헤더에 배치)
  // ============================================
  function initDarkMode() {
    // 헤더 찾기
    const masthead = document.querySelector('.masthead__inner-wrap');
    if (!masthead) {
      console.log('헤더를 찾을 수 없습니다. 재시도 중...');
      setTimeout(initDarkMode, 100);
      return;
    }

    // 이미 버튼이 있으면 생성하지 않음
    if (document.getElementById('dark-mode-toggle')) return;

    // 다크모드 토글 버튼 생성
    const toggleButton = document.createElement('button');
    toggleButton.id = 'dark-mode-toggle';
    toggleButton.innerHTML = '🌙';
    toggleButton.setAttribute('aria-label', '다크모드 전환');
    toggleButton.className = 'dark-mode-toggle-header';
    
    // 헤더에 버튼 추가
    masthead.appendChild(toggleButton);

    // 저장된 테마 불러오기
    const currentTheme = localStorage.getItem('theme') || 'light';
    if (currentTheme === 'dark') {
      document.documentElement.setAttribute('data-theme', 'dark');
      toggleButton.innerHTML = '☀️';
    }

    // 토글 버튼 클릭 이벤트
    toggleButton.addEventListener('click', function() {
      const theme = document.documentElement.getAttribute('data-theme');
      
      if (theme === 'dark') {
        document.documentElement.setAttribute('data-theme', 'light');
        localStorage.setItem('theme', 'light');
        toggleButton.innerHTML = '🌙';
      } else {
        document.documentElement.setAttribute('data-theme', 'dark');
        localStorage.setItem('theme', 'dark');
        toggleButton.innerHTML = '☀️';
      }
    });
  }
  
  // ============================================
  // 3. 초기화
  // ============================================
  function init() {
    initCategoryToggle();
    initDarkMode();
  }
  
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();