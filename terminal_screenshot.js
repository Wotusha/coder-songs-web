const { chromium } = require('playwright');

(async () => {
    const browser = await chromium.launch({ headless: true });
    const page = await browser.newPage();
    await page.setViewportSize({ width: 1280, height: 800 });
    
    await page.goto('http://localhost:3000', { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(3000);
    
    await page.screenshot({ path: '/workspace/terminal_output.png', fullPage: true });
    console.log('Screenshot captured');
    await browser.close();
})();
