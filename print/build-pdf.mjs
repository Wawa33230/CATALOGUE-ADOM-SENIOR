import pkg from '/opt/node22/lib/node_modules/playwright/index.js';
import { execFileSync } from 'node:child_process';
const { chromium } = pkg;

// Deux sorties :
//  - dist/catalogue-adomsenior.pdf            A4 exact (210 × 297 mm) : écran, e-mail, impression bureautique
//  - dist/catalogue-adomsenior-imprimeur.pdf  216 × 303 mm = A4 + 3 mm de fonds perdus sur chaque bord,
//                                              avec TrimBox/BleedBox renseignées pour l'imprimeur
const BLEED_MM = 3;

const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });

async function render(out, bleed) {
  const p = await b.newPage();
  await p.goto('file://' + process.cwd() + '/catalogue-print.html', { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  if (bleed) {
    await p.addStyleTag({ content: `
      @page { size: ${210 + 2 * BLEED_MM}mm ${297 + 2 * BLEED_MM}mm; margin: 0; }
      .page { width: ${210 + 2 * BLEED_MM}mm; height: ${297 + 2 * BLEED_MM}mm; }
      .trim { position: absolute; left: ${BLEED_MM}mm; top: ${BLEED_MM}mm; width: 210mm; height: 297mm; }
      /* la photo du sommaire touche les bords haut, droit et bas : elle déborde dans le fond perdu */
      .toc-photo { margin: -${BLEED_MM}mm -${BLEED_MM}mm -${BLEED_MM}mm 0; }
    ` });
    // Les fonds pleine page (photos + voiles de couleur) couvrent tout le format avec fonds perdus ;
    // tout le reste est replacé dans la zone de coupe A4.
    await p.evaluate(() => {
      const FULL = '.cover-photo, .cover-scrim, .divider-photo, .divider-scrim, .closing-photo, .closing-scrim';
      document.querySelectorAll('.page').forEach((page) => {
        const trim = document.createElement('div');
        trim.className = 'trim';
        [...page.children].forEach((c) => { if (!c.matches(FULL)) trim.appendChild(c); });
        page.appendChild(trim);
      });
    });
  }
  await p.pdf({ path: out, printBackground: true, preferCSSPageSize: true });
  await p.close();
  console.log('PDF : ' + out);
}

await render('../dist/catalogue-adomsenior.pdf', false);
await render('../dist/catalogue-adomsenior-imprimeur.pdf', true);
await b.close();

execFileSync('python3', ['-I', 'set-print-boxes.py', '../dist/catalogue-adomsenior-imprimeur.pdf', String(BLEED_MM)], { stdio: 'inherit' });
