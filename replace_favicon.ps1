$dir = "d:\GrowwPark projects\Bloom"
$files = Get-ChildItem -Path $dir -Filter "*.html"
$oldStr = '<link rel="icon" type="image/svg+xml" href="assets/favicon.svg">'
$newStr = '<link rel="icon" type="image/jpeg" href="assets/images/favicon1.jpg">'

foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw
    if ($content -match [regex]::Escape($oldStr)) {
        $content = $content -replace [regex]::Escape($oldStr), $newStr
        [IO.File]::WriteAllText($file.FullName, $content, [System.Text.Encoding]::UTF8)
        Write-Host "Updated $($file.Name)"
    }
}
