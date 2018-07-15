""" CSC108 Assignment 3: Social Networks - Starter code """
from typing import List, Tuple, Dict, TextIO


#=============================helper functions==================================
def get_raw_list(profiles_file: TextIO) -> List[List[str]]:
    """Return a roughly organized list containing the lines in profiles_file.
    """
    raw = []
    for line in profiles_file:
        raw.append(line)
    index = []
    
    for j in range(len(raw)):
        if raw[j] == '\n':
            index.append(j + 1)
    index.insert(0, 0)
    raw_list = []
    
    for i1 in range(len(index) - 1):
        changed1 = []
        for i2 in raw[index[i1]:index[i1 + 1] - 1]:
            changed1.append(i2.replace('\n', ''))
        raw_list.append(changed1)
    changed2 = []
    for i3 in raw[index[-1]:]:
        changed2.append(i3.replace('\n', ''))
    raw_list.append(changed2)
    return raw_list


def get_in_order(not_in_order: List[List[str]]) -> List[List[str]]:
    """Return in_order with person's name in "FirstName(s) LastName" format 
    modified from not_in_order.
    >>> lst = [['a, b', 'c, d', 'e, f'], ['g, h', 'i, j']]
    >>> get_in_order(lst)
    [['b a', 'd c', 'f e'], ['h g', 'j i']]
    """
    in_order = []
    for i in range(len(not_in_order)):
        sub_list = []
        for name in not_in_order[i]:
            if ',' in name:
                first_name = name[name.index(',') + 2:].strip()
                last_name = name[:name.index(',')].strip()
                full_name = first_name + ' ' + last_name
                sub_list.append(full_name)
            else:
                sub_list.append(name)
        in_order.append(sub_list)
    return in_order


def get_person_to_friends(person_to_friends: Dict[str, List[str]], raw_list: \
    List[str], in_order: List[str]) -> None:
    """Update the "person to friends" dictionary person_to_friends to include 
    data from in_order.
    """
    keys = []
    for i1 in range(len(in_order)):
        keys.append(in_order[i1][0])
    
    name_list = []
    for i2 in range(len(in_order)):
        sub = []
        for j in range(1, len(in_order[i2])):
            if ',' in raw_list[i2][j]:
                sub.append(in_order[i2][j])
        name_list.append(sub)
    
    for key1 in keys:
        if key1 in person_to_friends:
            for name in name_list[keys.index(key1)]:
                if name not in person_to_friends[key1]:
                    person_to_friends[key1].append(name)
        else:
            if name_list[keys.index(key1)] != []:
                person_to_friends[key1] = name_list[keys.index(key1)]
    
    for key3 in person_to_friends:
        person_to_friends[key3].sort()


def get_person_to_networks(person_to_networks: Dict[str, List[str]], raw_list: \
    List[str], in_order: List[str]) -> None:
    """Update the "person to networks" dictionary person_to_networks to include 
    data from in_order.
    """
    keys = []
    for i1 in range(len(in_order)):
        keys.append(in_order[i1][0])
    
    network = []
    for i3 in range(len(in_order)):
        sub1 = []
        for j3 in range(1, len(in_order[i3])):
            if ',' not in raw_list[i3][j3]:
                sub1.append(in_order[i3][j3])
        network.append(sub1)
    
    for key2 in keys:
        if key2 in person_to_networks:
            for name1 in network[keys.index(key2)]:
                if name1 not in person_to_networks[key2]:
                    person_to_networks[key2].append(name1)
        else:
            if network[keys.index(key2)] != []:
                person_to_networks[key2] = network[keys.index(key2)]
    
    for key4 in person_to_networks:
        person_to_networks[key4].sort()


def get_same_network(person: str, person_to_networks: Dict[str, List[str]]) -> List[str]:
    """Return a list of people from person_to_networks that have the same network.
    """
    network_to_people = invert_network(person_to_networks)
    same_network = []
    for network in network_to_people:
        if person in network_to_people[network]:
            for names in network_to_people[network]:
                if names != person:
                    same_network.append(names)
    return same_network


def get_same_last_name(person: str, person_to_friends: Dict[str, List[str]]) -> List[str]:
    """Return a list of people from person_to_friends that have the same last 
    name with the person.
    """
    people = get_total_people(person_to_friends)
    same_last_name = []
    for name2 in people:
        if name2[name2.index(' ') + 1:] == person[person.index(' ') + 1:] and \
name2 != person:
            same_last_name.append(name2)
    return same_last_name


def get_total_people(person_to_friends: Dict[str, List[str]]) -> List[str]:
    """Return a list of people appear in person_to_friends.
    """
    people = []
    for key1 in person_to_friends:
        if key1 not in people:
            people.append(key1)
        for name1 in person_to_friends[key1]:
            if name1 not in people:
                people.append(name1)
    return people


def get_friend_list(people: List[str], friends_of_friends: List[str], same_network: \
    List[str], same_last_name: List[str]) -> List[str]:
    """Return a list of person who are friends of person depends on friends_of_friends,
    same_network and same_last_name.
    """
    friend_list = []
    for name in people:
        score = 0
        for name1 in friends_of_friends:
            if name1 == name:
                score = score + 1
        if name in same_network:
            score = score + 1
        if score != 0:
            if name in same_last_name:
                score = score + 1
            friend_list.append(name)
    return friend_list


def get_score_list(people: List[str], friends_of_friends: List[str], same_network: \
    List[str], same_last_name: List[str]) -> List[str]:
    """Return a list of score depends on friends_of_friends, same_network and
    same_last_name.
    """
    score_list = []
    for name in people:
        score = 0
        for name1 in friends_of_friends:
            if name1 == name:
                score = score + 1
        if name in same_network:
            score = score + 1
        if score != 0:
            if name in same_last_name:
                score = score + 1
            score_list.append(score)
    return score_list


