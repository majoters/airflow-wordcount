#FROM apache/airflow:2.7.1-python3.12
FROM apache/airflow:2.10.3-python3.12

USER root
#RUN apt-get update && \
#    apt-get install -y gcc python3-dev openjdk-11-jdk && \
#    apt-get clean
RUN apt-get update && \
apt-get install -y openjdk-17-jdk && \
apt-get clean && \
rm -rf /var/lib/apt/lists/*

# Set JAVA_HOME environment variable
ENV JAVA_HOME /usr/lib/jvm/java-17-openjdk-arm64

USER airflow

RUN pip install apache-airflow==2.10.3 \
    apache-airflow-providers-apache-spark \
    apache-airflow-providers-openlineage==1.13.0 \
    pyspark