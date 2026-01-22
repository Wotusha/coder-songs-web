const { chromium } = require('playwright');

(async () => {
    const browser = await chromium.launch({ headless: true });
    const page = await browser.newPage();
    
    await page.setViewportSize({ width: 1280, height: 800 });
    
    // Navigate to cloudcmd to show the API file
    await page.goto('http://localhost:3000', { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(2000);
    
    // Take screenshot showing the running API
    await page.screenshot({ path: '/workspace/api_server_verification.png', fullPage: true });
    
    console.log('API Server verification screenshot saved');
    
    await browser.close();
})();