def score_three(score_list: List[str], friend_list: List[str]) -> List[str]:
    """Return a list of people from friend_list with score three.
    """
    three = []
    for i in range(len(score_list)):
        if score_list[i] == 3:
            three.append(friend_list[i])
    three.sort()
    return three


def score_two(score_list: List[str], friend_list: List[str]) -> List[str]:
    """Return a list of people from friend_list with score two.
    """
    two = []
    for i in range(len(score_list)):
        if score_list[i] == 2:
            two.append(friend_list[i])
    two.sort()
    return two


def score_one(score_list: List[str], friend_list: List[str]) -> List[str]:
    """Return a list of people from friend_list with score one.
    """
    one = []
    for i in range(len(score_list)):
        if score_list[i] == 1:
            one.append(friend_list[i])
    one.sort()
    return one


def get_tupple(score_list: List[str], friend_list: List[str]) -> List[str]:
    """Return the friend recommendations for the given person as a list of 
    tuples where the first element of each tuple is a potential friend's name 
    (in the same format as the dictionary keys) and the second element is that 
    potential friend's score.
    """
    three = score_three(score_list, friend_list)
    two = score_two(score_list, friend_list)
    one = score_one(score_list, friend_list)
    
    final = []
    for name4 in three:
        tup = (name4, 3)
        final.append(tup)
    for name5 in two:
        tup = (name5, 2)
        final.append(tup)
    for name6 in one:
        tup = (name6, 1)
        final.append(tup)
    
    return final


#===========================end helper functions================================


def load_profiles(profiles_file: TextIO, person_to_friends: Dict[str, List[str]], \
    person_to_networks: Dict[str, List[str]]) -> None:
    """Update the "person to friends" dictionary person_to_friends and the
    "person to networks" dictionary person_to_networks to include data from
    profiles_file.

    Docstring examples not given since result depends on input data.
    """
    raw_list = get_raw_list(profiles_file)
    in_order = get_in_order(raw_list)
    get_person_to_friends(person_to_friends, raw_list, in_order)
    get_person_to_networks(person_to_networks, raw_list, in_order)
    

def get_average_friend_count(person_to_friends: Dict[str, List[str]]) -> float:
    """Return the average number of friends that people who appear as keys in 
    the given "person to friends" dictionary have.
    """
    num = 0
    for keys in person_to_friends:
        num = num + len(person_to_friends[keys])
    try:
        ave = num / len(person_to_friends)
        return ave
    except ZeroDivisionError:
        return 0
    
    
def get_families(person_to_friends: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """Return a "last name to first names" dictionary based on the given "person
    to friends" dictionary.
    """
    families = {}
    for keys in person_to_friends:
        if keys[keys.index(' ') + 1:] not in families:
            families[keys[keys.index(' ') + 1:]] = [keys[:keys.index(' ')]]
        else:
            if keys[:keys.index(' ')] not in families[keys[keys.index(' ') + 1:]]:
                families[keys[keys.index(' ') + 1:]].append(keys[:keys.index(' ')])
        for names in person_to_friends[keys]:
            if names[names.index(' ') + 1:] not in families:
                families[names[names.index(' ') + 1:]] = [names[:names.index(' ')]]
            else:
                if names[:names.index(' ')] not in families[names[names.index(' ') + 1:]]:
                    families[names[names.index(' ') + 1:]].append(names[:\
                                                                        names.index(' ')])
    for last_names in families:
        families[last_names].sort()
    return families


def invert_network(person_to_networks: Dict[str, List[str]]) -> Dict[str, List[str]]:
    """Return a "network to people" dictionary based on the given "person to networks"
    dictionary. The values in the dictionary are sorted alphabetically.
    
    The example dictionary below is based on example file profiles.txt.
    """
    network_to_people = {}
    keys = []
    for names in person_to_networks:
        for name in person_to_networks[names]:
            keys.append(name)
    for names in person_to_networks:
        for key in person_to_networks[names]:
            if key not in network_to_people:
                network_to_people[key] = [names]
            else:
                if names not in network_to_people[key]:
                    network_to_people[key].append(names)
    for k in network_to_people:
        network_to_people[k].sort()
    return network_to_people
                    


def get_friends_of_friends(person_to_friends: Dict[str, List[str]], \
    person: str) -> List[str]:
    """Given a "person to friends" dictionary and the name of a person (in the 
    same format as the dictionary keys), return the list of names of people who 
    are friends of the named person's friends.
    """
    f = []
    fof = []
    if person in person_to_friends:
        for name in person_to_friends[person]:
            f.append(name)
    for name1 in f:
        if name1 in person_to_friends:
            for name2 in person_to_friends[name1]:
                if name2 != person:
                    fof.append(name2)
        fof.sort()
    return fof
    
    
def make_recommendations(person: str, person_to_friends: Dict[str, List[str]], \
    person_to_networks: Dict[str, List[str]]) -> List[Tuple[str, int]]:
    """Return the friend recommendations for the given person as a list of 
    tuples where the first element of each tuple is a potential friend's name 
    (in the same format as the dictionary keys) and the second element is that 
    potential friend's score.
    """
    friends_of_friends = get_friends_of_friends(person_to_friends, person)
    same_network = get_same_network(person, person_to_networks)
    people = get_total_people(person_to_friends)
    same_last_name = get_same_last_name(person, person_to_friends)
    
    friend_list = get_friend_list(people, friends_of_friends, same_network, \
same_last_name)
    score_list = get_score_list(people, friends_of_friends, same_network, \
same_last_name)
    
    final = get_tupple(score_list, friend_list)
    return final


if __name__ == '__main__':
    import doctest
    doctest.testmod()
