
def main():
    
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"--- Begin report of {book_path}---")
    print(f"{num_words} words found in the document")
    count_words = get_count_words(text)
      
    #print(count_words)
    list_Dicts = create_dict(count_words)
    list_Dicts.sort(reverse=True,key=sort_on)
    
    print_list(list_Dicts)
def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_count_words(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
    
def create_dict(dict):
    for alpha in list(dict.keys()):
        if alpha.isalpha() == False:
            dict.pop(alpha)
    list_of_dicts = [{"key": key, "value": value} for key, value in dict.items()]
    
    return(list_of_dicts)

def sort_on(list_dicts):
    return list_dicts["value"]

def print_list(list):
    for x in list:
        print(f"The '{x["key"]}' character awas found {x["value"]} times")

    print("-- End Report --")


main()