# WDM-Flink-Statefun
Instructions for getting the Apache Flink Docker container:
* `git clone https://github.com/apache/flink-statefun-docker`
* `cd 2.0.0`
* `docker build -t flink-statefun:2.0.0 .`

Run the whole demo:
* `docker-compose up`

Rebuild single container:
* `docker-compose up -d --no-deps --build <service-name>`

# Ask Asterios

* How do we scale the Flink side -> not just duplicating containers, need to share state as well -> how to configure and define this in Kubernetes?
* What about the replies -> should be non-blocking -> save ID per request and listen on an reply output topic?
