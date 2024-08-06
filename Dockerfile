#Stage 1:Build Frontend
FROM node:18 as build-stage

WORKDIR /code

COPY ./Frontend/ecommerce_inventory/ /code/Frontend/ecommerce_inventory/

WORKDIR /code/Frontend/ecommerce_inventory

#Installing Packages
RUN npm install

#Building Frontend
RUN npm run build

# Stage 2:Build Backend
FROM python:3.11.0

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

# Copy django project to container
COPY ./Backend/EcommerceInventory/ /code/Backend/EcommerceInventory/

# Install requirements
RUN pip install -r Backend/EcommerceInventory/requirements.txt

# Copy static files
COPY --from=build-stage ./code/Frontend/ecommerce_inventory/build /code/Backend/EcommerceInventory/static/
COPY --from=build-stage ./code/Frontend/ecommerce_inventory/build/static /code/Backend/EcommerceInventory/static/
COPY --from=build-stage ./code/Frontend/ecommerce_inventory/build/index.html /code/Backend/EcommerceInventory/EcommerceInventory/templates/index.html/

# Run django management commands
RUN python ./Backend/EcommerceInventory/manage.py migrate

# Run django collectstatic command
RUN python ./Backend/EcommerceInventory/manage.py collectstatic --no-input

# expose port
EXPOSE 80

WORKDIR /code/Backend/EcommerceInventory

# Run django server
CMD ["gunicon", "EcommerceInventory.wsgi:application", "--bind", "0.0.0.0:8000"]