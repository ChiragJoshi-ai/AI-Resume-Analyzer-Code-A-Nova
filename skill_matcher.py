from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from skills import SKILLS


def calculate_similarity(resume_text, job_description):

    documents = [resume_text, job_description]

    cv = CountVectorizer().fit_transform(documents)
    similarity = cosine_similarity(cv)

    score = similarity[0][1] * 100
    return round(score, 2)


def extract_skills(resume_text):

    found_skills = []

    for skill in SKILLS:
        if skill in resume_text:
            found_skills.append(skill)

    return found_skills


def missing_skills(resume_skills, job_description):

    jd_skills = []

    for skill in SKILLS:
        if skill in job_description:
            jd_skills.append(skill)

    missing = list(set(jd_skills) - set(resume_skills))

    return missing