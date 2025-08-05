def count_words(content):
    return len(content.split())

def count_char(content):
    count_dict = dict()
    for char in content:
        char = char.lower()
        if (char != '\n') and (char != " "):
            if char in count_dict:
                count_dict[char] += 1
            else:
                count_dict[char] = 1
    return count_dict

def sort_on(items):
    return items["num"]

def pretty_print_stats(path):
    with open(path) as f:
        content = f.read()
    count =  count_words(content)
    count_dict=count_char(content)
    liste = []
    for char in count_dict:
        liste.append({"char": char, "num": count_dict[char]})
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    liste.sort(reverse = True, key=sort_on)
    for elem in liste:
        if elem["char"].isalpha():
            print(f"{elem["char"]}: {elem["num"]}")
    print("============= END ===============")
    # print(count_dict.sort()) 
