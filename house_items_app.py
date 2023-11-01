import streamlit as st
import sqlite3

# Create a Streamlit web app
st.title("House Items Management")

# Connect to a SQLite database
conn = sqlite3.connect("house_items.db")
cur = conn.cursor()

# Create a table to store house items if it doesn't exist
cur.execute("""
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY,
        name TEXT,
        category TEXT
    )
""")
conn.commit()

# Function to add an item to the database
def add_item(name, category):
    cur.execute("INSERT INTO items (name, category) VALUES (?, ?)", (name, category))
    conn.commit()

# Function to retrieve items from the database
def get_items():
    cur.execute("SELECT name, category FROM items")
    return cur.fetchall()

# Function to delete an item from the database
def delete_item(name):
    cur.execute("DELETE FROM items WHERE name=?", (name,))
    conn.commit()

# Sidebar to add items
st.sidebar.header("Add Item")
item_name = st.sidebar.text_input("Item Name")
item_category = st.sidebar.selectbox("Category", ["Furniture", "Electronics", "Appliances"])
add_button = st.sidebar.button("Add Item")

# Main content
st.write("## Your House Items")

if add_button and item_name:
    add_item(item_name, item_category)
    st.success(f"Added {item_name} to the {item_category} category!")

items = get_items()
if not items:
    st.write("You have no items in your list.")
else:
    for item in items:
        st.write(f"**{item[0]}** (Category: {item[1]})")
        if st.button(f"Delete {item[0]}"):
            delete_item(item[0])

# Close the database connection
conn.close()
