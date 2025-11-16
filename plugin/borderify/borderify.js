// plugin/borderify/borderify.js
console.log("%c🛑 STOP THE SLOP: ACTIVE DEFENSE", "color: #ff0066; font-weight: bold; font-size: 14px;");

const SLOP_SITES = {
  reddit: { regex: /reddit\.com/i, color: "#ff4500", label: "REDDIT SLOP" },
  chatgpt: { regex: /chat\.openai\.com|chatgpt\.com/i, color: "#10a37f", label: "CHATGPT ZONE" }
};

function defend() {
  const url = window.location.href;
  const host = window.location.hostname;

  // LOG URL (task requirement)
  console.log(`%cURL: ${url}`, "color: cyan; font-weight: bold;");

  let site = Object.values(SLOP_SITES).find(s => s.regex.test(host));

  if (site) {
    // CHANGE BORDER (task requirement)
    document.body.style.cssText = `
      border: 6px solid ${site.color} !important;
      box-shadow: 0 0 20px ${site.color}80 !important;
      transition: all 0.4s ease !important;
    `;
    console.log(`%c${site.label} DETECTED`, `color: ${site.color}; background: black; padding: 5px; font-weight: bold;`);
  } else {
    document.body.style.border = "";
    document.body.style.boxShadow = "";
  }
}

// Run on load
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", defend);
} else {
  defend();
}

// SPA support (Reddit & ChatGPT are SPAs)
let lastUrl = location.href;
new MutationObserver(() => {
  if (location.href !== lastUrl) {
    lastUrl = location.href;
    defend();
  }
}).observe(document, { subtree: true, childList: true });