# TourRecommender
This is simply a project that intends to create a recommender application for tourists and travelers who want to visit hotels, restaurants, stores, etc...and find the right stuff to purchase in those places 

The recommender application will consists of four parts:

## The frontend/user interface
This is where the profiled user will include his details.
It is also where recommendations will appear for him to view.

## The recommender model
The model is a statistical or ML model that is trained to collect data from the location, and filter out what information is relevant to the user.

## The API
I will use FastAPI to connect both ends. The fitted model will instruct the API on what information from the backend to feed onto the frontend.

## The backend/database
The database will contain tables that house information about nearby locations, stores, products. I will use a graph algorithm to map locations, and a binary tree algorithm to structure how the model extracts what places to go, and what products to find.

