# RabbitMQ POC

## Install

- Create and activate the virtual environment:

```sh
$ python -m venv venv
$ source ./venv/bin/activate
```

- Install dependencies:

```sh
$ pip install -r ./requirements.txt
```

## How to run

- Start the RabbitMQ

```sh
$ docker-compose -f docker-compose.yml up -d
```

- Subscribe to one of the queues (nse_queue | nyse_queue)

```sh
$ ./src/subscriber.py <QUEUE-NAME> nse.*
$ ./src/subscriber.py nse_queue nse.*
$ ./src/subscriber.py nyse_queue nyse.*
```

- Publish

```sh
$ ./src/producer.py
```

- Spin down the stack

```sh
$ docker-compose -f docker-compose.yml down
```

## References

- https://medium.com/@rahulsamant_2674/python-rabbitmq-8c1c3b79ab3d
