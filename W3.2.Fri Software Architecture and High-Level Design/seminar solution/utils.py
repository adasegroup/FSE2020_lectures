import yaml

import filters as f


def get_users(tagged_names, database):
    # first, make sure we know the person
    names = []
    if len(tagged_names) % 2 == 0:
        # assume several Name Surname or Surname Name instances
        for i in range(0, len(tagged_names), 2):
            name_surname = ' '.join(tagged_names[i:i + 2])
            surname_name = ' '.join(tagged_names[i:i + 2][::-1])
            names.extend([name_surname, surname_name])

    else:
        # we don't know the person
        raise ValueError('weird number of names found: {}'.format(len(tagged_names)))

    found_users = {}
    for user_type, users in database.items():
        for name in names:
            if name in users:
                found_users.update({ name: users[name] })

    return found_users


def get_user_tags(message_tags, users):
    user_tags = {}
    for user_name, user_info in users.items():
        for tag in message_tags:
            user_tag_value = user_info.get(tag, 'unknown')
            user_tags[(user_name, tag)] = user_tag_value
    return user_tags


def compose_reply(user_tags):
    reply = []
    for (user_name, tag), tag_value in user_tags.items():
        reply.append(
            '{} of {}: {}.'.format(tag, user_name, tag_value)
        )
    return '\n'.join(reply)


def get_database():
    with open('staff.yml') as f:
        database = yaml.load(f)
    return database


def process_message(message_string):
    database = get_database()

    message = {'raw': message_string}
    message = f.pipeline(message)

    try:
        users = get_users(message['names'], database)
    except ValueError as e:
        return 'Could not complete request'

    try:
        user_tags = get_user_tags(message['tags'], users)
    except ValueError as e:
        return 'Could not complete request'

    reply_text = compose_reply(user_tags)
    return reply_text

