# Image Generator Simple Web App

This Python script is part of a project that uses the Streamlit library to create a web application for generating AI images. The application uses the Replicate library to run a model that generates images based on user input.

## Usage

To run the script, use the following command:

```bash
streamlit run main.py
```

## Features

The script provides a user interface with the following features:

- A form in the sidebar where the user can input the desired width and height of the image (between 256 and 2048 pixels), and a text prompt that describes the image to be generated.
- A "Generate Image" button that, when clicked, sends the user's input to the Replicate model and displays the generated image on the main page of the application.

## Dependencies

The script requires the following Python packages, which are listed in the `requirements.txt` file:

- [Streamlit](https://streamlit.io/)
- [Replicate](https://replicate.com/)

I use this model
- [sdxl](https://replicate.com/stability-ai/sdxl)

## Configuration

The script uses an API token for the Replicate service, which is stored in the `.streamlit/secrets.toml` file. The token is accessed through the `st.secrets` dictionary with the key `"REPLICATE_API_TOKEN"`.

## Code Structure

The script is structured into three main functions:

- `configure_sidebar()`: This function sets up the form in the sidebar and returns a dictionary with the user's input.
- `main_page()`: This function takes the user's input as arguments, sends it to the Replicate model, and displays the generated image.
- `main()`: This function calls the other two functions and serves as the entry point for the script.

The script is executed from the `if __name__ == "__main__":` block at the end of the file.
