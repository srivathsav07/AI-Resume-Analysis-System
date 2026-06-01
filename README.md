# 🤖 AI Resume Analyzer

An intelligent, AI-powered resume analysis system that automatically evaluates resumes against job descriptions, calculates ATS compatibility scores, and provides personalized recommendations.

## 🎯 Features

### Core Features
- **Resume Upload & Parsing** - Supports PDF and DOCX formats
- **Job Description Analysis** - Extract required skills and experience level
- **ATS Score Calculation** - Calculate resume-to-job compatibility
- **Skill Gap Analysis** - Identify missing and matched skills
- **AI-Powered Insights** - LLM-based deep analysis (OpenAI, Gemini, Claude)
- **Personalized Recommendations** - Actionable suggestions for improvement
- **Interactive Dashboard** - Beautiful visualizations and metrics

### Advanced Features
- **Resume Comparison** - Compare multiple resumes against one job description
- **Job Matching** - Find best matching jobs based on candidate skills
- **Interview Questions Generator** - Generate role-specific interview questions
- **Improvement Plan** - Structured 4-month learning roadmap
- **Learning Resources** - Curated courses and learning materials

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- API keys (at least one of):
  - OpenAI API key
  - Google Gemini API key
  - Claude (Anthropic) API key

### Installation

1. **Clone the repository** (or extract the zip file)
```bash
cd resume-analyzer
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 📋 Project Structure

```
resume-analyzer/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── README.md                       # This file
└── modules/
    ├── __init__.py
    ├── resume_parser.py           # Resume parsing and text extraction
    ├── jd_analyzer.py             # Job description analysis
    ├── ats_scorer.py              # ATS score calculation
    ├── llm_analyzer.py            # LLM-based analysis (OpenAI, Gemini, Claude)
    └── recommendation_engine.py   # Recommendation generation
```

## 📚 Module Documentation

### ResumeParser
Extracts text from resume files and identifies:
- Personal details (name, email, phone)
- Skills (from predefined skill database)
- Resume content preview

```python
from modules.resume_parser import ResumeParser

parser = ResumeParser()
resume_data = parser.parse_resume(uploaded_file)
```

### JobDescriptionAnalyzer
Analyzes job descriptions and extracts:
- Job title
- Required skills
- Experience level
- Key responsibilities

```python
from modules.jd_analyzer import JobDescriptionAnalyzer

analyzer = JobDescriptionAnalyzer()
jd_data = analyzer.analyze_jd(job_description_text)
```

### ATSScorer
Calculates resume-to-job compatibility:

```python
from modules.ats_scorer import ATSScorer

scorer = ATSScorer()
score = scorer.calculate_score(resume_skills, required_skills)
```

**Formula:** `(Matched Skills / Required Skills) × 100`

### LLMAnalyzer
Provides AI-powered analysis using your choice of LLM:

```python
from modules.llm_analyzer import LLMAnalyzer

llm = LLMAnalyzer(api_key, "OpenAI GPT-4")
analysis = llm.analyze(resume_data, jd_data, ats_score)
```

**Supported Providers:**
- OpenAI GPT-4
- Google Gemini
- Anthropic Claude

### RecommendationEngine
Generates actionable recommendations:

```python
from modules.recommendation_engine import RecommendationEngine

