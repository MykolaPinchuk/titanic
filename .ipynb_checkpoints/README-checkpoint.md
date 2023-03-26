# This is a project to predict Titanic passenger survival.

I build a simple random forest model and deploy it on GCP via AppEngine. Model is served via Flask web-app. Prediction of 1 means survival. This repo contains everything needed to build and deploy such a model. This process will take 2-4 minutes. To do this, follow the steps below:

1. Clone this repo.
2. Cd into titanic-app.
3. gcloud init
4. gcloud app deploy
5. follow the link, shown in the console after the previous command to verify that webapp works.