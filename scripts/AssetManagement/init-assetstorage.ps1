<#
.Synopsis
    init-assetstorage - Create folders and database structures for storing and managing field work assets 

.DESCRIPTION
    Forest assessment trips commonly yield valuable assets in addition to protocol based datasets. For example, images, video, GPS track logs, etc. 
    Storing these assets in a consistent way preserves the value of the assets. This script creates a folder structure for asset storage.
    
     

.EXAMPLE
   ./init-assetstorage -projectRoot c:/adkhistorygis -tripidentifier curtis-pond_7-3-2016


   
#>

[CmdletBinding()]
    param (
        [parameter(mandatory=$true, HelpMessage="Enter the project root path .")]
        [ValidateScript({ Test-Path $_ -PathType Container })]
        [string] $projectRoot,
        [parameter(mandatory=$true, HelpMessage="Enter the project template root path .")]
        [ValidateScript({ Test-Path $_ -PathType Container })]
        [string] $projectTemplateRoot,
        [parameter(mandatory=$true, HelpMessage="Enter A Trip Identifier Name")]
        [string] $tripidentifier),
        [parameter()]
        [string] $archiveRoot = "c:\archive"


CLS
Set-StrictMode -Version 4


$tripFolderFullPath = "$($projectRoot)\$($tripidentifier)"

# Alter this list to change the set of folders created by the script
$assetFolderList = "jpg", "raw", "video", "gps", "gps\waypoints", "gps\tracks", "gps\recordings", "gps\images"

If ( $(test-path $tripFolderFullPath) -eq $false ) {
    mkdir $tripFolderFullPath
    write-host "Trip folder created." -ForegroundColor White -BackgroundColor Green
} Else {
    write-host "Trip folder exists. " -BackgroundColor Magenta -ForegroundColor Yellow
}

Foreach($assetFolder in $assetFolderList) {
    $assetFolderPath = "$($tripFolderFullPath)\$($assetfolder)"
    if ( $(test-path $assetFolderPath ) -eq $false ) {
        new-item $assetFolderPath -type directory
        Write-Host "Folder Created: $assetFolder" -ForegroundColor White -BackgroundColor Green
    } else {
        Write-Host "Folder Exists: $assetFolder" -ForegroundColor White -BackgroundColor Green
    }
}

# Get the asset metadata template file and copy it into the project tree
Copy-Item -path "$($projectTemplateRoot)\templates\asset_folder_metadata.xml" -destination "$tripFolderFullPath\asset_folder_metadata.xml"
$settingsFilePath = "$($tripFolderFullPath)\asset_folder_metadata.xml"
if ( $(test-path $settingsFilePath ) -eq $false ) {
    Write-Host "Project metadata file not found. Exiting." -ForegroundColor White -BackgroundColor red
    exit
}

# Update the paths in the asset metadata file
[xml]$settingsfile = New-Object XML
$settingsfile.Load($settingsFilePath)
$settingsfile.settings.paths.rootPath = $projectRoot
$settingsfile.settings.paths.archiveRootPath = $archiveRoot
$settingsfile.settings.paths.tripProjectName = $tripidentifier
$settingsfile.settings.paths.AllResourcesListFile = "$($tripidentifier)_all_resources.txt"
$settingsfile.settings.paths.webAlblumListFile = "$($tripidentifier)_webalbum_jpgs.txt"
$settingsfile.settings.paths.deleteImagesListFile = "$($tripidentifier)_delete_jpgs.txt"
$settingsfile.Save("$($tripFolderFullPath)\asset_folder_metadata.xml")

Write-Host "Done." -ForegroundColor White -BackgroundColor Green

