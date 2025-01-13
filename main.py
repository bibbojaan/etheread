    # Import necessary libraries
import cohere
from flask import Flask, render_template, request

api_key = "vx1CvtuvSBj82vPryNJSHxPxITiKmVCrq2eZl69z"
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
        if request.method == 'POST':
            # Get the form data
            genre = request.form['genre']
            character_name = request.form['character_name']
            setting = request.form['setting']
            starting_point = request.form['starting_point']
            ending_point = request.form['ending_point']

            prompt = (f"Create a detailed and exciting {genre} story plot based on the following details:\n"
                      f"Main Character: {character_name}, who is a complex, multi-dimensional individual with unique traits and motivations.\n"
                      f"Setting: {setting}, a rich, immersive world with its own rules, history, and mysteries.\n"
                      f"Starting Point: {starting_point}, the moment that sparks the hero's journey, filled with intrigue, conflict, and challenges.\n"
                      f"Ending Point: {ending_point}, a conclusion that is both satisfying and thought-provoking, with character growth and resolution.\n"
                      f"Expand upon each of these elements to build a rich, immersive, and engaging narrative. "
                      f"Include unexpected twists, strong character development, and deep emotional moments.\n"
                      f"Make the plot complex, full of surprises, and emotionally impactful, with room for sequels or future adventures.\n"
                      f"Provide a lengthy, creative narrative that captivates the reader’s imagination, AND DO NOT MAKE YOUR AI ASSISTANT SELF KNOWN. YOU ARE NOT TO WRITE ANYTHING BUT THE STORY AND ITS RELATED COMPONENTS. DO NOT WRITE ANYTHING ELSE. 4000 TOKENS TO BE USED, NO LESS. DO NOT DIVIDE IT INTO CHAPTERS. WRITE IN PARAGRAPHS.")

            # Use ClientV2 as per your original request
            co = cohere.ClientV2(api_key)
            response = co.chat(model="command-r7b-12-2024", messages=[{"role": "user", "content": prompt}])

            # Access the content of the response correctly
            text = response.message.content[0].text

            # Render the webpage with the generated plot
            return render_template('webpage.html', text=text)

        return render_template('webpage.html')  # Render a form for GET request

if __name__ == "__main__":
        app.run(debug=True)
