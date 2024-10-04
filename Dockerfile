FROM spark:python3
LABEL authors="anjacobs"

WORKDIR .
COPY app.py .
EXPOSE 8080 4040
CMD ["/opt/spark/bin/spark-submit", "--master", "local", "app.py"]