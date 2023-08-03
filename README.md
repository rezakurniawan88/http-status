## INSTALLATION

1. Clone repository :
``` bash
git clone https://github.com/rezakurniawan88/http-status.git
```
2. Change directory to http-status
```bash
cd http-status
```
3. Install requests module
```bash
pip3 install requests
```

## HOW TO USE

``` bash
How to use : python3 http-status.py [options] [url/list]

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     Scan with single url
  -l LIST, --list LIST  Scan with multi url/list file, format(.txt)
```

## EXAMPLE

### Scan With Single Url
``` bash
$ python3 http-status.py -u https://example.com

 ______ ______ ______ ______ ______ ______ ______ ______
|______|______|______|______|______|______|______|______|
 _     _   _                      _        _
| |   | | | |                    | |      | |
| |__ | |_| |_ _ __           ___| |_ __ _| |_ _   _ ___
| '_ \| __| __|  _ \   ____  / __| __/ _` | __| | | / __|
| | | | |_| |_| |_) | |____| \__ | || (_| | |_| |_| \__ \
|_| |_|\__|\__| .__/         |___/\__\__,_|\__|\__,_|___/
              | |
              |_|
 ______ ______ ______ ______ ______ ______ ______ ______
|______|______|______|______|______|______|______|______|

                                        @rezakurniawan88

Starting ...

Status  |     Website
[200]   : https://example.com

```

### Scan With List File
``` bash
$ python3 http-status.py -l list-url.txt

 ______ ______ ______ ______ ______ ______ ______ ______
|______|______|______|______|______|______|______|______|
 _     _   _                      _        _
| |   | | | |                    | |      | |
| |__ | |_| |_ _ __           ___| |_ __ _| |_ _   _ ___
| '_ \| __| __|  _ \   ____  / __| __/ _` | __| | | / __|
| | | | |_| |_| |_) | |____| \__ | || (_| | |_| |_| \__ \
|_| |_|\__|\__| .__/         |___/\__\__,_|\__|\__,_|___/
              | |
              |_|
 ______ ______ ______ ______ ______ ______ ______ ______
|______|______|______|______|______|______|______|______|

                                        @rezakurniawan88

Starting ...

Status  |     Website
[200]   : https://example.com
[403]   : https://admin.example.com
[503]   : https://abc.example.com
[404]   : https://def.example.com
```
