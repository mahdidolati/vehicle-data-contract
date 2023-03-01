# Misc
Install guest additions:
```
sudo apt install build-essential dkms linux-headers-$(uname -r)
sudo ./VBoxLinuxAdditions.run 
sudo usermod --append --groups vboxsf $USER
```

Generate ssh key:
```
ssh-keygen -t ed25519 -C "mehdidolati@hotmail.com"
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

Turn the directory to repo:
```
sudo apt install git
git init
git add ...
git config --global user.email "mehdidolati@hotmail.com"
git config --global user.name "Mahdi Dolati"
git commit -m "add initial contract creation code"
git remote add origin git@github.com:mahdidolati/vehicle-data-contract.git
git push --set-upstream origin master
```

Github fingerprints:
Public key fingerprints can be used to validate a connection to a remote server.

These are GitHub's public key fingerprints:
```
SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8 (RSA)
SHA256:br9IjFspm1vxR3iA35FWE+4VTyz1hYVLIE2t1/CeyWQ (DSA - deprecated)
SHA256:p2QAMXNIC1TJYWeIOttrVc98/R1BUFWu3/LiyKgUfQM (ECDSA)
SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU (Ed25519)
```
You can add the following ssh key entries to your ~/.ssh/known_hosts file to avoid manually verifying GitHub hosts:
```
github.com ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOMqqnkVzrm0SdG6UOoqKLsabgH5C9okWi0dh2l9GKJl
github.com ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBEmKSENjQEezOmxkZMy7opKgwFB9nkt5YRrYMjNuG5N87uRgg6CLrbo5wAdT/y6v0mKV0U2w0WZ2YB/++Tpockg=
github.com ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEAq2A7hRGmdnm9tUDbO9IDSwBK6TbQa+PXYPCPy6rbTrTtw7PHkccKrpp0yVhp5HdEIcKr6pLlVDBfOLX9QUsyCOV0wzfjIJNlGEYsdlLJizHhbn2mUjvSAHQqZETYP81eFzLQNnPHt4EVVUh7VfDESU84KezmD5QlWpXLmvU31/yMf+Se8xhHTvKSCZIFImWwoG6mbUoWf9nzpIoaSjB+weqqUUmpaaasXVal72J+UX2B+2RPW3RcT0eOzQgqlJL3RKrTJvdsjE3JEAvGq3lGHSZXy28G3skua2SmVi/w4yCE6gbODqnTWlg7+wC604ydGXA8VJiS5ap43JXiUFFAaQ==
```

Check version of Ubuntu:
```
cat /etc/lsb-release
```



    1  sudo apt update
    2  python --version
    3  python3 --version
    4  pip
    5  sudo apt install python3-pip
    6  pip install web3
    7  pip install py-solc-x
    8  pip install eth-utils
    9  pip install python-dotenv
   10  ls
   11  sudo apt install build-essential dkms linux-headers-$(uname -r)
   12  sudo ./VBoxLinuxAdditions.run 
   13  echo $USER
   14  sudo usermod --append --groups vboxsf $USER
   15  ssh-keygen -t ed25519 -C "mehdidolati@hotmail.com"
   16  eval "$(ssh-agent -s)"
   17  ssh-add ~/.ssh/id_ed25519
   18  git init
   19  git add main.py SimpleStorageContract.sol 
   20  sudo apt install git
   21  git init
   22  git add main.py SimpleStorageContract.sol 
   23  git commit -m "add initial contract creation code"
   24  git config --global user.email "mehdidolati@hotmail.com"
   25  git config --global user.name "Mahdi Dolati"
   26  git commit -m "add initial contract creation code"
   27  git remote add origin git@github.com:mahdidolati/vehicle-data-contract.git
   28  git push
   29  git push --set-upstream origin master
   30  git status
   31  release_lsb -all
   32  release_lsb --all
   33  lsb_release
   34  cat /etc/lsb-release 
   35  python --version
   36  python3 --version
   37  git status
   38  git add README.md 
   39  git commit -m "add readme"
   40  git push
   41  sudo apt install ./code_1.75.1-1675893397_amd64.deb 
   42  pip install python-dotenv
   43  cd ~/Projects/
   44  ls
   45  cd smart-contract/
   46  ls
   47  python3 main.py 
   48  ll
   49  python3 main.py 
   50  python3
   51  pip show module solcx
   52  pip list
   53  pip show module py-solc-x
   54  pyton3
   55  python3
   56  pip show module python-dotenv
   57  git status
   58  git add README.md 
   59  git commit -m "add version of pip modules"
   60  git push
   61  git status
   62  python3 main.py 
   63  cd ~/Downloads/
   64  chmod a+x ganache-2.7.0-linux-x86_64.AppImage 
   65  ./ganache-2.7.0-linux-x86_64.AppImage 
   66  sudo add-apt-repository universe
   67  sudo apt install libfuse2
   68  ./ganache-2.7.0-linux-x86_64.AppImage 
   69  ./configure
   70  make
   71  sudo apt install m4
   72  make
   73  ./configure
   74  make
   75  make check
   76  sudo make install
   77  sudo apt install p7zip
   78  sudo apt install zlib1g-dev
   79  apt show openssl
   80  sudo apt install openssl -y
   81  cd ..
   82  git clone git@github.com:blynn/pbc.git
   83  cd pbc/
   84  ls
   85  ./configure
   86  ls
   87  nano INSTALL 
   88  ./configure
   89  ls
   90  nano configure.ac 
   91  ./configure.ac
   92  cd ..
   93  ls
   94  cd gmp-6.2.1/
   95  ls
   96  sudo ldconfig
   97  cd ..
   98  cd pbc/
   99  ls
  100  autoconf
  101  sudo apt install autoconf
  102  sudo apt install automake
  103  sudo apt install libtool
  104  nano configure.ac 
  105  autoconf --verbose --install
  106  autoconf --verbose
  107  sudo apt install autoconf-archive
  108  autoconf --verbose
  109  ls
  110  whereis m4
  111  sudo apt install g__
  112  sudo apt install g++
  113  sudo apt install make
  114  sudo apt install m4
  115  sudo apt autoremove
  116  autoconf
  117  suto apt remove m4
  118  sudo apt remove m4
  119  sudo apt autoremove
  120  sudo apt install m4
  121  autoconf
  122  whereis autoconf
  123  sudo apt install autoconf
  124  autoconf
  125  cd ..
  126  git clone git://git.sv.gnu.org/autoconf-archive.git
  127  cd autoconf-archive/
  128  ls
  129  find . -name AX_CXX_COMPILE_STDCXX
  130  find . -name README.md
  131  find . -name AX_CXX_COMPILE_STDCXX_14
  132  find . -name ax_cxx_compile_stdcxx_14
  133  cd ..
  134  sudo apt remove autoconf-archive
  135  cd autoconf-archive/
  136  ./configure 
  137  autoreconf --install --force
  138  ls
  139  nano README
  140  nano README.md 
  141  nano README-maint 
  142  sudo apt install -y gnulib
  143  nano README-maint 
  144  sudo apt install texinfo
  145  ./bootstrap.sh 
  146  nano README-maint 
  147  ./configure 
  148  nano README-maint 
  149  make maintainer-all
  150  make
  151  nano README-maint 
  152  sudo make install
  153  cd ..
  154  ls
  155  cd pbc/
  156  ls
  157  autoconf
  158  autoconf-archive
  159  cd ..
  160  cd autoconf-archive/`
  161  cd autoconf-archive/
  162  sudo make install check
  163  cd ..
  164  cd pbc/
  165  ls
  166  nano README 
  167  nano INSTALL 
  168  ./configure
  169  autoconf
  170  whereis autorconf-archive
  171  cd ..
  172  cd autoconf-archive/
  173  sudo apt remove autoconf
  174  sudo apt remove m4
  175  sudo apt autoremove
  176  ./bootstrap.sh 
  177  autoreconf
  178  sudo apt install autoreconf
  179  sudo apt install autoconf
  180  ./bootstrap.sh 
  181  ./configure
  182  make maintainer-all
  183  automake --add-missing
  184  cd ..
  185  cd pbc-0.5.14/
  186  ./configure LDFLAGS="-lgmp"
  187  sudo apt install flex
  188  ./configure LDFLAGS="-lgmp"
  189  sudo apt install bison
  190  ./configure LDFLAGS="-lgmp"
  191  make
  192  sudo make install
  193  sudo ldconfig
  194  cd ..
  195  git clone git@github.com:ASTRI-Security-Lab/libbswabe.git
  196  rm -r libbswabe/
  197  ls
  198  cd libbswabe-0.9/
  199  ./configure
  200  sudo apt install openssl
  201  sudo apt install libcrypto++-dev
  202  ./configure
  203  sudo apt install libcrypto
  204  sudo apt install libssl-dev
  205  sudo apt install liblzo2-dev
  206  sudo apt install libpam0g-dev
  207  ./configure
  208  make
  209  sudo apt install libglib2.0-dev
  210  make
  211  sudo apt install glibc-source -y
  212  make
  213  sudo apt install libglib2.0-0
  214  ./configure
  215  make
  216  sudo make install
  217  java
  218  history 100
  219  history 1000

