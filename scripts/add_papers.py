#!/usr/bin/env python3
"""
Search and add new papers from arXiv with interactive selection
"""

import json
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent))

from arxiv_scraper import ArxivScraper

def main():
    import argparse

    parser = argparse.ArgumentParser(description='Search and add new papers interactively')
    parser.add_argument('--query', type=str, required=True, help='Search query')
    parser.add_argument('--max-results', type=int, default=20, help='Max results')
    parser.add_argument('--category', type=str, help='Category to assign')

    args = parser.parse_args()

    scraper = ArxivScraper(max_results=args.max_results, days_back=365)

    # Search papers
    query = f"all:{args.query} AND (cat:cs.AI OR cat:cs.RO OR cat:cs.CV OR cat:cs.LG)"
    papers = scraper.search_papers(query)

    if not papers:
        print("No papers found")
        return

    print(f"\nFound {len(papers)} papers:\n")
    for i, paper in enumerate(papers, 1):
        print(f"[{i}] {paper['title']}")
        print(f"    {paper['authors'][0] if paper['authors'] else 'Unknown'} et al.")
        print(f"    {paper['published']} | {paper['url']}")
        print()

    # Load existing papers
    data_file = Path('data/papers.json')
    existing_ids = set()
    if data_file.exists():
        with open(data_file, 'r') as f:
            existing_papers = json.load(f)
            existing_ids = set(p['id'] for p in existing_papers)

    # Filter new papers
    new_papers = [p for p in papers if p['id'] not in existing_ids]
    print(f"\nNew papers: {len(new_papers)}")

    if new_papers:
        # Add category
        category = args.category or scraper.classify_paper(new_papers[0])
        for paper in new_papers:
            paper['auto_category'] = category

        # Update papers file
        all_papers = existing_papers + new_papers
        with open(data_file, 'w') as f:
            json.dump(all_papers, f, indent=2)

        print(f"Added {len(new_papers)} new papers to {data_file}")

if __name__ == '__main__':
    main()
