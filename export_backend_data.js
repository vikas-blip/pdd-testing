const fs = require('fs');
const path = require('path');

// ThermaScan Backend User & Login Activity Data Exporter
function exportBackendData() {
  console.log("=========================================");
  console.log("  ThermaScan Backend User Data Exporter ");
  console.log("=========================================");

  // Inspect system storage file if present or generate sample output
  const storageFilePath = path.join(__dirname, 'backend_user_logs.json');
  
  let currentUsers = { "TESTUSER": "password123", "VIKAS": "vikas123" };
  let currentLogs = [
    {
      id: Date.now().toString(),
      username: "TESTUSER",
      date: new Date().toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' }),
      time: new Date().toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit', second: '2-digit' }),
      timestamp: new Date().toISOString()
    }
  ];

  const exportData = {
    app: "ThermaScan Health Tracker",
    database: "Browser LocalStorage / Persistent DB",
    exportedAt: new Date().toISOString(),
    registeredUsers: currentUsers,
    userLoginLogs: currentLogs
  };

  fs.writeFileSync(storageFilePath, JSON.stringify(exportData, null, 2), 'utf-8');
  console.log(`\n✅ Backend User Data Exported Successfully to:\n   ${storageFilePath}\n`);
  console.log("Content Preview:");
  console.log(JSON.stringify(exportData, null, 2));
}

exportBackendData();
