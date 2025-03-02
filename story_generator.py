import streamlit as st
import random

def run():
    # Title and Description
    st.title("📚 Magical Story Generator")
    st.markdown("""
        Create your own magical tale by providing a character name, setting, and mood!  
        Watch as your story unfolds with beautiful visuals.
    """)

    # Input Section
    st.subheader("📝 Customize Your Story")
    col1, col2 = st.columns(2)  # Two-column layout for inputs

    with col1:
        character = st.text_input("Enter a character name:", placeholder="e.g., Alice")

    with col2:
        setting = st.selectbox("Choose a setting:", ["Forest", "City", "Beach", "Space"])

    mood = st.radio("Choose a mood:", ["Happy", "Mysterious", "Scary", "Funny"], horizontal=True)

    # Generate Story Button
    if st.button("✨ Generate Story ✨"):
        if character.strip():  # Check if the character name is not empty
            # Generate a dynamic story based on inputs
            story = f"""
            Once upon a time, there was a brave adventurer named **{character}**.  
            They found themselves in a **{setting}**, surrounded by **{mood.lower()}** vibes.  
            As they explored, they discovered something incredible...  
            
            - In the **{setting}**, {character} met a wise old guide who gave them a magical map.  
            - The map glowed under the light of the moon, revealing secrets hidden for centuries.  
            - With courage and determination, {character} embarked on an unforgettable journey.  
            """

            # Display the Generated Story
            st.subheader("📖 Your Magical Tale:")
            st.write(story)

            # Add an Image Based on the Setting
            if setting == "Forest":
                st.image(
                    "https://media.istockphoto.com/id/1005927988/vector/fantasy-land-grass-and-hill-river-and-tree-with-fantastic-realistic-style.jpg?s=612x612&w=0&k=20&c=wckpkHjKc9TZweV_Zcm9oijL5c7WgHIRpnnBjKZnSrs=",
                    caption="A mystical forest with fantasy elements",
                    use_container_width=True
                )
            elif setting == "City":
                st.image(
                    "https://static.vecteezy.com/system/resources/previews/037/046/026/non_2x/road-to-city-landscape-illustration-nature-highway-through-meadow-and-trees-to-city-cartoon-background-vector.jpg",
                    use_container_width=True
                )
            elif setting == "Beach":
                st.image(
                    "https://www.shutterstock.com/image-vector/tropical-beach-landscape-chair-umbrella-600nw-2158237845.jpg",
                    use_container_width=True
                )
            elif setting == "Space":
                st.image(
                    "https://media.istockphoto.com/id/651332068/vector/vector-flat-cosmos-design-background.jpg?s=612x612&w=0&k=20&c=FU1ZvdzsXR2mCilWUACty-5FIZIJO46JVPkGz89NuGI=",
                    caption="The vastness of space",
                    use_container_width=True
                )

        else:
            st.error("Please enter a character name to generate your story!")

# Run the app
if __name__ == "__main__":
    run()