/* Mobile Navigation: weißes Vollbild-Blatt, 160 ms Blende, keine Abdunklung. */
(function () {
  var toggle = document.querySelector('.nav-toggle');
  var sheet = document.getElementById('mobile-nav');
  if (!toggle || !sheet) return;

  var closeBtn = sheet.querySelector('.nav-close');
  var lastFocus = null;

  function open() {
    lastFocus = document.activeElement;
    sheet.hidden = false;
    document.body.classList.add('nav-open');
    toggle.setAttribute('aria-expanded', 'true');
    if (closeBtn) closeBtn.focus();
  }

  function close() {
    sheet.hidden = true;
    document.body.classList.remove('nav-open');
    toggle.setAttribute('aria-expanded', 'false');
    if (lastFocus) lastFocus.focus();
  }

  toggle.addEventListener('click', open);
  if (closeBtn) closeBtn.addEventListener('click', close);

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && !sheet.hidden) close();
  });

  // Ein Wechsel auf Desktopbreite darf kein offenes Blatt zurücklassen.
  var mq = window.matchMedia('(min-width: 672px)');
  var onChange = function (e) { if (e.matches && !sheet.hidden) close(); };
  if (mq.addEventListener) mq.addEventListener('change', onChange);
  else if (mq.addListener) mq.addListener(onChange);
})();
