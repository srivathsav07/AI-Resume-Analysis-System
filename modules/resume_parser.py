import pdfplumber
import re
from docx import Document
from io import BytesIO

class ResumeParser:
    def __init__(self):
        self.skill_database = [
            "Python", "Java", "C++", "JavaScript", "SQL", "React", "Vue", "Angular",
            "Django", "Flask", "Node.js", "Express", "MongoDB", "PostgreSQL", "MySQL",
            "AWS", "Azure", "GCP", "Docker", "Kubernetes", "Git", "CI/CD", "Linux",
            "Machine Learning", "Deep Learning", "TensorFlow", "PyTorch", "Pandas",
            "NumPy", "Scikit-learn", "Tableau", "Power BI", "Excel", "Statistics",
            "Data Analysis", "Web Scraping", "API Development", "REST", "GraphQL",
            "Agile", "Scrum", "JIRA", "Confluence", "HTML", "CSS", "Bootstrap",
            "Responsive Design", "Testing", "Unit Testing", "Integration Testing",
            "Communication", "Leadership", "Problem Solving", "Analytical Skills"
        ]
    
    def extract_text_from_pdf(self, file):
        """Extract text from PDF file"""
        text = ""
        try:
            with pdfplumber.open(file) as pdf:
                for page in pdf.pages:
                    text += page.extract_text() or ""
        except Exception as e:
            raise Exception(f"Error reading PDF: {str(e)}")
        return text
    
    def extract_text_from_docx(self, file):
        """Extract text from DOCX file"""
        text = ""
        try:
            doc = Document(file)
            for para in doc.paragraphs:
                text += para.text + "\n"
        except Exception as e:
            raise Exception(f"Error reading DOCX: {str(e)}")
        return text
    
    def extract_email(self, text):
        """Extract email address from text"""
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        match = re.search(pattern, text)
        return match.group(0) if match else "Not found"
    
    def extract_phone(self, text):
        """Extract phone number from text"""
        pattern = r'\b(?:\+?1[-.\s]?)?\(?([0-9]{3})\)?[-.\s]?([0-9]{3})[-.\s]?([0-9]{4})\b'
        match = re.search(pattern, text)
        return match.group(0) if match else "Not found"
    
    def extract_skills(self, text):
        """Extract skills from resume text"""
        skills_found = []
        text_lower = text.lower()
        
        for skill in self.skill_database:
            if skill.lower() in text_lower:
                skills_found.append(skill)
        
        return list(set(skills_found))  # Remove duplicates
    
    def extract_name(self, text):
        """Extract name from text (usually first line or near top)"""
        lines = text.split('\n')
        # Get first non-empty line as name
        for line in lines[:10]:
            line = line.strip()
            if len(line) > 0 and len(line) < 100 and not any(char.isdigit() for char in line):
                return line
        return "Not found"
    
    def parse_resume(self, uploaded_file):
        """Main method to parse resume"""
        # Extract text based on file type
        if uploaded_file.type == "application/pdf":
            text = self.extract_text_from_pdf(uploaded_file)
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            text = self.extract_text_from_docx(uploaded_file)
        else:
            raise Exception("Unsupported file format")
        
        # Extract information
        resume_data = {
            "name": self.extract_name(text),
            "email": self.extract_email(text),
            "phone": self.extract_phone(text),
            "skills": self.extract_skills(text),
            "raw_text": text[:500]  # First 500 chars for preview
        }
        
        return resume_data
