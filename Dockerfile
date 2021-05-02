# python3.8 lambda base image
FROM public.ecr.aws/lambda/python:3.8
FROM jenkins/jenkins:lts
FROM jenkins/jenkins:2.277.2-lts-jdk11

MAINTAINER wasim bagwan <wasimbagwan55@gmail.com>


COPY --chown=jenkins:jenkins executors.groovy /usr/share/jenkins/ref/init.groovy.d/executors.groovy

COPY lambda_function.py ./

# Overwrite the command by providing a different command directly in the template.
CMD ["lambda_function.lambda_handler"]