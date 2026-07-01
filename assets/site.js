/* Aventario shared site behaviors. Loaded on every page (CSP: script-src 'self').
   - UTM / referrer capture (attribution on every lead)
   - Real newsletter subscribe -> Supabase, with honeypot spam guard
   - GA funnel events: form_start, scroll_depth (only fire once consent granted)
   No dependencies. Everything is guarded so a missing element never throws. */
(function () {
  'use strict';

  var SB_URL = 'https://zpuywttjadohtxvaloyq.supabase.co';
  var SB_KEY = 'sb_publishable_0R1ZCaygbhIA4xY3MhpN6w_qOFeRhoa';

  // ---- Attribution: capture UTMs + referrer once per session -------------
  function captureAttr() {
    try {
      var stored = JSON.parse(sessionStorage.getItem('av_attr') || 'null');
      if (stored) return stored;
      var q = new URLSearchParams(location.search);
      var attr = {};
      ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content', 'gclid'].forEach(function (k) {
        var v = q.get(k);
        if (v) attr[k] = v.slice(0, 200);
      });
      if (document.referrer && document.referrer.indexOf(location.origin) !== 0) {
        attr.referrer = document.referrer.slice(0, 300);
      }
      attr.landing_page = location.pathname;
      sessionStorage.setItem('av_attr', JSON.stringify(attr));
      return attr;
    } catch (e) { return {}; }
  }
  var ATTR = captureAttr();
  // Exposed so the contact / webinar / whitepaper form handlers can merge it in.
  window.avAttr = function () { try { return JSON.parse(sessionStorage.getItem('av_attr') || '{}'); } catch (e) { return {}; } };

  // ---- Real newsletter subscribe ----------------------------------------
  function bindNewsletter(form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var btn = form.querySelector('button');
      var emailEl = form.querySelector('input[type=email]');
      var hp = form.querySelector('input[name=company_website]'); // honeypot
      if (hp && hp.value) { if (btn) btn.textContent = 'Subscribed'; return; } // bot: swallow silently
      var email = emailEl ? emailEl.value.trim() : '';
      if (!email) return;
      if (btn) { btn.disabled = true; btn.textContent = 'Subscribing...'; }
      var data = Object.assign({ email: email, source: location.pathname, consent: true }, ATTR);
      fetch(SB_URL + '/rest/v1/subscribers', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', apikey: SB_KEY, Prefer: 'return=minimal,resolution=merge-duplicates' },
        body: JSON.stringify(data)
      }).then(function (r) {
        if (btn) { btn.disabled = false; btn.textContent = r.ok ? 'Subscribed' : 'Try again'; }
      }).catch(function () {
        if (btn) { btn.disabled = false; btn.textContent = 'Try again'; }
      });
    });
  }
  function initNewsletters() {
    var forms = document.querySelectorAll('form[data-newsletter]');
    for (var i = 0; i < forms.length; i++) bindNewsletter(forms[i]);
  }

  // ---- GA funnel events (no-op until consent loads gtag) -----------------
  function ga() { if (typeof window.gtag === 'function') window.gtag.apply(null, arguments); }
  function initFunnelEvents() {
    var started = false;
    document.addEventListener('focusin', function (e) {
      if (started) return;
      var t = e.target;
      if (t && (t.tagName === 'INPUT' || t.tagName === 'TEXTAREA' || t.tagName === 'SELECT') && t.closest('form')) {
        started = true;
        ga('event', 'form_start', { form_location: location.pathname });
      }
    }, { passive: true });

    var marks = [25, 50, 75, 100], hit = {};
    window.addEventListener('scroll', function () {
      var h = document.documentElement;
      var max = h.scrollHeight - h.clientHeight;
      if (max <= 0) return;
      var pct = Math.round((h.scrollTop / max) * 100);
      for (var i = 0; i < marks.length; i++) {
        if (pct >= marks[i] && !hit[marks[i]]) {
          hit[marks[i]] = true;
          ga('event', 'scroll_depth', { percent: marks[i], page_path: location.pathname });
        }
      }
    }, { passive: true });
  }

  function init() { initNewsletters(); initFunnelEvents(); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