recommender = RecommendationEngine()
recommendations = recommender.generate_recommendations(
    resume_data, jd_data, ats_score
)
```

## 🎮 Usage Guide

### Mode 1: Single Resume Analysis
1. Upload your resume (PDF or DOCX)
2. Paste the job description
3. Click analyze
4. View:
   - ATS Score with gauge visualization
   - Skills matching analysis
   - AI-powered insights
   - Personalized recommendations

### Mode 2: Compare Resumes
1. Upload multiple resumes
2. Paste one job description
3. Get ranking of candidates by ATS score
4. Compare skill matches visually

### Mode 3: Job Matching
1. Upload your resume
2. System matches against sample job database
3. View best matching roles
4. See match percentage for each job

## 📊 Scoring System

### ATS Score Breakdown
- **0-30%**: Poor - Significant skill gaps
- **30-50%**: Below Average - Some skills missing
- **50-70%**: Average - Good foundation, needs improvement
- **70-85%**: Good - Strong match, minor gaps
- **85-100%**: Excellent - Excellent match!

## 🔧 Configuration

### Skill Database
Modify the skill database in:
- `modules/resume_parser.py` - Update `skill_database`
- `modules/jd_analyzer.py` - Update `skill_database`

### LLM Settings
Customize LLM behavior in:
- `modules/llm_analyzer.py` - Adjust temperature, max_tokens, model selection

## 🔑 API Key Setup

### OpenAI
1. Get API key from https://platform.openai.com/
2. Enter key in the sidebar when selecting "OpenAI GPT-4"

### Google Gemini
1. Get API key from https://makersuite.google.com/
2. Enter key when selecting "Google Gemini"

### Claude (Anthropic)
1. Get API key from https://console.anthropic.com/
2. Enter key when selecting "Claude"

## 🧠 How It Works

### Resume Analysis Pipeline
1. **Upload** → Resume file upload via Streamlit
2. **Extract** → Text extraction from PDF/DOCX
3. **Parse** → Skill and info extraction using regex
4. **Analyze** → Compare with job description
5. **Score** → Calculate ATS compatibility
6. **Enhance** → Get LLM-based deep analysis
7. **Recommend** → Generate improvement suggestions
8. **Visualize** → Display results in interactive dashboard

### Skill Matching Algorithm
```
Matched Skills = Resume Skills ∩ Required Skills
ATS Score = (Matched Skills Count / Required Skills Count) × 100
```

## 📈 Sample Output

### ATS Dashboard Shows:
- Overall ATS Score (0-100%)
- Matched vs Missing Skills
- Skill match percentage
- Interview readiness score
- Improvement recommendations
- Learning resources

## 🎓 Example

```
Resume Skills: [Python, SQL, Power BI]
Job Required: [Python, SQL, Tableau, Statistics]

Matched: Python, SQL (2 skills)
Missing: Tableau, Statistics (2 skills)

ATS Score: 2/4 × 100 = 50%

Recommendations:
1. Learn Tableau - Essential for this role
2. Study Statistics fundamentals
3. Build a data visualization project
4. Get Power BI certification
```

## 🚀 Advanced Features

### Resume Ranking
Compare multiple candidates and get ranked results with scores.

### Job Recommendation
Find jobs that match your skill profile from a database.

### Interview Question Generator
Get role-specific interview questions.

### 4-Month Improvement Plan
Structured learning roadmap with monthly milestones.

### Learning Resources
Curated courses, platforms, and project ideas for skill development.

## 🐛 Troubleshooting

### PDF Extraction Issues
- Ensure PDF is not scanned/image-based
- Try DOCX format if PDF fails
- Update pdfplumber: `pip install --upgrade pdfplumber`

### API Key Errors
- Verify API key is valid
- Check API key has necessary permissions
- Ensure billing is set up (for paid APIs)

### Skill Not Detected
- Add the skill to the skill database in parser modules
- Use exact capitalization matching
- Check resume has the skill mentioned clearly

## 📝 License
This project is open source and available under the MIT License.

## 🤝 Contributing
Contributions are welcome! Feel free to submit pull requests with improvements.

## 📧 Support
For issues or questions, please create an issue in the repository.

## 🎯 Future Enhancements
- [ ] Database integration for resume history
- [ ] Cover letter generation
- [ ] Resume formatting templates
- [ ] Interview preparation module
- [ ] Salary prediction based on skills
- [ ] Skill trend analysis
- [ ] LinkedIn profile integration
- [ ] Export reports as PDF

## 📚 Resources

### Learning Paths
- [Python Learning Path](https://www.python.org/about/gettingstarted/)
- [Data Science Stack](https://www.datacamp.com/)
- [Web Development](https://www.freecodecamp.org/)
- [Cloud Computing](https://aws.amazon.com/free/)

### Tools & Platforms
- [LeetCode](https://leetcode.com/) - Coding practice
- [Coursera](https://www.coursera.org/) - Online courses
- [GitHub](https://github.com/) - Portfolio showcase
- [Stack Overflow](https://stackoverflow.com/) - Problem solving

---

**Made with ❤️ for job seekers and recruiters**

Last Updated: 2024
