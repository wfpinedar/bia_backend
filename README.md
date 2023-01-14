# Bia backend test

This repo contains code and information about test.

## 1. Install environment

For install all necessary packages first we need to define virtual environment with poetry is like this:

```bash
poetry shell
```

Now install necessary packages: 

```bash
poetry install
```

## 2. Run project

go to main folder and run:

```bash
PYTHONPATH=. poetry run python app/main.py
```

### 2.1 run tests

```bash
poetry run pytest -vv
```


## 3. Curl query and results
### Query for daily:
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/api/v1/meter/usage?date=2022-10-26&period=daily&skip=0&limit=100' \
  -H 'accept: application/json'
```
Result:
```json
[
  {
    "meter_date": "2022-10-26T00:00:00",
    "value": 3.8699999999989814
  },
  {
    "meter_date": "2022-10-26T01:00:00",
    "value": 4.389999999999418
  },
  {
    "meter_date": "2022-10-26T02:00:00",
    "value": 3.4899999999997817
  },
  {
    "meter_date": "2022-10-26T03:00:00",
    "value": 2.9800000000013824
  },
  {
    "meter_date": "2022-10-26T04:00:00",
    "value": 3.0799999999999272
  },
  {
    "meter_date": "2022-10-26T05:00:00",
    "value": 2.9200000000000728
  },
  {
    "meter_date": "2022-10-26T06:00:00",
    "value": 3.180000000000291
  },
  {
    "meter_date": "2022-10-26T07:00:00",
    "value": 2.639999999999418
  },
  {
    "meter_date": "2022-10-26T09:00:00",
    "value": 2.6700000000000728
  },
  {
    "meter_date": "2022-10-26T10:00:00",
    "value": 3.600000000000364
  },
  {
    "meter_date": "2022-10-26T11:00:00",
    "value": 3.7999999999992724
  },
  {
    "meter_date": "2022-10-26T12:00:00",
    "value": 4.110000000000582
  },
  {
    "meter_date": "2022-10-26T13:00:00",
    "value": 4.959999999999127
  },
  {
    "meter_date": "2022-10-26T14:00:00",
    "value": 5.440000000000509
  },
  {
    "meter_date": "2022-10-26T15:00:00",
    "value": 5
  },
  {
    "meter_date": "2022-10-26T16:00:00",
    "value": 5.399999999999636
  },
  {
    "meter_date": "2022-10-26T17:00:00",
    "value": 5.039999999999054
  },
  {
    "meter_date": "2022-10-26T18:00:00",
    "value": 4.8700000000008
  },
  {
    "meter_date": "2022-10-26T19:00:00",
    "value": 4.489999999999782
  },
  {
    "meter_date": "2022-10-26T20:00:00",
    "value": 4.799999999999272
  },
  {
    "meter_date": "2022-10-26T21:00:00",
    "value": 4.68999999999869
  },
  {
    "meter_date": "2022-10-26T22:00:00",
    "value": 4.709999999999127
  },
  {
    "meter_date": "2022-10-26T23:00:00",
    "value": 3.929999999998472
  }
]
```

### Query for weekly
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/api/v1/meter/usage?date=2022-10-26&period=weekly&skip=0&limit=100' \
  -H 'accept: application/json'
```
Result:
```json
[
  {
    "meter_date": "2022-10-24T00:00:00",
    "value": 571.71
  },
  {
    "meter_date": "2022-10-25T00:00:00",
    "value": 616.8000000000002
  },
  {
    "meter_date": "2022-10-26T00:00:00",
    "value": 586.0499999999993
  },
  {
    "meter_date": "2022-10-27T00:00:00",
    "value": 592.6800000000003
  },
  {
    "meter_date": "2022-10-28T00:00:00",
    "value": 573.9500000000007
  },
  {
    "meter_date": "2022-10-29T00:00:00",
    "value": 551.9799999999996
  }
]
```
### Query for monthly
```bash
curl -X 'GET' \
  'http://127.0.0.1:8000/api/v1/meter/usage?date=2022-10-26&period=monthly&skip=0&limit=100' \
  -H 'accept: application/json'
```
Result:
```json
[
  {
    "meter_date": "2022-10-12T00:00:00",
    "value": 539.76
  },
  {
    "meter_date": "2022-10-13T00:00:00",
    "value": 571.9000000000001
  },
  {
    "meter_date": "2022-10-14T00:00:00",
    "value": 558.7499999999998
  },
  {
    "meter_date": "2022-10-15T00:00:00",
    "value": 547.8400000000001
  },
  {
    "meter_date": "2022-10-16T00:00:00",
    "value": 390.27
  },
  {
    "meter_date": "2022-10-17T00:00:00",
    "value": 490.44000000000005
  },
  {
    "meter_date": "2022-10-18T00:00:00",
    "value": 530.9000000000001
  },
  {
    "meter_date": "2022-10-19T00:00:00",
    "value": 530.7199999999993
  },
  {
    "meter_date": "2022-10-20T00:00:00",
    "value": 530.5699999999997
  },
  {
    "meter_date": "2022-10-21T00:00:00",
    "value": 573.9500000000007
  },
  {
    "meter_date": "2022-10-22T00:00:00",
    "value": 534.4200000000001
  },
  {
    "meter_date": "2022-10-23T00:00:00",
    "value": 393.9500000000007
  },
  {
    "meter_date": "2022-10-24T00:00:00",
    "value": 571.71
  },
  {
    "meter_date": "2022-10-25T00:00:00",
    "value": 616.8000000000002
  },
  {
    "meter_date": "2022-10-26T00:00:00",
    "value": 586.0499999999993
  },
  {
    "meter_date": "2022-10-27T00:00:00",
    "value": 592.6800000000003
  },
  {
    "meter_date": "2022-10-28T00:00:00",
    "value": 573.9500000000007
  },
  {
    "meter_date": "2022-10-29T00:00:00",
    "value": 551.9799999999996
  },
  {
    "meter_date": "2022-10-30T00:00:00",
    "value": 433.6800000000003
  }
]
```
