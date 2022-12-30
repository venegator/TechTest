#This dockerfile applies multi-stage pattern to build the final image.
FROM debian:11-slim AS builder
RUN apt-get update && \
    apt-get install --no-install-suggests --no-install-recommends --yes python3-venv gcc libpython3-dev && \
    python3 -m venv /venv && \
    /venv/bin/pip install --upgrade pip setuptools wheel && \
    rm -rf /var/lib/apt/lists/*

# Creating another stage for python virtualenv building. This step will only be executed when changes to requirements.txt are applied.
FROM builder AS builder-venv
COPY requirements.txt /requirements.txt
RUN /venv/bin/pip install --disable-pip-version-check -r /requirements.txt

# Last stage is to use a python distroless image and copy the created virtualenv and application to get a minimal image.
FROM gcr.io/distroless/python3-debian11
COPY --from=builder-venv /venv /venv
COPY getweather.py /app
WORKDIR /app
ENTRYPOINT ["/venv/bin/python3", "getweather.py"]