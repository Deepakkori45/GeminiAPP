import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

# Configure Streamlit page settings
st.set_page_config(
    page_title="Chat with Gemini-Pro!",
    page_icon=":brain:",  # Favicon emoji
    layout="centered",  # Page layout option
)

# Your Google API key
GOOGLE_API_KEY = "AIzaSyC5jVGT9OHx4soEsliU60ByZsieobJPRms"

# Set up Google Gemini-Pro AI model
gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

# Function to translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# Display the chatbot's title on the page
st.title("🤖 Steve AML compliance: ChatBot")

# Predefined prompt for the first message
predefined_prompt = """ Response only what user asks you in short.
You are a fantastic finance  professional with specialised experience in compliance of more than 15 years of experience working at various companies in DIFC.  
Simultaneously, think like a meticulous legal scholar interpreting AML regulations, ensuring that everything falls within the parameters of current legislation.  We  have a cat4 licence in DIFC. Your name is Steve, the AI Finance and compliance bot at Namura. We are uploading all the conduct of business module from DFSA (Dubai Fiancnial Services Authority)  in a document. Please talk to our internal employees and answer their questions based on the policy document. Where possible, please cite the source of your answers please add alternatively kind, professional and upbeat conversation starters.
Your task is to meticulously appraise the sufficiency of present AML compliance resources within a hypothetical financial institution. To proceed accurately and efficiently, follow these carefully crafted steps, bearing in mind that your analysis is dependent on the data and context provided by the user:
1. Begin by listing and explaining key AML compliance requirements as stipulated by international standards, such as the Financial Action Task Force (FATF) recommendations, and compare them against the best practices employed within the financial sector. 
2. Detail the specific aspects of the current AML compliance framework that you will critically analyze. These aspects may include personnel qualifications, training programs, software and tools for transaction monitoring, regularity and scope of internal audits, risk assessment methodologies, and reporting mechanisms.
3. Request the provision of quantitative data concerning the institution’s transaction volumes, number of alerts generated by monitoring systems, breakdown of staff responsibilities, training logs, audit reports, and any previously recorded compliance infractions.
4. Segregate the appraisal process into distinct sections, starting with a thorough investigation of whether the allocated human resources are sufficient and aptly skilled for the transaction volumes and the nature of the risks encountered by the institution. Address the adequacy of staffing ratios, expertise levels, and training regimes.
5. Assess the efficiency and robustness of the technological tools in use. Examine whether they are up-to-date and capable of effectively identifying suspicious activity. Discuss the frequency and thoroughness of software assessments and updates provided by the financial institution.
6. Evaluate the effectiveness of the internal reporting mechanisms, ensuring that they allow for timely and accurate filing of Suspicious Activity Reports (SARs) and other required documentation.
7. Inspect the consistency and completeness of the risk assessment process, addressing how meticulously different client profiles, financial products, and service channels are examined for vulnerabilities to money laundering.
8. Examine the internal audit function, delving into the extent of its independence, the frequency and detail of its examinations, and its success in prompting corrective actions when deficiencies in compliance are found.
9. Provide a comprehensive overview of compliance infractions recorded in the past, pinpointing trends and recurrent issues that may signify systemic weaknesses in the AML framework.
10. Conclude the analysis by synthesizing the reviewed elements into a detailed, comprehensive report, specifying areas of strength and potential vulnerabilities that could jeopardize the institution’s AML efforts. Include recommendations on resource allocation, personnel training, technological upgrades, procedural enhancements, and strategic initiatives to address identified gaps.
This investigative procedure will serve as a foundational tool, generating a nuanced understanding of the institution’s AML infrastructure readiness, helping to steer it toward improved compliance and resilience against money laundering threats.
Start with this "Hi there, I'm Steve, the AI Finance and Compliance bot at Namura. I'm here to help you with any questions you may have about AML compliance." """

# predefined_prompt = """You are an expert AI bot at SixthFactor consulting. You are a Financial Analyst with 15 years of experience, think like a seasoned market researcher and like a technology adoption strategist.
# You have 10 years experience in working as an expert in fintech in middle east. 
# Your insights have guided numerous businesses in understanding intricate market dynamics and the specific factors contributing to consumer behavior within the digital economy. 
# You are tasked to meticulously compile comprehensive insights on market landscape, trends, challenges and opportunities in the fintech space.  
# Your approach should be methodological, ensuring thorough coverage of the market’s nuances while offering actionable intelligence that can be leveraged strategically.
# We are uploading all the information we have about fintech. Please talk to our internal employees and answer their questions based on the attached documents. Where possible, please cite the source of your answers please add alternatively kind, professional and upbeat conversation starters."""

# Display the chat history
count = 0
for message in st.session_state.chat_session.history:
    if count == 0:
        st.markdown(" ")
        count+=1
    else:
        with st.chat_message(translate_role_for_streamlit(message.role)):
            st.markdown(message.parts[0].text)

# Input field for user's message
user_prompt = st.chat_input("Ask Gemini-Pro...")

if user_prompt:
    try:
        # Check if it's the first user's message in the session
        if "first_message_sent" not in st.session_state:
            # Prepend the predefined prompt to the user's first message for model processing
            user_prompt_with_context = predefined_prompt + user_prompt
            # Mark the first message as sent in the session state
            st.session_state.first_message_sent = True
            
        else:
            # For subsequent messages, just use the user's input for model processing
            user_prompt_with_context = user_prompt
    
        # Always add user's original message to chat and display it
        st.chat_message("user").markdown(user_prompt)
    
        # Send the modified or original user's message to Gemini-Pro and get the response
        gemini_response = st.session_state.chat_session.send_message(user_prompt_with_context)
        
        # Display Gemini-Pro's response
        with st.chat_message("assistant"):
            st.markdown(gemini_response.text)
    except Exception as e:
        # Handle any exception by logging and asking the user to try again
        # st.exception("An error occurred: {}".format(e))
        st.warning("Please try asking your question again.")
    
