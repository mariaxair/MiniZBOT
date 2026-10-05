// Renders pink-october.html to PNG at 1x and 2x. Requires Playwright.
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const browser = await chromium.launch();
  for (const [scale, out] of [[1, 'pink-october.png'], [2, 'pink-october@2x.png']]) {
    const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: scale });
    await page.goto('file://' + path.resolve(__dirname, 'pink-october.html'));
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: path.resolve(__dirname, out) });
    await page.close();
  }
  await browser.close();
})();
