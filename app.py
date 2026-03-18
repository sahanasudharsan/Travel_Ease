from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId
import os
from datetime import datetime

app = Flask(__name__)

# Use local MongoDB
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client.travel_ease

# Collections
itineraries = db.itineraries
memories = db.memories

@app.route('/')
def index():
    # Popular destinations mock data
    destinations = [
        {"name": "Paris, France", "image": "https://images.unsplash.com/photo-1499856871958-5b9627545d1a?auto=format&fit=crop&q=80&w=600", "desc": "The City of Light awaits your discovery."},
        {"name": "Kyoto, Japan", "image": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?auto=format&fit=crop&q=80&w=600", "desc": "Experience traditional temples and serene gardens."},
        {"name": "Santorini, Greece", "image": "https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?auto=format&fit=crop&q=80&w=600", "desc": "Stunning sunsets and iconic whitewashed houses."},
        {"name": "Bali, Indonesia", "image": "https://images.unsplash.com/photo-1537996194471-e657df975ab4?auto=format&fit=crop&q=80&w=600", "desc": "A tropical paradise perfectly suited for relaxation."}
    ]
    return render_template('index.html', destinations=destinations)

@app.route('/itinerary')
def itinerary():
    all_itineraries = list(itineraries.find().sort("date", 1))
    return render_template('itinerary.html', itineraries=all_itineraries)

@app.route('/add_itinerary', methods=['POST'])
def add_itinerary():
    title = request.form.get('title')
    location = request.form.get('location')
    date = request.form.get('date')
    notes = request.form.get('notes')
    
    if title and location and date:
        itineraries.insert_one({
            "title": title,
            "location": location,
            "date": date,
            "notes": notes,
            "created_at": datetime.now()
        })
    return redirect(url_for('itinerary'))

@app.route('/delete_itinerary/<id>')
def delete_itinerary(id):
    itineraries.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('itinerary'))

@app.route('/memories')
def memories_page():
    all_memories = list(memories.find().sort("date", -1))
    return render_template('memories.html', memories=all_memories)

@app.route('/add_memory', methods=['POST'])
def add_memory():
    title = request.form.get('title')
    location = request.form.get('location')
    date = request.form.get('date')
    description = request.form.get('description')
    
    if title and location:
        memories.insert_one({
            "title": title,
            "location": location,
            "date": date,
            "description": description,
            "created_at": datetime.now()
        })
    return redirect(url_for('memories_page'))

@app.route('/delete_memory/<id>')
def delete_memory(id):
    memories.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('memories_page'))

if __name__ == '__main__':
    app.run(debug=True)
