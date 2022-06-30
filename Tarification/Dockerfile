FROM python:3.10
ADD main.py .
RUN pip install requests beautifulsoup4


RUN pip install -r requirements.txt
CMD ["python", "-m", "unittest", "discover", "-s" ,"Tests"]