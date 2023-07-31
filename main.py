from HashMap import HashMap


def main():
    hash_map = HashMap()
    print('Creating hash map.')
    print('HashMap size: {}, Capacity: {}\n'.format(len(hash_map.buckets), hash_map.hash_map_capacity))

    print('Adding elements and resize hash map.')
    print('_______________________')
    hash_map.put('Bred', 'Pitt')
    hash_map.put('Russel', 'Crow')
    hash_map.put('John', 'Travolta')
    hash_map.put('Quentin', 'Tarantino')
    hash_map.put('Arnold', 'Schwarzenegger')
    hash_map.put('Sylvester', 'Stallone')
    hash_map.put('Jackie', 'Chan')
    hash_map.put('Bradley', 'Cooper')
    hash_map.put('Matthew', 'McConaughey')
    hash_map.put('Leonardo', 'DiCaprio')

    print('\nHashMap size: {}, Capacity: {}'.format(len(hash_map.buckets), hash_map.hash_map_capacity))
    print('----------- OUTPUT -----------')
    hash_map.print_all()
    print()

    print('Change element by key "John": Travolta -> Malkovich. ')
    hash_map.put('John', 'Malkovich')
    print('_______________________')
    print('\nHashMap size: {}, Capacity: {}'.format(len(hash_map.buckets), hash_map.hash_map_capacity))
    print('----------- OUTPUT -----------')
    hash_map.print_all()
    print()

    print('Getting element by key "Leonardo".')
    print('_______________________')
    item = hash_map.get("Leonardo")
    print('Got: {}'.format(item))
    print()

    key = "Leonardo"
    print('Removing element by key "{}".'.format(key))
    print('_______________________')
    print('Removing {}'.format(key))
    hash_map.remove(key)
    print('_______________________')
    print('\nHashMap size: {}, Capacity: {}'.format(len(hash_map.buckets), hash_map.hash_map_capacity))
    print('----------- OUTPUT -----------')
    hash_map.print_all()
    print()

    print('Removing elements and resize hash map.')
    print('_______________________')
    hash_map.remove('Russel')
    hash_map.remove('John')
    hash_map.remove('Quentin')
    hash_map.remove('Arnold')
    hash_map.remove('Sylvester')
    hash_map.remove('Matthew')
    print('\nHashMap size: {}, Capacity: {}'.format(len(hash_map.buckets), hash_map.hash_map_capacity))
    print('----------- OUTPUT -----------')
    hash_map.print_all()
    print()


if __name__ == '__main__':
    main()
