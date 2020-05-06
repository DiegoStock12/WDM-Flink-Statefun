FROM flink-statefun:2.0.0

RUN mkdir -p /opt/statefun/modules/test
ADD module.yaml /opt/statefun/modules/test