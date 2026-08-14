# ThermaScan Netlify Deployment Utility
# This script packages the static app files and deploys them to Netlify via the Netlify REST API.

$ErrorActionPreference = "Stop"

# Clear host and show a premium CLI header
Clear-Host
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host "          ThermaScan Netlify Deployer             " -ForegroundColor Green -BackgroundColor DarkBlue
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host ""

# 1. Ask for Netlify Personal Access Token
Write-Host "To deploy this app, you need a Netlify Personal Access Token (PAT)." -ForegroundColor White
Write-Host "If you don't have one:" -ForegroundColor DarkGray
Write-Host "  1. Go to: https://app.netlify.com/user/applications" -ForegroundColor Yellow
Write-Host "  2. Click 'New access token'" -ForegroundColor Yellow
Write-Host "  3. Copy and paste the token below." -ForegroundColor Yellow
Write-Host ""

$token = Read-Host "Enter your Netlify Personal Access Token"
$token = $token.Trim()

if ([string]::IsNullOrEmpty($token)) {
    Write-Error "A Personal Access Token is required to deploy. Please run the script again."
    Exit
}

# Define authorization header
$headers = @{
    "Authorization" = "Bearer $token"
}

# 2. Authenticate and verify token
Write-Host "`nVerifying your token..." -ForegroundColor Yellow
try {
    $user = Invoke-RestMethod -Uri "https://api.netlify.com/api/v1/user" -Method Get -Headers $headers
    Write-Host "Successfully authenticated as: $($user.email)" -ForegroundColor Green
} catch {
    Write-Host "Authentication failed! Check your token and try again." -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Red
    Exit
}

# 3. Choose site configuration
Write-Host "`nChoose an option:" -ForegroundColor White
Write-Host "  [1] Create a new site (Recommended)" -ForegroundColor Cyan
Write-Host "  [2] Deploy to an existing site" -ForegroundColor Cyan
$choice = Read-Host "Select [1 or 2]"

$siteId = ""
$siteName = ""
$siteUrl = ""

if ($choice -eq "2") {
    # Fetch existing sites
    Write-Host "`nFetching your Netlify sites..." -ForegroundColor Yellow
    try {
        $sites = Invoke-RestMethod -Uri "https://api.netlify.com/api/v1/sites" -Method Get -Headers $headers
        if ($sites.Count -eq 0) {
            Write-Host "No existing sites found in your Netlify account. Creating a new one instead." -ForegroundColor Yellow
            $choice = "1"
        } else {
            Write-Host "`nAvailable sites:" -ForegroundColor White
            for ($i = 0; $i -lt $sites.Count; $i++) {
                Write-Host "  [$($i + 1)] $($sites[$i].name) ($($sites[$i].ssl_url))" -ForegroundColor Cyan
            }
            $siteIndex = Read-Host "Select site index [1-$($sites.Count)]"
            $siteIndex = [int]$siteIndex - 1
            if ($siteIndex -ge 0 -and $siteIndex -lt $sites.Count) {
                $siteId = $sites[$siteIndex].id
                $siteName = $sites[$siteIndex].name
                $siteUrl = $sites[$siteIndex].ssl_url
            } else {
                Write-Error "Invalid selection. Exiting."
                Exit
            }
        }
    } catch {
        Write-Host "Failed to fetch sites!" -ForegroundColor Red
        Write-Host $_.Exception.Message -ForegroundColor Red
        Exit
    }
}

if ($choice -ne "2") {
    # Create a new site
    Write-Host "`nCreating a new Netlify site..." -ForegroundColor Yellow
    
    # Netlify auto-generates site names if name is not supplied
    $body = @{
        name = "thermascan-" + (Get-Random -Minimum 10000 -Maximum 99999).ToString()
    } | ConvertTo-Json
    
    try {
        $newSite = Invoke-RestMethod -Uri "https://api.netlify.com/api/v1/sites" -Method Post -Headers $headers -ContentType "application/json" -Body $body
        $siteId = $newSite.id
        $siteName = $newSite.name
        $siteUrl = $newSite.ssl_url
        Write-Host "Created site: $siteName" -ForegroundColor Green
    } catch {
        # Fallback to auto-created name by leaving body empty
        try {
            $newSite = Invoke-RestMethod -Uri "https://api.netlify.com/api/v1/sites" -Method Post -Headers $headers
            $siteId = $newSite.id
            $siteName = $newSite.name
            $siteUrl = $newSite.ssl_url
            Write-Host "Created site: $siteName" -ForegroundColor Green
        } catch {
            Write-Host "Failed to create a new site!" -ForegroundColor Red
            Write-Host $_.Exception.Message -ForegroundColor Red
            Exit
        }
    }
}

# 4. Zip site contents
Write-Host "`nPackaging app files..." -ForegroundColor Yellow
$zipPath = Join-Path $PSScriptRoot "thermascan-deploy.zip"

# Clean up old zip if it exists
if (Test-Path $zipPath) {
    Remove-Item $zipPath -Force
}

# List files to package
$filesToPackage = @(
    (Join-Path $PSScriptRoot "index.html"),
    (Join-Path $PSScriptRoot "style.css"),
    (Join-Path $PSScriptRoot "app.js"),
    (Join-Path $PSScriptRoot "manifest.json"),
    (Join-Path $PSScriptRoot "serviceWorker.js")
)

# Verify all files exist
foreach ($file in $filesToPackage) {
    if (-not (Test-Path $file)) {
        Write-Error "Required file missing: $file"
        Exit
    }
}

try {
    # Zip files at the root level of the archive
    Compress-Archive -Path $filesToPackage -DestinationPath $zipPath -Force
    Write-Host "Packaged successfully into thermascan-deploy.zip" -ForegroundColor Green
} catch {
    Write-Host "Failed to zip files!" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Red
    Exit
}

# 5. Upload/Deploy zip file to Netlify
Write-Host "`nUploading to Netlify... (This may take a few seconds)" -ForegroundColor Yellow
$deployHeaders = @{
    "Authorization" = "Bearer $token"
    "Content-Type"  = "application/zip"
}

try {
    $deployResponse = Invoke-RestMethod -Uri "https://api.netlify.com/api/v1/sites/$siteId/deploys" -Method Post -Headers $deployHeaders -InFile $zipPath
    Write-Host "`n==================================================" -ForegroundColor Green
    Write-Host "          DEPLOYMENT SUCCESSFUL!                  " -ForegroundColor Green -BackgroundColor Black
    Write-Host "==================================================" -ForegroundColor Green
    Write-Host "Site Name:  $siteName" -ForegroundColor White
    Write-Host "Site URL:   $siteUrl" -ForegroundColor Cyan
    Write-Host "Deploy ID:  $($deployResponse.id)" -ForegroundColor White
    Write-Host "State:      $($deployResponse.state)" -ForegroundColor White
    Write-Host "==================================================" -ForegroundColor Green
    Write-Host "`nYou can copy and paste the URL above to show your reviewer!" -ForegroundColor Yellow
} catch {
    Write-Host "`nDeployment failed!" -ForegroundColor Red
    Write-Host $_.Exception.Message -ForegroundColor Red
} finally {
    # Clean up zip file
    if (Test-Path $zipPath) {
        Remove-Item $zipPath -Force
    }
}

Write-Host "`nPress any key to exit..."
[void][System.Console]::ReadKey($true)
