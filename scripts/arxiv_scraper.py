#!/usr/bin/env python3
"""
Arxiv Paper Scraper for World Action Models
Fetches papers from arXiv with specific keywords and categories
"""

import feedparser
import requests
import json
import time
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import re

class ArxivScraper:
    """ArXiv paper scraper with filtering and ranking capabilities"""

    BASE_URL = "http://export.arxiv.org/api/query"

    # Keywords related to World Action Models, VLA, Robotics
    KEYWORDS = {
        "VLA": [
            "vision-language-action", "VLA model", "robotics transformer",
            "openvla", "embodied ai", "multimodal policy"
        ],
        "World Model": [
            "world model", "predictive model", "world action model",
            "dreamer", "jepa", "latent dynamics"
        ],
        "Robotics": [
            "robotic manipulation", "robot learning", "manipulation policy",
            "robot foundation model", "generalist robot"
        ],
        "Action Learning": [
            "action representation", "diffusion policy", "behavior transformer",
            "action chunking", "imitation learning"
        ],
        "Reasoning": [
            "chain of thought", "planning", "reasoning in robotics",
            "task planning", "think before act"
        ],
        "Simulation": [
            "sim2real", "domain adaptation", "simulator",
            "physics simulation", "isaac gym"
        ]
    }

    CATEGORIES = [
        "cs.AI",           # Artificial Intelligence
        "cs.RO",           # Robotics
        "cs.CV",           # Computer Vision
        "cs.LG",           # Machine Learning
        "cs.CL",           # Computation and Language
    ]

    def __init__(self, max_results: int = 100, days_back: int = 180):
        self.max_results = max_results
        self.days_back = days_back
        self.cutoff_date = datetime.now() - timedelta(days=days_back)

    def build_query(self, keywords: List[str], categories: List[str]) -> str:
        """Build arXiv search query from keywords and categories"""
        # Combine keywords with OR
        keyword_query = " OR ".join([f'all:{kw}' for kw in keywords])
        # Combine categories with OR
        cat_query = " OR ".join([f'cat:{cat}' for cat in categories])
        # Combine with AND
        query = f"({keyword_query}) AND ({cat_query})"
        return query

    def search_papers(self, query: str) -> List[Dict]:
        """Search arXiv with given query"""
        papers = []
        start = 0
        batch_size = 100

        while start < self.max_results:
            params = {
                'search_query': query,
                'start': start,
                'max_results': min(batch_size, self.max_results - start),
                'sortBy': 'submittedDate',
                'sortOrder': 'descending'
            }

            try:
                response = requests.get(self.BASE_URL, params=params, timeout=30)
                response.raise_for_status()
                feed = feedparser.parse(response.content)

                if not feed.entries:
                    break

                for entry in feed.entries:
                    paper = self.parse_entry(entry)
                    if paper and self._is_recent(paper):
                        papers.append(paper)
                        if len(papers) >= self.max_results:
                            return papers

                start += batch_size
                time.sleep(1)  # Rate limiting

            except Exception as e:
                print(f"Error fetching papers: {e}")
                break

        return papers

    def parse_entry(self, entry) -> Optional[Dict]:
        """Parse arXiv feed entry into paper dict"""
        try:
            arxiv_id = entry.id.split('/abs/')[-1]
            published = datetime(*entry.published_parsed[:6])

            # Extract categories
            categories = [tag.term for tag in entry.tags]

            # Get primary category
            primary_category = categories[0] if categories else "cs.AI"

            paper = {
                'id': arxiv_id,
                'title': entry.title,
                'authors': [author.name for author in entry.authors],
                'summary': entry.summary,
                'published': published.strftime('%Y-%m-%d'),
                'published_iso': published.isoformat(),
                'categories': categories,
                'primary_category': primary_category,
                'url': f"https://arxiv.org/abs/{arxiv_id}",
                'pdf_url': entry.link.replace('/abs/', '/pdf/') + '.pdf',
                'code_url': None,
                'project_url': None,
            }

            # Extract links for code and project pages
            for link in entry.get('links', []):
                href = link.get('href', '')
                if 'github.com' in href and paper['code_url'] is None:
                    paper['code_url'] = href
                elif paper['project_url'] is None and any(x in href for x in ['project', 'page']):
                    paper['project_url'] = href

            return paper

        except Exception as e:
            print(f"Error parsing entry: {e}")
            return None

    def _is_recent(self, paper: Dict) -> bool:
        """Check if paper is within the date range"""
        try:
            paper_date = datetime.fromisoformat(paper['published_iso'])
            return paper_date >= self.cutoff_date
        except:
            return True

    def classify_paper(self, paper: Dict) -> str:
        """Classify paper into category based on title and abstract"""
        text = f"{paper['title'].lower()} {paper['summary'].lower()}"

        classification_scores = {}

        for category, keywords in self.KEYWORDS.items():
            score = 0
            for keyword in keywords:
                if keyword.lower() in text:
                    score += 1
                    # Boost for exact matches in title
                    if keyword.lower() in paper['title'].lower():
                        score += 2
            classification_scores[category] = score

        # Return category with highest score, or "Other" if no match
        max_score = max(classification_scores.values())
        if max_score == 0:
            return "Other"
        return max(classification_scores, key=classification_scores.get)

    def fetch_all_categories(self) -> Dict[str, List[Dict]]:
        """Fetch papers for all keyword categories"""
        all_papers = {}

        for category, keywords in self.KEYWORDS.items():
            print(f"Fetching papers for category: {category}")
            query = self.build_query(keywords, self.CATEGORIES)
            papers = self.search_papers(query)

            # Add category to each paper
            for paper in papers:
                paper['auto_category'] = category

            all_papers[category] = papers
            time.sleep(2)  # Rate limiting between categories

        return all_papers

    def deduplicate_papers(self, papers_dict: Dict[str, List[Dict]]) -> List[Dict]:
        """Deduplicate papers across categories"""
        seen_ids = set()
        unique_papers = []

        for category, papers in papers_dict.items():
            for paper in papers:
                if paper['id'] not in seen_ids:
                    seen_ids.add(paper['id'])
                    paper['categories'] = [category] + paper.get('categories', [])
                    unique_papers.append(paper)

        # Sort by date (newest first)
        unique_papers.sort(key=lambda x: x['published_iso'], reverse=True)
        return unique_papers

    def save_to_json(self, papers: List[Dict], filename: str):
        """Save papers to JSON file"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(papers, f, ensure_ascii=False, indent=2)
        print(f"Saved {len(papers)} papers to {filename}")

    def generate_markdown(self, papers: List[Dict], output_file: str):
        """Generate markdown formatted paper list"""
        md_content = "# 📚 Latest ArXiv Papers - World Action Models\n\n"
        md_content += f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        md_content += f"Total papers: {len(papers)}\n\n"

        # Group by auto_category
        by_category = {}
        for paper in papers:
            category = paper.get('auto_category', 'Other')
            if category not in by_category:
                by_category[category] = []
            by_category[category].append(paper)

        for category, category_papers in by_category.items():
            md_content += f"## {category}\n\n"
            md_content += f"| Paper | Date | Code |\n"
            md_content += f"|-------|------|------|\n"

            for paper in category_papers[:20]:  # Limit to top 20 per category
                title = paper['title'].replace('|', '\\|')
                date = paper['published']
                url = paper['url']

                # Authors (first 3)
                authors = ', '.join(paper['authors'][:3])
                if len(paper['authors']) > 3:
                    authors += ' et al.'

                # Code link
                code_badge = ''
                if paper.get('code_url'):
                    code_badge = f"[🔗 Code]({paper['code_url']})"

                md_content += f"| [{title}]({url})<br><small>{authors}</small> | {date} | {code_badge} |\n"

            md_content += "\n"

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f"Generated markdown: {output_file}")


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Scrape ArXiv for World Action Model papers')
    parser.add_argument('--max-results', type=int, default=100, help='Max results per category')
    parser.add_argument('--days-back', type=int, default=180, help='Days back to search')
    parser.add_argument('--output', type=str, default='data/papers.json', help='Output JSON file')
    parser.add_argument('--md-output', type=str, default='docs/latest-papers.md', help='Output markdown file')
    parser.add_argument('--category', type=str, help='Specific category to fetch (optional)')

    args = parser.parse_args()

    scraper = ArxivScraper(max_results=args.max_results, days_back=args.days_back)

    if args.category:
        # Fetch specific category
        keywords = scraper.KEYWORDS.get(args.category, [])
        if not keywords:
            print(f"Unknown category: {args.category}")
            return

        query = scraper.build_query(keywords, scraper.CATEGORIES)
        papers = scraper.search_papers(query)
        for paper in papers:
            paper['auto_category'] = args.category
    else:
        # Fetch all categories
        papers_dict = scraper.fetch_all_categories()
        papers = scraper.deduplicate_papers(papers_dict)

    # Save results
    scraper.save_to_json(papers, args.output)
    scraper.generate_markdown(papers, args.md_output)

    print(f"\nTotal unique papers found: {len(papers)}")
    print(f"Categories: {set(p.get('auto_category', 'Other') for p in papers)}")


if __name__ == '__main__':
    main()
