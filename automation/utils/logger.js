const fs = require('fs');
const path = require('path');

class Logger {
    constructor() {
        this.logDir = path.resolve(__dirname, '../../Test Results/Logs');
        if (!fs.existsSync(this.logDir)) {
            fs.mkdirSync(this.logDir, { recursive: true });
        }
        this.logFile = path.join(this.logDir, 'execution.log');
    }

    log(level, message) {
        const timestamp = new Date().toISOString();
        const formatted = `[${timestamp}] [${level.toUpperCase()}] ${message}\n`;
        console.log(formatted.trim());
        fs.appendFileSync(this.logFile, formatted);
    }

    info(msg) { this.log('info', msg); }
    warn(msg) { this.log('warn', msg); }
    error(msg) { this.log('error', msg); }
}

module.exports = new Logger();
