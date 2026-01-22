const { chromium } = require('playwright');

(async () => {
    const browser = await chromium.launch({ headless: true });
    const page = await browser.newPage();
    
    await page.setViewportSize({ width: 1280, height: 800 });
    
    await page.goto('http://localhost:3000', { waitUntil: 'networkidle' });
    
    // Wait for the page to fully load
    await page.waitForTimeout(2000);
    
    // Refresh to show the newly downloaded file
    await page.reload({ waitUntil: 'networkidle' });
    await page.waitForTimeout(2000);
    
    // Take screenshot showing the workspace with the neural model
    await page.screenshot({ path: '/workspace/neural_model_verification.png', fullPage: true });
    
    console.log('Verification screenshot saved to /workspace/neural_model_verification.png');
    
    await browser.close();
})();
