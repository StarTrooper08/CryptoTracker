# CrytoTracker Application


**Development Process**
1. Created Empty repository on github
2. Clone it locallly
3. Changed directory to project folder
![part](https://user-images.githubusercontent.com/72031540/205778486-542bde49-8139-444d-94cb-c626e9002ea7.png)

4. Initialize virtual environment
5. Created .gitignore file and added venv path to it because we want to push venv to be pushed to github.
6. installed required python libraries using pip install
![part1](https://user-images.githubusercontent.com/72031540/205778686-f1aad03a-6e34-4df0-a0fd-f390c6e0fb00.png)
7. created app.py
   > touch app.py
8. Code 
```python

#import libs

import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px
from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta

crypto_mapping = {"Bitcoin":"BTC-USD","Ethereum":"ETH-USD"}


#streamlit app title

st.title("Crypto Tracker")
st.image("header.png", width=900)

#sidebar
crypto_option = st.sidebar.selectbox(
    "Which Crypto currency do you want to visualize?",("Bitcoin","Ethereum")
)

#start and end date for tracking value
start_date = st.sidebar.date_input("Start Date", date.today() - relativedelta(month=1))
end_date = st.sidebar.date_input("End Date", date.today())


data_interval = st.sidebar.selectbox(

"Data Interval",
{
    "1m",
    "2m",
    "5m",
    "15m",
    "30m",
    "60m",
    "90m",
    "1h",
    "1d",
    "5d",
    "1wk",
    "1mo",
    "3mo",
},

)

symbol_crypto = crypto_mapping[crypto_option]

data_crypto = yf.Ticker(symbol_crypto)

value_selector = st.sidebar.selectbox(
    "Value Selector", ("Open","High","Low","Close","Volume")
)

if st.sidebar.button("Generate"):
    crypto_hist = data_crypto.history(
        start=start_date, end=end_date, interval=data_interval
    )

    fig = px.line(crypto_hist,
    x = crypto_hist.index,y=value_selector,
    labels={"x":"Date"})
    st.plotly_chart(fig)
```
> First imported libraries then created titile of web app and sidebar for our app using streamlit, used crypto price data from yfinance library, and plotted it using plotly library 
9. Created requirements.txt file and mentioned required/used libraries. So that we can easily install only required libs for this app docker image.
10. Created Dockerfile and configured it for our web app.
```Dockerfile
FROM python:3.9-slim
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 8501
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```
11. Build Docker Image Locally
![part2](https://user-images.githubusercontent.com/72031540/205784546-28305784-5ce0-4b30-8258-4077b7b84b6a.png)
12. Tested Docker Image locally whether its running properly or not.
![part3](https://user-images.githubusercontent.com/72031540/205784715-26062af4-c8b5-4661-8bb7-ff9a76f0a1de.png)
13. Used dockerslim to minimize docker size and find Vulnerabilities
14. Tested slimmed image created using dockerslim running properly locally or not.
15. Created Repository on Dockerhub so that we can push our image to it.
16. Created Github actions CI/CD which will build and push docker image to our dockerhub registry automatically after every git commit on our main branch.
```yaml
name: Build and Push Docker Image to Docker Hub

on:
  push:
    branches: ['main']

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Log in to Docker Hub
        uses: docker/login-action@28218f9b04b4f3f62068d7b6ce6ca5b26e35336c
        with:
          username: ${{ secrets.DOCKER_USER }}
          password: ${{ secrets.DOCKER_PASS }}

      - name: Build the Docker image
        run: docker build . --file Dockerfile --tag ${{ secrets.DOCKER_USER }}/cryptotracker

      - name: Docker Push
        run: docker push ${{ secrets.DOCKER_USER }}/cryptotracker
```
![Screenshot1](https://user-images.githubusercontent.com/72031540/205791194-19073214-5a63-46df-9b3c-0a448ebc4219.png)
![Screenshot from 2022-12-06 07-15-37](https://user-images.githubusercontent.com/72031540/205791291-eb8db791-5e1a-48af-9370-2be70bc04bf4.png)

17. Added Docker Image to Slim.ai collection. And started process of hardening and optimizing docker image.
![Screenshot from 2022-12-06 07-17-19](https://user-images.githubusercontent.com/72031540/205791476-890d0436-1422-4513-a31b-a57fc48b205b.png)
![Screenshot from 2022-12-06 07-18-00](https://user-images.githubusercontent.com/72031540/205791561-d368ec16-6782-44bf-b7e7-0596a95dc666.png)
![Screenshot from 2022-12-06 07-18-44](https://user-images.githubusercontent.com/72031540/205791583-0bdf985b-ba9a-4aac-8d49-9e67409b28b3.png)
![Screenshot from 2022-12-06 07-21-00](https://user-images.githubusercontent.com/72031540/205791614-9e4d9a8e-0352-40b3-9a2b-189ebee2d722.png)
![Screenshot from 2022-12-06 07-21-21](https://user-images.githubusercontent.com/72031540/205791638-981ad379-d0ca-4e6c-aea7-de8641c14430.png)
![Screenshot from 2022-12-06 07-22-18](https://user-images.githubusercontent.com/72031540/205791743-2e647b61-9b07-467f-9884-57747be69f2c.png)
![Screenshot from 2022-12-06 07-22-51](https://user-images.githubusercontent.com/72031540/205791783-61379f28-1284-4f4f-a842-46896381c38f.png)
![Screenshot from 2022-12-06 07-23-11](https://user-images.githubusercontent.com/72031540/205791827-7f4d66f4-ce9e-4844-9a92-6f141553e4c6.png)
![Screenshot from 2022-12-06 07-24-04](https://user-images.githubusercontent.com/72031540/205791854-2e54e90c-118a-4633-89f1-2c1659106aac.png)
![Screenshot from 2022-12-06 07-24-19](https://user-images.githubusercontent.com/72031540/205791871-41a7d7bb-3107-4e02-a371-36b17b64cf2c.png)
![Screenshot from 2022-12-06 07-24-54](https://user-images.githubusercontent.com/72031540/205791888-31a30a16-7c6f-4ebd-83e7-e1e408a42ae9.png)


18. Hardened and optimized the Image using Slim.ai
![Screenshot from 2022-12-06 07-29-12](https://user-images.githubusercontent.com/72031540/205791920-11077be4-782f-4cb5-8fb2-48aabb6923ac.png)
19. And Done with the development process .Thank you :)


Slim.ai Collection for this app:
https://portal.slim.dev/collections/rkcol.2IW3VKKwp1eRIr4TbV4E2Armuzn

**Installation for setting up app Locally**
1. Fork this repository
2. clone the repo locally
  ``` git clone https://github.com/StarTrooper08/CryptoTracker.git```
3. cd CryptoTracker
4. python3 -m venv venv
5. pip install -r requirements.txt
6. streamlit run app.py


You can also pull image directly using docker or slimai
```cmd
docker pull atharvas08/cryptotracker
```
