const { chromium } = require('playwright');

(async () => {
    const browser = await chromium.launch({ headless: true });
    const page = await browser.newPage();
    
    await page.setViewportSize({ width: 1280, height: 800 });
    
    await page.goto('http://localhost:3000', { waitUntil: 'networkidle' });
    
    // Wait for the page to fully load
    await page.waitForTimeout(2000);
    
    // Take screenshot
    await page.screenshot({ path: '/workspace/cloudcmd_screenshot.png', fullPage: true });
    
    console.log('Screenshot saved to /workspace/cloudcmd_screenshot.png');
    
    await browser.close();
})();