https://stackoverflow.com/questions/17373306/error-in-linking-gmp-while-compiling-cpabe-package-from-its-source-code
```
./configure --with-gmp-include=/home/mahdi/Programs/gmp-6.2.1 --with-gmp-lib=/home/mahdi/Programs/gmp-6.2.1/.libs --with-pbc-include=/home/mahdi/Programs/pbc-0.5.14/include --with-pbc-lib=/home/mahdi/Programs/pbc-0.5.14/.libs --with-bswabe-include=/home/mahdi/Programs/libbswabe-0.9 --with-bswabe-lib=/home/mahdi/Programs/libbswabe-0.9
make LDFLAGS="-lgmp -lpbc -lcrypto -L/usr/lib/x86_64-linux-gnu -lglib-2.0 -lbswabe -lgmp"
make install
```

It might be trivial for some of you, but policy_lang.y is missing a semicolon in line 67, hence the compilation fails with:

 policy_lang.y: In function ‘yyparse’:
 policy_lang.y:67:38: error: expected ‘;’ before ‘}’ token
 result: policy { final_policy = $1 }
It can be fixed by changing line 67 to

 result: policy { final_policy = $1; }



 ====

    1  sudo apt update
    2  python --version
    3  python3 --version
    4  pip
    5  sudo apt install python3-pip
    6  pip install web3
    7  pip install py-solc-x
    8  pip install eth-utils
    9  pip install python-dotenv
   10  ls
   11  sudo apt install build-essential dkms linux-headers-$(uname -r)
   12  sudo ./VBoxLinuxAdditions.run 
   13  echo $USER
   14  sudo usermod --append --groups vboxsf $USER
   15  ssh-keygen -t ed25519 -C "mehdidolati@hotmail.com"
   16  eval "$(ssh-agent -s)"
   17  ssh-add ~/.ssh/id_ed25519
   18  git init
   19  git add main.py SimpleStorageContract.sol 
   20  sudo apt install git
   21  git init
   22  git add main.py SimpleStorageContract.sol 
   23  git commit -m "add initial contract creation code"
   24  git config --global user.email "mehdidolati@hotmail.com"
   25  git config --global user.name "Mahdi Dolati"
   26  git commit -m "add initial contract creation code"
   27  git remote add origin git@github.com:mahdidolati/vehicle-data-contract.git
   28  git push
   29  git push --set-upstream origin master
   30  git status
   31  release_lsb -all
   32  release_lsb --all
   33  lsb_release
   34  cat /etc/lsb-release 
   35  python --version
   36  python3 --version
   37  git status
   38  git add README.md 
   39  git commit -m "add readme"
   40  git push
   41  sudo apt install ./code_1.75.1-1675893397_amd64.deb 
   42  pip install python-dotenv
   43  cd ~/Projects/
   44  ls
   45  cd smart-contract/
   46  ls
   47  python3 main.py 
   48  ll
   49  python3 main.py 
   50  python3
   51  pip show module solcx
   52  pip list
   53  pip show module py-solc-x
   54  pyton3
   55  python3
   56  pip show module python-dotenv
   57  git status
   58  git add README.md 
   59  git commit -m "add version of pip modules"
   60  git push
   61  git status
   62  python3 main.py 
   63  cd ~/Downloads/
   64  chmod a+x ganache-2.7.0-linux-x86_64.AppImage 
   65  ./ganache-2.7.0-linux-x86_64.AppImage 
   66  sudo add-apt-repository universe
   67  sudo apt install libfuse2
   68  ./ganache-2.7.0-linux-x86_64.AppImage 
   69  make clean
   70  ./configure
   71  make
   72  cd gmp-6.2.1/
   73  ls
   74  make clean
   75  ./configure
   76  make
   77  sudo make install
   78  sudo ldconfig
   79  cd ..
   80  cd pbc-0.5.14/
   81  ls
   82  make clean
   83  make clear
   84  ./configure
   85  make
   86  sudo make install
   87  sudo ldconfig
   88  cd ..
   89  cd libbswabe-0.9/
   90  make clean
   91  ./configure 
   92  make
   93  sudo make install
   94  sudo ldconfig
   95  cd ..
   96  cd cpabe-0.11/
   97  ls
   98  make clean
   99  ./configure 
  100  make
  101  make clean
  102  history 1000

  ===
    1  sudo apt update
    2  python --version
    3  python3 --version
    4  pip
    5  sudo apt install python3-pip
    6  pip install web3
    7  pip install py-solc-x
    8  pip install eth-utils
    9  pip install python-dotenv
   10  ls
   11  sudo apt install build-essential dkms linux-headers-$(uname -r)
   12  sudo ./VBoxLinuxAdditions.run 
   13  echo $USER
   14  sudo usermod --append --groups vboxsf $USER
   15  ssh-keygen -t ed25519 -C "mehdidolati@hotmail.com"
   16  eval "$(ssh-agent -s)"
   17  ssh-add ~/.ssh/id_ed25519
   18  git init
   19  git add main.py SimpleStorageContract.sol 
   20  sudo apt install git
   21  git init
   22  git add main.py SimpleStorageContract.sol 
   23  git commit -m "add initial contract creation code"
   24  git config --global user.email "mehdidolati@hotmail.com"
   25  git config --global user.name "Mahdi Dolati"
   26  git commit -m "add initial contract creation code"
   27  git remote add origin git@github.com:mahdidolati/vehicle-data-contract.git
   28  git push
   29  git push --set-upstream origin master
   30  git status
   31  release_lsb -all
   32  release_lsb --all
   33  lsb_release
   34  cat /etc/lsb-release 
   35  python --version
   36  python3 --version
   37  git status
   38  git add README.md 
   39  git commit -m "add readme"
   40  git push
   41  sudo apt install ./code_1.75.1-1675893397_amd64.deb 
   42  pip install python-dotenv
   43  cd ~/Projects/
   44  ls
   45  cd smart-contract/
   46  ls
   47  python3 main.py 
   48  ll
   49  python3 main.py 
   50  python3
   51  pip show module solcx
   52  pip list
   53  pip show module py-solc-x
   54  pyton3
   55  python3
   56  pip show module python-dotenv
   57  git status
   58  git add README.md 
   59  git commit -m "add version of pip modules"
   60  git push
   61  git status
   62  python3 main.py 
   63  cd ~/Downloads/
   64  chmod a+x ganache-2.7.0-linux-x86_64.AppImage 
   65  ./ganache-2.7.0-linux-x86_64.AppImage 
   66  sudo add-apt-repository universe
   67  sudo apt install libfuse2
   68  ./ganache-2.7.0-linux-x86_64.AppImage 
   69  make clean
   70  ./configure
   71  make
   72  ./configure
   73  make
   74  make install
   75  sudo make install
   76  locate libbswabe
   77  locate libbswabe.so
   78  cd ..
   79  cd cpabe-0.11/
   80  make clean
   81  ./configure --with-gmp-include=/home/mahdi/Programs/gmp-6.2.1 --with-gmp-lib=/home/mahdi/Programs/gmp-6.2.1/.libs --with-pbc-include=/home/mahdi/Programs/pbc-0.5.14/include --with-pbc-lib=/home/mahdi/Programs/pbc-0.5.14/.libs --with-bswabe-include=/home/mahdi/Programs/libbswabe-0.9 --with-bswabe-lib=/home/mahdi/Programs/libbswabe-0.9
   82  make LDFLAGS="-lgmp -lpbc -lcrypto -L/usr/lib/x86_64-linux-gnu -lglib -lbswabe -lgmp"
   83  sudo apt install libglib2.0-dev
   84  sudo apt install libgtk2.0-dev
   85  make LDFLAGS="-lgmp -lpbc -lcrypto -L/usr/lib/x86_64-linux-gnu -lglib-2.0 -lbswabe -lgmp"
   86  sudo make install
   87  sudo ldconfigu
   88  sudo ldconfig
   89  cd ..
   90  cpabe-setup -v
   91  cpabe-enc -h
   92  history 1000

