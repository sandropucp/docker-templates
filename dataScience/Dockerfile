#Use the latest ubuntu image
FROM ubuntu:latest

# Author
LABEL author="Sandro Sanchez"

# Run a system update and install python
RUN apt-get update && apt-get install -y python3 \
    python3-pip

# Install jupyter
RUN pip3 install jupyter

# Install Numpy
RUN pip3 install numpy

# Install Pandas
RUN pip3 install pandas

# Install Statsmodel
RUN pip3 install statsmodels

# Install Matplot lib
RUN pip3 install matplotlib

# Install Plotly
RUN pip3 install plotly

# Install Seaborn
RUN pip3 install seaborn

# Install Sklearn
RUN pip3 install scikit-learn

# Install Tensorflow
RUN pip3 install tensorflow

# Create a new system user
RUN useradd -ms /bin/bash jupyter

# Change to this new user
USER jupyter

# Set the container working directory to the user home folder
WORKDIR /home/jupyter

# Star the jupyter notebook
ENTRYPOINT ["jupyter", "notebook", "--ip=*"]