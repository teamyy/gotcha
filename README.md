# Gotcha
A crawler to find a lot of humor post

## Installation
If you have setuptools, installed,
```
python setup.py install
```
Only install successfully on **Linux** system and **Debian, Redhat, Centos** linux distributions will be guaranteed.

## Initialize After Install Scrapyd
If you just initialize,
```
python gotcha.py -c init --egg="/usr/local/lib/python2.7/dist-packages/gotcha-{version}-py2.7.egg"
```

## Avaliable Commands
To run one of the spiders,
```
python gotcha.py -c run --spider={spider}
```

To stop the job of the spider of running,
```
python gotcha.py -c cancel --job={jobid}
```

To display the crawl jobs status,
```
python gotcha.py -c status
```

To display the available spider list,
```
python gotcha.py -c list
```