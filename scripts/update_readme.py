#!/usr/bin/env python3
"""
Update README.md with latest papers from data/papers.json
"""

import json
import re
from pathlib import Path

def load_papers(filepath='data/papers.json'):
    """Load papers from JSON file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def categorize_papers(papers):
    """Group papers by category"""
    categories = {
        'VLA': [],
        'World Model': [],
        'Robotics': [],
        'Action Learning': [],
        'Reasoning': [],
        'Simulation': [],
        'Other': []
    }

    for paper in papers:
        cat = paper.get('auto_category', 'Other')
        categories[cat].append(paper)

    return categories

def generate_latest_section(papers):
    """Generate the Latest Papers section for README"""
    categories = categorize_papers(papers)

    section = "## 🆕 Latest Papers (Auto-updated)\n\n"
    section += "> Papers are automatically fetched daily from arXiv. Last updated: "

    # Get latest date
    if papers:
        latest_date = max(p.get('published', '') for p in papers)
        section += f"{latest_date}\n\n"
    else:
        section += "N/A\n\n"

    # Generate table for each category
    for cat_name, cat_papers in categories.items():
        if not cat_papers:
            continue

        section += f"### {cat_name}\n\n"
        section += "| Paper | Date | Code |\n"
        section += "|-------|------|------|\n"

        for paper in cat_papers[:10]:  # Top 10 per category
            title = paper['title'].replace('|', '\\|').replace('[', '\\[').replace(']', '\\]')
            url = paper['url']
            date = paper['published']

            # Authors
            authors = ', '.join(paper['authors'][:2])
            if len(paper['authors']) > 2:
                authors += ' et al.'

            # Code badge
            code_badge = ''
            if paper.get('code_url'):
                code_badge = f"[🔗]({paper['code_url']})"

            section += f"| [{title}]({url})<br><small>{authors}</small> | {date} | {code_badge} |\n"

        section += "\n"

    section += "---\n\n"

    return section

def update_readme():
    """Update README.md with latest papers section"""
    readme_path = Path('README.md')
    papers = load_papers()

    if not papers:
        print("No papers found, skipping update")
        return

    # Read existing README
    try:
        readme_content = readme_path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print("README.md not found")
        return

    # Generate new latest section
    new_section = generate_latest_section(papers)

    # Find and replace the latest papers section
    pattern = r'## 🆕 Latest Papers.*?(?=\n## |$)'
    replacement = new_section.rstrip() + '\n\n'

    # Check if section exists
    if re.search(pattern, readme_content, re.DOTALL):
        updated_content = re.sub(pattern, replacement, readme_content, count=1, flags=re.DOTALL)
    else:
        # Insert after overview section
        pattern = r'(## Table of Contents.*?\n\n)'
        updated_content = re.sub(pattern, r'\1' + replacement, readme_content, count=1)

    # Write back
    readme_path.write_text(updated_content, encoding='utf-8')
    print("README.md updated successfully")

if __name__ == '__main__':
    update_readme()
