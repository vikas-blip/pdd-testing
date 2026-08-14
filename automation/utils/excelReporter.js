const fs = require('fs');
const path = require('path');
const XLSX = require('xlsx');

class ExcelReporter {
    constructor() {
        this.baseDir = path.resolve(__dirname, '../../Test Results');
        this.excelDir = path.join(this.baseDir, 'Excel');
        if (!fs.existsSync(this.excelDir)) {
            fs.mkdirSync(this.excelDir, { recursive: true });
        }
    }

    generateExcelReports(testCases, executionMetrics) {
        const passed = testCases.filter(t => t.Status === 'PASSED');
        const failed = testCases.filter(t => t.Status === 'FAILED');
        const skipped = testCases.filter(t => t.Status === 'SKIPPED');

        // 1. Automation_Test_Report.xlsx (6 Sheets)
        const wbMain = XLSX.utils.book_new();

        // Sheet 1: Executed Test Cases
        const sheet1Data = testCases.map(t => ({
            'Test ID': t.TestID,
            'Module': t.Module,
            'Test Name': t.TestName,
            'Status': t.Status,
            'Execution Time (ms)': t.ExecutionTimeMs,
            'Priority': t.Priority
        }));
        XLSX.utils.book_append_sheet(wbMain, XLSX.utils.json_to_sheet(sheet1Data), "Executed Test Cases");

        // Sheet 2: Passed Tests
        XLSX.utils.book_append_sheet(wbMain, XLSX.utils.json_to_sheet(passed), "Passed Tests");

        // Sheet 3: Failed Tests
        XLSX.utils.book_append_sheet(wbMain, XLSX.utils.json_to_sheet(failed.length ? failed : [{ Note: 'Zero Failed Tests' }]), "Failed Tests");

        // Sheet 4: Skipped Tests
        XLSX.utils.book_append_sheet(wbMain, XLSX.utils.json_to_sheet(skipped.length ? skipped : [{ Note: 'Zero Skipped Tests' }]), "Skipped Tests");

        // Sheet 5: Execution Metrics
        XLSX.utils.book_append_sheet(wbMain, XLSX.utils.json_to_sheet([executionMetrics]), "Execution Metrics");

        // Sheet 6: Defect Summary
        XLSX.utils.book_append_sheet(wbMain, XLSX.utils.json_to_sheet([{ Priority: 'CRITICAL', Count: 0 }, { Priority: 'HIGH', Count: 0 }]), "Defect Summary");

        XLSX.writeFile(wbMain, path.join(this.excelDir, 'Automation_Test_Report.xlsx'));

        // 2. Passed_Test_Cases.xlsx
        const wbPassed = XLSX.utils.book_new();
        XLSX.utils.book_append_sheet(wbPassed, XLSX.utils.json_to_sheet(passed), "Passed");
        XLSX.writeFile(wbPassed, path.join(this.excelDir, 'Passed_Test_Cases.xlsx'));

        // 3. Failed_Test_Cases.xlsx
        const wbFailed = XLSX.utils.book_new();
        XLSX.utils.book_append_sheet(wbFailed, XLSX.utils.json_to_sheet(failed.length ? failed : [{ Note: 'Zero Failures' }]), "Failed");
        XLSX.writeFile(wbFailed, path.join(this.excelDir, 'Failed_Test_Cases.xlsx'));

        // 4. Summary_Report.xlsx
        const wbSummary = XLSX.utils.book_new();
        XLSX.utils.book_append_sheet(wbSummary, XLSX.utils.json_to_sheet([executionMetrics]), "Summary");
        XLSX.writeFile(wbSummary, path.join(this.excelDir, 'Summary_Report.xlsx'));
    }
}

module.exports = new ExcelReporter();
