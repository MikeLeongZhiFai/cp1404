
import wikipedia

def search():
    user_input = input("Please input the search keyword: ")
    while user_input != "":
        try:
            page_results = wikipedia.page(user_input)
            print(page_results.title)
            print(page_results.summary)
            print(page_results.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)
        user_input = input("Please input the search keyword: ")
    print("Thank you :)")

search()