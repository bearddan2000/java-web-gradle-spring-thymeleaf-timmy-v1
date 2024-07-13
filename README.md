# java-web-gradle-spring-thymeleaf-timmy-v1

## Description
This is a school requested web based report, which is sent via email and saved to google drive.

The email uses rich text to organize and provide links to files on the google drive. 

## Tech description
Requirements for the report are found on the pdf file: *timmy.pdf*, additional feature were added for learning purposes.

Each web page is saved as an image then inserted into a pdf file. The web page endpoint and pdf file name is derived
from `py-api-srv`.

## Tech stack
- java
    - spring
    - thymeleaf
- python
    - flask
        - cors
        - requests

## Docker stack
- gradle:jdk11
- python:latest
- ubuntu:22.04

## To run
`sudo ./install.sh -u`

## To stop
`sudo ./install.sh -d`

## For help
`sudo ./install.sh -h`
