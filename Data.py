graph = {
    "you": ["alice", "bob", "claire"],
    "alice": ["peggy"],
    "bob": ["anuj", "peggy"],
    "claire": ["thom", "jonny"],
    "peggy":[],
    "anuj": [],
    "thom": [],
    "jonny": []
}

from collections import deque

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if seller(person):
                print (person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False

def seller(name):
    return name.endswith("m")

print(search("you"))