import sys

N, M = map(int, sys.stdin.readline().split())

room_names = [sys.stdin.readline().strip() for _ in range(N)]
room_names = sorted(room_names)

room = {}
for name in room_names:
    room[name] = []
    
for info in range(M):
    r, s, t = sys.stdin.readline().split()
    room[r].append(int(s))
    room[r].append(int(t))

cnt = 0
for name in room_names:
    room[name] = sorted(room[name])
    empty_list = []
    for i in range(0, len(room[name]), 2):
        start = room[name][i]
        end = room[name][i+1]
        if i == 0:
            if start == 9:
                continue
            else:
                empty_list.append(f"09-{start}")
        else:
            previous_end = room[name][i-1]
            empty_list.append(f"{previous_end}-{start}")
            if previous_end == start:
                empty_list.pop()
            else: pass
    if len(room[name]) == 0:
        empty_list.append(f"09-18")
    elif end != 18:
        empty_list.append(f"{end}-18")
    else: pass

    if cnt == 0:
        pass
    else:
        print(f"-----")
    print(f"Room {name}:")
    if len(empty_list) == 0:
        print(f"Not available")
    else:
        print(f"{len(empty_list)} available:")
        for time in empty_list:
            print(time)
    cnt += 1