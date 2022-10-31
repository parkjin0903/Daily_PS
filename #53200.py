def solution(skill, skill_trees):
    answer = 0
    
    
    for skill_com in skill_trees:
        skill_list = list(skill)
        
        for ch in skill_com:
            if ch in skill:
                if ch != skill_list.pop(0):
                    break
        else:
            answer += 1
                
                    
    return answer