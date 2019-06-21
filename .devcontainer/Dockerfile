#-------------------------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See https://go.microsoft.com/fwlink/?linkid=2090316 for license information.
#-------------------------------------------------------------------------------------------------------------

FROM continuumio/miniconda3

# ENTRYPOINT [ "/bin/bash", "-c" ]
# Install git, process tools
RUN apt-get update && apt-get -y install git procps

RUN mkdir /workspace
WORKDIR /workspace

# Install pylint
# RUN pip install pylint

# Install Python dependencies from requirements.txt if it exists
# COPY .devcontainer/environment.yml.temp environment.yml* /workspace/
# RUN if [ -f "environment.yml" ]; then conda env update base -f environment.yml && rm environment.yml*; fi
COPY environment.yml tmp/environment.yml
RUN ["/bin/bash", "-c", "conda update --all"]
RUN ["/bin/bash", "-c", "conda env update -f tmp/environment.yml"]
RUN ["/bin/bash", "-c", "conda env list"]

RUN ["/bin/bash", "-c", "echo 'source activate nlp' > ~/.bashrc"]
RUN ["/bin/bash", "-c", "source activate nlp"]

# CMD ["python -m spacy download en_core_web_sm"]

# Clean up
RUN apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

# Set the default shell to bash instead of sh
ENV SHELL /bin/bash

