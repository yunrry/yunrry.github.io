function showCategory(category, event) {
    document.querySelectorAll('.category-section').forEach(el => el.classList.remove('active'));
    document.querySelectorAll('.category-tab').forEach(el => el.classList.remove('active'));
    document.querySelector(`[data-category="${category}"]`).classList.add('active');
    event.currentTarget.classList.add('active');
  }
  
  function showDoc(path) {
    fetch(path)
      .then(res => res.text())
      .then(text => {
        document.getElementById('doc-content').innerHTML = marked.parse(text);
      });
  }
  