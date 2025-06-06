import streamlit as st
import random

# Restaurant Categories
restaurants = {
    "Mexican": ["Soccer Taco", "Don Gallo", "Salsaritas", "Las Fuentes", "Taco Bell", "Chivo", "El Mez", "Cancun", "Amigos", "Chuys", "Moes", "Babalu", "Zalate"],
    "Italian": ["Blaze Pizza", "Olive Garden", "Carabbas", "Altrudas", "A dopo"],
    "American": ["Cookout", "Wingstop", "Chilis", "Stock & Barrel", "Southern Grit", "Double Dogs", "Chick-Fil-A", "Jimmy Johns", "Jersey Mikes", "Firebirds", "Connors", "Waffle House", "Zaxbys", "Longhorn", "McDonalds", "Hot Birds", "McAlisters", "Drakes", "Checkers"],
    "Asian": ["Kabuki", "Panda Express", "Wasabi", "PF Changs", "Fin-Two", "Wok Chow", "Nama", "Chaiyo", "Hungry Sumo", "Q Korean Steakhouse", "KOKO"],
    "Fast Food": ["McDonalds", "Chick-Fil-A", "Taco Bell", "Jimmy Johns", "Zaxbys", "Cookout", "Panda Express", "Wingstop", "Blaze", "Salsaritas", "Checkers", "Sonic"],
    "Breakfast": ["First Watch", "Maple Street Biscuit Company", "Waffle House", "Frothy Monkey", "Panera", "Red Bud", "Petes", "Chick-Fil-A", "Cracker Barrel", "Dunkin Donuts", "Aretha Frankensteins"],
    "Fancy": ["Connors", "Firebirds", "Lonesome Dove", "Melting Pot", "PF Changs", "Cheesecake Factory", "Brass Pearl", "Kefi", "Chesapeakes", "Babalu", "The Kennedy", "Cafe 4", "Tuplo Honey", "Elkmont Station", "Vida"]
}

# Dynamically create "Everything" category
restaurants["Everything"] = list(set(restaurant for category in restaurants.values() for restaurant in category))

# Streamlit App Interface
st.title("🍽️ Where Should We Eat?")

# Dropdown for category selection
category = st.selectbox(
    "Choose a cuisine type:",
    options=list(restaurants.keys())
)

# Button to generate a random restaurant
if st.button("Decide for Me!"):
    random_choice = random.choice(restaurants[category])
    st.success(f"You guys should go to **{random_choice}**!")

# Footer
st.caption("Helping Bugs Decide Where to Eat Since 2025 ❤️")
