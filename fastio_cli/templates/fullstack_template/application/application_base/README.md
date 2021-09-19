# FastApp Template

Create virtualenv

```
virtualenv -p python3.7 venv
source venv-3.7/bin/activate

cs fastapp && pip install -r requirements.txt 
```

Migrations


```shell
cd fastapp
make migrate
```
