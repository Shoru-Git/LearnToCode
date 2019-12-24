name="SW32-01"
ip="10.0.32.01"
directory="SW32"
template="template.ksr"

sed -e "s/__NAME__/$name/;s/__IP__/$ip/;s/__DIR__/$directory/" $template >> $name.ksr