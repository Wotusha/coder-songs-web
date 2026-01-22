const { chromium } = require('playwright');

(async () => {
    const browser = await chromium.launch({ headless: true });
    const page = await browser.newPage();
    
    await page.setViewportSize({ width: 1280, height: 800 });
    
    await page.goto('http://localhost:3000', { waitUntil: 'networkidle' });
    
    // Wait for the page to fully load
    await page.waitForTimeout(2000);
    
    // Navigate to the workspace folder
    await page.click('a[href="/fs/workspace/"]');
    await page.waitForTimeout(2000);
    
    // Take screenshot showing the script files
    await page.screenshot({ path: '/workspace/script_creation.png', fullPage: true });
    
    console.log('Script creation screenshot saved to /workspace/script_creation.png');
    
    await browser.close();
})();
