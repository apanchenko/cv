const puppeteer = require('puppeteer');
(async () => {  
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    await page.goto(`file://${__dirname}/cv.html`, {
        waitUntil: 'networkidle2'
    });
    await page.pdf({ path: 'Anton_Panchenko.pdf', format: 'a4' });
    await browser.close();
})();