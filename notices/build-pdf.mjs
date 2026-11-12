import pkg from '/opt/node22/lib/node_modules/playwright/index.js';
const { chromium } = pkg;

// Usage : cd notices && node build-pdf.mjs
// Produit deux PDF dans ../dist :
//  - fiche-entretien-douche-adomsenior.pdf          A4 (210 x 297 mm) : envoi par e-mail, impression bureau
//  - fiche-entretien-douche-adomsenior-IMPRIMEUR.pdf A4 + 3 mm de fonds perdus (216 x 303 mm) : à envoyer à l'imprimeur
const BLEED_CSS = `
  @page { size: 216mm 303mm; margin: 0; }
  .page { width: 216mm; height: 303mm; padding: 3mm 16mm 19.5mm; }
  .topbar { height: 7mm; }
  .topbar::after { width: 49mm; height: 7mm; }
  .folio { left: 16mm; right: 16mm; bottom: 10mm; }
`;

const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
for (const [out, css] of [
  ['../dist/fiche-entretien-douche-adomsenior.pdf', null],
  ['../dist/fiche-entretien-douche-adomsenior-IMPRIMEUR.pdf', BLEED_CSS],
]) {
  const p = await b.newPage();
  await p.goto('file://' + process.cwd() + '/fiche-entretien-douche.html', { waitUntil: 'networkidle' });
  if (css) await p.addStyleTag({ content: css });
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({ path: out, printBackground: true, preferCSSPageSize: true });
  console.log('PDF:', out);
  await p.close();
}
await b.close();
