#  AI Resume Analyzer
#  Deployment link: https://github.com/srivathsav07/AI-Resume-Analysis-System
An AI-powered Resume Screening and Optimization Platform that analyzes resumes against job descriptions using Large Language Models (LLMs), Natural Language Processing (NLP), and ATS (Applicant Tracking System) scoring techniques.

The system automatically extracts candidate skills, experience, education, and project information from uploaded resumes, compares them with job requirements, identifies missing keywords, calculates ATS compatibility scores, and generates personalized recommendations to improve job application success rates.

---

##  Features

### Resume Parsing

* Extract text from PDF and DOCX resumes
* Identify candidate details (Name, Email, Phone)
* Detect technical and soft skills
* Extract education, projects, and experience

### Job Description Analysis

* Analyze job requirements
* Extract required skills and keywords
* Identify experience expectations
* Understand role responsibilities

### ATS Score Calculation

* Match resume skills against job requirements
* Calculate ATS compatibility score
* Provide skill-wise match breakdown
* Highlight missing keywords

### AI-Powered Insights

* Integration with OpenAI GPT
* Integration with Google Gemini
* Integration with Anthropic Claude
* Generate professional resume evaluations

### Recommendation Engine

* Skill gap identification
* Resume improvement suggestions
* Learning roadmap generation
* Personalized career recommendations

### Interactive Dashboard

* ATS score visualization
* Skill match analytics
* Resume comparison charts
* Recommendation summaries

---

## 🏗️ System Architecture

```text
Resume Upload (PDF/DOCX)
          │
          ▼
Resume Parser
          │
          ▼
Skill Extraction
          │
          ▼
Job Description Analyzer
          │
          ▼
ATS Scoring Engine
          │
          ▼
LLM-Based Analysis
          │
          ▼
Recommendation Engine
          │
          ▼
Interactive Dashboard
```

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Frameworks & Libraries

* Streamlit
* Pandas
* Plotly
* pdfplumber
* python-docx
* Regex

### AI & NLP

* OpenAI GPT
* Google Gemini
* Anthropic Claude
* Prompt Engineering
* Natural Language Processing (NLP)

### Deployment

* Streamlit Cloud
* Docker
* Heroku
* AWS
* Google Cloud Platform

---

## 📂 Project Structure

```text
resume-analyzer/
│
├── app.py
├── requirements.txt
├── README.md
│
├── modules/
│   ├── resume_parser.py
│   ├── jd_analyzer.py
│   ├── ats_scorer.py
│   ├── llm_analyzer.py
│   └── recommendation_engine.py
│
└── assets/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/ai-resume-analyzer.git
cd ai-resume-analyzer
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_key
GEMINI_API_KEY=your_gemini_key
CLAUDE_API_KEY=your_claude_key
```

### Run Application

```bash
streamlit run app.py
```

Application will start at:

```text
http://localhost:8501
```

---

## 📊 ATS Score Methodology

The ATS score is calculated based on skill matching between the candidate resume and job description.

Formula:

ATS Score = (Matched Skills / Required Skills) × 100

### Score Interpretation

| Score Range | Rating        |
| ----------- | ------------- |
| 0–30%       | Poor          |
| 31–50%      | Below Average |
| 51–70%      | Average       |
| 71–85%      | Good          |
| 86–100%     | Excellent     |

---

## 💡 Example Workflow

1. Upload Resume (PDF/DOCX)
2. Paste Job Description
3. Extract Skills & Keywords
4. Calculate ATS Score
5. Identify Missing Skills
6. Generate AI Feedback
7. Receive Personalized Recommendations

---

## 🎯 Key Outcomes

* Automated Resume Screening
* Faster Candidate Evaluation
* Improved ATS Compatibility
* Skill Gap Identification
* AI-Based Career Guidance
* Enhanced Job Application Success Rate

---

## 🔮 Future Enhancements

* Resume Ranking System
* Cover Letter Generator
* Interview Question Generator
* Job Recommendation Engine
* Resume Version Tracking
* Advanced NLP Skill Extraction
* Real-Time Job Portal Integration

---

## 📈 Business Impact

This solution helps:

### Job Seekers

* Improve resume quality
* Increase ATS score
* Identify missing skills
* Receive actionable recommendations

### Recruiters

* Reduce manual screening effort
* Standardize candidate evaluation
* Improve hiring efficiency
* Rank applicants effectively

---

## 👨‍💻 Author

**B. Srivathsav**

Aspiring Data Analyst | AI & Automation Enthusiast

Skills:

* Python
* SQL
* Power BI
* Data Analytics
* Machine Learning
* Generative AI
* Prompt Engineering

---

##  Project Highlights

✔ LLM-Powered Resume Analysis

✔ ATS Compatibility Scoring

✔ NLP-Based Skill Extraction

✔ Interactive Streamlit Dashboard

✔ Recruiter-Friendly Evaluation System

✔ Production-Ready Architecture

---

If you found this project useful, consider giving it a ⭐ on GitHub.

