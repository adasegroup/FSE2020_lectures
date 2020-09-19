import re


def cleaning_filter(message):
    message_header = []
    message_content = []

    target_array = message_header
    for line in message['raw'].splitlines():
        if line.strip() == '':
            target_array = message_content
        target_array.append(line)

    message['header'] = message_header
    message['content'] = '\n'.join(message_content)
    return message


def position_tag_filter(message):
    if 'position' in message['content'].lower():
        message_tags = message.get('tags', [])
        message_tags.append('position')
        message['tags'] = message_tags

    return message


def team_tag_filter(message):
    if 'team' in message['content'].lower():
        message_tags = message.get('tags', [])
        message_tags.append('team')
        message['tags'] = message_tags

    return message


def name_filter(message):
    names = re.findall('[A-Z][a-z]*', message['content'])
    message['names'] = names
    return message


def pipeline(message):
    message = cleaning_filter(message)
    message = position_tag_filter(message)
    message = team_tag_filter(message)
    message = name_filter(message)
    return message

