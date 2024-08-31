import streamlit as st

# song: how sweet by newjeans :D
st.audio("audio/HowSweet.mp3", format="audio/mpeg", loop=True)

# audio style
st.markdown(
    """
    <style>
    audio {
        background-color: #ffcbcc;
        border-radius: 10px;
        padding: 10px;
    }
    audio::-webkit-media-controls-panel,
    audio::-webkit-media-controls-enclosure {
    background-color: #ff9c9d;}

    audio::-webkit-media-controls-time-remaining-display,
    audio::-webkit-media-controls-current-time-display {
    color: white;
    text-shadow: none; 
}

    audio::-webkit-media-controls-play-button {
        background-image: url("https://img.icons8.com/?size=100&id=lynRTHxnDIHB&format=png&color=000000");
        background-size: contain;
        background-repeat: no-repeat;
        background-position: center;
    }

    audio::-webkit-media-controls-timeline {
    background-color: #ffcbcc;
    border-radius: 25px;
    margin-left: 10px;
    margin-right: 10px;
    padding: 10px;
}

    audio::-webkit-media-controls-timeline-container {
        background-color: #ff9c9d;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# buttons styles
st.markdown("""
<style>
.element-container:has(#btnOne) + div button {
    background-image: url("https://img.icons8.com/?size=100&id=eS3gmr9rE68k&format=png&color=000000");
    background-size: contain;
    color: transparent;
    border: none;
    width: 100px;  
    height: 100px; 
    padding: 0;    
    margin: 0;     
    background-repeat: no-repeat;
    box-shadow: 0px 4px 8px rgb(255, 156, 157);   
}

.element-container:has(#btnTwo) + div button {
    background-image: url("https://img.icons8.com/?size=100&id=l0MHuHf3syOd&format=png&color=000000");
    background-size: contain;
    color: transparent;
    border: none;
    width: 100px;  
    height: 100px; 
    padding: 0;    
    margin: 0;     
    background-repeat: no-repeat;
    box-shadow: 0px 4px 8px rgb(156, 255, 157);   
}

.element-container:has(#btnThree) + div button {
    background-image: url("https://img.icons8.com/?size=100&id=mJbFA2D6hmnY&format=png&color=000000");
    background-size: contain;
    color: transparent;
    border: none;
    width: 100px;  
    height: 100px; 
    padding: 0;    
    margin: 0;     
    background-repeat: no-repeat;
    box-shadow: 0px 4px 8px rgb(157, 156, 255);   
}
</style>
""", unsafe_allow_html=True)

# click meee
st.image("images/clickme.png", width=200)


col1, col2, col3 = st.columns(3)

# button 1
with col1:
    st.markdown('<span id="btnOne"></span>', unsafe_allow_html=True)
    if st.button('', key='btnOne'):
        txt = st.text_area(
            "ˏˋ°•*⁀➷ My Hobbies ༊*·˚",
            "I draw in my spare time "
            "digitally and traditionally. "
            "I love reading my Bible every night before sleeping. 𓆩♡𓆪 "
            "I play Death Ball recently! "
            "I enjoy watching and reading manga. ",
        )

# button 2
with col2:
    st.markdown('<span id="btnTwo"></span>', unsafe_allow_html=True)
    if st.button('', key='btnTwo'):
        txt = st.text_area(
            "ˏˋ°•*⁀➷ About My Pets ༊*·˚",
            "I have a total of 9 pets here in the city "
            "and 10 in my home in the island. "
            "I love each and every one of them. 𓆩♡𓆪 "
            "They love snacks! "
            " ",
        )

# button 3
with col3:
    st.markdown('<span id="btnThree"></span>', unsafe_allow_html=True)
    if st.button('', key='btnThree'):
        txt = st.text_area(
            "ˏˋ°•*⁀➷ About Me ༊*·˚",
            "I am an only child. "
            "I am always faithful and I laugh a lot. "
            "Waiting long for someone is my pet peeve :< "
            "I help whenever I can because I'm blessed. ೄྀ࿐ ˊˎ- "
            " ",
        )

st.image("images/me.png")


# Sidebar content
name = st.sidebar.text_input(
    "Hi! Get to know me ﹒⪩⪨﹒", 
    "Anne Jenel G. Ilosorio")

st.sidebar.image("images/ppf.png", use_column_width=True)
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background-color: #c7ebf2;
        
    }
    </style>
    """,
    unsafe_allow_html=True
)

# My parents /expander
expander = st.expander("ˏˋ°•*⁀➷ My Lovely Parents ༊*·˚")
expander.write('''
    I am an only child of these two beautiful and very hard working people. 
    They love me and gave me good education despite of the circumstances we are facing right now.
    My source of strength, peace, and joy.
''')
expander.image("images/parents.png")

# Skills ratings expander
expander = st.expander("ˏˋ°•*⁀➷ My Skills Breakdown ༊*·˚")
expander.write('''
    This section will display a breakdown of my skills, rating them from 1 to 10 stars, with 10 being the highest and 1 being the lowest.
                             
''')

skills = {
    "Python": 4,
    "JavaScript": 7,
    "HTML/CSS": 7,
    "Data Analysis": 6,
    "Machine Learning": 5,
    "Art": 7,
    "Makeup": 3,
    "Cooking": 8,
    "Baking": 9,
    "Gaming": 6,
    "Eating": 10
}

def generate_stars(rating):
    full_star = "images/one.png"
    empty_star = "images/empty.png"
    stars = []
    for i in range(10):
        if i < rating:
            stars.append(full_star)
        else:
            stars.append(empty_star)
    return stars


for skill, rating in skills.items():
    expander.write(f"**{skill}**:")
    star_images = generate_stars(rating)
    cols = expander.columns(10)
    for col, star in zip(cols, star_images):
        col.image(star, width=20, use_column_width=False)


# ambot sad ni ser cute abi haha
st.balloons()


# references ˗ˏˋ ´ˎ˗
# 𓆩♡𓆪 https://discuss.streamlit.io/t/make-your-st-audio-stand-out-with-css-styling-techniques-toms-tutorial-friday-pt-1/37094
# 𓆩♡𓆪 https://docs.streamlit.io/develop/api-reference/widgets
# 𓆩♡𓆪 https://discuss.streamlit.io/t/create-2-different-buttons-with-different-styles/39380/9
# 𓆩♡𓆪 https://rgbacolorpicker.com/hex-to-rgba