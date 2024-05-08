import replicate
import streamlit as st

st.markdown("# :rainbow[AI Generated Images] :rainbow:")
REPLICATE_API_TOKEN = st.secrets["REPLICATE_API_TOKEN"]


def configure_sidebar() -> dict:
    with st.sidebar:
        with st.form("my form"):
            width = st.number_input("Width of the image", max_value=2048, min_value=256, value=1024, step=16)
            height = st.number_input("Height of the image", max_value=2048, min_value=256, value=1024, step=16)
            submit_button = st.form_submit_button("Generate Image", type="primary")
            prompt = st.text_area("Promt", value="A beautiful landscape with a river and mountains in the background")
    return {"width": width, "height": height, "prompt": prompt, "submit_button": submit_button}


def main_page(width: int, height: int, prompt: str, submit_button: bool):
    if not submit_button:
        return

    with st.spinner("Loading..."):
        result = replicate.run(
            ref="stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
            input=dict(width=width, height=height, prompt=prompt)
        )
        image = result[0]
        with st.container():
            st.image(image, use_column_width=True, caption="Generated Image")


def main():
    data = configure_sidebar()
    main_page(**data)


if __name__ == "__main__":
    main()
