// Renders a post to PNG at 1x and 2x. Requires Playwright.
//   node render.js           -> pink-october.png, pink-october@2x.png
//   node render.js minimal   -> pink-october-minimal.png, pink-october-minimal@2x.png
const { chromium } = require('playwright');
const path = require('path');
const name = process.argv[2] ? `pink-october-${process.argv[2]}` : 'pink-october';
(async () => {
  const browser = await chromium.launch();
  for (const [scale, suffix] of [[1, ''], [2, '@2x']]) {
    const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: scale });
    await page.goto('file://' + path.resolve(__dirname, `${name}.html`));
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: path.resolve(__dirname, `${name}${suffix}.png`) });
    await page.close();
  }
  await browser.close();
})();
