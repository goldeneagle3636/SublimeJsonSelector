packagePath="$HOME/Library/Application Support/Sublime Text 3/Packages"
jsonSelectorPath="$packagePath/SublimeJsonSelect"
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $DIR
mkdir -p "$jsonSelectorPath"
rm -rf "$jsonSelectorPath/"
cp -R . "$jsonSelectorPath"
open "$jsonSelectorPath"
