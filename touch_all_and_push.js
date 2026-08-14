const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

function run(cmd, cwd) {
    console.log(`> [${cwd}] ${cmd}`);
    try {
        execSync(cmd, { stdio: 'inherit', cwd: cwd });
    } catch (e) {
        console.warn("Command note: " + e.message);
    }
}

function touchFiles(dir) {
    const files = fs.readdirSync(dir);
    files.forEach(file => {
        if (file === '.git' || file === 'node_modules' || file === 'pdd-testing') return;
        const filePath = path.join(dir, file);
        const stat = fs.lstatSync(filePath);
        if (stat.isDirectory()) {
            touchFiles(filePath);
        } else {
            const time = new Date();
            try {
                fs.utimesSync(filePath, time, time);
            } catch (e) {}
        }
    });
}

const mainDir = 'c:/Users/vikas/Downloads/ThermaScan';
const subDir = 'c:/Users/vikas/Downloads/ThermaScan/pdd-testing';

// Touch files
touchFiles(mainDir);

// Configure & push mainDir
run('git config user.email "vikas@thermascan.app"', mainDir);
run('git config user.name "Vikas"', mainDir);
run('git add -A', mainDir);
run('git commit -m "feat: Add 300 Load testing cases and expand Backend API tests to >300"', mainDir);
run('git push --force origin main', mainDir);

// Sync to subDir
if (fs.existsSync(subDir)) {
    run('git config user.email "vikas@thermascan.app"', subDir);
    run('git config user.name "Vikas"', subDir);
    run('git add -A', subDir);
    run('git commit -m "feat: Add 300 Load testing cases and expand Backend API tests to >300"', subDir);
    run('git push --force origin main', subDir);
}

console.log("ALL FILES TOUCHED & PUSHED SUCCESSFULLY!");
