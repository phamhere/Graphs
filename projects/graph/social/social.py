import random


class User:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        for i in range(numUsers):
            self.addUser(f"User {i+1}")

        # Create friendships with total = avg * users
        possibleFriendships = []
        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1):
                possibleFriendships.append((userID, friendID))
        random.shuffle(possibleFriendships)

        totalFriendships = (numUsers * avgFriendships) // 2
        for i in range(totalFriendships):
            self.addFriendship(
                possibleFriendships[i][0], possibleFriendships[i][1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME

        q = [[userID]]
        # setting the userID in visited dict value to None
        while len(q) > 0:
            path = q.pop(0)
            v = path[-1]
            # if v not in visited, make a dict entry and queue up neighbors
            if v not in visited:
                visited[v] = path
                for neighbor in self.friendships[v]:
                    if neighbor not in visited:
                        new_path = list(path)
                        new_path.append(neighbor)
                        q.append(new_path)
        return visited

    def percentageInSocialNetwork(self):
        totalNetworks = 0
        for user in self.users:
            totalNetworks += len(self.getAllSocialPaths(user))
        return ((totalNetworks / len(self.users)) / len(self.users)) * 100

    def degreeOfSeparation(self):
        pass


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
    print(sg.percentageInSocialNetwork())
