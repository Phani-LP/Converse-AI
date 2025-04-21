# ConverseAI

**ConverseAI** is an advanced AI-powered chatbot platform built using Django. It is designed to provide seamless and interactive communication experiences by leveraging the latest advancements in AI technology. Recently, the project has been upgraded to use **Google Gemini-Flash 1.5**, replacing CohereAI, to deliver enhanced multimodal capabilities, improved performance, and greater efficiency.

---

## 🌟 Key Features of Gemini-Flash 1.5

### Multimodal Capabilities

- Processes and generates various forms of data, including **text, images, video, and audio**.
- Enables tasks like **image and video captioning**, **question answering from videos**, and more.

### Speed and Efficiency

- Designed for **high-volume, high-frequency tasks**.
- Optimized for **speed** and **cost-effectiveness**, making it ideal for real-world applications.

### Long Context Window

- Capable of processing and understanding **significantly longer pieces of text** compared to previous models.

### Improved Performance

- Excels in tasks such as:
  - **Summarization**
  - **Chat applications**
  - **Data extraction**
- Delivers **accurate and context-aware responses**.

### Versatility

- Suitable for a **wide range of applications** across different domains, including education, healthcare, customer support, and more.

### 1.5 Flash

- The latest addition to the Gemini model family.
- **Highly optimized for speed and efficiency**.
- Demonstrates **superior multimodal reasoning** capabilities.

---

## 🚀 Real-World Applications

ConverseAI is not just a theoretical project; it has been designed with real-world use cases in mind. Here are some examples of how it can be applied:

1. **Customer Support**:

   - Automate responses to customer queries with accurate and context-aware answers.
   - Handle multimedia inputs like images or videos for better support.

2. **Education**:

   - Provide students with AI-assisted learning tools for answering questions, summarizing content, and more.
   - Enable interactive learning experiences with multimodal capabilities.

3. **Healthcare**:

   - Assist in patient support by answering health-related queries.
   - Process and analyze medical images or reports for better insights.

4. **Content Creation**:

   - Generate high-quality summaries, captions, and descriptions for text, images, and videos.
   - Assist in creative writing and brainstorming.

5. **Data Analysis**:
   - Extract valuable insights from large datasets.
   - Summarize lengthy reports or documents for quick understanding.

---

## 🛠️ Installation and Setup

Follow these steps to set up the project on your local machine:

1. **Clone the Repository**:

   ```bash
   git clone <repository-url>
   cd ConverseAI
   ```

2. **Create a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate 
   # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables:**<br>
   Add your Google Gemini API Key in a new file named variables.py:

   ```bash
   # filepath: ConverseAI/variables.py
   API_KEY = "your-google-gemini-api-key"
   ```

   <code>
   1 vulnerability 
   hardcoded-credentials Embedding credentials in source code  risks unauthorized access 
   </code>

5. **Apply Migrations:**
   ```bash
   python manage.py migrate
   ```
6. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```
7. **Access the Application:**<br>
   Open your browser and navigate to http://127.0.0.1:8000.
