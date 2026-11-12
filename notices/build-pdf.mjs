import pkg from '/opt/node22/lib/node_modules/playwright/index.js';
const { chromium } = pkg;

// Usage : cd notices && node build-pdf.mjs
// Produit dans ../dist :
//  - *-adomsenior.pdf           A4 (210 x 297 mm) : envoi par e-mail, impression au bureau
//  - *-adomsenior-IMPRIMEUR.pdf avec 3 mm de fonds perdus : à envoyer à l'imprimeur
// Le dossier VISAP (dépliant 3 volets) n'existe qu'en version imprimeur : son fichier
// intègre déjà les fonds perdus (633 x 303 mm, soit 627 x 297 mm une fois coupé).

// Ajoute 3 mm de fonds perdus à une page A4 (216 x 303 mm)
const A4_BLEED = `
  @page { size: 216mm 303mm; margin: 0; }
  .page { width: 216mm; height: 303mm; padding-top: 3mm; padding-left: 16mm; padding-right: 16mm; }
  .topbar { height: 7mm; }
  .topbar::after { width: 49mm; }
  .folio { left: 16mm; right: 16mm; bottom: 10mm; }
`;
const FICHE_BLEED = A4_BLEED + `.page { padding-bottom: 19.5mm; }`;

const jobs = [
  ['fiche-entretien-douche.html', 'fiche-entretien-douche-adomsenior.pdf', null],
  ['fiche-entretien-douche.html', 'fiche-entretien-douche-adomsenior-IMPRIMEUR.pdf', FICHE_BLEED],
  ['pv-reception.html', 'pv-reception-adomsenior.pdf', null],
  ['pv-reception.html', 'pv-reception-adomsenior-IMPRIMEUR.pdf', A4_BLEED],
  ['visap.html', 'visap-depliant-adomsenior-IMPRIMEUR.pdf', null],
];

const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
for (const [src, out, css] of jobs) {
  const p = await b.newPage();
  await p.goto('file://' + process.cwd() + '/' + src, { waitUntil: 'networkidle' });
  if (css) await p.addStyleTag({ content: css });
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({ path: '../dist/' + out, printBackground: true, preferCSSPageSize: true });
  console.log('PDF: ../dist/' + out);
  await p.close();
}
await b.close();
