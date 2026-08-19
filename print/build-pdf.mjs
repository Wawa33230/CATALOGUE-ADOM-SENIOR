import pkg from '/opt/node22/lib/node_modules/playwright/index.js';
const { chromium } = pkg;

const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
const p = await b.newPage();
await p.goto('file://' + process.cwd() + '/catalogue-print.html', { waitUntil: 'networkidle' });
await p.pdf({
  path: '../dist/catalogue-adomsenior.pdf',
  format: 'A4',
  printBackground: true,
  preferCSSPageSize: true,
});
console.log('PDF: ../dist/catalogue-adomsenior.pdf');
await b.close();
