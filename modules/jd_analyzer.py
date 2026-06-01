import re

class JobDescriptionAnalyzer:
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
    
    def extract_job_title(self, text):
        """Extract job title from JD"""
        # Common patterns for job titles
        patterns = [
            r'(?:Position|Title|Role):\s*(.+?)(?:\n|$)',
            r'(Data Analyst|Software Engineer|Developer|Manager|Designer|Analyst)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1).strip()
        
        # Default to first line if no pattern matches
        lines = text.split('\n')
        return lines[0] if lines else "Job Title Not Found"
    
    def extract_required_skills(self, text):
        """Extract required skills from JD"""
        skills_found = []
        text_lower = text.lower()
        
        for skill in self.skill_database:
            if skill.lower() in text_lower:
                skills_found.append(skill)
        
        return list(set(skills_found))  # Remove duplicates
    
    def extract_experience_level(self, text):
        """Extract experience level requirement"""
        text_lower = text.lower()
        
        if 'entry' in text_lower or 'fresher' in text_lower or 'junior' in text_lower:
            return "Entry Level"
        elif 'mid' in text_lower or 'intermediate' in text_lower:
            return "Mid Level"
        elif 'senior' in text_lower or 'lead' in text_lower:
            return "Senior Level"
        else:
            return "Not Specified"
    
    def extract_responsibilities(self, text):
        """Extract key responsibilities"""
        # Look for bullet points or numbered lists
        responsibilities = []
        lines = text.split('\n')
        
        responsibility_section = False
        for line in lines:
            if 'responsibility' in line.lower() or 'duties' in line.lower():
                responsibility_section = True
                continue
            
            if responsibility_section and (line.strip().startswith('-') or line.strip().startswith('•') or re.match(r'^\d+\.', line.strip())):
                cleaned = re.sub(r'^[-•\d.]\s*', '', line.strip())
                if cleaned:
                    responsibilities.append(cleaned)
        
        return responsibilities[:5]  # Return first 5 responsibilities
    
    def analyze_jd(self, job_description):
        """Main method to analyze job description"""
        jd_data = {
            "job_title": self.extract_job_title(job_description),
            "required_skills": self.extract_required_skills(job_description),
            "experience_level": self.extract_experience_level(job_description),
            "responsibilities": self.extract_responsibilities(job_description),
            "raw_text": job_description[:500]
        }
        
        return jd_data
