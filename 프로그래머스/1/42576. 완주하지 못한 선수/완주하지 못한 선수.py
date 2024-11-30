def solution(participant, completion):
    answer = ''
    part_dict = {}
    for name in participant:
        part_dict[name] = []
    
    for name in participant:
        part_dict[name].append(0)

    for name in completion:
        part_dict[name].remove(0)
    
    for name, comp in part_dict.items():
        if len(comp) > 0:
            answer = name
    return answer