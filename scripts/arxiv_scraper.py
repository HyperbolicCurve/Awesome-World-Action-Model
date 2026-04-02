#!/usr/bin/env python3
"""
Arxiv Paper Scraper for World Action Models
Fetches papers from arXiv with strict VLA/WAM filtering
"""

import arxiv
import json
from datetime import datetime, timedelta
import time

class ArxivScraperStrict:
    """ArXiv paper scraper with strict VLA/WAM filtering"""

    # Strict VLA/WAM keywords - must appear in title
    VLA_KEYWORDS = {
        'vla': ['vla', 'vision-language-action', 'vision language action'],
        'rt': ['rt-1', 'rt-2', 'robotics transformer'],
        'openvla': ['openvla'],
        'octo': ['octo', 'octo-model'],
        'pi': ['\\pi0', '\\pi*0', 'pi zero'],
        'vla_model': ['vlm-based action', 'vision-language model', 'multimodal policy'],
    }

    WORLD_MODEL_KEYWORDS = {
        'dreamer': ['dreamer', 'dreamer-v', 'dream zero'],
        'jepa': ['jepa', 'i-jepa', 'v-jepa', 'joint embedding'],
        'world_model': ['world action model', 'world model', 'world modeling'],
        'latent_dynamics': ['latent dynamics', 'predictive model'],
    }

    POLICY_KEYWORDS = {
        'diffusion': ['diffusion policy', 'action diffusion'],
        'act': ['action chunking', 'action chunking transformer', 'act'],
        'bet': ['behavior transformer', 'behaviortransformer', 'bet'],
        'peract': ['peract', 'behavior primitive'],
    }

    # Valid categories for VLA/WAM papers
    VALID_CATEGORIES = ['cs.AI', 'cs.RO', 'cs.CV', 'cs.LG']

    def __init__(self, max_results: int = 100, days_back: int = 180):
        self.max_results = max_results
        self.days_back = days_back
        self.cutoff_date = datetime.now() - timedelta(days=days_back)

    def check_vla_keywords(self, title: str, summary: str) -> bool:
        """Check if title contains VLA keywords"""
        title_lower = title.lower()
        for category, keywords in self.VLA_KEYWORDS.items():
            if any(kw in title_lower for kw in keywords):
                return True
        return False

    def check_world_model_keywords(self, title: str, summary: str) -> bool:
        """Check if title contains world model keywords"""
        title_lower = title.lower()
        summary_lower = summary.lower()
        for category, keywords in self.WORLD_MODEL_KEYWORDS.items():
            if any(kw in title_lower for kw in keywords):
                return True
        return False

    def check_policy_keywords(self, title: str, summary: str) -> bool:
        """Check if title contains policy keywords with robotics context"""
        title_lower = title.lower()
        summary_lower = summary.lower()

        # Must have policy keyword AND robotics/embodied keyword
        has_policy_keyword = False
        for category, keywords in self.POLICY_KEYWORDS.items():
            if any(kw in title_lower for kw in keywords):
                has_policy_keyword = True
                break

        robotics_keywords = ['robot', 'manipulation', 'embodied', 'control', 'grasp']
        has_robotics_context = any(kw in title_lower or kw in summary_lower for kw in robotics_keywords)

        return has_policy_keyword and has_robotics_context

    def classify_paper(self, title: str, summary: str) -> str:
        """Classify paper into category"""
        title_lower = title.lower()
        summary_lower = summary.lower()

        if self.check_vla_keywords(title, summary):
            return 'VLA'
        elif self.check_world_model_keywords(title, summary):
            return 'World Model'
        elif self.check_policy_keywords(title, summary):
            return 'Policy'
        else:
            return 'Other'

    def search_papers(self, queries: list) -> list:
        """Search arXiv with multiple queries"""
        all_papers = []
        seen_ids = set()

        for query in queries:
            print(f'Searching: {query[:60]}...')
            try:
                client = arxiv.Client()
                search = arxiv.Search(
                    query=query,
                    max_results=30,
                    sort_by=arxiv.SortCriterion.SubmittedDate,
                    sort_order=arxiv.SortOrder.Descending
                )

                for r in client.results(search):
                    arxiv_id = r.get_short_id()
                    if arxiv_id in seen_ids:
                        continue

                    # Check categories
                    if not any(cat in r.categories for cat in self.VALID_CATEGORIES):
                        continue

                    # Check title relevance
                    category = self.classify_paper(r.title, r.summary)

                    # Only add if relevant (not 'Other')
                    if category == 'Other':
                        continue

                    seen_ids.add(arxiv_id)

                    # Extract project/code links
                    code_url = None
                    project_url = None
                    for link in r.links:
                        link_str = str(link)
                        if 'github' in link_str and code_url is None:
                            code_url = link_str
                        elif 'project' in link_str.lower() or link_str.count('/') > 5:
                            project_url = link_str

                    paper = {
                        'id': arxiv_id,
                        'title': r.title,
                        'authors': [a.name for a in r.authors],
                        'summary': r.summary[:500],
                        'published': r.published.strftime('%Y-%m-%d'),
                        'published_iso': r.published.isoformat(),
                        'url': f"https://arxiv.org/abs/{arxiv_id}",
                        'pdf_url': f"https://arxiv.org/pdf/{arxiv_id}",
                        'categories': list(r.categories),
                        'primary_category': r.primary_category,
                        'code_url': code_url,
                        'project_url': project_url,
                        'auto_category': category
                    }

                    all_papers.append(paper)
                    if len(all_papers) >= self.max_results:
                        break

                time.sleep(1)
            except Exception as e:
                print(f'  Error: {e}')

            if len(all_papers) >= self.max_results:
                break

        # Sort by date (newest first)
        all_papers.sort(key=lambda x: x['published_iso'], reverse=True)
        return all_papers

    def save_to_json(self, papers: list, filename: str):
        """Save papers to JSON file"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(papers, f, ensure_ascii=False, indent=2)
        print(f"Saved {len(papers)} papers to {filename}")

    def generate_markdown(self, papers: list, filename: str):
        """Generate markdown formatted paper list"""
        # Group by category
        from collections import defaultdict
        by_category = defaultdict(list)
        for p in papers:
            by_category[p['auto_category']].append(p)

        md = "# 📚 Latest ArXiv Papers - World Action Models\n\n"
        md += f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        md += f"Total papers: {len(papers)}\n\n"

        for category in ['VLA', 'World Model', 'Policy']:
            if category not in by_category or not by_category[category]:
                continue

            cat_papers = by_category[category][:15]  # Limit to 15 per category
            md += f"## {category}\n\n"
            md += "| Paper | Date | Code |\n"
            md += "|-------|------|------|\n"

            for p in cat_papers:
                title = p['title'].replace('|', '\\|')
                date = p['published']
                url = p['url']

                # Code badge
                code_badge = ''
                if p.get('code_url'):
                    code_badge = f"[🔗]({p['code_url']})"
                elif p.get('project_url'):
                    code_badge = f"[🔗]({p['project_url']})"

                authors = p['authors'][0] if p['authors'] else 'Unknown'
                if len(p['authors']) > 1:
                    authors += ' et al.'

                md += f"| [{title}]({url})<br><small>{authors}</small> | {date} | {code_badge} |\n"

            md += "\n"

        md += "---\n"

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(md)
        print(f"Generated markdown: {filename}")


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Scrape ArXiv for VLA/WAM papers')
    parser.add_argument('--max-results', type=int, default=50, help='Max results')
    parser.add_argument('--days-back', type=int, default=90, help='Days back to search')
    parser.add_argument('--output', type=str, default='data/papers.json', help='Output JSON file')
    parser.add_argument('--md-output', type=str, default='docs/latest-papers.md', help='Output markdown file')

    args = parser.parse_args()

    scraper = ArxivScraperStrict(max_results=args.max_results, days_back=args.days_back)

    # Strict VLA/WAM queries
    queries = [
        # VLA-specific queries
        'ti:"vision language action" OR ti:"VLA" OR ti:"VLA model"',
        'ti:"world action model" OR ti:"world model for robotics"',
        'ti:"diffusion policy" AND all:"robot"',
        'ti:"action chunking" AND all:"robot"',
        'ti:"behavior transformer" AND all:"robot"',
        # Robotics policies
        'ti:"robot learning" AND (ti:"manipulation" OR ti:"embodied")',
    ]

    papers = scraper.search_papers(queries)

    # Save results
    scraper.save_to_json(papers, args.output)
    scraper.generate_markdown(papers, args.md_output)

    print(f"\nTotal papers: {len(papers)}")
    print(f"Categories: {set(p['auto_category'] for p in papers)}")


if __name__ == '__main__':
    main()
