# Another one of my more sloppy ones, would refactor if I had time today

from aoc import get_input


PACKET_TYPE_LITERAL = 4

LENGTH_TYPES = [15, 11]

def decode(str):
    return "".join(["{0:04b}".format(int(c, 16)) for c in str])


def read_packets(str, fixed_number=-1):
    packets = []
    while len(str) > 0 and int(str, 2) != 0 and fixed_number != 0:
        packet_version = str[0:3]
        packet_type_id = int(str[3:6], 2)
        fixed_number -= 1

        
        if packet_type_id == PACKET_TYPE_LITERAL:
            content = ""
            pointer = 6
            while True:
                section = str[pointer:pointer+5]
                content += section[1:]

                if section[0] == "0":
                    break 

                pointer += 5

            packet = (int(packet_version, 2), packet_type_id, int(content, 2))

            packets.append(packet)
            str = str[pointer+5:]
        else:
            packet_length_id = int(str[6], 2)
            length = LENGTH_TYPES[packet_length_id]

            packet_content_length = int(str[7:7+length], 2)
            if packet_length_id == 0:
                sub_packet = str[7+length:7+length+packet_content_length]
                _, p = read_packets(sub_packet)
                str = str[7+length+packet_content_length:]
            else:
                sub_packet = str[7+length:]
                str, p = read_packets(sub_packet, packet_content_length)

            packet = (int(packet_version, 2), packet_type_id, p)
            packets.append(packet)

    return str, packets


def version_sum(packets):
    vsum = 0
    for packet in packets:
        if packet[1] != PACKET_TYPE_LITERAL:
            vsum += version_sum(packet[2])
        
        vsum += packet[0]

    return vsum

def resolve_packet(packet):
    def resolve_lit(packet):
        return packet[2]

    def resolve_sum(packet):
        return sum([resolve_packet(packet) for packet in packet[2]])

    def resolve_product(packet):
        p = 1
        for packet in packet[2]:
            p *= resolve_packet(packet)
        return p

    def resolve_min(packet):
        return min([resolve_packet(packet) for packet in packet[2]])

    def resolve_max(packet):
        return max([resolve_packet(packet) for packet in packet[2]])

    def resolve_gt(packet):
        p0 = packet[2][0]
        p1 = packet[2][1]
        return int(resolve_packet(p0) > resolve_packet(p1))
    
    def resolve_lt(packet):
        p0 = packet[2][0]
        p1 = packet[2][1]
        return int(resolve_packet(p0) < resolve_packet(p1))

    def resolve_eq(packet):
        p0 = packet[2][0]
        p1 = packet[2][1]
        return int(resolve_packet(p0) == resolve_packet(p1))

    resolve_map = [
        resolve_sum,
        resolve_product,
        resolve_min,
        resolve_max,
        resolve_lit,
        resolve_gt,
        resolve_lt,
        resolve_eq
    ]

    return resolve_map[packet[1]](packet)

if __name__ == "__main__":
    data = get_input(16)

    d = decode(data)
    _, packets = read_packets(d)

    print("Part 1")
    print(version_sum(packets))

    print("Part 2")
    print(resolve_packet(packets[0]))
    