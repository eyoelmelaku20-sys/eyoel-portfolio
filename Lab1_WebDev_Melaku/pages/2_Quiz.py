"""
Georgia Tech - CS1301
Web Dev Lab - Part 2: Interactive Quiz
Quiz Topic: What Type of Pizza Are You?
"""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "..", "Images") 
import streamlit as st
 
# ------------------------------------------------------------
# Page setup
# ------------------------------------------------------------
st.title("🍕 What Type of Pizza Are You?")
st.write("Answer these 5 questions to find out your pizza match!")
 
# first image - just a fun pizza pic to kick off the quiz
st.image(os.path.join(IMAGE_DIR, "pizza_pepp.jpg"), caption="Let's begin!")
 
# this list will hold one letter (A, B, C, or D) for every question I answer
# at the end, I check which letter shows up the most to decide my result
answers = []
 
# ------------------------------------------------------------
# Question 1 - Multiple Choice (st.radio)
# only lets the user pick ONE option out of the list
# ------------------------------------------------------------
st.subheader("1. Friday night, you'd rather be...")
q1 = st.radio("Choose one:", ["Watching a movie", "At a party", "Studying", "Trying something new"])
 
# depending on which option they picked, add the matching letter to my list
if q1 == "Watching a movie":
    answers.append("A")  # A = Margherita
elif q1 == "At a party":
    answers.append("B")  # B = Classic Pepperoni
elif q1 == "Studying":
    answers.append("C")  # C = Veggie Delight
else:
    answers.append("D")  # D = Hawaiian
 
# ------------------------------------------------------------
# Question 2 - Multi-Select (st.multiselect) #NEW
# this lets the user pick MULTIPLE toppings, not just one
# it's different from st.radio because radio only allows a single choice
# ------------------------------------------------------------
st.subheader("2. Pick your favorite toppings:")
toppings = st.multiselect("Select all that apply:", ["Pepperoni", "Mushrooms", "Pineapple", "Extra Cheese"])
 
# toppings is a LIST of whatever the user checked off
# I just check if certain toppings are "in" that list
if "Pepperoni" in toppings:
    answers.append("B")
elif "Pineapple" in toppings:
    answers.append("D")
elif "Mushrooms" in toppings:
    answers.append("C")
else:
    answers.append("A")  # default if none of the above were picked
 
# second image - shows different topping options
st.image(os.path.join(IMAGE_DIR, "pizza-basil.jpg"), caption="Yum!")
 
# ------------------------------------------------------------
# Question 3 - Number Input (st.number_input)
# lets the user type in a specific number (not just pick from a list)
# ------------------------------------------------------------
st.subheader("3. How many hours did you sleep last night?")
sleep = st.number_input("Hours:", min_value=0, max_value=24, value=7)
 
# less sleep = more likely to want something bold/spicy (Pepperoni)
# more sleep = more relaxed, simple pick (Margherita)
if sleep < 6:
    answers.append("B")
else:
    answers.append("A")
 
# ------------------------------------------------------------
# Question 4 - Slider (st.slider) #NEW
# lets the user drag a bar to pick a number in a range, instead of typing it
# ------------------------------------------------------------
st.subheader("4. Rate your spontaneity (1-10):")
spontaneity = st.slider("Slide to rate:", 1, 10, 5)
 
# higher spontaneity score = more adventurous = Hawaiian (pineapple is a bold choice!)
# lower score = more cautious = Veggie Delight
if spontaneity >= 7:
    answers.append("D")
else:
    answers.append("C")
 
# ------------------------------------------------------------
# Question 5 - Select Box (st.selectbox)
# similar to radio, but shows a dropdown menu instead of buttons
# ------------------------------------------------------------
st.subheader("5. Pick your favorite season:")
season = st.selectbox("Choose one:", ["Spring", "Summer", "Fall", "Winter"])
 
if season == "Summer":
    answers.append("D")
elif season == "Fall":
    answers.append("B")
else:
    answers.append("A")
 
# third image - right before showing the result
st.image(os.path.join(IMAGE_DIR, "pizza-cheese.jpg"), caption="Last step!") 
# ------------------------------------------------------------
# Results section
# ------------------------------------------------------------
# this dictionary connects each letter to its matching pizza type
# so I don't need a giant if/elif chain to print the final answer
results = {
    "A": "Margherita",
    "B": "Classic Pepperoni",
    "C": "Veggie Delight",
    "D": "Hawaiian",
}
 
# the button makes sure results only show up AFTER the user clicks it
# instead of appearing instantly while they're still answering
if st.button("Reveal My Pizza Type!"):
    # set(answers) removes duplicate letters, so I'm only checking each letter once
    # key=answers.count tells max() to pick the letter that appears most often
    winner = max(set(answers), key=answers.count)
 
    st.subheader(f"You are: {results[winner]}! 🎉")
    st.balloons()  # NEW - fun animation to celebrate the result
 
