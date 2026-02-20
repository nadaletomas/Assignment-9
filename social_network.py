class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
   '''

    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        """Adds a friend if they are not already in the friend list"""
        if friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''

    def __init__(self):
        self.people = {}

    def add_person(self, name):
        """Adds a new person to the network"""
        if name not in self.people:
            self.people[name] = Person(name)
        else:
            print(f"{name} already exists in the network.")

    def add_friendship(self, person1_name, person2_name):
        """Creates a bidirectional friendship between two people"""
        if person1_name not in self.people:
            print(f"Friendship not created. {person1_name} doesn't exist!")
            return

        if person2_name not in self.people:
            print(f"Friendship not created. {person2_name} doesn't exist!")
            return

        person1 = self.people[person1_name]
        person2 = self.people[person2_name]

        person1.add_friend(person2)
        person2.add_friend(person1)

    def print_network(self):
        """Prints all people and their friends"""
        for name, person in self.people.items():
            friend_names = [friend.name for friend in person.friends]
            print(f"{name} is friends with: {', '.join(friend_names)}")


# -----------------
# Test your code here
# -----------------

network = SocialNetwork()

# Add people
network.add_person("Alex")
network.add_person("Jordan")
network.add_person("Morgan")
network.add_person("Taylor")
network.add_person("Casey")
network.add_person("Riley")

# Test duplicate
network.add_person("Alex")

# Create friendships
network.add_friendship("Alex", "Jordan")
network.add_friendship("Alex", "Morgan")
network.add_friendship("Jordan", "Taylor")
network.add_friendship("Morgan", "Casey")
network.add_friendship("Taylor", "Riley")
network.add_friendship("Casey", "Riley")
network.add_friendship("Morgan", "Riley")
network.add_friendship("Alex", "Taylor")

# Test non-existent person
network.add_friendship("Jordan", "Johnny")

print("\nSocial Network:")
network.print_network()



"""
Design Memo

The graph data structure is the best way to model a social network because in a social network, relationships between individuals are bidirectional and non-hierarchical. In a social network, an individual may be connected to many people, and those people may be connected to many others. This creates a complex web of relationships that cannot be modeled efficiently using simpler data structures. Using a graph to model people as nodes and relationships as edges, we can model this complex web of relationships accurately.

A list would be a poor choice because lists are linear sequences of elements. They do not have any inherent notion of relationships between elements. While we could use a list to store names, it would not model who is connected to whom in a simple way. A tree is also not a good choice because a tree has a hierarchical parent-child relationship with a single root node. In a social network, there is no top-level person, and relationships are between equals, not from superiors to subordinates in a hierarchical fashion.

The adjacency list representation proved to be an efficient way of handling the problem. Adding a person to the list is efficient because it only requires adding to a dictionary. Adding friendships to the list is also efficient because we append to a list. However, the drawback is that in order to check for duplicate friendships, we have to search through the
list of a person’s friends, which takes as long as the number of friends they have. But since most people do not have very large lists of friends, adjacency lists are still efficient and scalable for social network systems.

"""