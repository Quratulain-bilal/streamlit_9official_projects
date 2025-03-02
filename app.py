import streamlit as st

# Import all project modules
import bmi_calculator
import password_generator
import hangman_game
import number_guessing_game
import health_dashboard
import expense_tracker
import story_generator
import computer_guessing_game
import rock_paper_scissors
import sir_form

# Set page configuration for wide layout and custom title
st.set_page_config(
    page_title="Python Projects Hub",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling (Light Theme)
st.markdown("""
    <style>
        /* General light theme */
        body {
            background-color: #f9f9f9;
            color: #333333;
            font-size: 18px;
        }

        /* Header and Footer */
        .header, .footer {
            background-color: #ffffff;
            padding: 20px;
            text-align: center;
            border-radius: 10px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        .footer a {
            color: #007BFF;
            text-decoration: none;
        }

        .footer a:hover {
            text-decoration: underline;
        }

        /* Sidebar styling */
        .sidebar .sidebar-content {
            width: 250px !important;
            background-color: #ffffff;
            color: #333333;
            box-shadow: 2px 0 6px rgba(0, 0, 0, 0.1);
        }

        /* Section headers in sidebar */
        .sidebar h3 {
            color: #007BFF; /* Blue for headers */
            font-weight: bold;
            margin-top: 20px;
            margin-bottom: 10px;
        }

        /* Divider lines in sidebar */
        .sidebar hr {
            border: none;
            border-top: 1px solid #007BFF;
            margin: 15px 0;
        }

        /* Main content area */
        .main .block-container {
            background-color: #ffffff;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        /* Buttons */
        .stButton > button {
            background-color: #007BFF;
            color: #ffffff;
            border-radius: 8px;
            font-size: 18px;
            padding: 10px 20px;
            border: none;
        }

        .stButton > button:hover {
            background-color: #0056b3;
        }

        /* Input fields */
        .stTextInput > div > div > input,
        .stNumberInput > div > div > input {
            background-color: #f0f0f0;
            color: #333333;
            border: 1px solid #007BFF;
            border-radius: 8px;
            font-size: 18px;
        }

        /* Cards for main content */
        .card {
            background-color: #ffffff;
            border: 1px solid #007BFF;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown("""
    <div class="header">
        <h1>🌟 Python Projects Hub 🌟</h1>
        <p>Explore exciting Python projects built using Streamlit!</p>
    </div>
""", unsafe_allow_html=True)

# Navigation Menu (Sidebar)
st.sidebar.markdown("### 🚀 Navigation")
page = st.sidebar.radio("Go to:", [
    "🏠 Home",
    "📊 BMI Calculator",
    "🔒 Password Generator",
    "🎮 Hangman Game",
    "🔢 Number Guessing Game",
    "🩺 Health Dashboard",
    "💰 Expense Tracker",
    "📖 Story Generator",
    "🤖 Computer Guessing Game",
    "✌️ Rock-Paper-Scissors",
    "📝 Sir's Form",
    "📚 View Code",
    "☁️ Use Google Colab"
])

# Footer Section
st.markdown("""
    <div class="footer">
        <p>Developed with ❤️ by <a href="https://github.com" target="_blank">Your GitHub Profile</a></p>
    </div>
""", unsafe_allow_html=True)

# Main Content Area
if page == "🏠 Home":
    st.markdown("""
        <div class="card">
            <h2>Welcome to the Python Projects Hub!</h2>
            <p>This app is a collection of **exciting Python projects** built using Streamlit. Explore each project using the sidebar:</p>
            <ul>
                <li><strong>📊 BMI Calculator</strong>: Track your health metrics.</li>
                <li><strong>🔒 Password Generator</strong>: Create secure passwords.</li>
                <li><strong>🎮 Hangman Game</strong>: Play a fun word-guessing game.</li>
                <li><strong>🔢 Number Guessing Game</strong>: Test your guessing skills.</li>
                <li><strong>🩺 Health Dashboard</strong>: Stay fit with calorie and hydration tracking.</li>
                <li><strong>💰 Expense Tracker</strong>: Manage your finances.</li>
                <li><strong>📖 Story Generator</strong>: Create magical tales.</li>
                <li><strong>🤖 Computer Guessing Game</strong>: Let the computer guess your number.</li>
                <li><strong>📝 Sir's Form</strong>: Submit your details for feedback.</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

# BMI Calculator
elif page == "📊 BMI Calculator":
    bmi_calculator.run()

# Password Generator
elif page == "🔒 Password Generator":
    password_generator.run()

# Hangman Game
elif page == "🎮 Hangman Game":
    hangman_game.run()

# Number Guessing Game
elif page == "🔢 Number Guessing Game":
    number_guessing_game.run()

# Health Dashboard
elif page == "🩺 Health Dashboard":
    health_dashboard.run()

# Expense Tracker
elif page == "💰 Expense Tracker":
    expense_tracker.run()

# Story Generator
elif page == "📖 Story Generator":
    story_generator.run()

# Computer Guessing Game
elif page == "🤖 Computer Guessing Game":
    computer_guessing_game.run()

# Rock-Paper-Scissors
elif page == "✌️ Rock-Paper-Scissors":
    rock_paper_scissors.run()

# Sir's Form
elif page == "📝 Sir's Form":
    sir_form.run()

# View Code
elif page == "📚 View Code":
    st.title("📚 View Project Code")
    st.markdown("Select a project to view its source code:")

    # Dropdown to select project
    project = st.selectbox("Choose a project:", [
        "📊 BMI Calculator",
        "🔒 Password Generator",
        "🎮 Hangman Game",
        "🔢 Number Guessing Game",
        "🩺 Health Dashboard",
        "💰 Expense Tracker",
        "📖 Story Generator",
        "🤖 Computer Guessing Game",
        "✌️ Rock-Paper-Scissors",
        "📝 Sir's Form"
    ])

    # Display code based on selection
    if project.startswith("📊"):
        try:
            with open("bmi_calculator.py", "r", encoding="utf-8") as file:
                code = file.read()
            st.code(code, language="python")
        except Exception as e:
            st.error(f"Error: Unable to read the file. Details: {e}")

    elif project.startswith("🔒"):
        try:
            with open("password_generator.py", "r", encoding="utf-8") as file:
                code = file.read()
            st.code(code, language="python")
        except Exception as e:
            st.error(f"Error: Unable to read the file. Details: {e}")

    elif project.startswith("🎮"):
        try:
            with open("hangman_game.py", "r", encoding="utf-8") as file:
                code = file.read()
            st.code(code, language="python")
        except Exception as e:
            st.error(f"Error: Unable to read the file. Details: {e}")

    elif project.startswith("🔢"):
        try:
            with open("number_guessing_game.py", "r", encoding="utf-8") as file:
                code = file.read()
            st.code(code, language="python")
        except Exception as e:
            st.error(f"Error: Unable to read the file. Details: {e}")

    elif project.startswith("🩺"):
        try:
            with open("health_dashboard.py", "r", encoding="utf-8") as file:
                code = file.read()
            st.code(code, language="python")
        except Exception as e:
            st.error(f"Error: Unable to read the file. Details: {e}")

    elif project.startswith("💰"):
        try:
            with open("expense_tracker.py", "r", encoding="utf-8") as file:
                code = file.read()
            st.code(code, language="python")
        except Exception as e:
            st.error(f"Error: Unable to read the file. Details: {e}")

    elif project.startswith("📖"):
        try:
            with open("story_generator.py", "r", encoding="utf-8") as file:
                code = file.read()
            st.code(code, language="python")
        except Exception as e:
            st.error(f"Error: Unable to read the file. Details: {e}")

    elif project.startswith("🤖"):
        try:
            with open("computer_guessing_game.py", "r", encoding="utf-8") as file:
                code = file.read()
            st.code(code, language="python")
        except Exception as e:
            st.error(f"Error: Unable to read the file. Details: {e}")

    elif project.startswith("✌️"):
        try:
            with open("rock_paper_scissors.py", "r", encoding="utf-8") as file:
                code = file.read()
            st.code(code, language="python")
        except Exception as e:
            st.error(f"Error: Unable to read the file. Details: {e}")

    elif project.startswith("📝"):
        try:
            with open("sir_form.py", "r", encoding="utf-8") as file:
                code = file.read()
            st.code(code, language="python")
        except Exception as e:
            st.error(f"Error: Unable to read the file. Details: {e}")

# Use Google Colab
elif page == "☁️ Use Google Colab":
    st.title("☁️ How to Use Google Colab for Your Projects")
    st.markdown("""
        Follow these steps to write, save, and share your Streamlit app using Google Colab:
    """)

    # Step 1: Write Code in Google Colab
    st.subheader("📝 Step 1: Write Your Code in Google Colab")
    st.markdown("""
        1. Open Google Colab by clicking the link below:
           [Open Google Colab](https://colab.research.google.com/)
        2. Create a new notebook by clicking **File > New Notebook**.
        3. Write your Python code in the cells provided. For example:
           ```python
           import streamlit as st

           st.title("Hello, World!")
           st.write("This is my first Streamlit app!")
           ```
        4. Save your notebook by clicking **File > Save** or pressing `Ctrl + S`.
    """)

    # Add YouTube Video Tutorial
    st.subheader("🎥 Beginner's Guide to Google Colab")
    st.markdown("""
        If you're new to Google Colab, watch this beginner-friendly video tutorial:
    """)
    st.video("https://www.youtube.com/watch?v=inN8seMm7UI")  # Replace with an appropriate beginner video

    # Step 2: Save Files Locally
    st.subheader("💾 Step 2: Save Your Files Locally")
    st.markdown("""
        1. To save your files permanently, download them from Google Colab:
           - Click on the **"Files"** tab in the left sidebar.
           - Right-click on the file you want to save and select **"Download"**.
        2. Organize your files into a folder on your computer. Example:
           ```
           my_streamlit_app/
           │
           ├── app.py
           ├── bmi_calculator.py
           ├── password_generator.py
           └── requirements.txt
           ```
    """)

    # Step 3: Upload Files to GitHub
    st.subheader("🌐 Step 3: Upload Your Files to GitHub")
    st.markdown("""
        1. Go to [GitHub](https://github.com/) and create an account if you don't already have one.
        2. Create a new repository by clicking the **"New"** button.
        3. Give your repository a name (e.g., `my-streamlit-app`) and click **"Create Repository"**.
        4. Upload your files to GitHub:
           - Drag and drop your files into the repository.
           - Or use the **"Add File"** button to upload files manually.
        5. Commit your changes by clicking **"Commit Changes"**.
        6. Share your GitHub repository link with others so they can access your code.
    """)

    # Step 4: Run Streamlit App
    st.subheader("🚀 Step 4: Run Your Streamlit App on Google Colab")
    st.markdown("""
        1. Install the required libraries by running this command in a code cell:
           ```bash
           !pip install streamlit pyngrok
           ```
        2. Add the following code to a new code cell and run it:
           ```python
           from pyngrok import ngrok
           import threading
           import os

           # Start Streamlit app in the background
           def run_streamlit():
               os.system("streamlit run app.py")

           threading.Thread(target=run_streamlit).start()

           # Create ngrok tunnel
           public_url = ngrok.connect(port=8501)
           print("Public URL:", public_url)
           ```
        3. After running the above code, you will see a `Public URL` in the output.
        4. Copy and paste this URL into your browser to access your Streamlit app.
    """)

    # Step 5: Access Your App
    st.subheader("🌐 Step 5: Access Your App")
    st.markdown("""
        1. Share the `Public URL` with others to let them use your app.
        2. If you make changes to your code, re-run the cells to update the app.
    """)
