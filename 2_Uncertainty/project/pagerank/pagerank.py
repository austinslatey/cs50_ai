import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    n_pages = len(corpus)
    probabilities = {}
    linked_pages = corpus[page]

    if linked_pages:
        for p in corpus:
            probabilities[p] = (1 - damping_factor) / n_pages
        for linked_page in linked_pages:
            probabilities[linked_page] += damping_factor / len(linked_pages)
    else:
        # if no links, respond as if there are links to all pages
        for p in corpus:
            probabilities[p] = 1 / n_pages

    return probabilities


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    page_rank = {page: 0 for page in corpus}
    pages = list(corpus.keys())

    # Start with random page
    current_page = random.choice(pages)

    for _ in range(n):
        page_rank[current_page] += 1
        probabilities = transition_model(corpus, current_page, damping_factor)
        current_page = random.choices(pages, weights=[probabilities[p] for p in pages], k=1)[0]

    # Normalize results
    page_rank = {page: rank / n for page, rank in page_rank.items()}

    return page_rank


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    N = len(corpus)
    pagerank = {page: 1 / N for page in corpus}
    new_pagerank = pagerank.copy()
    converged = False

    while not converged:
        converged = True
        for page in pagerank:
            rank = (1 - damping_factor) / N
            for potential_linker in corpus:
                if page in corpus[potential_linker]:
                    rank += damping_factor * pagerank[potential_linker] / len(corpus[potential_linker])
                elif not corpus[potential_linker]:
                    rank += damping_factor * pagerank[potential_linker] / N
            if abs(new_pagerank[page] - rank) > 0.001:
                converged = False
            new_pagerank[page] = rank

        pagerank = new_pagerank.copy()
    return pagerank

if __name__ == "__main__":
    main()
