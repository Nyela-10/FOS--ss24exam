from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Sample mental health tips for each mood
mental_health_tips = {
    "Good": [
        "Practice gratitude daily.",
        "Engage in physical activity.",
        "Connect with loved ones."
    ],
    "Moderate": [
        "Take short breaks throughout the day.",
        "Practice deep breathing exercises.",
        "Engage in a hobby you enjoy."
    ],
    "Below Average": [
        "Seek professional help if needed.",
        "Practice self-compassion.",
        "Set small achievable goals."
    ]
}