====
    1  sudo apt update
    2  python --version
    3  python3 --version
    4  pip
    5  sudo apt install python3-pip
    6  pip install web3
    7  pip install py-solc-x
    8  pip install eth-utils
    9  pip install python-dotenv
   10  ls
   11  sudo apt install build-essential dkms linux-headers-$(uname -r)
   12  sudo ./VBoxLinuxAdditions.run 
   13  echo $USER
   14  sudo usermod --append --groups vboxsf $USER
   15  ssh-keygen -t ed25519 -C "mehdidolati@hotmail.com"
   16  eval "$(ssh-agent -s)"
   17  ssh-add ~/.ssh/id_ed25519
   18  git init
   19  git add main.py SimpleStorageContract.sol 
   20  sudo apt install git
   21  git init
   22  git add main.py SimpleStorageContract.sol 
   23  git commit -m "add initial contract creation code"
   24  git config --global user.email "mehdidolati@hotmail.com"
   25  git config --global user.name "Mahdi Dolati"
   26  git commit -m "add initial contract creation code"
   27  git remote add origin git@github.com:mahdidolati/vehicle-data-contract.git
   28  git push
   29  git push --set-upstream origin master
   30  git status
   31  release_lsb -all
   32  release_lsb --all
   33  lsb_release
   34  cat /etc/lsb-release 
   35  python --version
   36  python3 --version
   37  git status
   38  git add README.md 
   39  git commit -m "add readme"
   40  git push
   41  sudo apt install ./code_1.75.1-1675893397_amd64.deb 
   42  pip install python-dotenv
   43  cd ~/Projects/
   44  ls
   45  cd smart-contract/
   46  ls
   47  python3 main.py 
   48  ll
   49  python3 main.py 
   50  python3
   51  pip show module solcx
   52  pip list
   53  pip show module py-solc-x
   54  pyton3
   55  python3
   56  pip show module python-dotenv
   57  git status
   58  git add README.md 
   59  git commit -m "add version of pip modules"
   60  git push
   61  git status
   62  python3 main.py 
   63  cd ~/Downloads/
   64  chmod a+x ganache-2.7.0-linux-x86_64.AppImage 
   65  ./ganache-2.7.0-linux-x86_64.AppImage 
   66  sudo add-apt-repository universe
   67  sudo apt install libfuse2
   68  ./ganache-2.7.0-linux-x86_64.AppImage 
   69  ./configure
   70  make
   71  sudo apt install m4
   72  make
   73  ./configure
   74  make
   75  make check
   76  sudo make install
   77  sudo apt install p7zip
   78  sudo apt install zlib1g-dev
   79  apt show openssl
   80  sudo apt install openssl -y
   81  cd ..
   82  git clone git@github.com:blynn/pbc.git
   83  cd pbc/
   84  ls
   85  ./configure
   86  ls
   87  nano INSTALL 
   88  ./configure
   89  ls
   90  nano configure.ac 
   91  ./configure.ac
   92  cd ..
   93  ls
   94  cd gmp-6.2.1/
   95  ls
   96  sudo ldconfig
   97  cd ..
   98  cd pbc/
   99  ls
  100  autoconf
  101  sudo apt install autoconf
  102  sudo apt install automake
  103  sudo apt install libtool
  104  nano configure.ac 
  105  autoconf --verbose --install
  106  autoconf --verbose
  107  sudo apt install autoconf-archive
  108  autoconf --verbose
  109  ls
  110  whereis m4
  111  sudo apt install g__
  112  sudo apt install g++
  113  sudo apt install make
  114  sudo apt install m4
  115  sudo apt autoremove
  116  autoconf
  117  suto apt remove m4
  118  sudo apt remove m4
  119  sudo apt autoremove
  120  sudo apt install m4
  121  autoconf
  122  whereis autoconf
  123  sudo apt install autoconf
  124  autoconf
  125  cd ..
  126  git clone git://git.sv.gnu.org/autoconf-archive.git
  127  cd autoconf-archive/
  128  ls
  129  find . -name AX_CXX_COMPILE_STDCXX
  130  find . -name README.md
  131  find . -name AX_CXX_COMPILE_STDCXX_14
  132  find . -name ax_cxx_compile_stdcxx_14
  133  cd ..
  134  sudo apt remove autoconf-archive
  135  cd autoconf-archive/
  136  ./configure 
  137  autoreconf --install --force
  138  ls
  139  nano README
  140  nano README.md 
  141  nano README-maint 
  142  sudo apt install -y gnulib
  143  nano README-maint 
  144  sudo apt install texinfo
  145  ./bootstrap.sh 
  146  nano README-maint 
  147  ./configure 
  148  nano README-maint 
  149  make maintainer-all
  150  make
  151  nano README-maint 
  152  sudo make install
  153  cd ..
  154  ls
  155  cd pbc/
  156  ls
  157  autoconf
  158  autoconf-archive
  159  cd ..
  160  cd autoconf-archive/`
  161  cd autoconf-archive/
  162  sudo make install check
  163  cd ..
  164  cd pbc/
  165  ls
  166  nano README 
  167  nano INSTALL 
  168  ./configure
  169  autoconf
  170  whereis autorconf-archive
  171  cd ..
  172  cd autoconf-archive/
  173  sudo apt remove autoconf
  174  sudo apt remove m4
  175  sudo apt autoremove
  176  ./bootstrap.sh 
  177  autoreconf
  178  sudo apt install autoreconf
  179  sudo apt install autoconf
  180  ./bootstrap.sh 
  181  ./configure
  182  make maintainer-all
  183  automake --add-missing
  184  cd ..
  185  cd pbc-0.5.14/
  186  ./configure LDFLAGS="-lgmp"
  187  sudo apt install flex
  188  ./configure LDFLAGS="-lgmp"
  189  sudo apt install bison
  190  ./configure LDFLAGS="-lgmp"
  191  make
  192  sudo make install
  193  sudo ldconfig
  194  cd ..
  195  git clone git@github.com:ASTRI-Security-Lab/libbswabe.git
  196  rm -r libbswabe/
  197  ls
  198  cd libbswabe-0.9/
  199  ./configure
  200  sudo apt install openssl
  201  sudo apt install libcrypto++-dev
  202  ./configure
  203  sudo apt install libcrypto
  204  sudo apt install libssl-dev
  205  sudo apt install liblzo2-dev
  206  sudo apt install libpam0g-dev
  207  ./configure
  208  make
  209  sudo apt install libglib2.0-dev
  210  make
  211  sudo apt install glibc-source -y
  212  make
  213  sudo apt install libglib2.0-0
  214  ./configure
  215  make
  216  sudo make install
  217  java
  218  history 100
  219  history 1000
  220  source ~/.bashrc 
  221  java
  222  cd ..
  223  cd cpabe-0.11/
  224  ./configure
  225  cd cpabe-0.11/
  226  ls
  227  ./configure 
  228  make
  229  ./configure 
  230  make
  231  cd ..
  232  cd cpabe-0.11/
  233  ./configure 
  234  make
  235  whereis libpbc
  236  cd ..
  237  cd pbc-0.5.14/
  238  ls
  239  sudo make install
  240  cd ..
  241  ls
  242  cd cpabe-0.11/
  243  ls
  244  make
  245  ./configure
  246  make
  247  sudo apt install libgmp3-dev
  248  sudo apt install libgmp-dev
  249  ./config
  250  ./configure 
  251  make
  252  cd ..
  253  cd libbswabe-0.9/
  254  make install
  255  sudo make install
  256  cd ..
  257  cd cpabe-0.11/
  258  ls
  259  make
  260  sudo apt remove gmp
  261  cd ..
  262  ls
  263  cd gmp-6.2.1/
  264  ls
  265  sudo apt install libgmp-dev
  266  cd printf/
  267  cd ..
  268  l;s
  269  ls
  270  cd pbc-0.5.14/
  271  ./configure.sh
  272  cd ..
  273  cd gmp-6.2.1/
  274  sudo ldconfig
  275  cd ..
  276  cd pbc-0.5.14/
  277  sudo ldconfig
  278  cd ..
  279  ls
  280  cd libbswabe-0.9/
  281  sudo ldconfig
  282  cd ..
  283  cd cpabe-0.11/
  284  ls
  285  ./configure 
  286  make
  287  ./configure
  288  make
  289  sudo make
  290  find / -name gmp
  291  make
  292  ./configure --with-gmp-lib=/home/mahdi/Programs/gmp-6.2.1/.libs/ --with-gmp-include=/home/mahdi/Programs/gmp-6.2.1/
  293  make
  294  ./configure --with-gmp-lib=/home/mahdi/Programs/gmp-6.2.1/.libs --with-gmp-include=/home/mahdi/Programs/gmp-6.2.1
  295  make
  296  ./configure --with-gmp-lib=/home/mahdi/Programs/gmp-6.2.1/.libs --with-gmp-include=/home/mahdi/Programs/gmp-6.2.1 --with-pbc-include=/home/mahdi/Programs/pbc-0.5.14/include --with-pbc-lib=/home/mahdi/Programs/pbc-0.5.14/
  297  make
  298  ./configure --with-gmp-lib=/home/mahdi/Programs/gmp-6.2.1/.libs --with-gmp-include=/home/mahdi/Programs/gmp-6.2.1 --with-pbc-include=/home/mahdi/Programs/pbc-0.5.14/include --with-pbc-lib=/home/mahdi/Programs/pbc-0.5.14/.libs
  299  make
  300  cd ..
  301  cd pbc-0.5.14/
  302  ./configure 
  303  make
  304  sudo make install
  305  sudo ldconfigu
  306  sudo ldconfig
  307  make clean
  308  make
  309  make clean
  310  ./configure 
  311  make
  312  sudo make install
  313  sudo ldconfig
  314  cd ..
  315  cd libbswabe-0.9/
  316  ls
  317  make clean
  318  ./configure
  319  make
  320  sudo make install
  321  cd ..
  322  cd libbswabe-0.9/
  323  sudo ldconfigu
  324  sudo ldconfig
  325  cd ..
  326  cd cpabe-0.11/
  327  ls
  328  make clean
  329  ./cofigure
  330  ./configure 
  331  make
  332  locate liblgmp
  333  sudo apt install plocate
  334  locate liblgmp
  335  sudo locate liblgmp
  336  make
  337  locate libgmp
  338  cd ..
  339  cd cpabe-0.11/
  340  make
  341  sudo apt install libeigen3-dev
  342  make clean
  343  make clear
  344  ./configure
  345  make
  346  locate lgmp
  347  locate lpbc
  348  locate lbswabe
  349  locate lcrypto
  350  locate crypto
  351  locate pbc
  352  locate pbc.so
  353  locate pbc.a
  354  locate pbc.dyl
  355  locate gmp.so
  356  locate gmp.a
  357  history 1000


