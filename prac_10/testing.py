"""
CP1404/CP5632 Practical
Wikipedia API Example using wikipedia library
"""

import wikipedia

def search_wiki():
    while True:
        title = input("Enter page title: ").strip()
        if title == "":
            print("Thank you.")
            break

        try:
            page = wikipedia.page(title, autosuggest=False)
            print(f"\nTitle: {page.title}\n")
            print(f"Summary:\n{page.summary}\n")
            print(f"URL: {page.url}\n")
        except wikipedia.exceptions.DisambiguationError as e:
            print("This title is ambiguous. Please be more specific. Suggestions:")
            print(", ".join(e.options[:10]))
        except wikipedia.exceptions.PageError:
            print(f'No Wikipedia page matches the title "{title}". Please try again.')

def main():
    print("=== Wikipedia Search ===")
    search_wiki()

if __name__ == "__main__":
    main()