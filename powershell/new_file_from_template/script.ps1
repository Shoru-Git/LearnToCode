$name = "SW32-01"
$ip = "10.0.32.1"
$directory = "SW32"
$template = ".\template.ksr"

Get-Content $template | ForEach-Object {
    $_ -replace "__NAME__","$name" `
    -replace "__IP__","$ip" `
    -replace "__DIR__","$directory"
} | Set-Content ".\$name.ksr"