from pprint import pprint


def parse_file(line: str) -> tuple:

    pos = line.find(' ')
    remote_addr = line[:pos]
    pos = line.find('"') + 1
    pos_b = line.find(' ', pos)
    request_type = line[pos:pos_b]
    pos_b += 1
    pos = line.find(' ', pos_b)
    requested_resource = line[pos_b:pos]
    return (remote_addr if remote_addr else None,
            request_type if request_type else None,
            requested_resource if requested_resource else None)


list_out = list()
with open('nginx_logs.txt', 'r', encoding='utf-8') as fr:
    list_out = [parse_file(line) for line in fr]
pprint(list_out)