const path = require('path');

const BASE_URL = process.env.BASE_URL || 'https://vikas-blip.github.io/pdd-testing/';

module.exports = {
    baseUrl: BASE_URL,
    timeout: 15000,
    headless: true,
    browser: 'chrome',
    outputDir: path.resolve(__dirname, '../../Test Results'),
    retryCount: 2,
    categories: [
        'Authentication', 'Authorization', 'Navigation', 'UI Validation',
        'Forms', 'CRUD Operations', 'Input Validation', 'Error Handling',
        'Session Management', 'File Upload', 'Accessibility', 'Responsive Design',
        'Performance Smoke Tests', 'Regression'
    ]
};
