FROM flink-statefun:2.0.0

RUN mkdir -p /opt/statefun/modules/test
RUN mdkir -p /opt/statefun/modules/stock

ADD stock_module.yaml /opt/statefun/modules/stock
ADD module.yaml /opt/statefun/modules/test