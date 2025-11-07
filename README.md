# Portfolio

Welcome to my portfolio repository! This project showcases my skills, projects, and experience as a developer.

## About Me

Brief introduction about yourself, your background, and what you're passionate about in software development.

## Skills

- Programming Languages: (e.g., JavaScript, Python, Java)
- Frameworks & Libraries: (e.g., React, Node.js, Express)
- Tools & Technologies: (e.g., Git, Docker, AWS)
- Databases: (e.g., MongoDB, PostgreSQL, MySQL)

## Projects

### Project 1
Brief description of your project, technologies used, and key features.
- **Tech Stack**: 
- **Demo**: [Live Demo](link)
- **Repository**: [GitHub](link)

### Project 2
Brief description of your project, technologies used, and key features.
- **Tech Stack**: 
- **Demo**: [Live Demo](link)
- **Repository**: [GitHub](link)

## Contact

- **Email**: your.email@example.com
- **LinkedIn**: [Your LinkedIn Profile](link)
- **GitHub**: [Your GitHub Profile](link)

## How to Run

Instructions for running any projects locally if applicable.

```bash
git clone https://github.com/yourusername/repository-name
cd repository-name
npm install
npm start
```

## Portfolio DB

This repository includes a small SQLite database used to store portfolio project entries.

- DB file: `data/portfolio.db`
- Table: `projects` (id, title, description, url, tech, date)

To (re)create the DB and populate it with two example projects, run:

```bash
python3 scripts/add_portfolio_projects.py
```

The script will create `data/portfolio.db` if it doesn't exist and insert two example rows (it skips duplicates by title).
