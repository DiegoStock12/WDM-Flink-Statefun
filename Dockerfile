FROM flink-statefun

RUN mkdir -p /opt/statefun/modules/test
ADD module.yaml /opt/statefun/modules/test