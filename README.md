# va-pysec-2023-1

## 1. Instalācija

Izmantoju linux Linux Mint 21.1 Cinnamon

##Python 3.11 instalācija 

```shell
sudo apt-get update
 sudo apt-get install python3.11
```
##Python 2.7.16 instalācija 

```shell
sudo apt-get install python2.7


$ ls -1 /usr/bin/python* | grep '.*[2-3]\(.[0-9]\+\)\?$'
/usr/bin/python2.7
/usr/bin/python3
/usr/bin/python3.10
/usr/bin/python3.11
/usr/bin/python3.9

```

## 2. Pārslēgšanās starp virtuālajām vidēm

```shell
python3.11 -m venv venv3.11
source /home/linux/Darbvirsma/Phtonsclonets/pysec2023/venv2/bin/activate
deactivate

virtualenv -p /usr/bin/python2.7 venv2
s
deactivate
```
#3. pip avotu instalācija, pielikumu info sagatavošana 
```shell
python3.11 -m venv venv3.11
pip install google
pip freeze > requirements.txt
```
