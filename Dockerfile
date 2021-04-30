# python3.8 lambda base image
FROM public.ecr.aws/lambda/python:3.8

COPY lambda_function.py ./

# Overwrite the command by providing a different command directly in the template.
CMD ["lambda_function.lambda_handler"]