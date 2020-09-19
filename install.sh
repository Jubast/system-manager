
# create program dir and copy files
path="$HOME/.local/share/jubast/system-manager"
\rm -rf $path

mkdir -p $path
\cp -rf config $path
\cp -rf src $path

# create symbolic link to main.py
ppath="$HOME/.local/bin"
mkdir -p $ppath

binpath="$ppath/system-manager"
srcpath="$path/src/main.py"

\rm -f $binpath
\ln -s $srcpath $binpath
